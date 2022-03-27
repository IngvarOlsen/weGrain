from time import sleep
from ulora import LoRa, ModemConfig, SPIConfig
import dht
import machine
from machine import Pin, ADC

# based on https://github.com/martynwheeler/u-lora

# PINOUT 
# RFM9X <--> ESP32 WROOM-32D
# VIN <--> 3v3
# GND <--> GND
# G0 <--> GPIO 0 (CAN BLOCK FROM FILESYSTEM ESP32 WHILE INSERTED)
# SCK <--> GPIO 14
# MISO <--> GPIO 12
# MOSI <--> GPIO 13
# CS <--> GPIO 5
# Lora Parameters

sensor = dht.DHT22(Pin(4))
batRead = ADC(Pin(34))

RFM95_RST = 27
RFM95_SPIBUS = SPIConfig.esp32_1
RFM95_CS = 5
RFM95_INT = 0
RF95_FREQ = 869.0
RF95_POW = 20
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 222

# initialise radio
lora = LoRa(RFM95_SPIBUS, RFM95_INT, CLIENT_ADDRESS, RFM95_CS, reset_pin=RFM95_RST, freq=RF95_FREQ, tx_power=RF95_POW, acks=True)


#ContainerId needs to be hard set
containerId = 2

while True:
    sensor.measure()
    #Battery level will be sent in next iteration
    batRead_value = batRead.read()
    #Temp, hum, containerID
    dataToSend = str(sensor.temperature()) + " , " + str(sensor.humidity()) + " , " + str(containerId) 
    print(dataToSend)
    lora.send_to_wait("30, 20, 2", SERVER_ADDRESS)
    # print("sent")
    sleep(10)
    #Needs to add logic which puts the esp32 into deepSleep once packet have been recived or the packets have been sent a couple of times
    #machine.deepsleep(100000)     #10000ms sleep time

