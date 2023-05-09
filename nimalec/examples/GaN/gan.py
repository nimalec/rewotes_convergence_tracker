#!/usr/bin/env python3
from kconverge.kconverge import Kconverge
from kconverge.calculation import DFTParameters, Material


threshold =  7.3498810939358E-4 ## threshold dE in Ry
work_dir = './ktest_converge'

##SCF Parameters
control = {'pseudo_dir': '../../../pseudos'}
pseudos = {'Ga': 'ga_pbe_gbrv_1.4.upf', 'N': 'n_pbe_gbrv_1.2.upf'}
system = {'ecutwfc': 40, 'occupations': 'smearing', 'degauss': 0.005}
electrons = {'mixing_beta': 0.3}
scf_parameters = DFTParameters(pseudos, control, system, electrons)

## Make instance of material object
lattice = [[1.5944652017623229, -2.7616947403529042, 0.0000000000000000], [1.5944652017623229,2.7616947403529042, 0.0000000000000000], [0.000000000000000, 0.0000000000000000, 5.192357249999999]]
species = ['Ga', 'Ga', 'N', 'N']
positions = [ [0.6666666666666666, 0.3333333333333333, 0.4990837100000000], [0.3333333333333333, 0.6666666666666666 , 0.999083710000000], [0.6666666666666666,    0.3333333333333333,     0.8759162900000000  ], [0.3333333333333333, 0.6666666666666666, 0.375916290000000] ]
material_structure = Material('GaN', lattice, species, positions)

##Setup and Run calculaiton
kconverge_workflow = Kconverge(threshold, work_dir, scf_parameters, material_structure)
kconverge_workflow.configure_run_convergence_calculations()
