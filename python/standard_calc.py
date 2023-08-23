def bound_to_180(angle):
    while angle < -180:
        angle += 360
    while angle > 360:
        angle -= 360
    return float(angle)


def is_angle_between(first_angle, middle_angle, second_angle):
    if first_angle < middle_angle < second_angle:
        return True
    elif first_angle < second_angle < middle_angle:
        return True
    elif second_angle < middle_angle < first_angle:
        return True
    elif second_angle < first_angle < middle_angle:
        return True
    elif middle_angle < first_angle < second_angle:
        return True
    elif middle_angle < second_angle < first_angle:
        return True
    else:
        return False


