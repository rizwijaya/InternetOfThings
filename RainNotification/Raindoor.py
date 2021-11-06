import RPi.GPIO as GPIO
import time

GPIO.setmod(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GBIO.setup(21, GPIO.OUT)
out = 21 # GPIO Pin dari si Solenoid Door Lock-nya
def solonoid_open(pin):  # Pintu terbuka
    GPIO.output(pin, GPIO.HIGH) 

def solonoid_closed(pin):  # Pintu tertutup
    GPIO.output(pin, GPIO.LOW)

def main():
    while True:

        if GPIO.input(18):  # Jika tidak hujan
            print("Tidak hujan")   
            solonoid_closed(out) # default akan menutup door lock (normally closed)
        else:  # Jika hujan
            print("Sudah, hujan")
            solonoid_open(out) # Jika terdapat tetesan (air) maka door lock terbuka (normally open)
        time.sleep(1)

if __name__ == '__main__' :
    try :
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()