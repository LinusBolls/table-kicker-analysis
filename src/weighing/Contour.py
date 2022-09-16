import math

import cv2

from src.settings import BALL_SPEED_MAX
from src.curve_calculation.get_longest_curve import get_longest_curve

class Contour:
    def __init__(self, contour, x, y, width, height, longest_curve, distance_to_prev_ball, circle_pos, circle_radius):
        self.contour = contour
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.width = width
        self.height = height
        self.longest_curve = longest_curve
        self.distance_to_prev_ball = distance_to_prev_ball


        self.circle_radius = circle_radius
        self.circle_diameter = circle_radius * 2
        self.circle_pos = circle_pos

def to_contour(last_ball, num_frames_since_ball):

    def dings(contour):
        x, y, width, height = cv2.boundingRect(contour)

        circle_pos, circle_radius, longest_curve = get_longest_curve(contour)

        if last_ball is None:
            distance_to_prev_ball = 0
        else:
            distance_to_prev_ball = math.dist((x, y), last_ball.pos) > BALL_SPEED_MAX * num_frames_since_ball

        return Contour(contour, x, y, width, height, longest_curve, distance_to_prev_ball, circle_pos, circle_radius)

    return dings