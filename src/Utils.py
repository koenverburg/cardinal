from os import path

def is_local(_folder_name):
  if (path.exists(_folder_name)):
    return True
  else:
    return False

def log_meta():
  print('blaat')
