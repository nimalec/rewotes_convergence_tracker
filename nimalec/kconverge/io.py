import subprocess
import re

import os
from os.path import exists

from pymatgen.io.pwscf import PWOutput

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
mpirun -np $PBS_NP pw.x -in scf.in > scf.out
'''
    with open(file_path, 'w') as f:
        f.write(runscript_text)

def extract_job_id_submission(run_file='job.pbs'):
    output = subprocess.Popen("qsub "+run_file, shell=True, stdout=subprocess.PIPE).stdout.read()
    return str(int(output[0:5]))

def extract_run_status(job_id):
    output = str(subprocess.Popen("qstat ", shell=True, stdout=subprocess.PIPE).stdout.read())
    out = str(job_id+".*$")
    items=re.findall(out,output,re.MULTILINE)
    if len(items) == 0:
        run_status = 'D'
    else:
        run_status = items[0][72]
    return run_status

def check_scf_out(directory):
    outfile = exists(os.path.join(directory, 'scf.out'))
    return outfile

def check_job_done(directory):
    file_path = os.path.join(directory, 'scf.out')
    outfile = exists(file_path)
    if outfile == True:
        if 'JOB DONE.' in open(file_path).read() and 'convergence has been achieved in' in open(file_path).read():
            status = True
        else:
            status = False
    else:
        status = False
    return status

def check_crash(directory):
    file_path = os.path.join(directory, 'CRASH')
    outfile = exists(file_path)
    if outfile == True:
        status = True
    else:
        status = False
    return status

def get_total_energy(file):
    pw_out = PWOutput(file)
    return pw_out.final_energy  
