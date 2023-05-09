#!/usr/bin/env python3
from kconverge.kconverge import Kconverge
from kconverge.calculation import DFTParameters, Material


threshold =  7.3498810939358E-4 ## threshold dE in Ry
work_dir = './ktest_converge'

##SCF Parameters
control = {'pseudo_dir': '../../../pseudo'}
pseudos = {'Ge': 'ga_pbe_gbrv_1.4.upf'}
system = {'ecutwfc': 40, 'occupations': 'smearing', 'degauss': 0.005}
electrons = {'mixing_beta': 0.3}
scf_parameters = DFTParameters(pseudos, control, system, electrons)

## Make instance of material object
lattice = [[5.9372086599999996,    0.0000000000000000,    0.0000000000000004], [1.933500000, 3.348920236, 0.000000000], [ 0.0000000000000000, 0.0000000000000000, 7.0806529999999999]]
species = ['Ge', 'Ge', 'Ge', 'Ge', 'Ge', 'Ge', 'Ge', 'Ge','Ge', 'Ge', 'Ge', 'Ge']
positions = [[ 0.0856035700000000, 0.0856035700000000, 0.0000000000000000], [  0.0000000000000010,    5.9372086599999996,    0.0000000000000004],[0.5856035700000000, 0.4143964300000000,  0.2500000000000000], [ 0.9143964300000000,    0.9143964300000000,    0.5000000000000000], [0.1694391000000000,    0.3720959400000000,    0.2454362400000000 ], [ 0.1279040600000000,    0.6694391000000000,    0.9954362400000000 ], [  0.8720959400000000,    0.3305609000000000 ,   0.4954362400000000], [ 0.6694391000000000,    0.1279040600000000,    0.0045637600000000 ] [ 0.3305609000000000 ,   0.8720959400000000,    0.5045637600000000], [   0.8305609000000000,    0.6279040600000000  ,   0.7454362400000000 ],[  0.3720959400000000,    0.1694391000000000 ,   0.7545637600000000 ],[ 0.6279040600000000,    0.8305609000000000,    0.2545637600000000] ]
material_structure = Material('Ge', lattice, species, positions)


##Setup and Run calculaiton
kconverge_workflow = Kconverge(threshold, work_dir, scf_parameters, material_structure)
kconverge_workflow.configure_run_convergence_calculations()
