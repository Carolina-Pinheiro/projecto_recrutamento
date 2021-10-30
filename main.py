from PIL import Image

desired_size = 416

for image_index in range(0,694):
    im_pth = "images/boat"+ str(image_index) +".png"

    try:
        im = Image.open(im_pth)
    except:
        print("File not found, skipped")

    old_size = im.size  # old_size[0] is in (width, height) format

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    im = im.resize(new_size, Image.ANTIALIAS)
   
    # create a new image and paste the resized on it
    new_im = Image.new("RGB", (desired_size, desired_size))
    new_im.paste(im, (0,0)) # paste image at (0,0) to keep bounding box location

    path = "images_squared/boat"+ str(image_index) +".png"
    new_im.save(path)
