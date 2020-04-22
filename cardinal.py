#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import logging
import requests
import threading
import argparse

logging.basicConfig(level=logging.INFO,
                    format='[%(name)s][%(levelname)s] %(message)')
logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(
    description='Cardinal - Getting your active repos local in one go')

parser.add_argument('--user', help='foo help')
parser.add_argument('--filter', help='foo help')
parser.add_argument('--token', help='foo help')
args = parser.parse_args()


class Cardinal(object):
    def start(self):
        self.get_projects()

    def get_projects(self):
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': "token {}".format(args.token)
        }
        repos = requests.get(
            "https://api.github.com/user/repos", headers=headers).text
        print(repos)


def main():
    print(args)
    system = Cardinal()
    system.start()


if __name__ == '__main__':
    main()
