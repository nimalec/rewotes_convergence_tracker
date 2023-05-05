"""Kconverge class
Determines optimal k-point mesh to achieve convergence in a DFT calculation.
version of May 2023
"""
class Kconverge:
   """
    Class used to execute convergence test with respect to k-poin mesh for a calculation.

    Attributes
    - - - - - - -
    _calculation_parameters : 'dict'
        Dictionary of the parameters extracted from the input file used for DFT calculations in convergence tests.
    _session : zhinst.toolkit.session.Session
        Instance of Zurich session for established connection.
    _hdawg : zhinst.toolkit.driver.devices.hdawg.HDAWG
        Instance of Zurich HDAWG driver.

    Methods
    - - - - - - -

    """
    def __init__(self, template_input_file, template_run_script, convergence_parameter, convergence_threshold, plot=True):
        ##Note ==> - template_input_file only provides input parameters
        ##          -template run_script ==> proivdes info necessary to run a calculation
        ## convergence_parameter ==> depending on calculation type, will determine an appropriate workflow to set up calculation
        ## convergence threshodl ==> depends on calculation type
        ##Assumes a pre-relaxed structure
        ## convergence parameters: phonon frequency, bands [scalar, vector, tensor]
        ## total energy
        ## total stress
        ## element of stress tensor
        ## phonon frequency (at q=0) and provided n
        ## band (at gamma) and provided n
        self._calculation_parameters = None
        self._input_structure = None
        self._run_information = None
        self._workflow = None
        self._kpoint_list = None
        self._convergence_threshold = None
        self._plot = plot
        self._work_dir = None

    def get_calculation_parameters(self):
        return 1

    def set_calculation_parameters(self):
        return 1

    def get_run_info(self):
        return 1

    def set_run_info(self):
        return 1

    def get_run_info(self):
        return 1

    def get_workflow_type(self):
        return 1

    def get_convergence_property(self):
        return 1

   def get_symmetry(self):

   def set_symmetry(self):

   def run_convergence_test(self):
       ## Should make a python file to run in the background (test this method first).
       ## should run in the background 'nohup python ' in background.
       ## Check continuously for run status ==>

   def kill_convergence_test(self):
