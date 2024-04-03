Requires python 3, a raspberry pi, and an enviro mini board.

Clone this library:

```git clone https://github.com/trian-gles/iris-kroger-23-24.git```

Run the setup script:
```sudo chmod +x setup.sh```
```./setup.sh```

Edit `device.json` replacing the connection string with your own:
- amartya : `HostName=iris-hub.azure-devices.net;DeviceId=amartya-rpi;SharedAccessKey=vjn2ghMZ3mPrqBLbDoheENZXpPYDAGvZ7COHEW22VK8=`
- shehani : `HostName=iris-hub.azure-devices.net;DeviceId=shehani-rpi;SharedAccessKey=yw7s1BpkXmndia6IJLRASnaz4/sOKSCKFG49ZJEZ35w=`
- rohit : `HostName=iris-hub.azure-devices.net;DeviceId=rohit-rpi;SharedAccessKey=B5cbhSPsq8H4THM4J3Ne2MGGLU8TnLC2UeD3CeZo0o4=`
- kieran : `HostName=iris-hub.azure-devices.net;DeviceId=kieran-rpi;SharedAccessKey=yqpMmXrdwKgPI32wBQ1+OnfWfYkoDH0wxDXVOsFqAyM=`

Run the main script:
```source env/bin/activate```
```python main.py```

OR to simulate occasional network outages:
```python main.py faulty```
