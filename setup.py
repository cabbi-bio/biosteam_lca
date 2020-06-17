#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:48:17 2020

@author: cyshi
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biosteam_lca", # Replace with your own username
    version="0.0.1",
    author="rui shi",
    author_email="cyshi@illinois.edu",
    description='The Biorefinery Simulation Moduels with Techno-Economic Analysis and Life Cycle Assessment',
    #"An Integrated Modeling Framework for Agile Life Cycle Assessment of Biorefineries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scyjth/biosteam_lca",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: University of Illinois/NCSA Open Source License',",
    ],    
    python_requires='>=3.6',
)
