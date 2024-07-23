from setuptools import setup, find_packages

setup(
    name='intro_devops',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # list your dependencies here
    ],
)
