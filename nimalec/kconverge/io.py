def generate_run_script(run_parameters, file_path):
    runscript_text =  f'''#!/bin/bash\n
#PBS -N {run_parameters['job_name']}
#PBS -j oe
#PBS -l nodes={run_parameters['nodes']}
#PBS -l ppn={run_parameters['ppn']}
#PBS -l walltime={run_parameters['walltime']}
#PBS -q D
#PBS -m abe
#PBS -M {run_parameters['email']}
#PBS -A {run_parameters['project']}\n
module add espresso/540-i-174-impi-044
mpirun -np $PBS_NP pw.x -in pw.in > pw.out
'''
    with open(file_path, 'w') as f:
        f.write(runscript_text)
