from setuptools import setup

setup(
    name="httpc",
    version='0.1',
    py_modules=['httpc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        httpc=httpc:cli
    ''',
)