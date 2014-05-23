import os, sys
from PIL import Image

#test_image  = Image.open('data/test_image.jpg')
#print 'Image Mode: %s' % test_image.mode
#print 'Width: %s px, Height: %s px' % (test_image.size[0], test_image.size[1])
#width, height = test_image.size
#pixels = list(test_image.getdata())
#for col in xrange(width):
#	print pixels[col:col+width]

orig_image = Image.open('data/cat_grumpy.png')
grayscale = orig_image.convert('LA')
grayscale.save('data/grayscale_orig.png')

size = 9, 8

im = Image.open('data/grayscale_orig.png')
im2 = im.resize((size[0], size[1]), Image.ANTIALIAS)
im2.save('data/thumb_orig.png')

orig_image = Image.open('data/cat_grumpy_modif.png')
grayscale = orig_image.convert('LA')
grayscale.save('data/grayscale_modif.png')

im = Image.open('data/grayscale_modif.png')
#im.thumbnail(size, Image.ANTIALIAS)
im2 = im.resize((size[0], size[1]), Image.ANTIALIAS)
im2.save('data/thumb_modif.png')

orig_thumb = Image.open('data/thumb_orig.png')
width, height = orig_thumb.size
pixels = list(orig_thumb.getdata())

print width
print height

diff = []
for row in xrange(height):
	for col in xrange(width):
		if col != width:
			diff.append(pixels[col+row] > pixels[(col+row)+1])

for col in xrange(width - 1):
	print diff[col:col+(width-1)]

modif_thumb = Image.open('data/thumb_modif.png')
width, height = modif_thumb.size
pixels = list(modif_thumb.getdata())

print width
print height

diff2 = []
for row in xrange(height):
	for col in xrange(width):
		if col != width:
			diff2.append(pixels[col+row] > pixels[(col+row)+1])

for col in xrange(width - 1):
	print diff2[col:col+(width-1)]

#convert the binary array to a hexa string
# a true value will have have a binary value of 1, and a false value will have one of 0
def hash_f(diff):
	decimal = 0
	hex_string = []
	
	for index, value in enumerate(diff):
		if value:
			decimal += 2**(index % 8)
		if (index % 8) == 7:
			hex_string.append(hex(decimal)[2:].rjust(2, '0'))
			decimal = 0
	ret_val = ''.join(hex_string)
	return ret_val

orig = hash_f(diff)
modif = hash_f(diff2)

print orig
print modif

print orig == modif
