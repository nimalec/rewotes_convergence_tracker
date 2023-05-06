import subprocess
import re
from os.path import exists

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

def extract_job_id_submission(run_file='job.pbs'):
    output = subprocess.Popen("qsub "+run_file, shell=True, stdout=subprocess.PIPE).stdout.read()
    return str(int(output[0:5]))

def extract_run_status(job_id):
    output = subprocess.Popen("qstat ", shell=True, stdout=subprocess.PIPE).stdout.read()
    items=re.findall(job_id+".*$",output,re.MULTILINE)
    if len(items) == 0:
        run_status = 'D'
    else:
        run_status = items[0][72]
    return run_status

def check_scf_out(directory):
    outfile = exists(os.path.join(directory), 'scf.out')
    return outfile
