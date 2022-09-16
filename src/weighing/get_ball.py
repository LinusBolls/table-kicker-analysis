import math

import cv2
import numpy as np

from src.settings import BALL_COLOR_RANGE_HSV, BALL_SPEED_MAX, Color
from src.util import draw_contour
from src.weighing.Contour import to_contour

def contour_key(last_ball, num_frames_since_ball):

    def dings(contour):
        last_ball_pos = last_ball.pos if last_ball is not None else contour.pos

        location = abs(math.dist(contour.pos, last_ball_pos) - BALL_SPEED_MAX * num_frames_since_ball)

        return contour.longest_curve - min(location * 1.2, 100)

    return dings

def get_ball(image, last_ball, num_frames_since_ball):

    # transform image to hsv format in order to be able to apply color range mask
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    ball_color_mask = cv2.inRange(hsv_image, BALL_COLOR_RANGE_HSV[0], BALL_COLOR_RANGE_HSV[1])

    hsv_color1 = np.asarray([0, 0, 0])   # white!
    hsv_color2 = np.asarray([10, 255, 255])   # yellow! note the order

    ball_color_mask = cv2.inRange(hsv_image, hsv_color1, hsv_color2)

    # mask = cv2.bitwise_or(ball_color_mask, ball_color_mask)
    # image = cv2.bitwise_and(image, image, mask=mask)
    image = ball_color_mask

    contours, hierarchy = cv2.findContours(ball_color_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    refined_contours = list(map(to_contour(last_ball, num_frames_since_ball), contours))
    # refined_contours.sort(key=rank_contours)

    # print(sorted(refined_contours, key=lambda x: x.longest_curve, reverse=True)[0].longest_curve)

    # refined_contours = sorted(refined_contours, key=functools.cmp_to_key(rank_contours))
    refined_contours = sorted(refined_contours, key=contour_key(last_ball, num_frames_since_ball), reverse=True)

    ball = refined_contours[0] if len(refined_contours) > 0 else None

    if ball is None:
        return (image, None, None)

    for c in refined_contours:
      draw_contour(image, c.contour, Color.BALL_CONTOUR)

    if ball is not None:
      num_frames_since_ball = 0
      draw_contour(image, ball.contour, Color.BALL_MATCH)
    else:
      num_frames_since_ball += 1

    last_ball = ball

    # longest_curve = None
    # longest_contour = None

    # for contour in contours:

    #     (x, y, w, h) = cv2.boundingRect(contour)

    #     contour_pos = (x + w / 2, y + h / 2)

    #     is_out_of_range = False if last_ball_pos is None else math.dist(contour_pos, last_ball_pos) > BALL_SPEED_MAX * num_frames_since_ball

    #     if IS_WITH_LOCK and is_out_of_range:
    #         continue

    #     longest_contour_curve = get_longest_curve(contour)

    #     if longest_curve is None or longest_contour_curve[2] > longest_curve[2]:
    #         longest_curve = longest_contour_curve
    #         longest_contour = contour

    #     draw_contour(image, contour, Color.BALL_CONTOUR)

    # if longest_curve is None:
    #     num_frames_since_ball += 1
    
    #     return (image, None, None)

    # draw_contour(image, longest_contour, Color.BALL_MATCH)

    # last_ball_pos = longest_curve[0]
    # num_frames_since_ball = 0

    return (image, ball.circle_pos, ball.circle_radius)