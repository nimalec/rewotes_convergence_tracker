from pymatgen.core.structure import Structure
from pymatgen.io.pwscf import PWInput

class Material:
    def __init__(self, name, lattice, atoms, positions):
        self._name = name
        self._atoms = atoms
        self._lattice = lattice
        self._positions = positions
        self._structure = Structure(self._lattice, self._atoms  self._positions)

     def get_name(self):
         return self._name

     def get_atoms(self):
         return self._atoms

     def get_lattice(self):
         return self._lattice

     def get_structure(self):
         return self._structure

class CalcParameters:
    def __init__(self, pseudos, control, system, electrons):
        self._pseudo = pseudos
        self._control = control
        self._system = system
        self._electrons = electrons

    def get_pseudo(self):
        return self._pseudo

    def get_control(self):
        return self._control

    def get_system(self):
        return self._system

    def get_electrons(self):
        return self._electrons

class Calculation:
    def __init__(self, calculation_parameters, structure, kpoints, kpoints_shift=(0,0,0)):
        self._kpoints_param = {'kpoints': kpoints, 'kpoints_shift': kpoints_shift}
        self._calculation_parameters = calculation_parameters
        self._structure = structure
        self._scf_calculation = PWInput(self._structure, self._calculation_parameters._pseudo, self._calculation_parameters._control, self._calculation_parameters._system, self._calculation_parameters._electrons, kpoints_grid = kpoints, kpoints_shift=kpoints_shift)
