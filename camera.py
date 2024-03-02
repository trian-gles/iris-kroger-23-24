from time import sleep, localtime
import json
import os
from pathlib import Path
from azure.iot.device import IoTHubDeviceClient
from azure.core.exceptions import AzureError
from azure.storage.blob import BlobClient
from picamera import PiCamera

def store_blob(blob_info, file_name):
    try:
        sas_url = "https://{}/{}/{}{}".format(
            blob_info["hostName"],
            blob_info["containerName"],
            blob_info["blobName"],
            blob_info["sasToken"]
        )

        print("\nUploading file: {} to Azure Storage as blob: {} in container {}\n".format(file_name, blob_info["blobName"], blob_info["containerName"]))

        # Upload the specified file
        with BlobClient.from_blob_url(sas_url) as blob_client:
            with open(file_name, "rb") as f:
                result = blob_client.upload_blob(f, overwrite=True)
                return (True, result)

    except FileNotFoundError as ex:
        # catch file not found and add an HTTP status code to return in notification to IoT Hub
        ex.status_code = 404
        return (False, ex)

    except AzureError as ex:
        # catch Azure errors that might result from the upload operation
        return (False, ex)

def main():
  d = open('device.json')
	conn_str = json.load(d)["conn_str"]
	d.close()
  device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
  device_client.connect()
  
  
  camera = PiCamera()
  camera.resolution = (1024, 768)
  camera.start_preview()
  await asyncio.sleep(2) # Warm up time
  while True:
    Path("/imgs").mkdir(parents=True, exist_ok=True)
    filename = f"/imgs/{localtime()}.jpg"
    camera.capture('filename')

    storage_info = device_client.get_storage_info_for_blob(os.path.basename(filename))

    success, result = store_blob(storage_info, os.path.abspath(filename)

    if success == True:
        print("Upload succeeded. Result is: \n") 
        print(result)
        print()

        device_client.notify_blob_upload_status(
            storage_info["correlationId"], True, 200, "OK: {}".format(PATH_TO_FILE)
        )

    else :
        # If the upload was not successful, the result is the exception object
        print("Upload failed. Exception is: \n") 
        print(result)
        print()

        device_client.notify_blob_upload_status(
            storage_info["correlationId"], False, result.status_code, str(result)
        )
    time.sleep(60)

if (__name__ == "__main__"):
  main()
