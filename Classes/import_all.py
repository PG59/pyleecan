# -*- coding: utf-8 -*-

"""File generated by generate_code() - pyleecan/Generator/run_generate_classes.py
WARNING! All changes made in this file will be lost!
"""

from pyleecan.Classes.Arc import Arc
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc2 import Arc2
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Classes.Circle import Circle
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.Classes.CondType21 import CondType21
from pyleecan.Classes.CondType22 import CondType22
from pyleecan.Classes.Conductor import Conductor
from pyleecan.Classes.Element import Element
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.Force import Force
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.GUIOption import GUIOption
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Classes.HoleMag import HoleMag
from pyleecan.Classes.Import import Import
from pyleecan.Classes.ImportGenMatrixSin import ImportGenMatrixSin
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin
from pyleecan.Classes.ImportMatlab import ImportMatlab
from pyleecan.Classes.ImportMatrix import ImportMatrix
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls
from pyleecan.Classes.InCurrent import InCurrent
from pyleecan.Classes.InCurrentDQ import InCurrentDQ
from pyleecan.Classes.InFlux import InFlux
from pyleecan.Classes.InForce import InForce
from pyleecan.Classes.Input import Input
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotMulti import LamSlotMulti
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.Line import Line
from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.MachineAsync import MachineAsync
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineSRM import MachineSRM
from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.MachineSync import MachineSync
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.MagnetFlat import MagnetFlat
from pyleecan.Classes.MagnetPolar import MagnetPolar
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.MagnetType12 import MagnetType12
from pyleecan.Classes.MagnetType13 import MagnetType13
from pyleecan.Classes.MagnetType14 import MagnetType14
from pyleecan.Classes.Magnetics import Magnetics
from pyleecan.Classes.MatEconomical import MatEconomical
from pyleecan.Classes.MatElectrical import MatElectrical
from pyleecan.Classes.MatHT import MatHT
from pyleecan.Classes.MatMagnetics import MatMagnetics
from pyleecan.Classes.MatStructural import MatStructural
from pyleecan.Classes.Material import Material
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.Node import Node
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.Notch import Notch
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.OutElec import OutElec
from pyleecan.Classes.OutGeo import OutGeo
from pyleecan.Classes.OutGeoLam import OutGeoLam
from pyleecan.Classes.OutMag import OutMag
from pyleecan.Classes.OutPost import OutPost
from pyleecan.Classes.OutStruct import OutStruct
from pyleecan.Classes.Output import Output
from pyleecan.Classes.PolarArc import PolarArc
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Simulation import Simulation
from pyleecan.Classes.Slot import Slot
from pyleecan.Classes.Slot19 import Slot19
from pyleecan.Classes.SlotMFlat import SlotMFlat
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.SlotMag import SlotMag
from pyleecan.Classes.SlotUD import SlotUD
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.Classes.SlotW13 import SlotW13
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW15 import SlotW15
from pyleecan.Classes.SlotW16 import SlotW16
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW24 import SlotW24
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.Classes.SlotW26 import SlotW26
from pyleecan.Classes.SlotW27 import SlotW27
from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.Classes.SlotW29 import SlotW29
from pyleecan.Classes.SlotW60 import SlotW60
from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.Classes.SlotWind import SlotWind
from pyleecan.Classes.Solution import Solution
from pyleecan.Classes.Structural import Structural
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Surface import Surface
from pyleecan.Classes.Trapeze import Trapeze
from pyleecan.Classes.Unit import Unit
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingCW1L import WindingCW1L
from pyleecan.Classes.WindingCW2LR import WindingCW2LR
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.WindingSC import WindingSC
from pyleecan.Classes.WindingUD import WindingUD
