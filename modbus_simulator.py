from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.device import ModbusDeviceIdentification

import threading
import time
import random
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.ERROR)

# Create the data block with 101 values (registers 0–100)
hr_data = [0]*100 + [1234]
block = ModbusSequentialDataBlock(0, hr_data)

# Shared context
store = ModbusSlaveContext(hr=block)
context = ModbusServerContext(slaves=store, single=True)

# Background thread to update register 100 every 2 seconds
def update_register():
    while True:
        new_value = random.randint(1000, 9999)
        context[0].setValues(3, 100, [new_value])  # 3 = holding registers
        print(f"🛠️  Updated register 100 to: {new_value}")
        time.sleep(2)

# Device identity (optional)
identity = ModbusDeviceIdentification()
identity.VendorName = "SimPLC"
identity.ProductName = "Dynamic Python Simulator"
identity.ModelName = "PM-Sim"
identity.MajorMinorRevision = "1.1"

# Start background thread
thread = threading.Thread(target=update_register, daemon=True)
thread.start()

# Start server
print("✅ Modbus Simulator running on 127.0.0.1:5020...")
StartTcpServer(context, identity=identity, address=("127.0.0.1", 5020))

