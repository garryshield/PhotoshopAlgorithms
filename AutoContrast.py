# TODO: need clip min and max

from PIL import Image
import numpy as np

src = Image.open("./i.png")
src_ndarray = np.array(src)

min_r = np.min(src_ndarray[:,:,0])
min_g = np.min(src_ndarray[:,:,0])
min_b = np.min(src_ndarray[:,:,0])
max_r = np.max(src_ndarray[:,:,0])
max_g = np.max(src_ndarray[:,:,0])
max_b = np.max(src_ndarray[:,:,0])
min_value = min(min_r, min_g, min_b)
max_value = max(max_r, max_g, max_b)

table = []
for i in range(256):
    if i < min_value:
        table.append(0)
    elif i > max_value:
        table.append(255)
    else:
        table.append((i - min_value) * 255 // (max_value - min_value))

for i in range(src_ndarray.shape[0]):
    for j in range(src_ndarray.shape[1]):
        src_ndarray[i][j][0] = table[src_ndarray[i][j][0]]
        src_ndarray[i][j][1] = table[src_ndarray[i][j][1]]
        src_ndarray[i][j][2] = table[src_ndarray[i][j][2]]

result = Image.fromarray(src_ndarray)
result.save("result.jpg")
