# earthworm2sac
Python script to get SAC files from earthworm wave_serverV or Winston. 

# Optional: Virtualenv
I recommend working with virtual environments. See  http://docs.python-guide.org/en/latest/dev/virtualenvs/

1. If you don't have pip installed yet, do as root or sudo:
`easy_install pip`
2. If you don't have virtualenv installed yet, do as root or sudo:
`pip install virtualenv`
3. as yourself, in some directory:
`virtualenv my-python`
4. activate the virtual environtment:
`source some-directory/my-python/bin/activate` (if you use bash)
`source some-directory/my-python/bin/activate.csh` (if you use csh)
5. type `which pip` to confirm that you are now using the virtual environment.
6. use pip to install packages in this virtual environment, for example, see below.
7. if you want to stop using the virtual environment:
`deactivate`

# Installation

This script uses obspy, which needs numpy, matplotlib, scipy, and a bunch of 
other stuff. Numpy needs to be completely installed first.
Another option is to use a third-party distributor such as Anaconda ("conda").

1. `git clone https://github.com/pnsn/earthworm2sac.git earthworm2sac`
2. `cd earthworm2sac`
3. `pip install numpy`
4. `pip install -r requirements.txt`

If this fails, install python-dev (ubuntu) or python-devel (centos) package and try again.

Put the earthworm2sac executable script in your PATH somewhere, or add the earthworm2sac directory to your path.

Not tested with Python3 but might work.
