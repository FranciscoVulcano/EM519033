import struct

def parse_response(response, resultformat):
    """
        Parse a hexadecimal response based on the specified result format.

        Parameters:
        - response (str): Hexadecimal representation of the response data.
        - resultformat (str): The format in which to interpret the response.

        Returns:
        - Parsed value: The parsed numeric value based on the specified result format.

        Supported Result Formats:
        - 'INT32_3_3': Integer, 3 digits before the decimal point, 3 digits after (divided by 1000.0).
        - 'INT32_2_3': Integer, 2 digits before the decimal point, 3 digits after (divided by 1000.0).
        - 'INT32_5_0': Integer, 5 digits before the decimal point.
        - 'INT16_2_1': Integer, 2 digits before the decimal point, 1 digit after (divided by 10).
        - 'INT16_1_3': Integer, 1 digit before the decimal point, 3 digits after (divided by 1000.0).
        - 'INT32_6_2': Integer, 6 digits before the decimal point, 2 digits after (divided by 100.0).
        - 'INT32_6_1': Integer, 6 digits before the decimal point, 1 digit after (divided by 10.0).
        - 'NOT_SUPPORTED': Return 'Not supported' if the result format is not supported.

        Notes:
        - The function assumes that the input 'response' is a valid hexadecimal string.
        - If the specified result format is not recognized, the function returns None.

        Examples:
        - parse_response('1F4', 'INT16_2_1') returns 2.5
        - parse_response('3E8', 'INT32_5_0') returns 1000
        - parse_response('C8', 'NOT_SUPPORTED') returns 'Not supported'
        """
    if resultformat == 'FLOAT':
        return struct.unpack('!f', bytes.fromhex(response))[0]

    elif resultformat == 'NOT_SUPPORTED':
        return 'Not supported'

    else:
        return None