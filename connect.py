#Code for connection to MQTT
import paho.mqtt.client as mqtt
from loop import WebSocket

broker= "192.168.1.160"  
port = 1883                         
username = "getparking"                   
password = "playtmbiz"   
#Subscribe to two topics where loop/ will receive "en/ex" and reconnected/ will receive "A/B-count"   
topic =  [("boom/",1),("connect/",1)]
client_id = "WebSocket"

websocket = None

# The callback for when the client receives a  response from the server.
def on_connect(client, level, userdata, flags,):
    print("Connected")
    global websocket
    websocket = WebSocket(client)
    client.subscribe(topic)
    client.publish("connect/","Connected",qos=1)
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
   websocket.processMessage(msg)


client = mqtt.Client(client_id=client_id,clean_session=False)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.loop_forever()


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.