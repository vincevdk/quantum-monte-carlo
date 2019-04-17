from setuptools import setup, find_packages
def readme():
    with open('README.md') as f:
        return f.read()

setup(name='QMCP',
      description='Package for Quantum Monte Carlo methods',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 3.5',
        'Topic :: Variational Monte Carlo',
      ],
      url='https://gitlab.kwant-project.org/peter-janderks/Project_2/commits/master',
      author='Peter-Jan Derks, Coen de Jong, Vincent van de Kerkhof',
      packages = find_packages(),
      include_package_data=True)
