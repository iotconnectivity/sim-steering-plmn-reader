# -*- coding: utf-8 -*- 

from setuptools import setup

setup(name='simplmn',
      version='0.1.1',
      description=
      'Display SIM card PLMN / FPLMN on Pod Group Steering List application',
      author='J. Félix Ontañón',
      author_email='felix.ontanon@podgroup.com',
      url='https://github.com/PodgroupConnectivity/sim-steering-plmn-read',
      platforms=['win32', 'linux2'],
      license='GNU LESSER GENERAL PUBLIC LICENSE',
      install_requires=[
          'asterix==0.3',
      ],
      dependency_links=[
          'git+ssh://git@github.com/PodgroupConnectivity/asterix.git@384068582c7d5dc28da3fc7fd2dfc3c908f1ff0b#egg=asterix-0.3'
      ],
      scripts=['bin/simplmn'],
)