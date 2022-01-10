from setuptools import find_packages, setup

with open("requirements.txt", 'r') as f:
    REQUIREMENTS = f.read()

setup(
    name='simple_elasticsearch_knn',
    version="0.1",
    packages=find_packages(
        include=['simple_elasticsearch_knn', 'simple_elasticsearch_knn.*']
    ),
    install_requires=[i for i in REQUIREMENTS.split('\n') if i is not ""]
)
