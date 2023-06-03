from setuptools import setup, find_packages

setup(
    name='replicPy',
    version='0.1.1',
    description='A sample Python framework',
    long_description=open('README.txt').read(),
    author='sudheesh s',
    author_email='sudheeshsubhash834@gmail.com',
    url='https://github.com/sudheeshsubash/ReplicPy',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'Jinja2>=3.1.2',
    ],
)
