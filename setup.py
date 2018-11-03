from setuptools import setup, find_packages

with open('README.rst', encoding='UTF 8') as f:
    readme = f.read()

setup(
        name='hr',
        version='0.1.0',
        description='Commandline user managment utility',
        long_description=readme
        author='Phil Winnington',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=[]
        )

