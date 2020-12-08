import os
import re

directory = input('Enter Songs Folder: ')
output = []
for path, dirs, files in os.walk(directory):
  ogg = None

  if (path == directory):
    continue

  for file in files:
    if '.ogg' in file or '.mp3' in file:
      ogg = file
      continue
  
  if ogg is None:
    output.append(re.sub('[^A-Za-z0-9\\\:;\-\(\)\s]+', '', path).replace(directory,"")[1:])

with open('./SongChecker.txt', 'w') as file:
  for x in (output):
      file.write(x + '\n\n')