from setuptools import setup

setup(
    entry_points={
        "console_scripts": [
            "gptos = gptos.ui.console:main",
        ],
    },
)
