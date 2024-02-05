from enum import Enum

class Commands(Enum):
    SERIAL_NUMBER = '0000'
    METER_ID = '0002'
    BAUD_RATE = '0003'
    SOFTWARE_VERSION = '0004'
    HARDWARE_VERSION = '0006'
    S0_OUTPUT_RATE = '0009'
    COMBINED_CODE = '000B'
    HOLIDAY_WEEKEND_T = '000C'
    CYCLE_TIME = '000D'
    L1_VOLTAGE = '000E'
    L2_VOLTAGE = '0010'
    L3_VOLTAGE = '0012'
    GRID_FREQUENCY = '0014'
    L1_CURRENT = '0016'
    L2_CURRENT = '0018'
    L3_CURRENT = '001A'
    TOTAL_ACTIVE_POWER = '001C'
    L1_ACTIVE_POWER = '001E'
    L2_ACTIVE_POWER = '0020'
    L3_ACTIVE_POWER = '0022'
    TOTAL_REACTIVE_POWER = '0024'
    L1_REACTIVE_POWER = '0026'
    L2_REACTIVE_POWER = '0028'
    L3_REACTIVE_POWER = '002A'
    TOTAL_APPARENT_POWER = '002C'
    L1_APPARENT_POWER = '002E'
    L2_APPARENT_POWER = '0030'
    L3_APPARENT_POWER = '0032'
    TOTAL_POWER_FACTOR = '0034'
    POWER_FACTOR = '0036'
    TIME = '003C'
    TIME_SWITCH = '0040'
    CRC_CODE = '0041'
    TOTAL_ACTIVE_ENERGY = '0100'
    L1_TOTAL_ACTIVE_ENERGY = '0102'
    L2_TOTAL_ACTIVE_ENERGY = '0104'
    L3_TOTAL_ACTIVE_ENERGY = '0106'
    FORWARD_ACTIVE_ENERGY = '0108'
    L1_FORWARD_ACTIVE_ENERGY = '010A'
    L2_FORWARD_ACTIVE_ENERGY = '010C'
    L3_FORWARD_ACTIVE_ENERGY = '010E'
    REVERSE_ACTIVE_ENERGY = '0110'
    L1_REVERSE_ACTIVE_ENERGY = '0112'
    L2_REVERSE_ACTIVE_ENERGY = '0114'
    L3_REVERSE_ACTIVE_ENERGY = '0116'
    TOTAL_REACTIVE_ENERGY = '0118'
    L1_REACTIVE_ENERGY = '011A'
    L2_REACTIVE_ENERGY = '011C'
    L3_REACTIVE_ENERGY = '011E'
    FORWARD_REACTIVE_ENERGY = '0120'
    L1_FORWARD_REACTIVE_ENERGY = '0122'
    L2_FORWARD_REACTIVE_ENERGY = '0124'
    L3_FORWARD_REACTIVE_ENERGY = '0126'
    REVERSE_REACTIVE_ENERGY = '0128'
    L1_REVERSE_REACTIVE_ENERGY = '012A'
    L2_REVERSE_REACTIVE_ENERGY = '012C'
    L3_REVERSE_REACTIVE_ENERGY = '012E'
    T1_TOTAL_ACTIVE_ENERGY = '0130'
    T1_FORWARD_ACTIVE_ENERGY = '0132'
    T1_REVERSE_ACTIVE_ENERGY = '0134'
    T1_TOTAL_REACTIVE_ENERGY = '0136'
    T1_FORWARD_REACTIVE_ENERGY = '0138'
    T1_REVERSE_REACTIVE_ENERGY = '013A'
    T2_TOTAL_ACTIVE_ENERGY = '013C'
    T2_FORWARD_ACTIVE_ENERGY = '013E'
    T2_REVERSE_ACTIVE_ENERGY = '0140'
    T2_TOTAL_REACTIVE_ENERGY = '0142'
    T2_FORWARD_REACTIVE_ENERGY = '0144'
    T2_REVERSE_REACTIVE_ENERGY = '0146'
    T3_TOTAL_ACTIVE_ENERGY = '0148'
    T3_FORWARD_ACTIVE_ENERGY = '014A'
    T3_REVERSE_ACTIVE_ENERGY = '014C'
    T3_TOTAL_REACTIVE_ENERGY = '014E'
    T3_FORWARD_REACTIVE_ENERGY = '0150'
    T3_REVERSE_REACTIVE_ENERGY = '0152'
    T4_TOTAL_ACTIVE_ENERGY = '0154'
    T4_FORWARD_ACTIVE_ENERGY = '0156'
    T4_REVERSE_ACTIVE_ENERGY = '0158'
    T4_TOTAL_REACTIVE_ENERGY = '015A'
    T4_FORWARD_REACTIVE_ENERGY = '015C'
    T4_REVERSE_REACTIVE_ENERGY = '015E'
    TIME_INTERVAL_1 = '0300'
    TIME_INTERVAL_2 = '030C'
    TIME_INTERVAL_3 = '0318'
    TIME_INTERVAL_4 = '0324'
    TIME_INTERVAL_5 = '0330'
    TIME_INTERVAL_6 = '033C'
    TIME_INTERVAL_7 = '0348'
    TIME_INTERVAL_8 = '0354'
    TIME_ZONE = '0360'
    SO_OUTPUT = '0009'

class CommandLenght(Enum):
    SERIAL_NUMBER = '02'
    METER_ID = '01'
    BAUD_RATE = '01'
    SOFTWARE_VERSION = '02'
    HARDWARE_VERSION = '02'
    S0_OUTPUT_RATE = '02'
    COMBINED_CODE = '01'
    HOLIDAY_WEEKEND_T = '01'
    CYCLE_TIME = '01'
    L1_VOLTAGE = '02'
    L2_VOLTAGE = '02'
    L3_VOLTAGE = '02'
    GRID_FREQUENCY = '02'
    L1_CURRENT = '02'
    L2_CURRENT = '02'
    L3_CURRENT = '02'
    TOTAL_ACTIVE_POWER = '02'
    L1_ACTIVE_POWER = '02'
    L2_ACTIVE_POWER = '02'
    L3_ACTIVE_POWER = '02'
    TOTAL_REACTIVE_POWER = '02'
    L1_REACTIVE_POWER = '02'
    L2_REACTIVE_POWER = '02'
    L3_REACTIVE_POWER = '02'
    TOTAL_APPARENT_POWER = '02'
    L1_APPARENT_POWER = '02'
    L2_APPARENT_POWER = '02'
    L3_APPARENT_POWER = '02'
    TOTAL_POWER_FACTOR = '02'
    POWER_FACTOR = '02'
    TIME = '04'
    TIME_SWITCH = '01'
    CRC_CODE = '01'
    TOTAL_ACTIVE_ENERGY = '02'
    L1_TOTAL_ACTIVE_ENERGY = '02'
    L2_TOTAL_ACTIVE_ENERGY = '02'
    L3_TOTAL_ACTIVE_ENERGY = '02'
    FORWARD_ACTIVE_ENERGY = '02'
    L1_FORWARD_ACTIVE_ENERGY = '02'
    L2_FORWARD_ACTIVE_ENERGY = '02'
    L3_FORWARD_ACTIVE_ENERGY = '02'
    REVERSE_ACTIVE_ENERGY = '02'
    L1_REVERSE_ACTIVE_ENERGY = '02'
    L2_REVERSE_ACTIVE_ENERGY = '02'
    L3_REVERSE_ACTIVE_ENERGY = '02'
    TOTAL_REACTIVE_ENERGY = '02'
    L1_REACTIVE_ENERGY = '02'
    L2_REACTIVE_ENERGY = '02'
    L3_REACTIVE_ENERGY = '02'
    FORWARD_REACTIVE_ENERGY = '02'
    L1_FORWARD_REACTIVE_ENERGY = '02'
    L2_FORWARD_REACTIVE_ENERGY = '02'
    L3_FORWARD_REACTIVE_ENERGY = '02'
    REVERSE_REACTIVE_ENERGY = '02'
    L1_REVERSE_REACTIVE_ENERGY = '02'
    L2_REVERSE_REACTIVE_ENERGY = '02'
    L3_REVERSE_REACTIVE_ENERGY = '02'
    T1_TOTAL_ACTIVE_ENERGY = '02'
    T1_FORWARD_ACTIVE_ENERGY = '02'
    T1_REVERSE_ACTIVE_ENERGY = '02'
    T1_TOTAL_REACTIVE_ENERGY = '02'
    T1_FORWARD_REACTIVE_ENERGY = '02'
    T1_REVERSE_REACTIVE_ENERGY = '02'
    T2_TOTAL_ACTIVE_ENERGY = '02'
    T2_FORWARD_ACTIVE_ENERGY = '02'
    T2_REVERSE_ACTIVE_ENERGY = '02'
    T2_TOTAL_REACTIVE_ENERGY = '02'
    T2_FORWARD_REACTIVE_ENERGY = '02'
    T2_REVERSE_REACTIVE_ENERGY = '02'
    T3_TOTAL_ACTIVE_ENERGY = '02'
    T3_FORWARD_ACTIVE_ENERGY = '02'
    T3_REVERSE_ACTIVE_ENERGY = '02'
    T3_TOTAL_REACTIVE_ENERGY = '02'
    T3_FORWARD_REACTIVE_ENERGY = '02'
    T3_REVERSE_REACTIVE_ENERGY = '02'
    T4_TOTAL_ACTIVE_ENERGY = '02'
    T4_FORWARD_ACTIVE_ENERGY = '02'
    T4_REVERSE_ACTIVE_ENERGY = '02'
    T4_TOTAL_REACTIVE_ENERGY = '02'
    T4_FORWARD_REACTIVE_ENERGY = '02'
    T4_REVERSE_REACTIVE_ENERGY = '02'
    TIME_INTERVAL_1 = '12'
    TIME_INTERVAL_2 = '12'
    TIME_INTERVAL_3 = '12'
    TIME_INTERVAL_4 = '12'
    TIME_INTERVAL_5 = '12'
    TIME_INTERVAL_6 = '12'
    TIME_INTERVAL_7 = '12'
    TIME_INTERVAL_8 = '12'
    TIME_ZONE = '12'
    SO_OUTPUT = '02'

class ResultFormat(Enum):
    SERIAL_NUMBER = 'NOT_SUPPORTED'
    METER_ID = 'NOT_SUPPORTED'
    BAUD_RATE = 'NOT_SUPPORTED'
    SOFTWARE_VERSION = 'FLOAT'
    HARDWARE_VERSION = 'FLOAT'
    S0_OUTPUT_RATE = 'FLOAT'
    COMBINED_CODE = 'NOT_SUPPORTED'
    HOLIDAY_WEEKEND_T = 'NOT_SUPPORTED'
    CYCLE_TIME = 'NOT_SUPPORTED'
    L1_VOLTAGE = 'FLOAT'
    L2_VOLTAGE = 'FLOAT'
    L3_VOLTAGE = 'FLOAT'
    GRID_FREQUENCY = 'FLOAT'
    L1_CURRENT = 'FLOAT'
    L2_CURRENT = 'FLOAT'
    L3_CURRENT = 'FLOAT'
    TOTAL_ACTIVE_POWER = 'FLOAT'
    L1_ACTIVE_POWER = 'FLOAT'
    L2_ACTIVE_POWER = 'FLOAT'
    L3_ACTIVE_POWER = 'FLOAT'
    TOTAL_REACTIVE_POWER = 'FLOAT'
    L1_REACTIVE_POWER = 'FLOAT'
    L2_REACTIVE_POWER = 'FLOAT'
    L3_REACTIVE_POWER = 'FLOAT'
    TOTAL_APPARENT_POWER = 'FLOAT'
    L1_APPARENT_POWER = 'FLOAT'
    L2_APPARENT_POWER = 'FLOAT'
    L3_APPARENT_POWER = 'FLOAT'
    TOTAL_POWER_FACTOR = 'FLOAT'
    POWER_FACTOR = 'FLOAT'
    TIME = 'NOT_SUPPORTED'
    TIME_SWITCH = 'NOT_SUPPORTED'
    CRC_CODE = 'NOT_SUPPORTED'
    TOTAL_ACTIVE_ENERGY = 'FLOAT'
    L1_TOTAL_ACTIVE_ENERGY = 'FLOAT'
    L2_TOTAL_ACTIVE_ENERGY = 'FLOAT'
    L3_TOTAL_ACTIVE_ENERGY = 'FLOAT'
    FORWARD_ACTIVE_ENERGY = 'FLOAT'
    L1_FORWARD_ACTIVE_ENERGY = 'FLOAT'
    L2_FORWARD_ACTIVE_ENERGY = 'FLOAT'
    L3_FORWARD_ACTIVE_ENERGY = 'FLOAT'
    REVERSE_ACTIVE_ENERGY = 'FLOAT'
    L1_REVERSE_ACTIVE_ENERGY = 'FLOAT'
    L2_REVERSE_ACTIVE_ENERGY = 'FLOAT'
    L3_REVERSE_ACTIVE_ENERGY = 'FLOAT'
    TOTAL_REACTIVE_ENERGY = 'FLOAT'
    L1_REACTIVE_ENERGY = 'FLOAT'
    L2_REACTIVE_ENERGY = 'FLOAT'
    L3_REACTIVE_ENERGY = 'FLOAT'
    FORWARD_REACTIVE_ENERGY = 'FLOAT'
    L1_FORWARD_REACTIVE_ENERGY = 'FLOAT'
    L2_FORWARD_REACTIVE_ENERGY = 'FLOAT'
    L3_FORWARD_REACTIVE_ENERGY = 'FLOAT'
    REVERSE_REACTIVE_ENERGY = 'FLOAT'
    L1_REVERSE_REACTIVE_ENERGY = 'FLOAT'
    L2_REVERSE_REACTIVE_ENERGY = 'FLOAT'
    L3_REVERSE_REACTIVE_ENERGY = 'FLOAT'
    T1_TOTAL_ACTIVE_ENERGY = 'FLOAT'
    T1_FORWARD_ACTIVE_ENERGY = 'FLOAT'
    T1_REVERSE_ACTIVE_ENERGY = 'FLOAT'
    T1_TOTAL_REACTIVE_ENERGY = 'FLOAT'
    T1_FORWARD_REACTIVE_ENERGY = 'FLOAT'
    T1_REVERSE_REACTIVE_ENERGY = 'FLOAT'
    T2_TOTAL_ACTIVE_ENERGY = 'FLOAT'
    T2_FORWARD_ACTIVE_ENERGY = 'FLOAT'
    T2_REVERSE_ACTIVE_ENERGY = 'FLOAT'
    T2_TOTAL_REACTIVE_ENERGY = 'FLOAT'
    T2_FORWARD_REACTIVE_ENERGY = 'FLOAT'
    T2_REVERSE_REACTIVE_ENERGY = 'FLOAT'
    T3_TOTAL_ACTIVE_ENERGY = 'FLOAT'
    T3_FORWARD_ACTIVE_ENERGY = 'FLOAT'
    T3_REVERSE_ACTIVE_ENERGY = 'FLOAT'
    T3_TOTAL_REACTIVE_ENERGY = 'FLOAT'
    T3_FORWARD_REACTIVE_ENERGY = 'FLOAT'
    T3_REVERSE_REACTIVE_ENERGY = 'FLOAT'
    T4_TOTAL_ACTIVE_ENERGY = 'FLOAT'
    T4_FORWARD_ACTIVE_ENERGY = 'FLOAT'
    T4_REVERSE_ACTIVE_ENERGY = 'FLOAT'
    T4_TOTAL_REACTIVE_ENERGY = 'FLOAT'
    T4_FORWARD_REACTIVE_ENERGY = 'FLOAT'
    T4_REVERSE_REACTIVE_ENERGY = 'FLOAT'
    TIME_INTERVAL_1 = 'NOT_SUPPORTED'
    TIME_INTERVAL_2 = 'NOT_SUPPORTED'
    TIME_INTERVAL_3 = 'NOT_SUPPORTED'
    TIME_INTERVAL_4 = 'NOT_SUPPORTED'
    TIME_INTERVAL_5 = 'NOT_SUPPORTED'
    TIME_INTERVAL_6 = 'NOT_SUPPORTED'
    TIME_INTERVAL_7 = 'NOT_SUPPORTED'
    TIME_INTERVAL_8 = 'NOT_SUPPORTED'
    TIME_ZONE = 'NOT_SUPPORTED'
    SO_OUTPUT = 'FLOAT'

