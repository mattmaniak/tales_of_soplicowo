"""Some trigonometrical wrappers."""


def limit_angle_to_360_deg(angle_deg: float) -> float:
    """
    Prevent an angle value multiplication.

    Parameters:
    angle_deg -- the angle measured in degrees.
    """

    if angle_deg < 0:
        return angle_deg + 360
    elif angle_deg >= 360:
        return angle_deg - 360
    else:
        return angle_deg


def get_angle_quarter(angle_deg: float) -> int:
    """
    Return the angle quarter.

    Parameters:
    angle_deg -- an angle measured in degrees.
    """

    if 0 <= angle_deg % 360 < 90:
        return 1
    elif 90 <= angle_deg % 360 < 180:
        return 2
    elif 180 <= angle_deg % 360 < 270:
        return 3
    if 270 <= angle_deg % 360 < 360:
        return 4
