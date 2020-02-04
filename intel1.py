import numpy as np
import cv2

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
    preprocessed_image = preproc(preprocessed_image, 1280, 768)
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
    preprocessed_image = preproc(preprocessed_image, 1280, 768)
    
    #[1x3x72x72] 
    # TODO: Preprocess the image for the car metadata model

    return preprocessed_image


#preprocessed_image = np.copy(input_image)
print('OpenCV version: ', cv2.__version__)
import cv2
import numpy as np

#img = cv2.imread('lena.jpg',0)
img=np.zeros([400,500, 3], np.uint8)+180# arreglos en filas, columnas

img = cv2.circle(img,(200,200),20,(250,20,20),3)
img = cv2.arrowedLine(img,(10,1),(200,200),(25,250,250),2)
img = cv2.rectangle(img, (100,100),(250,250),(220,220,220),1)
fntwrite = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, 'prueba',(50,200),fntwrite, 2, (230,230,230),1,cv2.LINE_AA)
cv2.imshow('foto',img)
img3=img-3
print(np.shape(img)/np.shape(img3))
cv2.waitKey(5000)
cv2.destroyAllWindows()