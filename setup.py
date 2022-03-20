from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Data Science Package'
LONG_DESCRIPTION = 'The package contains the utility functions needed in everyday life of a data science team revolving around data analytics tools, which are not available in other libraries'

# Setting up
setup(
    name="relart", 
    version=VERSION,
    author="Artem Moskalev",
    author_email="<Artem.Moskalev@relexsolutions.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[pandas, numpy], 
    long_description_content_type="text/markdown",
    url='https://github.com/mike-huls/toolbox',
    license='MIT',
    keywords=['python', 'data science']
)