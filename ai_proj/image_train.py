import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation

train_dir = "data/train/"
validation_split = 0.3


train_ds = keras.utils.image_dataset_from_directory(
    directory=train_dir,
    labels="inferred",
    label_mode="binary",
    color_mode="rgb",
    batch_size=32,
    image_size=(200, 200),
    shuffle=True,
    seed=1,
    validation_split=0.3,
    subset="training",
    verbose=True,
)

val_ds = keras.utils.image_dataset_from_directory(
    directory=train_dir,
    labels="inferred",
    label_mode="binary",
    color_mode="rgb",
    batch_size=32,
    image_size=(200, 200),
    shuffle=True,
    seed=1,
    validation_split=0.3,
    subset="validation",
    verbose=True,
)



classifier = keras.models.Sequential()

classifier.add(Conv2D(32, (3, 3), input_shape = (200, 200, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Conv2D(64, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Flatten())

classifier.add(Dense(units = 64, activation = 'relu'))

classifier.add(Dropout(0.5))

# output layer
classifier.add(Dense(1))
classifier.add(Activation('sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
classifier.fit(train_ds, epochs=20, validation_data=val_ds)

classifier.save("my_face_classifier_model.keras")


