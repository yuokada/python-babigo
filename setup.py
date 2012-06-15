from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='babigo',
        version=version,
        description="babigo translate module",
        long_description=open('README.md').read(),
        classifiers=[
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        keywords='babigo nlp',
        author='Yukihiro Okada',
        author_email='callistoiv+pypi@gmail.com',
        url='',
        license='BSD',
        packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            # -*- Extra requirements: -*-
            'BeautifulSoup',
            'httplib2',
            ],
        #entry_points={
        # 'console_scripts' : [
        # 'babigo-trans = babigo.translate',
        # ]
        #},
        )

