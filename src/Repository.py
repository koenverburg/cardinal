import git

from src import Utils

class Repository(object):
  def start(self, repository):
    if (self.can_clone(repository['name'])):
      self.clone(repository['url'])
    return

  def clone(self, url):
    return git.Git().clone(url)

  def can_clone(self, name):
    if (Utils.is_local(name)):
      print('[*] found {0} locally, will skip this later'.format(name))
      return False
    else:
      print('[*] project: {0}, will be downloaded'.format(name))
      return True

  def finalize(self):
    print('Finished')

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.finalize()

  def __enter__(self):
    return self
