import sys
import time
from dataclasses import dataclass
from EM519033.CRC import crc_append, validate_crc
from EM519033.enums import CommandLenght, Commands, Enum, ResultFormat
from EM519033.response_parser import parse_response
from gpiozero import OutputDevice
from serial import Serial


@dataclass
class ReceiveData:
    device_id: int
    mode: int
    data_lenght: int
    data: str
    crc: bytes


@dataclass
class SendData:
    device_id: int
    mode: int
    command: int
    command_lenght: int

    def to_bytes(self) -> bytes:
        hex_str = (
            str(self.device_id).zfill(2)
            + str(self.mode).zfill(2)
            + str(self.command).zfill(4)
            + str(self.command_lenght).zfill(4)
        )
        return bytes.fromhex(hex_str)


class EM519033:

    def __init__(self, port, baudrate=9600, timeout=0.25):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.comm = Serial(
            self.port, self.baudrate, timeout=self.timeout, parity="E"
        )
        self.DE_RE = OutputDevice(17)

    def send_command(self, data: SendData):
        """Prepares message, flushes incoming junk, and transmits frame."""
        # 1. Clear any stale bytes sitting in the RX buffer from previous timeout errors
        self.comm.reset_input_buffer()

        # 2. Build frame with CRC
        message = crc_append(data.to_bytes())

        # 3. Drive RS-485 Transmit Mode
        self.DE_RE.on()
        self.comm.write(message)

        # 4. Wait for hardware TX buffer to physically flush before dropping RS-485 DE line
        self.comm.flush()
        self.DE_RE.off()

    def receive_data(self):
        """Reads exact Modbus frame length based on header byte count."""
        # Standard Read Holding Registers (Mode 03) Header is 3 bytes: [ID, Function, ByteCount]
        header = self.comm.read(3)
        if len(header) < 3:
            return False  # Timeout / No response

        data_length = header[2]  # Third byte specifies payload length in bytes

        # Read remaining payload + 2 bytes for CRC
        remaining = self.comm.read(data_length + 2)
        if len(remaining) < (data_length + 2):
            return False  # Incomplete response frame

        raw_frame = header + remaining

        # Validate CRC against exact byte frame
        if not validate_crc(raw_frame.hex()):
            return False

        device_id = header[0:1].hex()
        mode = header[1:2].hex()
        payload_hex = remaining[:data_length].hex()
        crc_hex = remaining[data_length:].hex()

        return ReceiveData(
            device_id=device_id,
            mode=mode,
            data_lenght=data_length,
            data=payload_hex,
            crc=crc_hex,
        )

    def get_value(self, device_id, value: Enum):
        """Retrieves and parses parameter value from meter."""
        value_key = value.value
        command_value = Commands[value_key].value
        command_length = CommandLenght[value_key].value

        message = SendData(
            device_id=device_id,
            mode=3,
            command=command_value,
            command_lenght=command_length,
        )
        self.send_command(message)

        received = self.receive_data()
        if not received:
            return None

        return parse_response(received.data, ResultFormat[value_key].value)