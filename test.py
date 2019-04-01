#!/usr/bin/python
# -*- coding: utf8 -*-

import paho.mqtt.client as mqtt

BROKER_ADDRESS = "test.mosquitto.org"
BROKER_PORT = 1883
BROKER_KEEPALIVE = 60

BROKER_TOPIC = "$SYS/broker/publish/messages/#"

def on_connect(client, userdata, flags, rc):
    client.subscribe(BROKER_TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    with open('test.txt','a+') as f:
        f.write("Message received: "  + msg.payload + "\n")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, BROKER_PORT, BROKER_KEEPALIVE)

print(100*'\n')
print(25*'#')
print("Informações do broker:")
print("Endereco: ", BROKER_ADDRESS)
print("Porta: ", BROKER_PORT)
print("Tempo de vida: ", BROKER_KEEPALIVE)
print(25*'#')
print('\n')
print("Conectando ao broker... \n")

client.loop_forever()
