#!/usr/bin/env python

from setuptools import setup

setup(
    name="mozilla_aws_cli_mozilla",
    description="Mozilla specific deployment of the mozilla_aws_cli",
    author="Mozilla Enterprise Information Security",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    install_requires=["mozilla_aws_cli"],
    keywords="maws Mozilla AWS CLI config",
    packages=["mozilla_aws_cli_config"],
    url="https://github.com/mozilla-iam/mozilla-aws-cli-mozilla",
    version="0.0.1",
    zip_safe=False,
)
