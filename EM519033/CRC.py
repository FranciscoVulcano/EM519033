import struct

def __crc(message):
    """
    Calculate a 16-bit CRC checksum for the given message.

    Parameters:
    - message (bytes): The input message represented as a sequence of bytes.

    Returns:
    - Tuple[int, int]: The calculated CRC as a tuple of two 8-bit values (crc_low, crc_high).

    Notes:
    - The function uses the CRC-16 algorithm with a polynomial of 0xA001.
    - The initial CRC value is set to 0xFFFF.
    - The input message should be represented as a sequence of bytes.

    Example:
    - __crc(b'\x01\x02\x03\x04'): Returns a tuple representing the calculated CRC.
    """
    crc = 0xFFFF
    for byte in message:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1

    crc_low = crc & 0xFF
    crc_high = (crc >> 8) & 0xFF

    return crc_low, crc_high

def crc_append(message):
    """
    Append a 16-bit CRC checksum to the given message.

    Parameters:
    - message (bytes): The input message represented as a sequence of bytes.

    Returns:
    - bytes: The modified message with the appended CRC.

    Notes:
    - The function calculates a 16-bit CRC using the CRC-16 algorithm with a polynomial of 0xA001.
    - The initial CRC value is set to 0xFFFF.
    - The CRC is appended to the end of the input message.

    Example:
    - crc_append(b'\x01\x02\x03\x04'): Returns the modified message with the appended CRC.
    """
    crc_low, crc_high = __crc(message)
    modified_message = message + struct.pack('<BB', crc_low, crc_high)
    return modified_message

def validate_crc(message):
    """
    Validate the CRC checksum of a received message.

    Parameters:
    - message (str): The received message in hexadecimal format.

    Returns:
    - bool: True if the CRC checksum is valid, False otherwise.

    Notes:
    - The function extracts the received CRC from the end of the message.
    - The CRC is calculated for the message without the appended CRC.
    - The calculated CRC is compared with the received CRC.

    Example:
    - validate_crc('01020304F1D2'): Returns True if the CRC is valid, False otherwise.
    """
    received_crc = message[-4:]  # gets the CRC from the message
    noncrc_message = message[:-4]  # gets the message without the CRC
    crc_values = __crc(bytes.fromhex(noncrc_message))  # calculates message CRC
    calculated_crc = str(hex(crc_values[0]))[2:] + str(hex(crc_values[1]))[2:]  # Converts the calculated CRC into a string

    if received_crc != calculated_crc:
        return False
    return True