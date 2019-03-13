# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.SlotWind import SlotWind

from pyleecan.Methods.Slot.SlotW28._comp_point_coordinate import _comp_point_coordinate
from pyleecan.Methods.Slot.SlotW28.build_geometry import build_geometry
from pyleecan.Methods.Slot.SlotW28.build_geometry_wind import build_geometry_wind
from pyleecan.Methods.Slot.SlotW28.check import check
from pyleecan.Methods.Slot.SlotW28.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotW28.comp_height import comp_height
from pyleecan.Methods.Slot.SlotW28.comp_height_wind import comp_height_wind
from pyleecan.Methods.Slot.SlotW28.comp_surface import comp_surface

from pyleecan.Classes.check import InitUnKnowClassError


class SlotW28(SlotWind):

    VERSION = 1
    IS_SYMMETRICAL = 1

    # cf Methods.Slot.SlotW28._comp_point_coordinate
    _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW28.build_geometry
    build_geometry = build_geometry
    # cf Methods.Slot.SlotW28.build_geometry_wind
    build_geometry_wind = build_geometry_wind
    # cf Methods.Slot.SlotW28.check
    check = check
    # cf Methods.Slot.SlotW28.comp_angle_opening
    comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW28.comp_height
    comp_height = comp_height
    # cf Methods.Slot.SlotW28.comp_height_wind
    comp_height_wind = comp_height_wind
    # cf Methods.Slot.SlotW28.comp_surface
    comp_surface = comp_surface
    # save method is available in all object
    save = save

    def __init__(
        self, W0=0.0122, H0=0.001, R1=0.003, W3=0.005, H3=0.003, Zs=36, init_dict=None
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["W0", "H0", "R1", "W3", "H3", "Zs"])
            # Overwrite default value with init_dict content
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "R1" in list(init_dict.keys()):
                R1 = init_dict["R1"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "H3" in list(init_dict.keys()):
                H3 = init_dict["H3"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
        # Initialisation by argument
        self.W0 = W0
        self.H0 = H0
        self.R1 = R1
        self.W3 = W3
        self.H3 = H3
        # Call SlotWind init
        super(SlotW28, self).__init__(Zs=Zs)
        # The class is frozen (in SlotWind init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        SlotW28_str = ""
        # Get the properties inherited from SlotWind
        SlotW28_str += super(SlotW28, self).__str__() + linesep
        SlotW28_str += "W0 = " + str(self.W0) + linesep
        SlotW28_str += "H0 = " + str(self.H0) + linesep
        SlotW28_str += "R1 = " + str(self.R1) + linesep
        SlotW28_str += "W3 = " + str(self.W3) + linesep
        SlotW28_str += "H3 = " + str(self.H3)
        return SlotW28_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from SlotWind
        if not super(SlotW28, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.H0 != self.H0:
            return False
        if other.R1 != self.R1:
            return False
        if other.W3 != self.W3:
            return False
        if other.H3 != self.H3:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from SlotWind
        SlotW28_dict = super(SlotW28, self).as_dict()
        SlotW28_dict["W0"] = self.W0
        SlotW28_dict["H0"] = self.H0
        SlotW28_dict["R1"] = self.R1
        SlotW28_dict["W3"] = self.W3
        SlotW28_dict["H3"] = self.H3
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        SlotW28_dict["__class__"] = "SlotW28"
        return SlotW28_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.H0 = None
        self.R1 = None
        self.W3 = None
        self.H3 = None
        # Set to None the properties inherited from SlotWind
        super(SlotW28, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    # Slot isthmus width.
    # Type : float, min = 0
    W0 = property(fget=_get_W0, fset=_set_W0, doc=u"""Slot isthmus width.""")

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    # Slot isthmus height.
    # Type : float, min = 0
    H0 = property(fget=_get_H0, fset=_set_H0, doc=u"""Slot isthmus height.""")

    def _get_R1(self):
        """getter of R1"""
        return self._R1

    def _set_R1(self, value):
        """setter of R1"""
        check_var("R1", value, "float", Vmin=0)
        self._R1 = value

    # Slot edge radius
    # Type : float, min = 0
    R1 = property(fget=_get_R1, fset=_set_R1, doc=u"""Slot edge radius""")

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    # Tooth width
    # Type : float, min = 0
    W3 = property(fget=_get_W3, fset=_set_W3, doc=u"""Tooth width""")

    def _get_H3(self):
        """getter of H3"""
        return self._H3

    def _set_H3(self, value):
        """setter of H3"""
        check_var("H3", value, "float", Vmin=0)
        self._H3 = value

    # Tooth height
    # Type : float, min = 0
    H3 = property(fget=_get_H3, fset=_set_H3, doc=u"""Tooth height""")
