#!/usr/bin/env python
import time
import os

import requests
import urllib.parse

import paho.mqtt.client as mqtt


mqtt_host = os.environ.get('MQTT_HOST', 'mqtt.core.bckspc.de')
mqtt_user = os.environ.get('MQTT_USER', None)
mqtt_pass = os.environ.get('MQTT_PASS', None)
mqtt_port = os.environ.get('MQTT_PORT', 1883)
ps3_host= os.environ.get('PS3_HOST', 'ps3.core.bckspc.de')

if mqtt_user is not None:
    mqtt.username_pw_set(mqtt_user, mqtt_pass)

def on_connect(client, userdata, flags, rc):
    client.subscribe("psa/alarm")
    client.subscribe("sensor/door/frame")
    client.subscribe("sensor/door/bell")
    print("Connected to mqtt with result code " + str(rc))

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    soundfile = None
    if topic == "psa/alarm":
        requests.get('http://' + ps3_host + '/notify.ps3mapi?msg=' + urllib.parse.quote(payload))
        requests.get('http://' + ps3_host + '/buzzer.ps3mapi?mode=3')
    elif topic == "sensor/door/frame" and payload == "open":
        requests.get('http://' + ps3_host + '/notify.ps3mapi?msg=' + urllib.parse.quote('DOOR OPENED'))
        requests.get('http://' + ps3_host + '/buzzer.ps3mapi?mode=3')
    elif topic == "sensor/door/bell" and payload == "pressed":
        requests.get('http://' + ps3_host + '/notify.ps3mapi?msg=' + urllib.parse.quote('DOOR BELL'))
        requests.get('http://' + ps3_host + '/buzzer.ps3mapi?mode=3')
    print("RECEIVED: " + topic + '  ' + payload)

client = mqtt.Client()
client.on_connect = on_connect

client.connect(mqtt_host, mqtt_port, 60)
client.on_message = on_message
client.loop_start()

while True:
    time.sleep(2)
