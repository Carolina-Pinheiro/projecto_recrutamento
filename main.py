from PIL import Image
import cv2
from bs4 import BeautifulSoup

X_MIN = 0
Y_MIN = 1
X_MAX = 2
Y_MAX = 3

def get_bounding_box_coords(image_index):
    doc_name = "annotations/boat" + str(image_index) + ".xml"
    with open(doc_name, 'r') as f:
        content = f.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content = BeautifulSoup(content, 'html.parser')
    # Finding all instances of tag   
    b_bndbox = bs_content.find_all('bndbox') 
    bounding_boxes=[]
    for box in b_bndbox:
        bounding_boxes.append([int(box.contents[1].contents[0]), 
                                            int(box.contents[3].contents[0]),
                                            int(box.contents[5].contents[0]),
                                            int(box.contents[7].contents[0])])
    return bounding_boxes



for image_index in range(0,693): #693
    im_pth = "images/boat"+ str(image_index) +".png"

    try:
        im = Image.open(im_pth)
    except:
        print("File not found, skipped")

    old_size = im.size  # old_size[0] is in (width, height) format
    desired_size = max(im.size)
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
   
    # create a new image and paste the image on it
    new_im = Image.new("RGB", (desired_size, desired_size))
    new_im.paste(im, (0,0)) # paste image at (0,0) to keep bounding box location
    path = "images_squared/boat"+ str(image_index) +".png"
    new_im.save(path)

    #See the bounding boxes used in the annotations
    """
    bounding_boxes = get_bounding_box_coords(image_index)
    #cv2.boundingRect() 
    img = cv2.imread(path) 
    for box in bounding_boxes:
        img = cv2.rectangle(img,(box[X_MIN],box[Y_MIN]),(box[X_MAX],box[Y_MAX]),(0,255,0),2)
        cv2.imshow('Window', img) 
        cv2.waitKey(0)
    """

    
   
    


