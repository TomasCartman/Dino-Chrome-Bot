import time

import pyautogui
from PIL import ImageGrab

x_position = 330

def capture_screen():
	screen = ImageGrab.grab()
	return screen
	
def detect_enemy(screen):
	f_colour = screen.getpixel((int(x_position), 405))
	for x in range(int(x_position), int(x_position + 15)):
		for y in range(405, 465):
			colour = screen.getpixel((x, y))
			if colour != f_colour:
				return True
			else:
				f_colour = colour

def jump():
	global x_position
	pyautogui.press('up')
	x_position += 0.5

print('Starting in 3 seconds...')
time.sleep(3)

while True:
	screen = capture_screen()
	if detect_enemy(screen):
		jump()
	