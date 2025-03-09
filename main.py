from PIL import Image
import numpy as np

img = Image.open("image.png").convert("L") # L means greyscale, there is also "RGB" and "RGBA"
pixels = img.load()
pixals = np.array(img)

# cluster size
block_size = 10
height, width = pixals.shape

# creating an empty file named output.txt
with open("output.txt", "w") as file: # w for write
    file.write("")

for y in range(0, height, block_size) :
    for x in range(0, width, block_size) :
        block = pixals[y:y+block_size, x:x+block_size]
        # clustring image using K-Means Clustering
        avg_intensity = np.mean(block)
        if avg_intensity <= 25 : 
            with open("output.txt", "a") as file:
                file.write("@")
        elif avg_intensity >= 26 and avg_intensity < 52 : 
            with open("output.txt", "a") as file:
                file.write("#")
        elif avg_intensity >= 52 and avg_intensity < 78 : 
            with open("output.txt", "a") as file:
                file.write("&")
        elif avg_intensity >= 78 and avg_intensity < 104 : 
            with open("output.txt", "a") as file:
                file.write("%")
        elif avg_intensity >= 104 and avg_intensity < 130 : 
            with open("output.txt", "a") as file:
                file.write("*")
        elif avg_intensity >= 130 and avg_intensity < 156 : 
            with open("output.txt", "a") as file:
                file.write("+")
        elif avg_intensity >= 156 and avg_intensity < 182 : 
            with open("output.txt", "a") as file:
                file.write("=")
        elif avg_intensity >= 182 and avg_intensity < 208 : 
            with open("output.txt", "a") as file:
                file.write(":")
        elif avg_intensity >= 208 and avg_intensity < 234 : 
            with open("output.txt", "a") as file:
                file.write(".")
        else : 
            with open("output.txt", "a") as file:
                file.write("`")

    with open("output.txt", "a") as file:
        file.write("\n")
