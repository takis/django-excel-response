import os

from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.rst', 'r') as f:
    README = f.read()

with open('VERSION', 'r') as vfile:
    VERSION = vfile.read().strip()

setup(
    name='django-excel-response',
    version=VERSION,
    author='Joey Wilhelm',
    author_email='tarkatronic@gmail.com',
    license='Apache',
    description='Django package to easily render Excel spreadsheets',
    long_description=README,
    packages=['excel_response'],
    include_package_data=True,
    url='https://github.com/tarkatronic/django-excel-response',
    download_url='https://github.com/tarkatronic/django-excel-response/archive/master.tar.gz',
    install_requires=[
        'Django>=2.2',
        'openpyxl>=3.0'
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
    zip_safe=False,
    test_suite='runtests.runtests'
)
