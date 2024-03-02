from time import sleep, localtime
from picamera import PiCamera
import asyncio

async def main():
  camera = PiCamera()
  camera.resolution = (1024, 768)
  camera.start_preview()
  await asyncio.sleep(2) # Warm up time
  while True:
    filename = f"{localtime()}.jpg"
    camera.capture('filename')
    await asyncio.sleep(60)

if (__name__ == "__main__"):
  asyncio.run(main())
