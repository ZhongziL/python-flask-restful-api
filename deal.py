from PIL import Image

Uploadpic = 'static/uploadPic/'
Createpic = 'static/createPic/'

def dealPicture(picSrc):
    im = Image.open(Uploadpic + picSrc)
    im.save(Createpic+picSrc, "jpeg")
    return picSrc

