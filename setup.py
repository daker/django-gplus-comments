#!/usr/bin/env python

from setuptools import setup, find_packages
from gplus_comments import __version__

setup(
    name='django-gplus-comments',
    version=__version__,
    description='Integrate Google+ comments into your Django website',
    author='Adnane Belmadiaf',
    author_email='adnane002@gmail.com',
    url='https://github.com/daker/django-gplus-comments',
    license="LICENSE.txt",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
)
