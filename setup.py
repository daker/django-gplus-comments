#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-gplus-comments',
    version='0.0.1',
    description='Integrate Google+ comments into your Django website',
    author='Adnane Belmadiaf',
    author_email='adnane002@gmail.com',
    license='New BSD License',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
)
