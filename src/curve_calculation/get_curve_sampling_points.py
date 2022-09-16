from settings import CURVE_SAMPLING_INTERVAL
from util import sick_modulo

def get_curve_sampling_points(contour):

    point_groups = []
    
    for idx, vertex in enumerate(contour):

        first_step = idx + int(CURVE_SAMPLING_INTERVAL / 2)
        second_step = idx + CURVE_SAMPLING_INTERVAL
    
        sampling_point_0 = vertex[0]
        sampling_point_1 = contour[sick_modulo(len(contour), first_step)][0]
        sampling_point_2 = contour[sick_modulo(len(contour), second_step)][0]

        group = (sampling_point_0, sampling_point_1, sampling_point_2, sick_modulo(len(contour), second_step) + 1)

        point_groups.append(group)

    return point_groups