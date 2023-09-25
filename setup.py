from setuptools import setup

from is_even import __version__

with open("README.md") as f:
    readme = f.read()

setup(
    name="is_even_methods",
    description="A collection of is_even methods",
    long_description=readme,
    long_description_content_type="text/markdown",
    version=__version__,
    url="https://github.com/Macosaro/is_even_methods/",
    packages=["is_even"],
    license="MIT",
)
