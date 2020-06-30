import os

from setuptools import setup, find_packages



base_packages = ["Flask==1.0.3"]



module_name = "toshies"
 

setup(

    name=module_name,

    version="1.0.0",

    author="Sabine Scheffer",

    author_email="sabinexscheffer@gmail.com",

    packages=find_packages(),

    install_requires=base_packages

    )