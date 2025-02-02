#!/usr/bin/env python
import os
import os.path
import re
import glob
from setuptools import (find_packages, setup)

VERSION_RE = re.compile('__version__\s*=\s*[\'"](.*)[\'"]')

def get_version():
    with open(os.path.join(
          os.path.dirname(os.path.abspath(__file__)),
          'airflow_code_editor/airflow_code_editor.py')) as f:
        for line in f:
            match = VERSION_RE.match(line)
            if match:
                return match.group(1)
    raise Exception

def get_package_data():
    return ([x.split('/', 1)[1] for x in glob.glob('airflow_code_editor/**/*.js', recursive=True)] +
            [x.split('/', 1)[1] for x in glob.glob('airflow_code_editor/**/*.css', recursive=True)] +
            [x.split('/', 1)[1] for x in glob.glob('airflow_code_editor/**/*.html', recursive=True)])

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().split('\n')

setup(
    name='airflow_code_editor',
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    package_data={ 'airflow_code_editor': get_package_data() },
    entry_points = {
        'airflow.plugins': [
            'airflow_code_editor = airflow_code_editor.airflow_code_editor:CodeEditorPlugin'
        ]
    },
    zip_safe=False,
    url='https://github.com/andreax79/airflow-code-editor',
    author='Andrea Bonomi',
    author_email='andrea.bonomi@gmail.com',
    description='Apache Airflow in browser code editor',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    license='Apache License, Version 2.0',
    classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
    ]
)

