Display SIM card PLMN / FPLMN on your browser
=====================================

[simplmn](https://github.com/IOTConnectivity/sim-steering-plmn-reader) - is a small executable that reads the SIM Card EF_PLMN and EF_FPLMN files and display the defined steering list graphically on Steering List application.

Usage
------

Help:

```
usage: simplmn [-h] pin

Display SIM card PLMN / FPLMN on Steering List application

positional arguments:
  pin         SIM Card PIN. Leave empty for non PIN protected SIM cards

optional arguments:
  -h, --help  show this help message and exit

```

Example:

```
$ simplmn 1234 # Whereas 1234 is your SIM card PIN. Leave it as empty if your SIM is not PIN protected
```

Installation
-------------

This application uses WINSCARD on Windows Systems or PCSC-Lite for Linux and Mac OSX systems. Ensure the required software and services for your OS are already enabled. In order to compile in Windows, [Visual C++ Python 2.7 compiler](https://www.microsoft.com/en-us/download/details.aspx?id=44266) needs to be installed as well.

Then, ensure the following dependencies are already installed in your system:

* [Python 2.7](http://python.org) 
* [SWIG](http://www.swig.org)
* [GIT](https://git-scm.com/)

Once all dependencies are installed, download the source code and execute:

```
$ python setup.py install
```

The setup.py file should downloads all python dependencies (asterix, pyscard, pycrypto, ecdsa). Resolve building dependencies yourself when compiling error occurs.

FAQ
---

**What is a roaming steering list?**
A roaming steering list is a set of preferences that steer the SIM card connectivity to certain networks. Carriers install those lists on SIM cards to steer roaming behaviour, so the best quality networks are selected outside of the home network, or for avoid expensive networks costs (depending on your plan).

**What do all those MCC, MNC, PLMN, FPLMN acronyms mean?**
MCC stands for Mobile Country Code, MNC for Mobile Network Code. The ITU-T Recommendation E.212 defines both MCC and MNC lists worldwide. A PLMN, or Public Land Mobile Network is a network ID formed by the combination of MCC and MNCs: e.g. 23410 refers to UK country (MCC: 234) and O2 network (MNC: 10). A FPLMN is simply a forbidden PLMN the device should avoid connecting to. Read the Mobile Country Code article on Wikipedia for further information.
