def generate_run_script(run_parameters, file_path):
    runscript_text =  f'''
    #!/bin/bash\n
    #PBS -N {run_parameters['job_name']}\n
    #PBS -j oe\n
    #PBS -l nodes={run_parameters['nodes']}\n
    #PBS -l ppn={run_parameters['ppn']}\n
    #PBS -l walltime={run_parameters['walltime']}\n
    #PBS -q D\n
    #PBS -m abe\n
    #PBS -M {run_parameters['email']}\n
    #PBS -A {run_parameters['project']}\n\n
    module add espresso/540-i-174-impi-044 \n
    mpirun -np $PBS_NP pw.x -in pw.in > pw.out  \n
    '''
    with open(file_path, 'w') as f:
        f.write(runscript_text)
