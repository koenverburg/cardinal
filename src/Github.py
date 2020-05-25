import json
import requests
import datetime

class Github(object):
  def __init__(self, _token, _months_ago):
    self.token = _token
    self.months_ago = _months_ago

  def request_projects(self):
    headers = {
      'Accept': 'application/vnd.github.v3+json',
      'Authorization': "token {}".format(self.token)
    }

    data = requests.get("https://api.github.com/user/repos?type=owne&sort=pushed", headers=headers).text
    return json.loads(data)

  def get_projects(self):
    projects = []
    repositories = self.request_projects()

    format = '%Y-%m-%dT%H:%M:%S%z'
    amount_of_days = int(30 * int(self.months_ago))
    amount_of_months_back = datetime.datetime.today() - datetime.timedelta(days=amount_of_days)

    for repository in repositories:
      if (datetime.datetime.strptime(repository['pushed_at'], format).date() > amount_of_months_back.date()):
        project = {
          "name": repository['name'],
          "url": repository['ssh_url'],
          "is_local": False
        }
        projects.append(project)
    return projects
