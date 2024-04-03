import azure_contact
import get_data
import asyncio
import json
import logging
import time
import sys

try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559

from bme280 import BME280

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


async def main():
    d = open('device.json')
    conn_str = json.load(d)["conn_str"]
    d.close()
    connection = azure_contact.Connection(conn_str)    
    if len(sys.argv) == 2 and sys.argv[1] == "faulty":
            connection.faulty = True
    await connection.connect()
	

    temp_obj = get_data.Temp()
    bme280 = BME280()
    i = 4
    while True:
        if i == 0:
            i = 4
        temp = temp_obj.get_temp()
        pressure = bme280.get_pressure() 
        humidity = bme280.get_humidity()
        light = ltr559.get_lux()
        last_send_time = time.time()
        msg_dict = {"temp" : temp, "pressure" : pressure, "humidity" : humidity, "light" : light}
        if i == 4:
           status = await connection.send_message(json.dumps(msg_dict))
        await connection.poll_queue() 
		
        while time.time() - last_send_time < 2:
            pass
        i -= 1

    await connection.close()

asyncio.run(main())
