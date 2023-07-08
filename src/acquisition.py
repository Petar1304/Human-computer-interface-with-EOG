import serial

# port for arduino
PORT = '/dev/ttyUSB0'

def open_serial():
    baud_rate = 9600
    try:
        ser = serial.Serial(PORT, baud_rate)
        return ser
    except:
        print("Couldn't establish connection with Arduino")

def process_data(data):
    data_list = data.strip().split(',')
    data = []
    data[0] = int(data_list[0]) * 5 / 1023
    data[1] = int(data_list[1]) * 5 / 1023
    return data

def readData():
    '''
    returns data in a list [ch1, ch2]
    '''
    ser = open_serial()
    arduino_data = ser.readline()
    data = process_data(arduino_data.decode(encoding='ascii', errors='ignore'))
    return data

