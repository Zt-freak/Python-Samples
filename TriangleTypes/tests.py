from triangles import Triangle_Type, get_triangle_type


def get_triangle_type_tests():
    assert get_triangle_type(60, 60, 60) == Triangle_Type.ACUTE
    assert get_triangle_type(82.8, 49, 48.2) == Triangle_Type.ACUTE
    assert get_triangle_type(56, 70.1, 53.9) == Triangle_Type.ACUTE
    assert get_triangle_type(30, 90, 60) == Triangle_Type.RIGHT
    assert get_triangle_type(50, 110, 20) == Triangle_Type.OBTUSE
    assert get_triangle_type(104.1, 31.5, 44.4) == Triangle_Type.OBTUSE
    assert get_triangle_type(0, 0, 0) == Triangle_Type.INVALID
    assert get_triangle_type(180, 0, 0) == Triangle_Type.INVALID
    assert get_triangle_type(56, 70.1, 52.9) == Triangle_Type.INVALID
    assert get_triangle_type(200, 20, -40) == Triangle_Type.INVALID

if __name__ == "__main__":
    get_triangle_type_tests()
    print("Everything passed")