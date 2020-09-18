import matplotlib.pyplot as plt
import numpy as np
import os
from skimage.transform import resize


def transfer():
    set_x = []
    set_y = []
    directory_name = r"C:\Users\zhiyuan\Desktop\Picosmos_转换"

    for i in os.listdir(directory_name + "\srcnn_x"):
        image_x = plt.imread(directory_name + r"\srcnn_x\\"+str(i))
        image_y = plt.imread(directory_name + r"\srcnn_y\\"+str(i))
        x = resize(image_x, (1920, 1080, 3))
        y = resize(image_y, (1920, 1080, 3))
        set_x.append(x)
        set_y.append(y)

    set_x = np.array(set_x)
    set_y = np.array(set_y)
    return set_x, set_y
