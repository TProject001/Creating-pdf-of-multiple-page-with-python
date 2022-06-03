from tkinter import filedialog as fd
from PIL import Image

image1=Image.open("CG_images\\CG1.jpg")
imglist=[]

for i in range(1,34):
    filename=fd.askopenfilename()
    imglist.append(Image.open(filename))
print("imglist = \n",imglist)

image1.save("multiple1.pdf",save_all=True,append_images=imglist)
#image1.save("CG 1.pdf")