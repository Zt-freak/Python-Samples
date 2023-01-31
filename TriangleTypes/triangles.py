from enum import Enum


class Triangle_Type(Enum):
    ACUTE = 1
    RIGHT = 2
    OBTUSE = 3
    INVALID = 4

def get_triangle_type(angle_degrees_a: float, angle_degrees_b: float, angle_degrees_c: float) -> Triangle_Type:
    '''
    Returns the triangle type based on three angle values in degrees.
    
    :param angle_degrees_a: float
    :param angle_degrees_b: float
    :param angle_degrees_c: float
    :return: Triangle_Type
    '''
    try:
        # Put the three angles in a list

        angles: list[float] = [angle_degrees_a, angle_degrees_b, angle_degrees_c]

        # Triangle should be 180 degress exact

        if sum(angles) != float(180):
            raise ValueError()

        # Triangle angles must be a positive value

        if any(angle <= 0 for angle in angles):
            raise ValueError()

        # Check if all angles are smaller than 90

        if all(angle < 90 for angle in angles):
            return Triangle_Type.ACUTE

        # Check if exactly one angle is 90 degrees

        if any(angle == 90 for angle in angles):
            return Triangle_Type.RIGHT

        # Any other case, the triangle is obtuse

        return Triangle_Type.OBTUSE
    except ValueError:

        # Return invalid if the angle values don't produce a triangle

        return Triangle_Type.INVALID