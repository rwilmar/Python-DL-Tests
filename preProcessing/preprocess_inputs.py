import cv2
import numpy as np

def preproc(input_image, height, width):
    image = cv2.resize(input_image, (width, height))
    image = image.transpose((2,0,1))
    image = image.reshape(1, 3, height, width)

    return image

def pose_estimation(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related pose estimation model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)
    
    preprocessed_image = preproc(preprocessed_image, 256, 456)
    #[1x3x256x456] 
    
    return preprocessed_image


def text_detection(input_image):
   
    preprocessed_image = np.copy(input_image)
    preprocessed_image = preproc(preprocessed_image, 768, 1280)
    #  [1x3x768x1280] - 

    return preprocessed_image


def car_meta(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related car metadata model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)
    preprocessed_image = preproc(preprocessed_image, 72, 72)
    
    # [1x3x72x72] - 
    # TODO: Preprocess the image for the car metadata model

    return preprocessed_image
