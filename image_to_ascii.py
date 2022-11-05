from PIL import Image
import time
import sys
import os

if len(sys.argv) < 2:
	filename = input("filename: ")
else:
	filename = sys.argv[1]
scales = []
scales.append('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". ')
scales.append('@%#*+=-:. ')
scales.append('@#$%?+;:*|/",.   ')
scales.append('     ⡀⢀⠠⠄⠂⠐⠁⠈⡁⡈⡂⣄⡐⢠⠉⠃⣀⢐⠒⠰⠘⠑⠊⠡⡉⡌⡒⡡⢉⡙⡤⣆⢒⠋⣠⡰⠇⠸⢰⠪⠎⢩⠲⣐⠓⠴⠖⠙⠚⡱⣤⡴⣌⣉⠛⣒⣔⠶⢣⢴⢱⠭⠹⡇⢸⠞⡭⣥⣦⡛⢧⢛⢹⢫⣖⣬⣴⣇⡞⠟⠷⢼⠻⣧⡟⢻⣎⢾⣛⣼⣶⣫⣭⠿⡿⢿⣟⣯⣷⣽⣾⣿'[::-1])
scales.append('   ⠂⠒⠰⠴⠶⠻⠿⢿⣿'[::-1])
scales.append('   ⠂⠒⠴⠶⠻⠿'[::-1])

im = Image.open(filename)
im_width = im.size[0]
im_height = im.size[1]
rgb_im = im.convert('RGB')
term_columns, term_rows = os.get_terminal_size()

step = 0
if im_height / int(term_rows) > im_width / int(term_columns):
	step = int(im_height / int(term_rows) + 0.5)
else:
	step = int(im_width / int(term_columns) + 0.5)
print(im_height, im_width)
print(term_rows, term_columns)
print(step)
s_index = 0
for density in scales:
	for x in range(0, im_height, int(step / 0.5)): # height and width of fonts are not the same
		for y in range(0, im_width, step):
			r, g, b = rgb_im.getpixel((y, x))
			index = (r + g * 0xff + b * 0xff * 0xff) / 0xff / 0xff / 0xff * len(density)
			index = int(index // 1)
			print(density[-index-1], end = '')
		print()
	time.sleep(1)
