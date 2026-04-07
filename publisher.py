#!/usr/bin/env python3
"""MQTT publisher that sends 'Gutentag, World!' to a broker.

Requires a running MQTT broker (e.g. mosquitto on localhost:1883).
Run: python3 publisher.py
"""
import paho.mqtt.client as mqtt

BROKER = 'localhost'
PORT = 1883
TOPIC = 'gutentag/world'
MESSAGE = 'Gutentag, World!'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.publish(TOPIC, MESSAGE)
        print(f'Published "{MESSAGE}" to topic "{TOPIC}"')
    else:
        print(f'Connection failed with code {rc}')
    client.disconnect()


client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)
client.loop_forever()
