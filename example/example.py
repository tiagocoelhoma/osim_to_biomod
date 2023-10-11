from osim_to_biomod import Converter, MuscleType, MuscleStateType

if __name__ == "__main__":
    model_path = "Models/"
    converter = Converter(
        model_path + "gait10dof18musc_updt_2.bioMod",
        model_path + "gait10dof18musc_updt_2_no_pinjoint.osim",
        ignore_muscle_applied_tag=False,
        ignore_fixed_dof_tag=False,
        ignore_clamped_dof_tag=False,
        mesh_dir="Geometry",
        muscle_type=MuscleType.HILL_DE_GROOTE,
        state_type=MuscleStateType.DEGROOTE,
        print_warnings=True,
        print_general_informations=True,
    )
    converter.convert_file()
