"""setup.py file for packaging ``swagexample``."""

from setuptools import setup, find_packages


with open('readme.md', 'r') as readme_file:
    readme = readme_file.read()


setup(
    name='swagexample',
    version='0.0.0',
    description="An example submission for the SWAG leaderboard.",
    long_description=readme,
    url='http://github.com/allenai/swagexample',
    author='Allen Institute for Artificial Intelligence',
    author_email='alexandria@allenai.org',
    keywords='deep learning swag allennlp',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    license='Apache',
    packages=find_packages(),
    install_requires=[
        'allennlp',
        'ipython',
        'torch',
        'torchvision'
    ],
    python_requires='>=3.6',
    zip_safe=False
)
