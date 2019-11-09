import os
from math import sqrt


def upload_facade_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return "{}_facade{}".format(instance.name, filename_ext.lower())


def get_dist_between_points(coordinates_1, coordinates_2):
    return sqrt(
        (coordinates_1[0] - coordinates_2[0]) ** 2
        + (coordinates_1[1] - coordinates_2[1]) ** 2
    )
