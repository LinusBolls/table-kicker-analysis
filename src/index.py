#! /usr/bin/python3

import cv2
import imutils

from settings import WINDOW_TITLE, Color, BALL_DIAMETER_RANGE
from weighing.get_ball import get_ball

def do_nothing():
    pass

cv2.namedWindow(WINDOW_TITLE)
cv2.resizeWindow(WINDOW_TITLE, 640, 480)
cv2.createTrackbar("Hue Min", WINDOW_TITLE, 0, 255, do_nothing)
cv2.createTrackbar("Hue Max", WINDOW_TITLE, 0, 255, do_nothing)
cv2.createTrackbar("Saturation Min", WINDOW_TITLE, 0, 255, do_nothing)
cv2.createTrackbar("Saturation Max", WINDOW_TITLE, 0, 255, do_nothing)
cv2.createTrackbar("Value Min", WINDOW_TITLE, 0, 255, do_nothing)
cv2.createTrackbar("Value Max", WINDOW_TITLE, 0, 255, do_nothing)

last_ball = None
num_frames_since_ball = 1

def run_frame(frame):
    frame, ball_pos, ball_radius = get_ball(frame, last_ball, num_frames_since_ball)

    if ball_pos is not None and ball_radius is not None:
        cv2.circle(frame, (int(ball_pos[0]), int(ball_pos[1])), int(ball_radius), Color.BALL_MATCH, 2)

    return frame

def main():
    vs = cv2.VideoCapture("in/code-kicker-orange.mov")

    num_frames_to_skip = 2017

    for i in range(num_frames_to_skip):
        vs.read()

    while True:

        hue_min = cv2.getTrackbarPos("Hue Min", "Slider")
        hue_max = cv2.getTrackbarPos("Hue Max", "Slider")
        sat_min = cv2.getTrackbarPos("Saturation Min", "Slider")
        sat_max = cv2.getTrackbarPos("Saturation Max", "Slider")
        val_min = cv2.getTrackbarPos("Value Min", "Slider")
        val_max = cv2.getTrackbarPos("Value Max", "Slider")

        # grab the current frame and initialize the occupied/unoccupied
        # text
        frame = vs.read()[1]

        # print(frame)
        
        if frame is None:
            break
        
        
        # resize the frame, convert it to grayscale, and blur it

        frame = run_frame(frame)

        frame = imutils.resize(frame, width=1000)


        

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray = cv2.GaussianBlur(gray, (21, 21), 0)
        # # if the first frame is None, initialize it
        # if firstFrame is None:
        # 	firstFrame = gray
        # 	continue

        # get_largest_white_area(frame)

        # compute the absolute difference between the current frame and
        # first frame
        # frameDelta = cv2.absdiff(firstFrame, gray)
        # thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        # dilate the thresholded image to fill in holes, then find contours
        # on thresholded image
        # thresh = cv2.dilate(thresh, None, iterations=2)
        # cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        # 	cv2.CHAIN_APPROX_SIMPLE)
        # cnts = imutils.grab_contours(cnts)
        # loop over the contours
        # for c in cnts:
            
        # 	# if the contour is too small, ignore it
        # 	if cv2.contourArea(c) < args["min_area"]:
        # 		continue

        # 	get_ball_probability(frame, c)

            
        # 	# compute the bounding box for the contour, draw it on the frame,
        # 	# and update the text
        # 	(x, y, w, h) = cv2.boundingRect(c)

        # 	# print(x, y, x + w, y + h)

        # 	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 	text = "Occupied"

        # draw the text and timestamp on the frame

        # cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
        # 	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
        # 	(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        # show the frame and record if the user presses a key
        cv2.rectangle(frame, (100, BALL_DIAMETER_RANGE[0]), (100, BALL_DIAMETER_RANGE[0]), Color.BALL_MATCH, 2)
        cv2.rectangle(frame, (100, BALL_DIAMETER_RANGE[1]), (100, BALL_DIAMETER_RANGE[1]), Color.BALL_MATCH, 2)
        # cv2.rectangle(frame, (100, 100), (BALL_DIAMETER_RANGE[1], BALL_DIAMETER_RANGE[1]), (255, 0, 0), 2)

        cv2.imshow(WINDOW_TITLE, frame)
        # cv2.imshow("Thresh", thresh)
        # cv2.imshow("Frame Delta", frameDelta)


        

        # key = None

        # while key != ord("l"):

        # key = cv2.waitKey(1) & 0xFF
        # # if the `q` key is pressed, break from the loop
        # if key == ord("q"):
        #     break

        if cv2.waitKey() & 0xFF == ord('q'):
            break
        
    # cleanup the camera and close any open windows
    vs.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()