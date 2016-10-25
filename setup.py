#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='blueflask',
    version='0.1.0',
    description="Flask boilerplate to create an application with the idea of pluggable blueprints.",
    author="Harrington Joseph",
    author_email='hello@hjoseph.com',
    url='https://github.com/harph/blueflask',
    packages=[
        'blueflask',
    ],
    package_dir={'blueflask':
                 'blueflask'},
    entry_points={
        'console_scripts': [
            'blueflask=blueflask.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='blueflask',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
