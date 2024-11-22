#!/usr/bin/env python3
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
    parser = argparse.ArgumentParser(description='Ajuste a temperatura da cor do monitor')
    parser.add_argument('temperature', choices=['warm', 'cool', 'normal'], help='Temperatura da cor desejada')
    parser.add_argument('-m', '--monitor', help='Monitor específico para ajustar a temperatura da cor')
    args = parser.parse_args()

    monitors = get_active_monitors()

    if args.monitor:
        if args.monitor in monitors:
            adjust_color_temperature(args.temperature, args.monitor)
        else:
            print(f"O monitor '{args.monitor}' não está ativo.")
    else:
        if len(monitors) == 1:
            adjust_color_temperature(args.temperature, monitors[0])
        else:
            print("Vários monitores ativos encontrados:")
            for i, monitor in enumerate(monitors, start=1):
                print(f"{i}. {monitor}")
            choice = input("Selecione o número do monitor para ajustar a temperatura da cor: ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(monitors):
                    adjust_color_temperature(args.temperature, monitors[index])
                else:
                    print("Número de monitor inválido.")
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir um número.")