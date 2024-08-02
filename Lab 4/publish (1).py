import paho.mqtt.publish as publish
import time
import board
import adafruit_dht

interval = 30 #Time between readings

##Start of credentials########################################

#ThingSpeak Channel ID (numeric id, not the name)
channel_ID = "<channel_id>" 			# your channel ID

# Your MQTT credentials for the Raspberry Pi
client_ID = "<client_id" 	# MQTT device ID
username = "<mqtt_username>" 	# MQTT device username
password = "<mqtt_password>" 	# MQTT device password

##End of your credentials#####################################

#For DHT-20, this won't be used
dhtDevice = adafruit_dht.DHT22(board.D12)

#hostname of the ThingSpeak MQTT broker
host = "mqtt3.thingspeak.com"

# Define the connection type as websockets and use port 80
t_transport = "websockets"
t_port = 80

# create a topic string to publish to the ThingSpeak channel
topic = "channels/" + channel_ID + "/publish"

while True:
	# Read Temperature and Humidity Values
	# If using DHT-20, this will be replaced by driver code
	try:
		temperature_c = dhtDevice.temperature
		humidity = dhtDevice.humidity
	except Exception as e:
		print(e)

	##Insert code to convert temperature_c to Fahrenheit
	temperature = temperature_c ##some equation

	payload = f"field1={temperature}&field2={humidity}"

# Publish Sensor Values
	try:
		publish.single(topic, payload, hostname=host, transport=t_transport, port=t_port, client_id=client_ID, auth={'username':username,'password':password})
		print("Temp: {:.1f} F, Humidity: {}% ".format(temperature, humidity))
		time.sleep(interval)
	except KeyboardInterrupt:
		print("Connection ended!")
		break
	except Exception as e:
		print (e)
		time.sleep(5)
