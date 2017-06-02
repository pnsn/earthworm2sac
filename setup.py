from setuptools import setup

setup(name="earthworm2sac", 
    version="0.0.1",
    description="Get SAC files out of an earthworm wave_serverV or winston",
    url="http://github.com/pnsn/earthworm2sac",
    author="Renate Hartog",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Science/Research',
    ],
    scripts=["earthworm2sac"],
    install_requires=["numpy","obspy>=0.10.2"],
    zip_safe=False)

