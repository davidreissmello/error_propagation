from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="error_propagation",
    version="0.0.4",
    author="David Reiss-Mello",
    author_email="davidreissmello@gmail.com",
    description="Package that computes error propagation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidreissmello/error_propagation",
    packages=["error_propagation", "error_propagation.finance"],
)
