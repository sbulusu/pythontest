import pkg_resources
from pip.req import parse_requirements
from setuptools import find_packages, setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below.


def read(fname):
    return open(pkg_resources.resource_filename(__name__, fname)).read()


# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="pythontest",
    version="0.0.1",
    author="Sridhar Bulusu",
    author_email="sridhar249@gmail.com",
    description="Python testing repository",
    license="BSD",
    keywords="python test",
    url="https://github.com/sbulusu/pythontest",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=reqs
)
