""" Setup for package """

from setuptools import setup, find_packages

setup(
    name="foo_param",
    version="0.1.0",
    packages=find_packages(),
    author="Brian Kenkel",
    author_email="briankenkel.t@gmail.com",
    description="A package for the Foo et al. parameterization",
    long_description=open('README.md', encoding="UTF-8").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/bkenks/foo_param",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
