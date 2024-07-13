from setuptools import setup, find_packages

setup(
    name="yt_extractor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'yt-extractor=yt_extractor:main',
        ],
    },
)
