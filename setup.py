from setuptools import setup
setup(
    name = 'soccer',
    version = '1.0.0',
    packages = ['soccer'],
    entry_points = {
        'console_scripts': [
            'soccer = soccer.__main__:main'
        ]
    })