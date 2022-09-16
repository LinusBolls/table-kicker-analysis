import math

from settings import CURVE_SAMPLING_TOLERANCE, BALL_DIAMETER_RANGE, BALL_SPEED_MAX
from src.curve_calculation.get_curve_sampling_points import get_curve_sampling_points
from src.curve_calculation.get_circle_data import get_circle_data
from util import is_on_circle

def get_longest_curve(contour):

    curves = [((0, 0), 0, 0)]

    sampling_point_groups = get_curve_sampling_points(contour)

    for group in sampling_point_groups:

        px, py, radius, diameter = get_circle_data(group[0], group[1], group[2])

        if diameter < BALL_DIAMETER_RANGE[0] or diameter > BALL_DIAMETER_RANGE[1]:
            continue

        if math.isnan(px) or math.isnan(py):
            continue

        curve_length = 0

        # determine length of curve
        for j in range(group[3], len(contour)):
            if is_on_circle((px, py), radius, contour[j][0], CURVE_SAMPLING_TOLERANCE):
                curve_length += 1
            else:
                break

        are_all_vertices_inside_circle = all(math.dist((px, py), vertex[0]) < radius + CURVE_SAMPLING_TOLERANCE for vertex in contour)
        
        if not are_all_vertices_inside_circle:
            continue
        
        curves.append(((px, py), radius, curve_length))

    curves_by_descending_length = sorted(curves, key=lambda x: x[2], reverse=True)

    return curves_by_descending_length[0]