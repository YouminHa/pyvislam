from setuptools import setup, find_packages
from pyvislam.info import __package_name__, __version__

# Read several file contents
with open('README.rst', 'r', encoding='utf-8') as f:
  readme = f.read()
with open('requirements.txt', 'r', encoding='utf-8') as f:
  requires = f.read().splitlines()
with open('test_requirements.txt', 'r', encoding='utf-8') as f:
  test_requires = f.read().splitlines()

setup(
  name = __package_name__,
  version = __version__,
  description = 'python visual-inertial slam library for study'
  long_description = readme,
  packages = find_packages(exclude=['contrib', 'docs', 'tests']),
  package_data = {'': ['*.yaml']},
  install_requires = requires,
  setup_requires = ['pytest-runner'],
  test_requires = test_requires,
  python_requires = '>=3.6',
  entry_points = {
    'console_scripts' : ['pyvislam=pyvislam.pyvislam:main']
  },
  classifiers = [
    'Environment :: Console',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 3.6'
  ]
)
