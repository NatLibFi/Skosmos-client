import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='skosmos-client',
    version='0.2.0',
    url='https://github.com/NatLibFi/Skosmos-client',
    author='Osma Suominen',
    author_email='osma.suominen@helsinki.fi',
    description='Python client library for accessing Skosmos REST API',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    py_modules=['skosmos_client'],
    install_requires=['requests','rdflib'],
    extras_require={
        'dev': ['bumpversion']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
