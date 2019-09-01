from setuptools import setup
setup(
    name = 'soccer',
    version = '0.2.0',
    packages = ['soccer'],
    entry_points = {
        'console_scripts': [
            'soccer = soccer.__main__:main'
        ]
    })