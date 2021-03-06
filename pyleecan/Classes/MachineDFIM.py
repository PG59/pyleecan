# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/MachineDFIM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/MachineDFIM
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .MachineAsync import MachineAsync

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.MachineDFIM.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.MachineDFIM.get_machine_type import get_machine_type
except ImportError as error:
    get_machine_type = error

try:
    from ..Methods.Machine.MachineDFIM.get_lam_list import get_lam_list
except ImportError as error:
    get_lam_list = error


from ._check import InitUnKnowClassError
from .LamSlotWind import LamSlotWind
from .Frame import Frame
from .Shaft import Shaft


class MachineDFIM(MachineAsync):
    """Doubly Fed Induction Machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineDFIM.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use MachineDFIM method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.MachineDFIM.get_machine_type
    if isinstance(get_machine_type, ImportError):
        get_machine_type = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineDFIM method get_machine_type: "
                    + str(get_machine_type)
                )
            )
        )
    else:
        get_machine_type = get_machine_type
    # cf Methods.Machine.MachineDFIM.get_lam_list
    if isinstance(get_lam_list, ImportError):
        get_lam_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineDFIM method get_lam_list: " + str(get_lam_list)
                )
            )
        )
    else:
        get_lam_list = get_lam_list
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        rotor=-1,
        stator=-1,
        frame=-1,
        shaft=-1,
        name="default_machine",
        desc="",
        type_machine=1,
        logger_name="Pyleecan.Machine",
        init_dict=None,
        init_str=None,
    ):
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
            if "rotor" in list(init_dict.keys()):
                rotor = init_dict["rotor"]
            if "stator" in list(init_dict.keys()):
                stator = init_dict["stator"]
            if "frame" in list(init_dict.keys()):
                frame = init_dict["frame"]
            if "shaft" in list(init_dict.keys()):
                shaft = init_dict["shaft"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "type_machine" in list(init_dict.keys()):
                type_machine = init_dict["type_machine"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        self.rotor = rotor
        self.stator = stator
        # Call MachineAsync init
        super(MachineDFIM, self).__init__(
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
            logger_name=logger_name,
        )
        # The class is frozen (in MachineAsync init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MachineDFIM_str = ""
        # Get the properties inherited from MachineAsync
        MachineDFIM_str += super(MachineDFIM, self).__str__()
        if self.rotor is not None:
            tmp = self.rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MachineDFIM_str += "rotor = " + tmp
        else:
            MachineDFIM_str += "rotor = None" + linesep + linesep
        if self.stator is not None:
            tmp = self.stator.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MachineDFIM_str += "stator = " + tmp
        else:
            MachineDFIM_str += "stator = None" + linesep + linesep
        return MachineDFIM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MachineAsync
        if not super(MachineDFIM, self).__eq__(other):
            return False
        if other.rotor != self.rotor:
            return False
        if other.stator != self.stator:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from MachineAsync
        MachineDFIM_dict = super(MachineDFIM, self).as_dict()
        if self.rotor is None:
            MachineDFIM_dict["rotor"] = None
        else:
            MachineDFIM_dict["rotor"] = self.rotor.as_dict()
        if self.stator is None:
            MachineDFIM_dict["stator"] = None
        else:
            MachineDFIM_dict["stator"] = self.stator.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        MachineDFIM_dict["__class__"] = "MachineDFIM"
        return MachineDFIM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.rotor is not None:
            self.rotor._set_None()
        if self.stator is not None:
            self.stator._set_None()
        # Set to None the properties inherited from MachineAsync
        super(MachineDFIM, self)._set_None()

    def _get_rotor(self):
        """getter of rotor"""
        return self._rotor

    def _set_rotor(self, value):
        """setter of rotor"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "rotor"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = LamSlotWind()
        check_var("rotor", value, "LamSlotWind")
        self._rotor = value

        if self._rotor is not None:
            self._rotor.parent = self

    rotor = property(
        fget=_get_rotor,
        fset=_set_rotor,
        doc=u"""Machine's Rotor

        :Type: LamSlotWind
        """,
    )

    def _get_stator(self):
        """getter of stator"""
        return self._stator

    def _set_stator(self, value):
        """setter of stator"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "stator"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = LamSlotWind()
        check_var("stator", value, "LamSlotWind")
        self._stator = value

        if self._stator is not None:
            self._stator.parent = self

    stator = property(
        fget=_get_stator,
        fset=_set_stator,
        doc=u"""Machine's Stator

        :Type: LamSlotWind
        """,
    )
