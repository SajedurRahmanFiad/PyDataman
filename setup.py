from setuptools import setup
import os
long_description = 'Store your variables outside the code!'
if os.path.exists('pyvariable\README.md'):
    long_description = open('pyvariable\README.md').read()

# This call to setup() does all the work
setup(
    name="PyDataman",
    version="1.0.2",
    description="Store your variables outside the code!",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['firebase', 'pyrebase4'],
    zip_safe = False,
    author="Sajedur Rahman Fiad",
    author_email="neural.gen.official@gmail.com",
    packages = ['pydataman']
)
