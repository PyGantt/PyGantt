#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'pandas>=0.18']

setup_requirements = requirements

test_requirements = requirements

setup(
    author="PyGantt developers",
    author_email='seth.mridul@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Gantt charts in python",
    entry_points={
        'console_scripts': [
            'pygantt=pygantt.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pygantt',
    name='pygantt',
    packages=find_packages(include=['pygantt']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pygantt/pygantt',
    version='0.1.0',
    zip_safe=False,
)
