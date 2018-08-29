from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def image_f(filename, text, dest):
	image = Image.open('Images/black.jpg')
	draw = ImageDraw.Draw(image)
	final_file = 'textonblack'
	w, h = image.size
	y_start = (2*h)/3
	if dest == 'hi':
		out_font = "Fonts/Lohit-Devanagari.ttf"
	elif dest == 'bn':
		out_font = "Fonts/BenSen.ttf"
	elif dest == 'pa':
		out_font = "Fonts/lohit.punjabi.1.1.ttf"
	else:
		out_font = "Fonts/calibri.ttf"
	font = ImageFont.truetype(out_font, 16)
	draw.rectangle(((0, 0), (w, h)), fill = "black")
	draw.text((10, 10), text, font = font, fill = "white")
	image.save(final_file, "PNG")
	return final_file
	#image.show()