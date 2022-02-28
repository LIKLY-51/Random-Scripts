from PIL import Image
import os

directory = 'C:\image'
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        image = Image.open(os.path.join(directory, filename))
        image_data = image.load()
        height,width = image.size
        for loop1 in range(height):
           for loop2 in range(width):
               print(image_data[loop1,loop2])
               #(51, 76, 178, 102)
               r,g,b,a = image_data[loop1,loop2]
               if (a == 102):
                   image_data[loop1,loop2] = 0,0,0,0
        
        image.save(os.path.join(directory, filename))
    else:
        continue