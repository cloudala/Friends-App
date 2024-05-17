import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.models import load_model

data = image_dataset_from_directory('data')
data = data.map(lambda x,y: (x/255, y))
data.as_numpy_iterator().next()

num_samples = len(data)
train_ratio = 0.7
validation_ratio = 0.2
test_ratio = 0.1

num_train_samples = int(train_ratio * num_samples)
num_test_samples = int(test_ratio * num_samples)
num_validation_samples = int(validation_ratio * num_samples)

train_data = data.take(num_train_samples)
validation_data = data.skip(num_train_samples).take(num_validation_samples)
test_data = data.skip(num_train_samples + num_validation_samples).take(num_test_samples)

model = load_model('friends_100.keras')

# plot diagnostic learning curves
def summarize_diagnostics(history):
    # Plot the learning curve
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='train accuracy')
    plt.plot(history.history['val_accuracy'], label='validation accuracy')
    plt.title('Model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('Epoch')
    plt.grid(True, linestyle='--', color='grey')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='train loss')
    plt.plot(history.history['val_loss'], label='validation loss')
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.grid(True, linestyle='--', color='grey')
    plt.legend()
    plt.savefig('test.png')

# add checkpoint in the .keras format (saves the entire model)
checkpoint_path_keras = '{epoch:02d}-{val_accuracy:.2f}.keras'
checkpoint_keras = ModelCheckpoint(checkpoint_path_keras, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

history = model.fit(train_data, validation_data=validation_data, epochs=10, verbose=1, callbacks = [checkpoint_keras])

summarize_diagnostics(history)

_, acc = model.evaluate(test_data, verbose=1)
print('> %.3f' % (acc * 100.0))