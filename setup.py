from setuptools import setup,find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/BelalAlaaa',
    author='Belal Alaa AL-deen',
    author_email='belalalaaahmedali@gmail.com',
)