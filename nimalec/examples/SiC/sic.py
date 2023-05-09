#!/usr/bin/env python3
from kconverge.kconverge import Kconverge
from kconverge.calculation import DFTParameters, Material


threshold =  7.3498810939358E-4 ## threshold dE in Ry
work_dir = './ktest_converge'

##SCF Parameters
control = {'pseudo_dir': '../../../pseudos'}
pseudos = {'Si': 'si_pbe_gbrv_1.0.upf', 'C':  'c_pbe_gbrv_1.2.upf'}
system = {'ecutwfc': 40, 'occupations': 'smearing', 'degauss': 0.005}
electrons = {'mixing_beta': 0.3}
scf_parameters = DFTParameters(pseudos, control, system, electrons)

## Make instance of material object
lattice = [[1.5383105051063497, -2.6644319526611402 , 0.0000000000000000], [1.5383105051063497 , 2.6644319526611402 , 0.0000000000000000],  [0.0000000000000000,  0.0000000000000000, 15.0980843199999999]]
species = ['Si', 'Si', 'Si','Si','Si', 'Si', 'C', 'C', 'C' , 'C', 'C', 'C']
positions = [ [0.3333333333333333,   0.6666666666666666,   0.8329861499999999], [0.6666666666666667,    0.3333333333333333 ,   0.3329861500000000], [0.6666666666666666  ,  0.3333333333333333,    0.6665005999999999], [0.3333333333333333  ,  0.6666666666666666  ,  0.1665006000000000 ], [0.0000000000000000  ,  0.0000000000000000 ,   0.4997294199999999 ], [0.0000000000000000 ,   0.0000000000000000 ,   0.9997294199999999], [0.0000000000000000  ,  0.0000000000000000  ,  0.8743664099999999], [ 0.0000000000000000  ,  0.0000000000000000  ,  0.3743664099999999], [ 0.3333333333333333 ,   0.6666666666666666  ,  0.7079967799999999], [ 0.6666666666666667  ,  0.3333333333333333 ,    0.2079967799999998], [0.6666666666666666  ,  0.3333333333333333   , 0.5415216399999999], [ 0.3333333333333333 ,   0.6666666666666666   , 0.0415216400000000]]
material_structure = Material('SiC', lattice, species, positions)

##Setup and Run calculaiton
kconverge_workflow = Kconverge(threshold, work_dir, scf_parameters, material_structure)
kconverge_workflow.configure_run_convergence_calculations()
