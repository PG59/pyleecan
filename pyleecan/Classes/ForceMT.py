# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/ForceMT.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/ForceMT
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Force import Force

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.ForceMT.comp_force import comp_force
except ImportError as error:
    comp_force = error

try:
    from ..Methods.Simulation.ForceMT.comp_force_nodal import comp_force_nodal
except ImportError as error:
    comp_force_nodal = error


from ._check import InitUnKnowClassError


class ForceMT(Force):
    """Force Maxwell tensor model"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.ForceMT.comp_force
    if isinstance(comp_force, ImportError):
        comp_force = property(
            fget=lambda x: raise_(
                ImportError("Can't use ForceMT method comp_force: " + str(comp_force))
            )
        )
    else:
        comp_force = comp_force
    # cf Methods.Simulation.ForceMT.comp_force_nodal
    if isinstance(comp_force_nodal, ImportError):
        comp_force_nodal = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ForceMT method comp_force_nodal: "
                    + str(comp_force_nodal)
                )
            )
        )
    else:
        comp_force_nodal = comp_force_nodal
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, is_comp_nodal_force=False, init_dict=None, init_str=None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "is_comp_nodal_force" in list(init_dict.keys()):
                is_comp_nodal_force = init_dict["is_comp_nodal_force"]
        # Set the properties (value check and convertion are done in setter)
        # Call Force init
        super(ForceMT, self).__init__(is_comp_nodal_force=is_comp_nodal_force)
        # The class is frozen (in Force init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ForceMT_str = ""
        # Get the properties inherited from Force
        ForceMT_str += super(ForceMT, self).__str__()
        return ForceMT_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Force
        if not super(ForceMT, self).__eq__(other):
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from Force
        ForceMT_dict = super(ForceMT, self).as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ForceMT_dict["__class__"] = "ForceMT"
        return ForceMT_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Force
        super(ForceMT, self)._set_None()
