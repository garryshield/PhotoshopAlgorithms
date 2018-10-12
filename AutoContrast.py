from PIL import Image
import numpy as np

src = Image.open("./i.png")
src_array = np.array(src)

percent = 0.001
src_r_list = src_array[:,:,0].flatten()
src_g_list = src_array[:,:,1].flatten()
src_b_list = src_array[:,:,2].flatten()

src_r_list = np.sort(src_r_list)
src_g_list = np.sort(src_g_list)
src_b_list = np.sort(src_b_list)
min_index = int(len(src_r_list) * percent)
max_index = min(int(len(src_r_list) * (1.0 - percent)), len(src_r_list) - 1)

min_r = src_r_list[min_index]
min_g = src_g_list[min_index]
min_b = src_b_list[min_index]
max_r = src_r_list[max_index]
max_g = src_g_list[max_index]
max_b = src_b_list[max_index]
min_value = min(min_r, min_g, min_b)
max_value = max(max_r, max_g, max_b)
print(min_r, max_r)
print(min_g, max_g)
print(min_b, max_b)

table = []
for i in range(256):
    if i < min_value:
        table.append(0)
    elif i > max_value:
        table.append(255)
    else:
        table.append((i - min_value) * 255 // (max_value - min_value))

for i in range(src_array.shape[0]):
    for j in range(src_array.shape[1]):
        src_array[i][j][0] = table[src_array[i][j][0]]
        src_array[i][j][1] = table[src_array[i][j][1]]
        src_array[i][j][2] = table[src_array[i][j][2]]

result = Image.fromarray(src_array)
result.save("./result.jpg")