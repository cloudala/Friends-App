import cv2
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model

friends_model = load_model('friends_100.keras')

img = cv2.imread('rachel (38).jpg')
plt.imshow(img)
plt.show()

resize = tf.image.resize(img, (256,256))
plt.imshow(resize.numpy().astype(int))
plt.show()

prediction = friends_model.predict(np.expand_dims(resize/255, 0))[0]
class_labels = ['Chandler', 'Joey', 'Monica', 'Phoebe', 'Rachel', 'Ross']

for i, prob in enumerate(prediction):
    print(f'{class_labels[i]}: {prob:.4f}')