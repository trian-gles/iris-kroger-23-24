import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
from sys import getsizeof
import random
from local_storage import save_data, reconnect


class Connection:
    def __init__(self, conn_str):
        self.conn_str = conn_str 
        self.device_client = IoTHubDeviceClient.create_from_connection_string(self.conn_str)
        self.outage = False
        self.faulty = False

    def outage(self):
        self.outage = True

    def reconnect(self):
        self.outage = False

    async def faulty_behaviour(self):
        if random.randrange(0,3) > 1:
            self.outage = not self.outage
            print("toggling outage")
            if (not self.outage):
                print("retrieving cached data")
                for d in reconnect():
                    size = getsizeof(d)
                    print(f"Reuploading {d}")
                    await self.device_client.send_message(d)

    async def connect(self):
        # Connect the device client.
        await self.device_client.connect()
        print("Connected to server")
        
    async def close(self):
        await self.device_client.shutdown()
        print("Closed server connection")
        
    async def send_message(self, message):
        if self.faulty:
            await self.faulty_behaviour()

        if self.outage:
            save_data(message)
            return False
        else:
            size = getsizeof(message)
            await self.device_client.send_message(message)
            print(f"Sent message : {message}")
            return True


async def main():
    # Fetch the connection string from an environment variable
    conn_str = "HostName=iris-hub.azure-devices.net;DeviceId=kieran-computer;SharedAccessKey=GwQXIvCXF++fCvycARzDxeAyt/U13fhIuAIoTCAAMkE="

    # Create instance of the device client using the authentication provider
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    print("Sending message...")
    await device_client.send_message("This is a message that is being sent")
    print("Message successfully sent!")

    # finally, shut down the client
    await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
