from pyModbusTCP.client import ModbusClient
#Modbus UCM316
c = ModbusClient(host="10.232.3.41", 
                 port=502,
                 unit_id=0,
                 debug=False,
                 auto_open=True, 
                 auto_close=True)

regs = c.read_holding_registers(4419, 10)

if regs:
    print(regs)
    print('UCM316 conexión Modbus correcta')
else:
    print("read error")

#Modbus Sensor de Nivel 
c = ModbusClient(host="10.232.3.40", 
                 port=7004,
                 unit_id=1,
                 debug=False,
                 auto_open=True, 
                 auto_close=True)

regs = c.read_holding_registers(5000, 10)

if regs:
    print(regs)
    print('Sensor de nivel FRM20 conexión Modbus correcta')
else:
    print("Error de conexión")

#Modbus Medidor ION8650
c = ModbusClient(host="10.232.0.53", 
                 port=503,
                 unit_id=1,
                 debug=False,
                 auto_open=True, 
                 auto_close=True)

regs = c.read_holding_registers(11, 10)

if regs:
    print(regs)
    print('Medidor ION8650 conexión Modbus correcta')
else:
    print("Error de conexión")
