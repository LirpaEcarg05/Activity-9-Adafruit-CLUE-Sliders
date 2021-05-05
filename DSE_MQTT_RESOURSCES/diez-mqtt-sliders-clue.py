from adafruit_clue import clue
import paho.mqtt.client as mqtt

# displaying all the text from index 0 to index 7
def display_text(clueValue):
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*(clueValue["clueSlider/accelXRange"], clueValue["clueSlider/accelYRange"], clueValue["clueSlider/accelZRange"]))
    clue_data[1].text = "Gyro: {} {} {} dps".format(*(clueValue["clueSlider/gyroXRange"], clueValue["clueSlider/gyroYRange"], clueValue["clueSlider/gyroZRange"]))
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*(clueValue["clueSlider/magneticXRange"], clueValue["clueSlider/magneticYRange"], clueValue["clueSlider/magneticZRange"]))
    clue_data[3].text = "Pressure: {} hPa".format(clueValue["clueSlider/pressureRange"])
    clue_data[4].text = "Temperature: {} C".format(clueValue["clueSlider/tempRange"])
    clue_data[5].text = "Humidity: {} %".format(clueValue["clueSlider/humidityRange"])
    clue_data[6].text = "Proximity: {}".format(clueValue["clueSlider/proximityRange"])
    clue_data[7].text = "Color: R:{}G:{}B:{}C:{}".format(*(clueValue["clueSlider/colorRRange"], clueValue["clueSlider/colorGRange"], clueValue["clueSlider/colorBRange"], clueValue["clueSlider/colorCRange"]))
    clue_data.show()
    
#the clue slider range 
clueData = {
    "clueSlider/accelXRange" : 0,
    "clueSlider/accelYRange" : 0,
    "clueSlider/accelZRange" : 0,
    "clueSlider/gyroXRange" : 0,
    "clueSlider/gyroYRange" : 0,
    "clueSlider/gyroZRange" : 0,
    "clueSlider/magneticXRange" : 0,
    "clueSlider/magneticYRange" : 0,
    "clueSlider/magneticZRange" : 0,
    "clueSlider/pressureRange" : clue.pressure,
    "clueSlider/tempRange" : clue.temperature,
    "clueSlider/humidityRange" : clue.humidity,
    "clueSlider/proximityRange" : clue.proximity,
    "clueSlider/colorRRange" : 0,
    "clueSlider/colorGRange" : 0,
    "clueSlider/colorBRange" : 0,
    "clueSlider/colorCRange" : 0
}


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("clueSlider/#")
        display_text(clueData)

def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload.decode())
    clueData[msg.topic]= msg.payload.decode()
    display_text(clueData)

clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()