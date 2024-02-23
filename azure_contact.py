import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient

class Connection:
    def __init__(self):
        self.conn_str = "HostName=iris-hub.azure-devices.net;DeviceId=kieran-computer;SharedAccessKey=GwQXIvCXF++fCvycARzDxeAyt/U13fhIuAIoTCAAMkE="
        self.device_client = IoTHubDeviceClient.create_from_connection_string(self.conn_str)

        # Connect the device client.
        self.device_client.connect()
        print("Connected to server")
        
    def close():
        self.device_client.shutdown()
        print("Closed server connection")
        
    def send_message(message):
        self.device_client.send_message(message)
        print(f"Sent message : {message}")


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