import os 
import time
from datetime import datetime
from pymodbus.client import ModbusTcpClient
import csv

# Show startup message
os.system('clear') # optional: clears the terminal
print("=========================================")
print(" 🔧 Modbus TCP Data Logger Starting Up")
print(" 📅", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(" ✅ Logging every 5 seconds")
print("=========================================\n")

PLC_IP = "127.0.0.1"
PLC_PORT = 5020

client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
connection = client.connect()

if connection:
    print("✅ Connected to simulator.")

    try:
        while True:
            # ✅ Keyword arguments required in pymodbus 3+
            result = client.read_holding_registers(address=100, count=1)

            if not result.isError():
                value = result.registers[0]
                print(f"📦 Register 100 value: {value}")
            else:
                print("❌ Error reading register.")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")

    finally:
        client.close()
        print("🔌 Connection closed.")

else:
    print("❌ Could not connect to simulator.")