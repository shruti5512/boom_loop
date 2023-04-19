import datetime
from time import sleep          # this lets us have a time delay
from pyA20.gpio import gpio
from pyA20.gpio import port
from threading import Timer

barrier_topic = "barrierex1/"

bbOpen = port.PA18
bbClose = port.PA19
# pinConnect = port.PA3
gpio.init()
gpio.setcfg(bbOpen, gpio.OUTPUT)
gpio.setcfg(bbClose, gpio.OUTPUT)

class WebSocket():
    def __init__(self,mqclient):
        self.client = mqclient


    def processMessage(self,msg):
        # print(msg.topic+" "+str(msg.payload))
            message= msg.payload.decode()
            rcvdData =  message
            print(rcvdData)
            ackData = "ACK" + rcvdData
            if message.startswith("OPEN") :
                gpio.output(bbOpen, 0)
                print("Open barrier")
                sleep(0.5)
                gpio.output(bbOpen, 1)
   
            elif(rcvdData == "CLOSE"):
                    gpio.output(bbClose, 0)
                    print("Close barrier")
                    sleep(0.5)
                    gpio.output(bbClose, 1)
            else:
                print("Error")

   