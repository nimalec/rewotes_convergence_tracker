#!/usr/bin/env python3
from kconverge.kconverge import Kconverge
from kconverge.calculation import DFTParameters, Material


threshold =  7.3498810939358E-4 ## threshold dE in Ry
work_dir = './ktest_converge'

##SCF Parameters
control = {'pseudo_dir': '../../../pseudos'}
pseudos = {'Mg': 'mg_pbe_gbrv_1.4.upf', 'S': 's_pbe_gbrv_1.4.upf'}
system = {'ecutwfc': 40, 'occupations': 'smearing', 'degauss': 0.005}
electrons = {'mixing_beta': 0.3}
scf_parameters = DFTParameters(pseudos, control, system, electrons)

## Make instance of material object
lattice = [[0.0000000000000000, 6.8907583727774568, 0.0000000000000000], [3.9105414099458464, 0.0000000000000000,  0.0000000000000000], [0.0000000000000000, -2.2685610174952568 , -4.5632732332881787]]
species = ['Mg', 'Mg', 'S', 'S', 'S', 'S']
positions = [[0.5000000000000000, 0.0000000000000000, 0.5000000000000000], [0.0000000000000000, 0.5000000000000000, 0.5000000000000000 ], [0.5800895199999999, 0.5000000000000000 , 0.2278141899999999], [0.4199104800000001 , 0.5000000000000000 , 0.7721858100000001], [0.0800895199999999 , 0.0000000000000000 ,   0.2278141899999999 ], [ 0.9199104800000000   , 0.0000000000000000 ,   0.7721858100000001] ]
material_structure = Material('MgS2', lattice, species, positions)

##Setup and Run calculaiton
kconverge_workflow = Kconverge(threshold, work_dir, scf_parameters, material_structure)
kconverge_workflow.configure_run_convergence_calculations()
