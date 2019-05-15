Quantum Monte Carlo Package
===========================

Made by: Coen de Jong, Peter-Jan Derks and Vincent van de Kerkhof

To install the package type `python setup.py install`
To run the code choose one of three quantum systems: harmonic oscillator, 
hydrogen atom or helium atom, and then while in the folders of these files 
type `python energy_and_variance.py` or `minimal_energy_finder.py`


The folder QMCP contains the folders:

    functions: 
        __init__.py 
        metropolis_algorithm.py
        energy_and_variance.py 
        error_calculation.py 
        minimal_energy_finder.py
    harmonic_oscillator:
         __init__.py 	
        minimal_energy_oscillator.py 
        oscillator.py 	
        vmc_oscillator.py 
    hydrogren_atom:
         __init__.py 
        hydrogen.py 	
        minimal_energy_hydrogen.py 
        vmc_hydrogen.py 
    helium_atom:
         __init__.py 
        helium_atom.py 	
        minimal_energy_helium.py 	
        vmc_helium.py 
    