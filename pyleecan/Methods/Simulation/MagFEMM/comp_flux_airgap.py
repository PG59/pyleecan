# -*- coding: utf-8 -*-

from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Classes._FEMMHandler import FEMMHandler


def comp_flux_airgap(self, output):
    """Compute using FEMM the flux in the airgap

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object
    """

    # Set the symmetry factor if needed
    if self.is_symmetry_a:
        sym = self.sym_a
        if self.is_antiper_a:
            sym *= 2
        if self.is_sliding_band:
            self.is_sliding_band = (
                True  # When there is a symmetry, there must be a sliding band.
            )
    else:
        sym = 1

    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    # Instanciate a new FEMM
    femm = FEMMHandler(not self.is_close_femm)
    if not self.import_file:  # True if None or len == 0
        self.get_logger().debug("Drawing machine in FEMM...")
        output.mag.FEMM_dict = draw_FEMM(
            femm,
            output,
            is_mmfr=self.is_mmfr,
            is_mmfs=self.is_mmfs,
            sym=sym,
            is_antiper=self.is_antiper_a,
            type_calc_leakage=self.type_calc_leakage,
            is_remove_vent=self.is_remove_vent,
            is_remove_slotS=self.is_remove_slotS,
            is_remove_slotR=self.is_remove_slotR,
            type_BH_stator=self.type_BH_stator,
            type_BH_rotor=self.type_BH_rotor,
            kgeo_fineness=self.Kgeo_fineness,
            kmesh_fineness=self.Kmesh_fineness,
            user_FEMM_dict=self.FEMM_dict,
            path_save=self.get_path_save_fem(output),
            is_sliding_band=self.is_sliding_band,
            transform_list=self.transform_list,
            rotor_dxf=self.rotor_dxf,
            stator_dxf=self.stator_dxf,
        )
    else:
        self.get_logger().debug("Reusing the FEMM file: " + self.import_file)
        output.mag.FEMM_dict = self.FEMM_dict
        # Open the document
        femm.openfemm()
        femm.main_minimize()
        femm.opendocument(self.import_file)

    # Solve for all time step and store all the results in output
    self.solve_FEMM(femm, output, sym)
