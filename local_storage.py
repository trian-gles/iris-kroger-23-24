from pathlib import Path
import os
import json

def init_storage():
  Path("./cached").mkdir(parents=True, exist_ok=True)

def save_data(data):
  print(f"Saving data locally : {data}")
  f = open(f'cached/data.json', 'r')
  text = f.read()
  if text:
    data_arr = json.loads(text)
  else:
    data_arr = []
  f.close()
  data_arr.append(data)
  f = open(f'cached/data.json', 'w')
  f.write(json.dumps(data_arr))
  f.close()

def reconnect():
  f = open('cached/data.json', 'r')
  text = f.read()
  f.close()
  f = open('cached/data.json', 'w')
  f.write(json.dumps([]))
  f.close()
  return json.loads(text)
