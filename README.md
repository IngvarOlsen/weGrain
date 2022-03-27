# weGrain
School iot project. We make a battery powered esp32 solution which can record humidity via a DHT22, sends it with LoRa to a battery powered Raspberry Pi Zero which hosts a Flask app. The App has a python and sqlite3 backend, which then gets used on a user interface, which shows pie and line charts of the data.
Right now it's in the prototype stage. The idea of the project was to help farmers in Africa monitor temperature and humidity of their harvested foods to better avoid contamination, excess humidity and overall quality 


## Linux setup

### 1. Run update and upgrade and install git
```
sudo apt update
sudo apt upgrade
sudo apt-get install git
```

### 2. Download files via github
```
git clone https://github.com/IngvarOlsen/weGrain.git
```

### 3. Make virtual enviroment inside the gitfolder, or copy the folders "template", "static" and app.py to your new enviroment
```
pip install virtualenv
mkdir weGrain
cd weGrain
virtualenv venv
venv/bin/activate
```

### 4. Once activated install Flask
```
pip install Flask
```

### 5. Install rest of dependencies 
```
sudo apt install sqlite3
pip install APScheduler
pip install adafruit-circuitpython-rfm9x
pip install adafruit-blinka
pip install board
```
