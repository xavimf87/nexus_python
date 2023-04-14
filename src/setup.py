from setuptools import setup, find_packages
from setuptools_scm import get_version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nexus_python",
    version=get_version(root='src', prefix='v'),
    author="Xavi Martinez",
    author_email="xavimartinezfa@gmail.com",
    description="A Python package that simplifies interaction with Nexus, a software artifact management platform. With this library, you can easily perform upload, download, and retrieve operations for Nexus repositories and repository items.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xavimf87/nexus_python",
    project_urls={
        "Bug Tracker": "https://github.com/xavimf87/nexus_python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free for non-commercial use",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "requests",
    ],
)
