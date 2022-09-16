# TODO: support n circles instead of just three
def get_circle_data(point0, point1, point2):

    x1, y1 = point0
    x2, y2 = point1
    x3, y3 = point2

    c = (x1-x2)**2 + (y1-y2)**2
    a = (x2-x3)**2 + (y2-y3)**2
    b = (x3-x1)**2 + (y3-y1)**2

    s = 2*(a*b + b*c + c*a) - (a*a + b*b + c*c) 

    px = (a*(b+c-a)*x1 + b*(c+a-b)*x2 + c*(a+b-c)*x3) / s
    py = (a*(b+c-a)*y1 + b*(c+a-b)*y2 + c*(a+b-c)*y3) / s 
    ar = a**0.5
    br = b**0.5
    cr = c**0.5 
    r = ar*br*cr / ((ar+br+cr)*(-ar+br+cr)*(ar-br+cr)*(ar+br-cr))**0.5

    return px, py, r, r * 2