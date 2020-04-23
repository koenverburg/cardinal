#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import git
import requests
import threading
import argparse
import datetime

parser = argparse.ArgumentParser(
    description='Cardinal - Getting your active repos local in one go')

parser.add_argument(
    '--months', '-m', help='Get all the repos you pushed to in the last X months')
parser.add_argument('--token', '-t', help='foo help')
parser.add_argument('--dir', '-d', help='foo help')
args = parser.parse_args()

threads = []


class Cardinal(object):
    def start(self):
        self.clone_list = []
        self.get_projects()

    def get_projects(self):
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': "token {}".format(args.token)
        }

        data = requests.get(
            "https://api.github.com/user/repos?type=owne&sort=pushed", headers=headers).text
        parsed_json = json.loads(data)

        self.loop_through(parsed_json)

    def loop_through(self, _repositories):
        format = '%Y-%m-%dT%H:%M:%S%z'
        amount_of_days = int(30 * int(args.months))
        amount_of_months_back = datetime.datetime.today(
        ) - datetime.timedelta(days=amount_of_days)
        print(amount_of_months_back)

        for repository in _repositories:
            if (datetime.datetime.strptime(repository['pushed_at'], format).date() > amount_of_months_back.date()):
                self.clone_list.append(repository['ssh_url'])
        self.clone()

    def cmd(self, _url):
        git.Git().clone(_url)

    def clone(self):
        for url in self.clone_list:
            print('[i] repo: {0}'.format(url))
            repo = threading.Thread(target=self.cmd(url))
            threads.append(repo)
            repo.start()


def main():
    print(args)
    system = Cardinal()
    system.start()


if __name__ == '__main__':
    main()
