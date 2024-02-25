import azure_contact
import get_data
import asyncio
import json
import logging
import time

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


async def main():
	d = open('device.json')
	conn_str = json.load(d)["conn_str"]
	d.close()

	connection = azure_contact.Connection(conn_str)
	await connection.connect()
	

	temp_obj = get_data.Temp()
	
	while True:
		temp = temp_obj.get_temp()
		pressure = get_data.get_pressure()
		humidity = get_data.get_humidity()
		light = get_data.get_light()
		last_send_time = time.time()
		logging.info(f"Temp : {temp}, Pressure = {pressure}, Humidity = {humidity}, Light = {light}")
		while time.time() - last_send_time < 10:
			pass
		
	await connection.send_message("Connected!")

	await connection.close()

asyncio.run(main())
