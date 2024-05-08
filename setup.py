import pathlib

import setuptools
from setuptools import setup

HERE = pathlib.Path(__file__).parent

with open(HERE / "README.md", encoding="utf-8") as f:
    README = f.read()


setup(
    name="cntime-nlp",
    version="0.1.1",
    keywords=["nlp", "time nlp"],
    url="https://github.com/taccisum/cntime-nlp",
    author="taccisum",
    author_email="taccisum@gmail.com",
    long_description_content_type="text/markdown",
    description="将中文时间表达词转为相应的时间字符串，支持时间点，时间段，时间间隔。",
    long_description=README,
    license="MIT Licence",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'arrow>=0.17.0',
        'loguru>=0.5.3',
        'regex>=2020.11.13',
    ],
    classifiers=["Programming Language :: Python :: 3.9"],
)
