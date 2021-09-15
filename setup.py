from setuptools import find_packages
from setuptools import setup

setup(
    name="error_propagation",
    version="0.0.1",
    author="David Reiss-Mello",
    author_email="davidreissmello@gmail.com",
    description="Package that computes error propagation",
    url="https://github.com/davidreissmello/error_propagation",
    packages=["error_propagation", "error_propagation.finance"],
)
