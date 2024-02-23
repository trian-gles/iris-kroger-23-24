import azure_contact
#import sensor_data
import asyncio
import json

async def main():
	d = open('device.json')
	conn_str = json.load(d)["conn_str"]
	d.close()

	connection = azure_contact.Connection(conn_str)
	await connection.connect()
	await connection.send_message("Connected!")

	await connection.close()

asyncio.run(main())
