import requests
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import skimage
from skimage.filters import rank
import scipy
from scipy import ndimage
from skimage import feature
import matplotlib
import os


proj_path = os.path.dirname(__file__)


class image_meta_data():

    def __init__(self, lat, long, key, img_x=640, img_y=640, fov=90, heading=235, pitch=10):

        self.coordinates = str(lat) + "," + str(long)
        self.image_resolution = str(img_x) + 'x' + str(img_y)
        self.key = str(key)
        self.fov = str(fov)
        self.heading = str(heading)
        self.pitch = str(pitch)


    def get_image_data(self):

        response = requests.get("https://maps.googleapis.com/maps/api/streetview?size=" +
                                self.image_resolution + "&location=" + self.coordinates +
                                "&fov=" + self.fov +"&heading=" + self.heading + "&pitch="
                                + self.pitch + "&key=" + self.key)

        return response

def open_image(response):

    i = Image.open(BytesIO(response.content))

    return i

def image_to_array(image):

    array = np.array(image)

    return array

def rgb_to_hsv(image_array):

    image_array = image_array / 255
    hsv_array = matplotlib.colors.rgb_to_hsv(image_array)

    return hsv_array

def calculate_mean_hue(hsv_array):

    mean_h = np.mean(hsv_array[:,:,0])

    return mean_h

def calculate_sd_hue(hsv_array):

    std_h = np.std(hsv_array[:,:,0])

    return std_h

def calculate_mean_sat(hsv_array):

    mean_s = np.mean(hsv_array[:,:,1])

    return mean_s

def calculate_sd_sat(hsv_array):

    std_s = np.std(hsv_array[:,:,1])

    return std_s

def calculate_mean_val(hsv_array):

    mean_v = np.mean(hsv_array[:,:,2])

    return mean_v

def calculate_sd_val(hsv_array):

    std_v = np.std(hsv_array[:,:,2])

    return std_v

def calculate_img_shannon_entropy(rgb_image):

    greyscale_image = rgb_image.convert('LA')
    entropy = skimage.measure.shannon_entropy(greyscale_image)

    return entropy

def canny_edge_detection(rgb_image):

    greyscale_image = rgb_image.convert('L')
    filtered_i = ndimage.gaussian_filter(np.array(greyscale_image), 4)

    edges = feature.canny(filtered_i)

    return edges

def plot_edges(edges):

    plt.imshow(edges, cmap=plt.cm.gray)
    plt.axis('off')
    plt.title('Canny filter, $\sigma=1$', fontsize=20)

    plt.show()

#image_meta_data = image_meta_data(51.524276, -0.134558, key)
#response = image_meta_data.get_image_data()
#image = open_image(response)
