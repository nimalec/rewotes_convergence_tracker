#!/usr/bin/env python3
from kconverge.kconverge import Kconverge
from kconverge.calculation import DFTParameters, Material


threshold =  7.3498810939358E-6 ## threshold dE in Ry
work_dir = './ktest_converge'

##SCF Parameters
control = {'pseudo_dir': '../../../pseudo'}   
pseudos = {'Si': 'si_pbe_gbrv_1.0.upf'}
system = {'ecutwfc': 40, 'occupations': 'smearing', 'degauss': 0.005}
electrons = {'mixing_beta': 0.3}
scf_parameters = DFTParameters(pseudos, control, system, electrons)


## Make instance of material object
lattice = [[3.867000000, 0.000000000, 0.000000000], [1.933500000, 3.348920236, 0.000000000], [1.933500000, 1.116306745, 3.157392278]]
species = ['Si', 'Si']
positions = [[0.0, 0.0, 0.0], [0.25, 0.25, 0.25]]
material_structure = Material('Si2', lattice, species, positions)

##Setup and Run calculaiton
kconverge_workflow = Kconverge(threshold, work_dir, scf_parameters, material_structure)
kconverge_workflow.configure_run_convergence_calculations()
