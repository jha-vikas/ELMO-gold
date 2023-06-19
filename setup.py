#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="gold",
    version="0.0.1",
    description="PyTorch Lightning Project Setup",
    author="",
    author_email="",
    #url="https://github.com/user/project",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "gold_train = gold.train:main",
            "gold_eval = gold.eval:main",
        ]
    },
)
