#!/usr/bin/env python3
from kconverge.kconverge import Kconverge
from kconverge.calculation import DFTParameters, Material


threshold =  7.3498810939358E-4 ## threshold dE in Ry
work_dir = './ktest_converge'

##SCF Parameters
control = {'pseudo_dir': '../../../pseudos'}
pseudos = {'P': 'p_pbe_gbrv_1.5.upf'}
system = {'ecutwfc': 40, 'occupations': 'smearing', 'degauss': 0.005}
electrons = {'mixing_beta': 0.3}
scf_parameters = DFTParameters(pseudos, control, system, electrons)

## Make instance of material object
lattice = [[ 0.0000000000000000, 5.6351172264936524, 0.0000000000000000], [19.6324366611214387, 0.0000000000000000, 0.0000000000000000],  [0.0000000000000000  , -1.6004025234166963  ,-6.1198546024297116]]
species = ['P', 'P',  'P', 'P', 'P', 'P',  'P', 'P', 'P', 'P' ]
positions = [[0.8542036300000000  ,  0.5873942799999999   , 0.3104098599999999] , [0.8277006899999999 ,   0.5570265599999999 ,   0.6386004499999999], [0.8277006899999999  ,  0.4429734400000001  ,  0.6386004499999999  ], [0.8542036300000000  ,  0.4126057200000001   , 0.3104098599999999 ] , [ 0.7728738300000000   , 0.5000000000000000 ,    0.0872081199999998], [0.4571346600000000 ,   0.4131145900000002 ,   0.6695400299999998], [ 0.2434564699999999   , 0.4420039800000002 ,   0.3414155599999998 ], [ 0.2434564699999999 ,   0.5579960199999998  ,  0.3414155599999998  ], [0.4571346600000000  ,  0.5868854099999998 ,   0.6695400299999998] , [0.3915107300000000  ,  0.5000000000000000   , 0.8748733000000000]]
material_structure = Material('P', lattice, species, positions)

##Setup and Run calculaiton
kconverge_workflow = Kconverge(threshold, work_dir, scf_parameters, material_structure)
kconverge_workflow.configure_run_convergence_calculations()
