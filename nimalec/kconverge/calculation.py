from pymatgen.core.structure import Structure
from pymatgen.io.pwscf import PWInput
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

from kconverge.io import generate_run_script

class Material:
    def __init__(self, name, lattice, atoms, positions):
        self._name = name
        self._atoms = atoms
        self._lattice = lattice
        self._positions = positions
        self._structure = Structure(self._lattice, self._atoms, self._positions)
        self._volume = self._structure.volume
        sg_analysis = SpacegroupAnalyzer(self._structure)
        self._space_group = sg_analysis.get_space_group_symbol()

    def get_name(self):
        return self._name

    def set_name(self):
        return self._name

    def get_atoms(self):
        return self._atoms

    def get_lattice(self):
        return self._lattice

    def get_structure(self):
        return self._structure

    def get_sites(self):
        return self._structure.sites

    def to_cif(self, file_path):
        self._structure.to(file_path)

class DFTParameters:
    def __init__(self, pseudos, control, system, electrons):
        self._pseudo = pseudos
        self._control = control
        self._system = system
        self._electrons = electrons

    def get_pseudos(self):
        return self._pseudo

    def get_control_parameters(self):
        return self._control

    def get_system_parameters(self):
        return self._system

    def get_electrons_parameters(self):
        return self._electrons

    def set_pseudo(self):
        return self._pseudo

    def set_control(self):
        return self._control

    def set_system(self):
        return self._system

    def set_electrons(self):
        return self._electrons

class SCFRunFiles:
    def __init__(self, job_name, nodes, ppn, queue, email, project, walltime='00:20:00'):
        self._run_parameters = {'job_name': job_name, 'nodes': nodes, 'ppn': ppn, 'email': email, 'project': project, 'walltime':  walltime}
    def make_runscript(self, file_path):
        generate_run_script(self._run_parameters, file_path)


class SCFCalculation:
    def __init__(self, calculation_parameters, structure, kpoints, kpoints_shift=(0,0,0)):
        self._kpoints_param = {'kpoints': kpoints, 'kpoints_shift': kpoints_shift}
        self._calculation_parameters = calculation_parameters
        self._calculation_parameters._control['calculation'] = 'scf'
        self._calculation_parameters._control['title'] = ''
        self._calculation_parameters._control['verbosity'] = 'low'
        self._calculation_parameters._control['restart_mode'] = 'from_scratch'
        self._calculation_parameters._control['wf_collect'] = '.true.'
        self._calculation_parameters._control['tstress'] = '.true.'
        self._calculation_parameters._control['tprnfor'] = '.true.'
        self._calculation_parameters._control['outdir'] = './'
        self._calculation_parameters._control['wfcdir'] = './'
        self._calculation_parameters._control['__prefix__'] = '__prefix__'
        self._calculation_parameters._electrons['startingwfc'] = 'atomic+random'
        self._calculation_parameters._electrons['diagonalization'] = 'david'
        self._calculation_parameters._electrons['diago_david_ndim'] = 4
        self._calculation_parameters._electrons['diago_full_acc'] = '.true.'
        self._structure = structure._structure
        self._scf_calculation = PWInput(self._structure, self._calculation_parameters._pseudo, self._calculation_parameters._control, self._calculation_parameters._system, self._calculation_parameters._electrons, kpoints_grid = self._kpoints_param['kpoints'], kpoints_shift=self._kpoints_param['kpoints_shift'])

    def return_params_dict(self):
        return self._scf_calculation.as_dict()

    def make_input_file(self, file_path):
        self._scf_calculation.write_file(file_path)

class SCFCalculationWorkflow:
    #def __init__(self):
        ##Configures calculaiton...
    #def make_work_dir(self):
    #def run_calculation(self):
    #def extract_total_energy(self):
    #def check_run_status(self):
    #def extract_stress_tensor(self):
    #def 
