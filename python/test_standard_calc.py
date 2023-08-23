from standard_calc import bound_to_180, is_angle_between

""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0

def test_bound_basic2():
    assert bound_to_180(155) == 155.0

def test_bound_basic3():
    assert bound_to_180(360) == 360.0

def test_bound_basic4():
    assert bound_to_180(-140) == -140.0

def test_bound_basic5():
    assert bound_to_180(450) == 90.0

def test_bound_basic6():
    assert bound_to_180(-550) == 170

""" Tests for is_angle_between() """

def test_between_basic1():
    assert is_angle_between(0, 1, 2) is True

def test_between_basic2():
    assert is_angle_between(4, 4, 4) is False

def test_between_basic3():
    assert is_angle_between(5, 3, 2) is True

def test_between_basic4():
    assert is_angle_between(-10, -6, -6) is False

def test_between_basic5():
    assert is_angle_between(-5, -7, -15) is True

def test_between_basic6():
    assert is_angle_between(-5, -5, -5) is False





