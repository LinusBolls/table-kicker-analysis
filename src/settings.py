WINDOW_TITLE = "Footage Analysis"

IS_WITH_LOCK = False

# lower = cv2.cvtColor(np.uint8([[[214, 65, 8]]]), cv2.COLOR_RGB2HSV)
# upper = cv2.cvtColor(np.uint8([[[249, 113, 44]]]), cv2.COLOR_RGB2HSV)
# BALL_COLOR_RANGE_HSV = (lower, upper)

#  #d64108 - hsv(17,96,84) - rgb(214, 65, 8)
#  #f9712c - hsv(20,82,98) - rgb(249, 113, 44)

# OpenCV uses H: 0-179, S: 0-255, V: 0-255
# BALL_COLOR_RANGE_HSV = ((0, 0, 100), (179, 100, 255))
BALL_COLOR_RANGE_HSV = ((17, 96, 84), (20, 82, 98))
# BALL_COLOR_RANGE_HSV = (np.array([17, 96, 84]), np.array([20, 82, 98]))

BALL_DIAMETER_RANGE = (40, 60)
BALL_SPEED_MAX = 10

CURVE_SAMPLING_INTERVAL = 30
CURVE_SAMPLING_TOLERANCE = 20

class Color:
    BALL_MATCH = (0, 0, 255)
    BALL_CONTOUR = (0, 255, 0)