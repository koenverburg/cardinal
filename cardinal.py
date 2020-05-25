#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from time import time
from functools import partial
from concurrent.futures import ThreadPoolExecutor
from src.Github import Github
from src.Repository import Repository

parser = argparse.ArgumentParser(description='Cardinal - Getting your active repositories local in one go')
parser.add_argument('--months', '-m', help='Limit the amount the repositories being pulled in')
parser.add_argument('--token', '-t', help='foo help')
args = parser.parse_args()

class Cardinal(object):
  def start(self):
    github = Github(args.token, args.months)
    repositories = github.get_projects()

    with ThreadPoolExecutor(len(repositories)) as executor:
      repository = Repository()
      func = partial(repository.start)
      executor.map(func, repositories)

def main():
  ts = time()

  system = Cardinal()
  system.start()

  print('Took {0}'.format(time() - ts))

if __name__ == '__main__':
  main()
