from PIL import Image, ImageEnhance
import os

fileDir = os.path.dirname(os.path.realpath(__file__))
srcPath = fileDir + "\\barnE.jpg"
barnE = Image.open(srcPath)

print('Pillow is a plugin that allows python to open images using Image')
barnE.show()

print('Press enter to continue.')
input()

print('It can edit the color of images and apply filters using ImageEnhance')
bw = ImageEnhance.Color(barnE)
bw.enhance(0).show("Black and White")

print('Press enter to continue.')
input()

print('It can also be used to create GIFs')
r0 = barnE
r1 = barnE.rotate(45)
r2 = barnE.rotate(90)
r3 = barnE.rotate(135)
r4 = barnE.rotate(180)
r5 = barnE.rotate(225)
r6 = barnE.rotate(270)
r7 = barnE.rotate(315)

r0.save("barnSpin.gif", save_all=True, append_images=[r1, r2, r3, r4, r5, r6, r7], duration = 50, loop = 0)
spinPath = fileDir + "\\barnSpin.gif"
spin = Image.open(spinPath)

print('GIFs will only open as still images when opened through PIL')
print('All of their frames will be accessible, however')
print('A GIF was just saved in the same directory this script is in')
print('To test, we can use [name].is_animated: ' + str(spin.is_animated))
print('We can also see how many frames it has, this one has ' + str(spin.n_frames))