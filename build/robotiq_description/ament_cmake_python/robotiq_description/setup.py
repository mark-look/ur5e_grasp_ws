from setuptools import find_packages
from setuptools import setup

setup(
    name='robotiq_description',
    version='1.3.0',
    packages=find_packages(
        include=('robotiq_description', 'robotiq_description.*')),
)
