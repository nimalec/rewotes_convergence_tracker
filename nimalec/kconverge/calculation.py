"""Kconverge calculation classes.
Classes here are used as object instances and sub-routines within the KConverge algorithm.
version of May 2023
"""

from pymatgen.core.structure import Structure
from pymatgen.io.pwscf import PWInput
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import os

from kconverge.io import *

class Material:
    """
    Class representing the structure and composition of material used in calculation.

    Attributes
    - - - - - - -
    _name : 'str'
        Name assigned to the material.
    _atoms : 'str'
        List of atomic species corresponding to sites.
    _lattice : 'list'
        3x3 list of lattice parameters of crystal in Angstroms.
    _positions : 'list'
        List of atomic positions in fractional coordinates.
    _structure : 'pymatgen.structure.Structure'
       Instance of Structure object in Pymatgen.
    _volume : 'float'
        Extracted volume in Ang.^3 of supercell.
    _space_group : 'str'
       Extracted space group of crystal
    """

    def __init__(self, name, lattice, atoms, positions):
        """
        Initiates instance of a Material class used in SCF workflows.
        Parameters:
            name : 'str'
               Name of material.
            lattice : 'list'
                 3x3 list of lattice parameters of crystal in Angstroms.
            atoms : 'list'
                List of atomic species corresponding to sites.
            positions : 'list'
                List of atomic positions in fractional coordinates.
        """
        self._name = name
        self._atoms = atoms
        self._lattice = lattice
        self._positions = positions
        self._structure = Structure(self._lattice, self._atoms, self._positions)
        self._volume = self._structure.volume
        sg_analysis = SpacegroupAnalyzer(self._structure)
        self._space_group = sg_analysis.get_space_group_symbol()

    def get_name(self):
        """
        Returns name of material.
        """
        return self._name

    def get_atoms(self):
        """
        Returns list of atomic species.
        """
        return self._atoms

    def get_lattice(self):
        """
        Returns crystal lattice.
        """
        return self._lattice

    def get_structure(self):
        """
        Returns instance of structure.
        """
        return self._structure

    def get_sites(self):
        """
        Returns atomic sites.
        """
        return self._structure.sites

    def to_cif(self, file_path):
        """
        Converts structure into a CIF file for visualization, provided filepath.
        """
        self._structure.to(file_path)

class DFTParameters:
    """
    Class used to keep track of SCF DFT parameters used in calculations.

    Attributes
    - - - - - - -
    _pseudo : 'dict'
        Dictionary of pseudopotential file names for each atom (e.g. '{W: W_pseudo.upf}').
    _control : 'dict'
        Dictionary of control parameters used in QE.
    _system : 'dict'
        Dictionary of system parameters used in QE.
    _electrons : 'dict'
        Dictionary of electron parameters used in QE.
    """
    def __init__(self, pseudos, control, system, electrons):
        """
        Initiates instance of a DFTParameters class used in SCF workflows.
        Parameters:
            pseudo : 'dict'
                Dictionary of pseudopotential file names for each atom (e.g. '{W: W_pseudo.upf}').
            control : 'dict'
                Dictionary of control parameters used in QE.
            system : 'dict'
                Dictionary of system parameters used in QE.
            electrons : 'dict'
                Dictionary of electron parameters used in QE.
        """
        self._pseudo = pseudos
        self._control = control
        self._system = system
        self._electrons = electrons

    def get_pseudos(self):
        """
        Returns psuedo Dictionary.
        """
        return self._pseudo

    def get_control_parameters(self):
        """
        Returns control Dictionary.
        """
        return self._control

    def get_system_parameters(self):
        """
        Returns systems Dictionary.
        """
        return self._system

    def get_electrons_parameters(self):
        """
        Returns electrons Dictionary.
        """
        return self._electrons

class SCFRunFiles:
    """
    Class used to manage settings and file generation for run files on the Matr3a cluster.

    Attributes
    - - - - - - -
    _run_parameters : 'dict'
        Dict. of run parameters to keep track of during run: {'job_name', 'nodes', 'ppn', 'email', 'project', 'walltime'}

    """
    def __init__(self, job_name, nodes, ppn, queue, email, project, walltime='00:20:00'):
        """
        Configures run settings.
        Parameters:
          job_name : 'str'
             Name of job.
          nodes : 'int'
             Number of nodes used in run.
          ppn : 'int'
             Number of processors per node used in run.
          queue : 'str'
             Type of queue setting.
          email : 'str'
             Email used to forward run info.
          project : 'str'
             Project name.
          Walltime : 'str'
             Walltime for run to finish.
        """
        self._run_parameters = {'job_name': job_name, 'nodes': nodes, 'ppn': ppn, 'email': email, 'project': project, 'walltime':  walltime}

    def make_runscript(self, file_path):
        """
        Genertes a run script provided the file path.
        """
        generate_run_script(self._run_parameters, file_path)


class SCFCalculation:
    """
    Class used to configure SCF calculation in QE.

    Attributes
    - - - - - - -
    _kpoints_param : 'dict'
        Dictionary used to keep track of kpoints and k shift.
    _calculation_parameters : 'kconverge.calculation.DFTParameters'
        Instance of DFTParameters used to configure SCF variables.
    _structure : 'kconverge.calculation.Material'
        Instance of Material object defining structure and composition of material.
    _scf_calculation : 'pymatgen.io.pwscf.PWInput'
        Instance of PWInput scf calculation parameters from Pymatgen.
    """
    def __init__(self, calculation_parameters, structure, kpoints, kpoints_shift=(0,0,0)):
        """
        Configures calculations and sets up appropriate directories.
        Parameters:
            calculation_parameters : 'kconverge.calculation.DFTParameters'
                Instance of DFTParameters used to configure SCF variables.
            structure : 'kconverge.calculation.Material'
                Instance of Material object defining structure and composition of material.
            kpoints : 'tuple'
                  3x1 tuple of k-point mesh density.
            kpoints_shift : 'tuple'
                3x1 tuple of k-point vector shift (used in phonon calculations).
        """
        self._kpoints_param = {'kpoints': kpoints, 'kpoints_shift': kpoints_shift}
        self._calculation_parameters = calculation_parameters
        self._calculation_parameters._control['calculation'] = 'scf'
        self._calculation_parameters._control['title'] = ''
        self._calculation_parameters._control['verbosity'] = 'low'
        self._calculation_parameters._control['restart_mode'] = 'from_scratch'
        self._calculation_parameters._control['wf_collect'] = True
        self._calculation_parameters._control['tstress'] = True
        self._calculation_parameters._control['tprnfor'] = True
        self._calculation_parameters._control['outdir'] = './'
        self._calculation_parameters._control['wfcdir'] = './'
        self._calculation_parameters._control['prefix'] = '__prefix__'
        self._calculation_parameters._electrons['startingwfc'] = 'atomic+random'
        self._calculation_parameters._electrons['diagonalization'] = 'david'
        self._calculation_parameters._electrons['diago_david_ndim'] = 4
        self._calculation_parameters._electrons['diago_full_acc'] = True
        self._structure = structure._structure
        self._scf_calculation = PWInput(self._structure, self._calculation_parameters._pseudo, self._calculation_parameters._control, self._calculation_parameters._system, self._calculation_parameters._electrons, kpoints_grid = self._kpoints_param['kpoints'], kpoints_shift=self._kpoints_param['kpoints_shift'])

    def return_params_dict(self):
        """
        Returns parameters dict.
        """
        return self._scf_calculation.as_dict()

    def make_input_file(self, file_path):
        """
        Returns input file provided file_path.
        """
        self._scf_calculation.write_file(file_path)

class SCFCalculationWorkflow:
    """
    Class used to configure and execute a SCF calculaiton with QE.

    Attributes
    - - - - - - -
    _scf_calculation : 'kconverge.calculaiton.SCFCalculation'
        Instance of class used to configure SCF calculation.
    _run_script : 'kconverge.calculaiton.SCFRunFiles'
        Instance of class for running SCF parameters.
    _work_dir : 'str'
        Work directory for calculation.
    _run_status : 'str'
        Dict. of parameters describing run status.
    _cwd : 'str'
       Current working directory.
    """
    def __init__(self, work_dir, calculation_parameters, structure, kpoints, job_name, nodes, ppn, queue, email, project, walltime='00:20:00', kpoints_shift=(0,0,0)):
        """
        Configures calculations and sets up appropriate directories.
        """
        self._scf_calculation = SCFCalculation(calculation_parameters, structure, kpoints, kpoints_shift)
        self._run_script = SCFRunFiles(job_name, nodes, ppn, queue, email, project, walltime='00:20:00')
        self._work_dir = work_dir
        self._run_status = {'run_status': 'P', 'job_id': None, 'job_name': job_name, 'email': email, 'done':  False, 'crash': False}
        self._cwd = os.getcwd()

    def setup_work_dir(self):
        """
        Configures and genreates work directories and files.
        """
        os.mkdir(self._work_dir)
        runscript_path = os.path.join(self._work_dir, 'job.pbs')
        infile_path = os.path.join(self._work_dir, 'scf.in')
        self._run_script.make_runscript(runscript_path)
        self._scf_calculation.make_input_file(infile_path)

    def run_calculation(self):
        """
        Submits a job.
        """
        os.chdir(self._work_dir)
        job_id = extract_job_id_submission(run_file='job.pbs')
        self._run_status['job_id'] = job_id
        os.chdir(self._cwd)

    def update_run_status(self):
        """
        Updates current run status.
        """
        queue_status = extract_run_status(self._run_status['job_id'])
        pw_out_status = check_scf_out(self._work_dir)
        if pw_out_status is True and queue_status == 'D':
            self._run_status['run_status'] = 'D'
        elif pw_out_status is False and queue_status == 'D':
            self._run_status['run_status'] = 'P'
        else:
            self._run_status['run_status'] = queue_status
        return self._run_status['run_status']

    def update_done_status(self):
        """
        Updates status if job is done.
        """
        self._run_status['done'] = check_job_done(self._work_dir)
        return self._run_status['done']

    def update_crash_status(self):
        """
        Updates status if job has crashed.
        """
        self._run_status['crash'] = check_crash(self._work_dir)
        return self._run_status['crash']

    def setup_work_dir_run(self):
        """
        Initites work directories and runs.
        """
        self.setup_work_dir()
        self.run_calculation()
        self.update_run_status()

    def get_total_energy(self):
        """
        Obtains total energy from calculation.
        """
        return get_total_energy(os.path.join(self._work_dir, 'scf.out'))
