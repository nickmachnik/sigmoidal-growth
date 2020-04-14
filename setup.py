import os
from setuptools import setup, find_packages, Command


__version__ = '0.0.1'

class CleanCommand(Command):
    """
    Custom clean command to tidy up the project root.
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info ./htmlcov')

setup(
    name='sigmoidal-growth',
    version=__version__,
    description='',
    # long_description_content_type="text/markdown",
    url='https://github.com/nickmachnik/sigmoidal-growth',
    setup_requires=[
        'setuptools>=18.0',
    ],
    packages=find_packages(),
    install_requires=[
        'numpy>=1.8.0',
        'scipy'
    ],
    cmdclass={
        'clean': CleanCommand
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
