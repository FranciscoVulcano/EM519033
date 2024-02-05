import time
from EM519033.EM519033 import EM519033
from EM519033 import parameters
from colorama import init, Fore, Style
import argparse

init(autoreset=True)  # Initialize colorama


def display_meter_data(meter):
    try:
        print(f"{Fore.YELLOW}{Style.BRIGHT}EM118090 Power Meter Test{Style.RESET_ALL}")
        print("\nLoading...", end="", flush=True)

        while True:
            voltage1 = meter.get_value(1, parameters.MeterParameters.L1_VOLTAGE)
            voltage2 = meter.get_value(1, parameters.MeterParameters.L2_VOLTAGE)
            voltage3 = meter.get_value(1, parameters.MeterParameters.L3_VOLTAGE)
            current1 = meter.get_value(1, parameters.MeterParameters.L1_CURRENT)
            current2 = meter.get_value(1, parameters.MeterParameters.L2_CURRENT)
            current3 = meter.get_value(1, parameters.MeterParameters.L3_CURRENT)
            frequency = meter.get_value(1, parameters.MeterParameters.GRID_FREQUENCY)
            power = meter.get_value(1, parameters.MeterParameters.TOTAL_ACTIVE_POWER)
            print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)

            print(f"{Fore.YELLOW}{Style.BRIGHT}EM118090 Power Meter Test{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Voltage L1:{Style.RESET_ALL} {voltage1} V {Fore.GREEN}Voltage L2:{Style.RESET_ALL} {voltage2} V {Fore.GREEN}Voltage L3:{Style.RESET_ALL} {voltage3} V")
            print(f"{Fore.BLUE}Current L1:{Style.RESET_ALL} {current1} A {Fore.BLUE}Current L2:{Style.RESET_ALL} {current2} A {Fore.BLUE}Current L3:{Style.RESET_ALL} {current3} A")
            print(f"{Fore.CYAN}Frequency:{Style.RESET_ALL} {frequency} Hz")
            print(f"{Fore.MAGENTA}Power:{Style.RESET_ALL} {power} kWh")
            print(f"\n{Fore.WHITE}Press 'Ctrl+C' to exit{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)
        print(f"{Fore.RED}{Style.BRIGHT}Exiting...{Style.RESET_ALL}")
        time.sleep(1)
        print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)
        exit()

    except:
        print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)
        print(f"{Fore.RED}{Style.BRIGHT}Somethig went wrong.{Style.RESET_ALL}")
        print(f"{Fore.RED}{Style.BRIGHT}Exiting...{Style.RESET_ALL}")
        time.sleep(1)  # Simulate an exit animation
        print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)
        exit()

def main():
    parser = argparse.ArgumentParser(description='Simple command line tool to test EM519033.')
    parser.add_argument('--port', type=str, help='Port to communicate to the device', required=True)
    args = parser.parse_args()

    meter = EM519033(port=args.port)
    display_meter_data(meter)

if __name__ == "__main__":
    main()
