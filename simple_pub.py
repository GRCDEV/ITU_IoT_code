import paho.mqtt.client as mqtt 
import time
import ufun


broker_addr = "test.mosquitto.org"

mqttc=mqtt.Client()
mqttc.connect(broker_addr, 1883, 60)

mqttc.loop_start()
while True:
    the_data = ufun.get_data_from_sensor()
    print("Publishing data", the_data)
    mqttc.publish("sensor/value", the_data)
    time.sleep(5)	# sleep for 5 seconds before next call

mqttc.loop_stop()
