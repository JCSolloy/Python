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
    print('Conexión Modbus correcta')
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
    print('Conexión Modbus correcta')
else:
    print("Error de conexión")
