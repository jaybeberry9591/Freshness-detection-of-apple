import serial;
import time
ser=serial.Serial('COM10',9600,timeout=1);
time.sleep(1)
time.sleep(1)
ser.write(b'nourin');
time.sleep(1)
ser.close()


   
  
