#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from setuptools import Command


class ReleaseCommand(Command):
    """Release options"""
    description = 'Set release options'
    user_options = [('mkproto', None, 'builds proto files, default is to assume they are prebuilt.'),
                    ('version=', None, 'sets the version, default is 0.1')]

    def initialize_options(self):
        self.mkproto = None
        self.version = None

    def finalize_options(self):
        self.mkproto = self.mkproto is not None

    def run(self):
        if self.version is not None:
            self.distribution.metadata.version = self.version
        if self.mkproto:
            workdir = os.path.dirname(os.path.abspath(__file__))
            os.system(os.path.join(workdir, 'init.sh'))


class CleanCommand(Command):
    """Clean package"""
    description = 'clean package'
    user_options = [('all', None, 'clean all, default is build only')]

    def initialize_options(self):
        self.all = None

    def finalize_options(self):
        self.all = self.all is not None

    def run(self):
        workdir = os.path.dirname(os.path.abspath(__file__))
        os.system('rm -rf ' + os.path.join(workdir, 'build'))
        if self.all:
            os.system('rm -rf ' + os.path.join(workdir, 'mservice.egg-info'))
            os.system('rm -rf ' + os.path.join(workdir, 'dist'))


setup(
    name='mservice',
    version='0.1',
    description='Marbles Daemon and gRPC Service Definitions',
    author='Paul Glendenning',
    author_email = "support@marbles.ai",
    license='Marbles AI Proprietary License',
    url='http://www.marbles.ai',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
    packages=find_packages(exclude=['*.test', '*.test.*', 'test.*', '*.log']),
    package_data={
        'mservice': ['../proto/*.proto'],
    },
    install_requires=[
        'protobuf',
        'grpcio',
        'grpcio-tools',
        'boto3',
        'watchtower',
        'python_daemon',
    ],
    scripts=['scripts/run-mservice.sh'],
    include_package_data=True,
    cmdclass={
        'clean': CleanCommand,
        'release': ReleaseCommand,
    },
    zip_safe=False,
)
