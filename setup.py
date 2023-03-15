from setuptools import find_packages, setup
from os.path import dirname
from os.path import join


def _read(file_name):
    with open(join(dirname(__file__), file_name)) as f:
        return f.read()


setup(name='m3_project',
      version='1',
      description='m3_project',
      package_dir={"": "app"},
      packages=find_packages('app'),
      dependency_links=('http://pypi.bars-open.ru/simple/',
                        '--extra-index-url http://pypi.bars-open.ru/simple/',
                        '--trusted-host pypi.bars-open.ru',),

      install_requires=(
          'django==2.2',
          'm3-django-compat==1.9.2',
          'm3-objectpack==2.2.47',),
      )
