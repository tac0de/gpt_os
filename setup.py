from setuptools import setup, find_packages

setup(
    name='gpt_os',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'gpt-os = system.__main__:main',
        ],
    },
    install_requires=[],
    author='YourNameHere',
    description='A modular operating system simulation for LLMs (GPT OS)',
    keywords='gpt os architecture ai memory llm shell',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Artificial Intelligence',
    ],
)
