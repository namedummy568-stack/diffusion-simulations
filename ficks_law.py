import numpy as np

def calculate_ficks_first_law(D, dC_dx):
    """
    Calculates the diffusion flux using Fick's First Law.

    Parameters:
    D (float): Diffusion coefficient (m^2/s)
    dC_dx (float): Concentration gradient (mol/m^4)

    Returns:
    float: Diffusion flux (mol/m^2·s)
    """
    J = -D * dC_dx
    return J

def calculate_ficks_second_law_steady_state(NA, DAB, P, R, T, z, yA1, yA2):
    """
    Calculates the molar flux for steady-state diffusion through a stagnant film.

    Parameters:
    NA (float): Molar flux of component A
    DAB (float): Diffusion coefficient of A in B
    P (float): Total pressure
    R (float): Ideal gas constant
    T (float): Temperature
    z (float): Film thickness
    yA1 (float): Mole fraction of A at point 1
    yA2 (float): Mole fraction of A at point 2

    Returns:
    float: Molar flux of component A
    """
    # This function is slightly misnamed as it calculates NA, not a derivative for Fick's Second Law directly.
    # It's based on the relevant equation provided in the Confluence page.
    NA_calc = (DAB * P / (R * T * z)) * (yA1 - yA2)
    return NA_calc

if __name__ == "__main__":
    # Example for Fick's First Law
    D_gas = 1.0e-5  # m^2/s
    dC_dx_gas = -0.1  # mol/m^4
    flux_gas = calculate_ficks_first_law(D_gas, dC_dx_gas)
    print(f"Diffusion flux (Fick's First Law): {flux_gas} mol/m^2·s")

    # Example for steady-state diffusion through a stagnant film
    DAB_val = 2.0e-5  # m^2/s
    P_val = 101325  # Pa
    R_val = 8.314  # J/(mol·K)
    T_val = 298.15  # K
    z_val = 0.01  # m
    yA1_val = 0.8
    yA2_val = 0.2
    molar_flux_stagnant_film = calculate_ficks_second_law_steady_state(
        None, DAB_val, P_val, R_val, T_val, z_val, yA1_val, yA2_val
    )
    print(f"Molar flux (stagnant film): {molar_flux_stagnant_film} mol/m^2·s")
