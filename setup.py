from setuptools import setup
    
def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="spotify-api.py",
    version="0.0.4",
    url="https://github.com/spotify-api/spotify-api.py",
    description="A simple wrapper for spotify api written in python!",
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=['spotifyapi'],
    keywords=['spotifyapi', 'spotify-api.py', 'spotify'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
)
