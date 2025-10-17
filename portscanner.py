#!/usr/bin/python

import socket
import asyncio


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("[*] Enter The Host To Scan ")
choise = int(input("[*] 1) Input Port\n[*] 2) Scan All Ports (More Time)\n"))

def portscanner_auto(host, timeout=3.0):
    for port in range(65536):
        try:
            with socket.create_connection((host, port), timeout):
                print(f"Port {port} is open")
        except (socket.timeout, ConnectionRefusedError):
            print(f"Port {port} is closed")
        except OSError as e:
            print(f"Port {port} - error: {e}")

def portscanner_hand(host, timeout=3.0):
    port = int(input("[*] Enter The Port To Scan "))
    try:
        with socket.create_connection((host, port), timeout):
            print(f"Port {port} is open")
    except (socket.timeout, ConnectionRefusedError):
        print(f"Port {port} is closed")
    except OSError as e:
        print(f"Port {port} - error: {e}")


if __name__ == "__main__":
    if choise == 1:
        portscanner_hand(host)
    elif choise == 2:
        portscanner_auto(host)
    else:
        print("Wrong Input!")