from pathlib import Path
import os

def init_storage():
  Path("/cached").mkdir(parents=True, exist_ok=True)

def save_data(data):
  file_count = len([name for name in os.listdir('/cached') if os.path.isfile(name)])
  f = open(f'data_{file_count}.json', 'wb')
  f.write(data)
  f.close()

def reconnect():
  pass
