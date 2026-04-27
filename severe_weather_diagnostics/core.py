import numpy as np


def calculate_bulk_shear(u_bottom, v_bottom, u_top, v_top):
    """
    Calculate bulk wind shear between two atmospheric levels.
    """
    du = u_top - u_bottom
    dv = v_top - v_bottom
    return np.sqrt(du**2 + dv**2)


def calculate_lapse_rate(temp_bottom, temp_top, height_bottom, height_top):
    """
    Calculate lapse rate in Celsius per kilometer.
    """
    if height_top <= height_bottom:
        raise ValueError("height_top must be greater than height_bottom.")

    height_difference_km = (height_top - height_bottom) / 1000
    temp_difference = temp_bottom - temp_top

    return temp_difference / height_difference_km

def calculate_stp_index(cape, shear_06km, lcl_height, srh_01km):
    """
    Calculate a Significant Tornado Parameter (STP) severe weather index.
    """
    if cape < 0 or shear_06km < 0 or lcl_height < 0 or srh_01km < 0:
        raise ValueError("Inputs cannot be negative.")

    cape_term = cape / 1500
    shear_term = shear_06km / 20
    srh_term = srh_01km / 150
    lcl_term = max(0, (2000 - lcl_height) / 1000)

    return cape_term * shear_term * srh_term * lcl_term


def classify_severe_risk(cape, shear_06km, lapse_rate):
    """
    Evaluate the severe weather risk based on the conditions.
    """
    if cape < 0 or shear_06km < 0:
        raise ValueError("CAPE and shear cannot be negative.")

    if cape >= 2500 and shear_06km >= 20 and lapse_rate >= 7:
        return "Significant"
    elif cape >= 1500 and shear_06km >= 15 and lapse_rate >= 6:
        return "Elevated"
    elif cape >= 500 and shear_06km >= 10:
        return "Marginal"
    else:
        return "Low"