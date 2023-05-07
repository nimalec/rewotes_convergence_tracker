"""Kconverge class
Determines optimal k-point mesh to achieve convergence in a DFT calculation.
version of May 2023
"""
import os

from kconverge.calculation import *

class Kconverge:
    """
    Class used to execute convergence test with respect to k-poin mesh for a calculation.

    Attributes
    - - - - - - -
    _calculation_parameters : 'dict'
        Dictionary of the parameters extracted from the input file used for DFT calculations in convergence tests.

    Methods
    - - - - - - -

    """
    def __init__(self, threshold, work_dir, scf_parameters, material, nodes=1, ppn=1, queue='qe', email='nl475@cornell.edu', project='nleclerc97-external'):
        self._work_dir = work_dir
        self._run_parameters = {'nodes': nodes, 'ppn': ppn, 'queue': queue, 'email': email, 'project': project}
        self._scf_parameters = scf_parameters
        self._material_structure = material
        self._threshold = threshold

    def configure_run_convergence_calculations(self):
        os.mkdir(self._work_dir)
        os.chdir(self._work_dir)

        ##Initialize k-point mesh for first two poitns to extract dE
        kmesh_initial_0 = (1,1,1)
        kmesh_initial_1 = (2,2,2)
        workdir_initial_0 = os.path.join(self._work_dir, 'scf_k_1')
        workdir_initial_1 = os.path.join(self._work_dir, 'scf_k_2')
        workflow_initial_0 = SCFCalculationWorkflow(workdir_initial_0, self._scf_parameters, self._material_structure, kmesh_initial_0, job_name='scf_k_1', nodes=self._run_parameters['nodes'], ppn=self._run_parameters['ppn'],queue=self._run_parameters['queue'] ,email=self._run_parameters['email'], project=self._run_parameters['project'])
        workflow_initial_0.setup_work_dir_run()
        workflow_initial_1 = SCFCalculationWorkflow(workdir_initial_1, self._scf_parameters, self._material_structure, kmesh_initial_1, job_name='scf_k_2', nodes=self._run_parameters['nodes'], ppn=self._run_parameters['ppn'],queue=self._run_parameters['queue'] ,email=self._run_parameters['email'], project=self._run_parameters['project'])
        workflow_initial_1.setup_work_dir_run()

        status_k_0 = workdir_initial_0.update_done_status()
        status_k_1 = workdir_initial_1.update_done_status()

        while status_k_0 == False and status_k_1 == False:
            status_k_0 = workdir_initial_0.update_done_status()
            status_k_1 = workdir_initial_1.update_done_status()
            crash_k_0 = workdir_initial_0.update_crash_status()
            crash_k_1 = workdir_initial_1.update_crash_status()
            if crash_k_0 == True or crash_k_1 == True:
                break
            else:
                continue

        E_0 = workflow_initial_1.get_total_energy()
        E_1 = workflow_initial_2.get_total_energy()
        dE_0 = E_1-E_0
        f = open(os.path.join(self._work_dir, "out.txt"), "w")
        f.write(str(dE_0))
        f.close()

        # if dE_0 < self._threshold:
        #     ##Start a while loop ...
        #     E_last = E_1
        #     dE = dE_0
        #     k_val = 3
        #     while dE < threshold:
        #         k_mesh = (k_val, k_val, k_val)
        #         work_dir = os.path.join(self._work_dir, 'scf_k_'+str(k_val))
        #         k_workflow = SCFCalculationWorkflow(work_dir, self._scf_parameters, self._material_structure, k_mesh, job_name='scf_k_'+str(k_val), nodes=self._run_parameters['nodes'], ppn=self._run_parameters['ppn'],queue=self._run_parameters['queue'] ,email=self._run_parameters['email'], project=self._run_parameters['project'])
        #         k_workflow.setup_work_dir_run()
        #         done_status = False
        #         while done_status == False:
        #             done_status = k_workflow.done_status()
        #             crash_status =  k_workflow.update_crash_status()
        #             if crash_status == True:
        #                 break
        #             else:
        #                 continue
        #         dE = k_workflow.get_total_energy() - E_last
        #         E_last =  k_workflow.get_total_energy()
        # else:
        #     pass
        # k_optimal = k_val
