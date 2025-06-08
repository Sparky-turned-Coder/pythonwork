from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.device import ModbusDeviceIdentification

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.ERROR)

# ✅ This puts 1234 into register 100
hr_data = [0]*100 + [1234]

store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, hr_data)  # start at address 0
)

context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = "SimPLC"
identity.ProductCode = "PM"
identity.ProductName = "PythonSimulatedPLC"
identity.ModelName = "PM-Sim"
identity.MajorMinorRevision = "1.0"

print("✅ Modbus Simulator running on 127.0.0.1:5020...")
StartTcpServer(context, identity=identity, address=("127.0.0.1", 5020))
