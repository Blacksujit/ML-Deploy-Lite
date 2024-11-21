# setup.py

from setuptools import setup, find_packages

setup(
    name='ml-deploy-lite',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'gunicorn',
        'docker',
        'pyyaml',
        'joblib',
        'scikit-learn',
        'prometheus_flask_exporter'
    ],
    description='A library to simplify ML model deployment',
    author='Sujit Nirmal (@blacksujit)',
    author_email='nirmalsujit981@gmail.com',
    url='https://github.com/Blacksujit/ML-Deploy-Lite.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)