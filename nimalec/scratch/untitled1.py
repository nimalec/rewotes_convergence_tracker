from kconverge.calculation import Material, DFTParameters, SCFCalculation, SCFRunFiles, SCFCalculationWorkflow
#
## Make instance of material object
lattice = [[3.867000000, 0.000000000, 0.000000000], [1.933500000, 3.348920236, 0.000000000], [1.933500000, 1.116306745, 3.157392278]]
species = ['Si', 'Si']
positions = [[0.0, 0.0, 0.0], [0.25, 0.25, 0.25]]
material_structure = Material('Si2', lattice, species, positions)

##DFT parameters
control = {'pseudo_dir': '../pseudo'}
pseudos = {'Si': 'si_pbe_gbrv_1.0.upf'}
system = {'ecutwfc': 40, 'occupations': 'smearing', 'degauss': 0.005}
electrons = {'mixing_beta': 0.3}
kpoints = (2,2,2)
dft_params = DFTParameters(pseudos, control, system, electrons)

workflow = SCFCalculationWorkflow('./test', dft_params, material_structure, kpoints, job_name='scf1', nodes=1, ppn=1,queue='qe' ,email='nl475@cornell.edu', project='nleclerc97')
workflow.setup_work_dir()
# dft_calc = SCFCalculation(dft_params, material_structure, kpoints)
# dft_calc.make_input_file('scf2.in')
#
# ##Run Script
# run_script = SCFRunFiles(job_name='Si2', nodes=4, ppn=2, queue='qe', email='nl475@cornell.edu', project='nleclerc-97')
# run_script.make_runscript(file_path='job.pbs')
