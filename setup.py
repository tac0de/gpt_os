from setuptools import setup, find_packages

setup(
    name="gptos",
    version="0.2.0",
    packages=find_packages(include=["gptos", "gptos.*"]),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gptos = gptos.ui.console:main',
        ],
    },
)
