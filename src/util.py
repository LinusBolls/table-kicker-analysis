import math

import cv2

def sick_modulo(dings, dongs):

    if dongs > dings:

        return dongs - math.floor(dongs / dings) * dings

    return dings % dongs

def draw_contour(image, contour, color):
    (x, y, w, h) = cv2.boundingRect(contour)

    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

def is_on_circle(circle_center, circle_radius, point, tolerance):
    dist = math.dist(circle_center, point)

    if (dist < circle_radius - tolerance or dist > circle_radius + tolerance):
        return False
    
    return True

