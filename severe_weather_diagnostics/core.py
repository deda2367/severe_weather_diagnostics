import numpy as np


def calculate_bulk_shear(u_bottom, v_bottom, u_top, v_top):
    """
    Calculate bulk wind shear magnitude between two levels.
    """
    du = u_top - u_bottom
    dv = v_top - v_bottom
    return np.sqrt(du**2 + dv**2)


def calculate_lapse_rate(temp_bottom, temp_top, height_bottom, height_top):
    """
    Calculate lapse rate in degrees Celsius per kilometer.
    """
    if height_top <= height_bottom:
        raise ValueError("height_top must be greater than height_bottom.")

    height_difference_km = (height_top - height_bottom) / 1000
    temp_difference = temp_bottom - temp_top

    return temp_difference / height_difference_km