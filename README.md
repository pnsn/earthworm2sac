# earthworm2sac
Python script to get SAC files from earthworm wave_serverV or Winston. 

# Installation
I recommend working with virtual environments. See  http://docs.python-guide.org/en/latest/dev/virtualenvs/
This script uses obspy, which needs numpy, matplotlib, scipy, and a bunch of 
other stuff. Numpy needs to be completely installed first.
Another option is to use a third-party distributor such as Anaconda ("conda").

1. `git clone https://github.com/pnsn/earthworm2sac.git earthworm2sac`
2. `cd earthworm2sac`
3. `pip install numpy`
4. `pip install -r requirements.txt`

Put the earthworm2sac executable script in your PATH somewhere, or add the earthworm2sac directory to your path.

Not tested with Python3 but might work.
