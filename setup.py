from setuptools import setup

setup(
    name='bimt',
    version='0.1.0',
    author='mtsz-thiago',
    author_email='thiagosz@cos.ufrj.br',
    packages=['bimt', 'bimt.test'],
    # scripts=['bin/script1','bin/script2'],
    url='https://github.com/mtsz-thiago/bimt',
    license='LICENSE.txt',
    description='Trabalho de disciplina',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.1.1",
        # "pytest",
    ]
)