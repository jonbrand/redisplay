#!/usr/bin/env python3
import sys
import argparse
import subprocess

def get_active_monitors():
    output = subprocess.check_output(['xrandr', '--listmonitors']).decode('utf-8')
    lines = output.strip().split('\n')
    monitors = []
    for line in lines[1:]:
        monitor_info = line.strip().split()
        if len(monitor_info) > 3:
            monitors.append(monitor_info[3])
    return monitors

def adjust_color_temperature(temperature, monitor):
    if temperature == 'warm':
        red, green, blue = 1.4, 1.0, 0.75
    elif temperature == 'cool':
        red, green, blue = 0.9, 1.0, 1.1
    else:
        red, green, blue = 1.0, 1.0, 1.0

    subprocess.run(['xrandr', '--output', monitor, '--gamma', f'{red}:{green}:{blue}'])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: redisplay <command> [options]")
        print("Commands:")
        print("  warm      Set color temperature to warm")
        print("  cool      Set color temperature to cool")
        print("  normal    Set color temperature to normal")
        sys.exit(1)

    command = sys.argv[1]
    if command not in ['warm', 'cool', 'normal']:
        print(f"Invalid command: {command}")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Adjust monitor color temperature')
    parser.add_argument('-m', '--monitor', help='Specific monitor to adjust color temperature')
    args = parser.parse_args(sys.argv[2:])

    monitors = get_active_monitors()

    if args.monitor:
        if args.monitor in monitors:
            adjust_color_temperature(command, args.monitor)
        else:
            print(f"The monitor '{args.monitor}' is not active.")
    else:
        if len(monitors) == 1:
            adjust_color_temperature(command, monitors[0])
        else:
            print("Multiple active monitors found:")
            for i, monitor in enumerate(monitors, start=1):
                print(f"{i}. {monitor}")
            choice = input("Select the monitor number to adjust color temperature: ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(monitors):
                    adjust_color_temperature(command, monitors[index])
                else:
                    print("Invalid monitor number.")
            except ValueError:
                print("Invalid input. Please enter a number.")