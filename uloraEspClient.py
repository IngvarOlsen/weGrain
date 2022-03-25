from time import sleep
from ulora import LoRa, ModemConfig, SPIConfig
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

# loop and send data
while True:
    lora.send_to_wait("Insert data here", SERVER_ADDRESS)
    print("sent")
    ## XXXXX Deep sleep 1 hour
    sleep(1)
