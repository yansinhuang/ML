from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open('/Users/yan/Downloads/tobWKbR.jpg').convert('L'))  # open the file and convert it into array
plt.figure("panguin")   # title
plt.axis('off')    # no axis display

# change it into only two values
rows, colums= img.shape
for i in range(rows):
    for j in range(colums):
        if img[i,j] <= 128:
            img[i,j] = 0
        else:
            img[i,j] = 1

# show
plt.imshow(img, cmap='gray')
plt.show()

