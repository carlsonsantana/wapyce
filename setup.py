# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Module to setup Wapyce.
"""

import os
from setuptools import find_packages
from setuptools import setup

BASE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def get_long_description():
    """
    Returns the long description of Wapyce.

    :return: The long description of Wapyce.
    :rtype: str
    """

    with open(
        os.path.join(BASE_DIRECTORY, 'README.md'),
        'r',
        encoding='utf-8'
    ) as readme_file:
        return readme_file.read()


def get_packages():
    """
    Returns the packages used for Wapyce.

    :return: The packages used for Wapyce.
    :rtype: list(str)
    """

    packages = find_packages(exclude=['tests'])
    packages.append('')

    return packages


def get_package_data():
    """
    Returns the packages with static files of Wapyce.

    :return: The packages with static files of Wapyce.
    :rtype: dict(str, list(str))
    """

    package_data = {'': ['requirements.txt']}

    return package_data


def get_requirements():
    """
    Returns the content of 'requirements.txt' in a list.

    :return: The content of 'requirements.txt'.
    :rtype: list(str)
    """

    requirements = []
    with open(
        os.path.join(BASE_DIRECTORY, 'requirements.txt'),
        'r',
        encoding='utf-8'
    ) as requirements_file:
        lines = requirements_file.readlines()
        for line in lines:
            requirements.append(line.strip())
    return requirements


setup(
    name='wapyce',
    description=(
        'A web server that store information of accessibility validation.'
    ),
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    version='1.0.0',
    url='https://github.com/carlsonsantana/wapyce',
    author='Carlson Santana Cruz',
    license='MIT',
    classifiers=[
        'Framework :: Django :: 2.1',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Quality Assurance'
    ],
    packages=get_packages(),
    package_data=get_package_data(),
    install_requires=get_requirements()
)
