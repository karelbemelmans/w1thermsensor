import os
import re
import functools
from pathlib import Path

from setuptools import find_packages, setup

#: Holds the configuration for the Python package
PACKAGES = find_packages()
META_FILE = Path("w1thermsensor").absolute() / "__init__.py"
KEYWORDS = [
    "w1",
    "therm",
    "DS1822",
    "DS18S20",
    "DS18B20",
    "rpi",
    "raspberry pi",
    "beagle bone",
    "linux",
    "cli",
    "api"
]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

#: Holds all requirements for the end user
INSTALL_REQUIRES = ["click"]

#: Holds all requirements for development and testing
EXTRAS_REQUIRES = {
    "tests": ["pytest", "pytest-mock", "coverage"]
}
EXTRAS_REQUIRES["dev"] = EXTRAS_REQUIRES["tests"] + ["flake8"]


here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", encoding="utf-8") as readme_file:
    README_CONTENTS = readme_file.read()


@functools.lru_cache()
def read(metafile):
    """
    Return the contents of the given meta data file assuming UTF-8 encoding.
    """
    with open(str(metafile), encoding="utf-8") as f:
        return f.read()


def get_meta(meta, metafile):
    """
    Extract __*meta*__ from the given metafile.
    """
    contents = read(metafile)
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), contents, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


setup(
    name="w1thermsensor",
    version=get_meta("version", META_FILE),
    license="MIT",
    description=(
        "A Python package and CLI tool to work with w1 temperature sensors like "
        "DS1822, DS18S20 & DS18B20 on the Raspberry Pi, Beagle Bone and other devices."
    ),
    long_description=README_CONTENTS,
    long_description_content_type="text/markdown",
    author="Timo Furrer",
    author_email="tuxtimo@gmail.com",
    maintainer="Timo Furrer",
    maintainer_email="tuxtimo@gmail.com",
    platforms=["Linux"],
    url="http://github.com/timofurrer/w1thermsensor",
    download_url="http://github.com/timofurrer/w1thermsensor",
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRES,
    python_requires=">=3.5.*",
    entry_points={
        "console_scripts": ["w1thermsensor = w1thermsensor.cli:cli"]
    },
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
)
