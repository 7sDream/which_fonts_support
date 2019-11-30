#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup, find_packages

from which_fonts_support import __version__

setup(
    name='which_fonts_support',
    keywords=['font', 'utilities'],
    version=__version__,
    packages=find_packages(),
    url='https://github.com/7sDream/which_fonts_support',
    license='MIT',
    author='7sDream',
    author_email='i@7sdre.am',
    description='Find which fonts support specified character',
    install_requires=[
        'wcwidth'
    ],
    entry_points={
        'console_scripts': ['which_fonts_support=which_fonts_support.cli:cli']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Text Processing :: Fonts',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
