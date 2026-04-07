from setuptools import setup, find_packages

setup(
    name='{repo_name}',
    version='0.1.0',
    description='{title} - A handy CLI tool',
    author='Efe Altıparmakoğlu',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            '{repo_name}={repo_name}.main:main',
        ],
    },
    python_requires='>=3.8',
)
