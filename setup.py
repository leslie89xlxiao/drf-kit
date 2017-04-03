import os

from setuptools import setup, find_packages

version = '1.0.0'

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='drf-kit',
    version=version,
    description='Drf-kit is django rest framework kit which contains help functions.',
    author='leslie89xlxiao',
    author_email='leslie89xlxiao@gmail.com',
    url='https://github.com/leslie89xlxiao/drf-kit',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Programming Language :: Python :: 2.7',
    ]
)
