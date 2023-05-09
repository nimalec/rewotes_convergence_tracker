#!/usr/bin/env python3
from kconverge.kconverge import Kconverge
from kconverge.calculation import DFTParameters, Material


threshold =  7.3498810939358E-4 ## threshold dE in Ry
work_dir = './ktest_converge'

##SCF Parameters
control = {'pseudo_dir': '../../../pseudo'}
pseudos = {'Ca': 'ca_pbe_gbrv_1.0.upf', 'F': 'f_pbe_gbrv_1.4.upf'}
system = {'ecutwfc': 40, 'occupations': 'smearing', 'degauss': 0.005}
electrons = {'mixing_beta': 0.3}
scf_parameters = DFTParameters(pseudos, control, system, electrons)

## Make instance of material object
lattice = [[3.5636170699999998, 0.0000000000000000, 0.0000000000000002], [0.0000000000000010, 5.9290983300000004, 0.0000000000000004], [0.0000000000000000,0.0000000000000000, 6.9917818599999997]]
species = ['Ca', 'Ca', 'Ca', 'Ca', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
positions = [[0.2500000000000000, 0.2490696799999998, 0.8881407700000000], [0.7500000000000000, 0.7509303200000002, 0.1118592300000000], [0.2500000000000000, 0.749069679999999, 0.6118592300000000], [0.7500000000000000, 0.2509303200000002, 0.3881407700000001 ], [ 0.2500000000000000 ,   0.4785842300000001 ,   0.1657371900000000] , [ 0.7500000000000000   , 0.5214157699999999  ,  0.8342628100000000 ], [ 0.2500000000000000  ,  0.9785842300000001    , 0.3342628100000000 ], [ 0.7500000000000000 ,   0.0214157699999999 ,   0.6657371900000000 ], [ 0.7500000000000000  ,  0.6434892600000000  ,  0.4264809500000000], [0.2500000000000000 ,   0.3565107400000000,     0.5735190500000000 ], [0.7500000000000000  ,  0.1434892600000000  ,  0.0735190500000000  ], [ 0.2500000000000000 ,   0.8565107400000000  ,  0.9264809500000000]]
material_structure = Material('CaF2', lattice, species, positions)


##Setup and Run calculaiton
kconverge_workflow = Kconverge(threshold, work_dir, scf_parameters, material_structure)
kconverge_workflow.configure_run_convergence_calculations()
