from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2


image = cv2.imread('/Users/theakaroline/Documents/fyp/data_project/images/imgs_part_1/PAT_8_15_820.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)