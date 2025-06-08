from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
from datetime import datetime
import csv
import time
import os

PLC_IP = "127.0.0.1"
PLC_PORT = 5020
REGISTER = 100
LOG_FILE = "data_log.csv"


def log_register_value(register: int, value: int) -> None:
    """Append timestamped register value to CSV."""
    timestamp = datetime.now().isoformat(timespec='seconds')
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, register, value])
    print(f"📝 Logged: {timestamp}, Register {register}, Value {value}")


def ensure_log_file_exists() -> None:
    """Create the CSV log file with headers if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "register", "value"])
        print(f"📁 Created new log file: {LOG_FILE}")


def main() -> None:
    client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
    if not client.connect():
        print("❌ Unable to connect to Modbus server.")
        return

    print("✅ Connected to Modbus server.")
    ensure_log_file_exists()

    try:
        while True:
            result = client.read_holding_registers(address=REGISTER, count=1)
            if result.isError():
                print("⚠️  Error reading register.")
            else:
                value = result.registers[0]
                log_register_value(REGISTER, value)

            time.sleep(2)

    except KeyboardInterrupt:
        print("\n🛑 Logging stopped by user.")

    finally:
        client.close()
        print("🔌 Disconnected from Modbus server.")


if __name__ == "__main__":
    main()
