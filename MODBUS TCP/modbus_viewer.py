#documentazione #https://pymodbus.readthedocs.io/en/latest/source/client.html
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
import struct, time
# --- Configuration ---
PLC_IP = "192.168.1.36"   # ESP32's IP
PLC_PORT = 502            # default Modbus/TCP port
SLAVE_ID=1
DWORD = 2
WORD =1
BOOL =1

# --- Connect to PLC ---
client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
client.connect()

while(1):
    holding_regs_results = client.read_holding_registers(address=0, count=4,device_id=SLAVE_ID) 
    input_regs_results = client.read_input_registers(address=0, count=16, device_id=SLAVE_ID)
    discrete_inputs_result = client.read_discrete_inputs(address=1, count=BOOL, device_id=SLAVE_ID)
    coils_result = client.read_coils(address=3,count=BOOL,device_id=SLAVE_ID)
    def read_md_float(md_number):
        starting_address = md_number + 2  # each MD occupies 2 Modbus registers
        rr = client.read_holding_registers(starting_address, DWORD, device_id=SLAVE_ID)
        if rr.isError():
            print(f"Error reading MD{md_number}")
            return None

        # Decode 32-bit float
        decoder = BinaryPayloadDecoder.fromRegisters(
            rr.registers,
            byteorder=Endian.Big,   # byte order
            wordorder=Endian.Big    # word order
        )
        value = decoder.decode_32bit_float()
        return value
    md0 = read_md_float(50)
    md2= read_md_float(54)
    md4= read_md_float(58)
    if not holding_regs_results.isError() and not input_regs_results.isError() and not discrete_inputs_result.isError() and not coils_result.isError(): 
        hold_regs = holding_regs_results.registers
        input_regs = holding_regs_results.registers
        discrete = int(discrete_inputs_result.bits[0])
        coil = int(coils_result.bits[0])
        hold_reg =int(holding_regs_results.registers[0])
        input_reg =int(input_regs_results.registers[0])
       
        print("BTN(%IX0.1): ", not(discrete), "| LED(%QX0.3): ", not(not(coil)), "| POT_ADC_raw(%IW0.0):", input_reg,
              "| LED_DAC_avg(%QW0.0):", hold_reg,"| MD0:", md0,"| MD2:", md2,"| MD4:", md4)
    else:
        print("Error reading modbus data")
    time.sleep(0.5)
#client.close()


