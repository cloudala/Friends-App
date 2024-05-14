import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint

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

# Display a few images from each set
fig, ax = plt.subplots(ncols=4, nrows=3, figsize=(20, 15))

# Plot images from train set
for idx, (images, labels) in enumerate(train_data.take(4)):
    for i in range(len(images)):
        ax[0, idx].imshow(images[i].numpy())
        ax[0, idx].set_title("Train: " + str(labels[i].numpy()))
        ax[0, idx].axis("off")
        break  # Show only the first image from each batch

# Plot images from validation set
for idx, (images, labels) in enumerate(validation_data.take(4)):
    for i in range(len(images)):
        ax[1, idx].imshow(images[i].numpy())
        ax[1, idx].set_title("Validation: " + str(labels[i].numpy()))
        ax[1, idx].axis("off")
        break

# Plot images from test set
for idx, (images, labels) in enumerate(test_data.take(4)):
    for i in range(len(images)):
        ax[2, idx].imshow(images[i].numpy())
        ax[2, idx].set_title("Test: " + str(labels[i].numpy()))
        ax[2, idx].axis("off")
        break

plt.show()

model = Sequential()
model.add(Conv2D(16, (3,3), 1, activation='relu', input_shape=(256,256,3)))
model.add(MaxPooling2D())
model.add(Conv2D(32, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(16, (3,3), 1, activation='relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print(model.summary())

# plot diagnostic learning curves
def summarize_diagnostics(history):
	# plot loss
	plt.subplot(211)
	plt.title('Cross Entropy Loss')
	plt.plot(history.history['loss'], color='blue', label='train')
	plt.plot(history.history['val_loss'], color='orange', label='test')
	# plot accuracy
	plt.subplot(212)
	plt.title('Classification Accuracy')
	plt.plot(history.history['accuracy'], color='blue', label='train')
	plt.plot(history.history['val_accuracy'], color='orange', label='test')
	# save plot to file
	plt.savefig('test.png')
	plt.close()

# add checkpoint in the .keras format (saves the entire model)
checkpoint_path_keras = '{epoch:02d}-{val_accuracy:.2f}.keras'
checkpoint_keras = ModelCheckpoint(checkpoint_path_keras, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')

history = model.fit(train_data, validation_data=validation_data, epochs=20, verbose=1, callbacks = [checkpoint_keras])

summarize_diagnostics(history)

_, acc = model.evaluate(test_data, verbose=1)
print('> %.3f' % (acc * 100.0))