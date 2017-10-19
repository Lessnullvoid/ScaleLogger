import serial, time

ser = serial.Serial('/dev/tty.usbserial-DN02G2ES', 9600)
par = serial.PARITY_NONE
bits =  serial.EIGHTBITS

while 1:
    serial_line = ser.readline()

    print(serial_line) # If using Python 2.x use: print serial_line
    # Do some other work on the data

    time.sleep(300) # sleep 5 minutes

    # Loop restarts once the sleep is finished

ser.close() # Only executes once the loop exits
