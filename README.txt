This is a code to manually operate a boombarrier using MQTT.
In this code the device (in this case Orange Pi) will connect to the available MQTT connection and listen to a topic.
The sensor present in the ground will sense the presence of vehicle and send a msg on the subscribed topic. Whereas this device will listen to topic and act accordingly. 
If the msg mentions "OPEN" the device will send a signal to manually open the barrier and if the msg mentions "CLOSE" the barrier will close.
Here you can see two python files. The connect.py file is to connect the device to the mentioned MQTT connection
The other file listens to the topic, decodes the received msg and sends signals accordingly. 
The connect.py will work in loop always and reconnect incase of lost connectivity.
