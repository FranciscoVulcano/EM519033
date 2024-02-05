from dataclasses import dataclass
from EM519033.CRC import crc_append, validate_crc
from serial import Serial
from EM519033.enums import Commands, CommandLenght, ResultFormat,Enum
from EM519033.response_parser import parse_response


@dataclass
class ReceiveData:
    device_id: int
    mode: int
    data_lenght: int
    data: int
    crc: bytes


@dataclass
class SendData:
    device_id: int
    mode: int
    command: int
    command_lenght: int

    def to_string(self) -> str:
        return (str(self.device_id).zfill(2) + str(self.mode).zfill(2) + str(self.command).zfill(4) +
                str(self.command_lenght).zfill(4))


class EM519033:
    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.comm = Serial(self.port, self.baudrate, timeout=self.timeout, parity='E')

    def send_command(self, data: SendData):
        """
        Convert a SendData object to a message, append CRC, and send it to the device.

        Parameters:
        - data (SendData): An object containing information to be sent to the device.

        Returns:
        - None

        Notes:
        - The method converts the SendData object to a hexadecimal message using the to_string method.
        - The CRC is appended to the message using the crc_append function.
        - The final message is sent to the device via the communication interface (self.comm.write).

        Example:
        - send_command(SendData(device_id=1, mode=4, command=2, command_length=6)):
          Converts the SendData object to a message, appends CRC, and sends it to the device.
        """
        message = data.to_string()
        hex_bytes = bytes.fromhex(message)
        message = crc_append(hex_bytes)
        self.comm.write(message)

    def receive_data(self):
        """
        Receive a message from the device, validate CRC, parse the message, and return the data in a ReceiveData object.

        Returns:
        - ReceiveData or False: If CRC validation succeeds, returns a ReceiveData object containing parsed information
                                (device_id, mode, data_length, data, crc). If CRC validation fails, returns False.

        Notes:
        - The method assumes that each message is 20 bytes long (adjust if needed).
        - The method relies on a communication interface represented by self.comm (e.g., a serial port).
        - The CRC validation is performed using the validate_crc function.
        - If CRC validation fails, the method returns False, indicating potential communication errors.

        Example:
        - receive_data(): Returns a ReceiveData object or False based on the received and parsed message.
        """
        message = self.comm.read(20).hex()
        if not validate_crc(message):
            return False
        data = self.__parse_message(message)
        return data

    def __parse_message(self, message):
        """
         Parse a received message and create a ReceiveData object with extracted information.

         Parameters:
         - message (str): The raw received message in hexadecimal format.

         Returns:
         - ReceiveData: An object containing the parsed information (device_id, mode, data_length, data, crc).

         Example:
         - parse_received_message('0102041F4B2E4C0F'): Returns a ReceiveData object with:
           - device_id = '01'
           - mode = '02'
           - data_length = 4
           - data = '1F4B2E4C'
           - crc = '0F'
         """
        device_id = message[:2]
        mode = message[2:4]
        data_lenght = int(message[4:6])
        data = message[6:(6+data_lenght*2)]
        crc = message[-4:]
        return ReceiveData(device_id, mode, data_lenght,data,crc)

    def get_value(self, device_id, value: Enum):
        """
        Retrieve a specific value from a device using the Modbus communication protocol.

        Parameters:
        - device_id (int): The unique identifier of the target device.
        - value (Enum): An Enum representing the desired value to retrieve.

        Returns:
        - Parsed value: The extracted and parsed value based on the specified Enum.
          Returns None if the communication or parsing process encounters an issue.

        Raises:
        - Any exceptions related to communication or parsing errors.

        Usage Examples:
        - Retrieve voltage from device with ID 1:
          voltage = meter.get_value(1, parameters.InstantaneousParameters.voltage)
        - Retrieve current from device with ID 1:
          current = meter.get_value(1, parameters.InstantaneousParameters.current)
        - Retrieve frequency from device with ID 1:
          frequency = meter.get_value(1, parameters.InstantaneousParameters.frequency)
        - Retrieve active total power from device with ID 1:
          power = meter.get_value(1, parameters.PowerParameters.active_total_power)

        Note:
        - This function relies on the Modbus communication protocol.
        - It sends a command to the device to retrieve the specified value.
        - The response is parsed based on the specified ResultFormat for the corresponding value.
        """

        value = value.value
        command_value = Commands[value].value
        command_length = CommandLenght[value].value
        message = SendData(device_id=device_id, mode=3, command=command_value, command_lenght=command_length)
        self.send_command(message)

        received_message = self.receive_data()
        if received_message is False:
            return None
        response = received_message.data
        parsed_value = parse_response(response, ResultFormat[value].value)
        return parsed_value