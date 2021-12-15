import re
import sys
import codecs
from os import path

from setuptools import setup


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()

with open('src/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    name='home-credit',
    version=version,
    url='http://github.com/Maxstyll/home-credit',
    author='Emerson Antonio',
    author_email='emerson.antonio.architect@gmail.com',
    description='home-credit, avaliação de linha de credito',
    license='MIT',
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)