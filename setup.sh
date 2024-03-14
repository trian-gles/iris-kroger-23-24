python -m venv env
source /env/bin/activate

sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
sudo apt install git
git clone https://github.com/pimoroni/enviroplus-python
cd enviroplus-python
sudo ./install.sh
cd ..
pip install pms5003==0.0.5
pip install st7735==0.0.5
pip install azure-iot-device

