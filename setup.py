#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name='geotrans_cluster',
    version='0.9.0',
    description='Third course reasearch project on developing the way to cluster bank clients from date, time and coordinates in their transaction history',
    author='Korsakov Aleksandr',
    author_email='corsakov.alex@yandex.ru',
    url='https://github.com/LarsWallenstein/Geotrans_cluster',
    py_modules=["geotrans_cluster"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI App :: MIT license"
        "Operating System :: OS Independent"
    ],
    long_description = long_description,
    long_description_content_type="text/markdown",
)

