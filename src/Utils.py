from os import path

def is_local(_folder_name):
  return bool((path.exists(_folder_name)))

def log_meta():
  print('blaat')
