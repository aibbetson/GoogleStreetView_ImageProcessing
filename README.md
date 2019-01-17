# GoogleStreetView_ImageProcessing
Allows the retrieval of images from the Google Street View (GSV) API and includes functions for image processing.

In order to retrieve images from the GSV API, an API key is required. More info can be found here: 
https://developers.google.com/maps/documentation/streetview/intro

When retrieving a street view image, users are able to input the following parameters: location, image resolution, field of view,
pitch and heading.

The following image processing functions are available: RGB to HSV conversion, calculate mean and/or standard deviation of Hue, Saturation 
and Value, Canny edge detection and calculate Shannon entropy.
