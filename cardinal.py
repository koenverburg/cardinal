#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import git
import requests
import threading
import argparse
import datetime
from os import path

parser = argparse.ArgumentParser(description='Cardinal - Getting your active repositories local in one go')
parser.add_argument('--months', '-m', help='Limit the amount the repositories being pulled in')
parser.add_argument('--token', '-t', help='foo help')
parser.add_argument('--dir', '-d', help='foo help')
args = parser.parse_args()

threads = []

class Cardinal(object):
  def start(self):
    self.projects = []
    self.get_projects()
    self.prepare_to_clone()
    self.initial_cloning()

  def get_projects(self):
    headers = {
      'Accept': 'application/vnd.github.v3+json',
      'Authorization': "token {}".format(args.token)
    }

    data = requests.get("https://api.github.com/user/repos?type=owne&sort=pushed", headers=headers).text
    parsed_json = json.loads(data)

    self.loop_through(parsed_json)

  def loop_through(self, _repositories):
    format = '%Y-%m-%dT%H:%M:%S%z'
    amount_of_days = int(30 * int(args.months))
    amount_of_months_back = datetime.datetime.today() - datetime.timedelta(days=amount_of_days)

    for repository in _repositories:
      if (datetime.datetime.strptime(repository['pushed_at'], format).date() > amount_of_months_back.date()):
        project = {
          "name": repository['name'],
          "url": repository['ssh_url'],
          "is_local": False
        }
        self.projects.append(project)

  def prepare_to_clone(self):
    for i, project in enumerate(self.projects):
      if (path.exists(project['name'])):
        print('[*] found {0} locally, will skip this later'.format(project['name']))
        project.update({'is_local': True})
      else:
        print('[*] project: {0}, will be downloaded'.format(project['name']))

  def cmd(self, _url):
    git.Git().clone(_url)

  def initial_cloning(self):
    # meta
    total = len(self.projects)
    cloning_count = sum(map(lambda x: x['is_local'] == False, self.projects))
    skipping_count = sum(map(lambda x: x['is_local'] == True, self.projects))
    print('[*] total repositories: {0}, cloning {1}, skipping {2}'.format(total, cloning_count, skipping_count))

    # cloning
    for project in self.projects:
      if(project.get('is_local') == True):
        print('[i] Skipping {0}'.format(project.get('name')))

      if (project.get('is_local') == False):
        print('[*] starting thread to clone: {0}'.format(project.get('name')))
        repo = threading.Thread(target=self.cmd(project.get('url')))
        threads.append(repo)
        repo.start()


def main():
  print(args)
  system = Cardinal()
  system.start()


if __name__ == '__main__':
  main()
