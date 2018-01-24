from setuptools import setup

setup(
    name="filecount",
    version="0.0.1-beta",
    description='filecount like wc-command',
    license='MIT',
    author='FUKUDA Yutaro',
    url='https://github.com/sktnkysh/filecount',
    entry_points={"console_scripts": ["filecount = filecount.filecount:main"]},)
