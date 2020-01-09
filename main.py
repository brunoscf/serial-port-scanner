import serial.tools.list_ports

def run():
    """
    Show all available com ports
    """
    available_ports = serial.tools.list_ports.comports()

    if available_ports:
        print("---AVAILABLE COM PORTS---")
        for port in available_ports:
            print(port.device)
    else:
        print("---NO COM PORT AVAILABLE---")


if __name__ == "__main__":
    run()