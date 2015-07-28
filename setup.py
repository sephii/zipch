#!/usr/bin/env python
from setuptools import find_packages, setup
from zipch import __version_str__


setup(
    name='zipch',
    version=__version_str__,
    packages=find_packages(),
    description='Switzerland zipcodes, cantons and municipalities database',
    author='Sylvain Fankhauser',
    author_email='sylvain.fankhauser@liip.ch',
    url='https://github.com/sephii/zipch',
    license='MIT',
    include_package_data=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
    ]
)
