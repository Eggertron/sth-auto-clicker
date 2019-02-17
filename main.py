import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time

game_coords = [163, 607, 543, 747]
bubble = [0, 0, 0, 0]
x_width = 30
y_width = 30
is_running = True

def shoot_some_soldiers(screen):
    global game_coords
    global bubble
    global x_width
    global y_width

    for y in range(5, len(screen) - 5):
        if bubble[1] < y < bubble[3]:
	    continue
        for x in range(5, len(screen[y]) - 5):
	    if bubble[0] < x < bubble[2]:
	        continue
	    elif screen [y][x] < 10:
	        actual_x = x + game_coords[0] + 2
		actual_y = y + game_coords[1]
		# shoot twice
		click(actual_x, actual_y)
		time.sleep(0.05)
		click(actual_x, actual_y)
		# create bubble
		bubble = [x - x_width, y - y_width, x + x_width, y + y_width]
		return

# only start the program after the mouse is on the left
while True:
    mouse_pos = queryMousePosition()
    print(mouse_pos)
    if mouse_pos['c'] < 0:
        break

while is_running:
    mouse_pos = queryMousePosition()

    if game_coords[0] < mouse_pos['x'] < game_coords[2] and game_coords[1] < mouse_pos['y'] < game_coords[3]:
        start_time = time.time()
	screen = np.array(ImageGrab.grab(bbox=game_coords))
	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
	shoot_some_soldiers(screen)
	print("Frame took {0} seconds".format((time.time() - start_time)))
