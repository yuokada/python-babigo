from setuptools import setup, find_packages
import sys
import os

version = '0.2.0'
if sys.version_info.major == 3:
    long_description = open('README.rst', 'r').read()
    install_requires = [
        # -*- Extra requirements: -*-
        'BeautifulSoup4',
        'httplib2',
    ]
else:
    long_description = open('README.rst', 'r').read().decode('utf-8')
    install_requires = [
        # -*- Extra requirements: -*-
        'BeautifulSoup4',
        'lxml',
        'httplib2',
    ]

setup(
    name='babigo',
    version=version,
    description='babigo translate module',
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],  # Get strings from
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='babigo nlp',
    author='Yukihiro Okada',
    author_email='callistoiv+pypi@gmail.com',
    url='https://github.com/yuokada/pythohn-babigo',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    tests_require=['nose', 'mock', 'coverage'],
    install_requires=install_requires,
    #entry_points={
    # 'console_scripts' : [
    # 'babigo-trans = babigo.translate',
    # ]
    #},
)
