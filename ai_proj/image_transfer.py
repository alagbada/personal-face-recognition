import numpy as np
import keras
from keras import layers
import matplotlib.pyplot as plt


train_dir = "data/train/"
validation_split = 0.3

train_ds = keras.utils.image_dataset_from_directory(
    directory=train_dir,
    labels="inferred",
    label_mode="binary",
    color_mode="rgb",
    batch_size=32,
    image_size=(160, 160),
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
    image_size=(160, 160),
    shuffle=True,
    seed=1,
    validation_split=0.3,
    subset="validation",
    verbose=True,
)

data_augmentation = keras.Sequential([
    keras.layers.RandomFlip("horizontal"),
    keras.layers.RandomRotation(0.1),
    keras.layers.RandomZoom(0.2)
])

base_model = keras.applications.Xception(
    weights='imagenet',  # Load weights pre-trained on ImageNet.
    input_shape=(160, 160, 3),
    include_top=False)  # Do not include the ImageNet classifier at the top.

base_model.trainable = False
inputs = keras.Input(shape=(160, 160, 3))

x = data_augmentation(inputs)
# We make sure that the base_model is running in inference mode here,
# by passing `training=False`. This is important for fine-tuning, as you will
# learn in a few paragraphs.
x = keras.applications.xception.preprocess_input(x)
x = base_model(x, training=False)
# Convert features of shape `base_model.output_shape[1:]` to vectors
x = keras.layers.GlobalAveragePooling2D()(x)
# A Dense classifier with a single unit (binary classification)
x = keras.layers.Dropout(0.4)(x)
outputs = keras.layers.Dense(1, activation="sigmoid")(x)
model = keras.Model(inputs, outputs)
model.summary(show_trainable=True)
#1e-5
model.compile(optimizer=keras.optimizers.SGD(),
              loss=keras.losses.BinaryCrossentropy(from_logits=False),
              metrics=[keras.metrics.BinaryAccuracy()])
model.fit(train_ds, epochs=20, validation_data=val_ds)

#model.save("my_face_classifier_model.keras")

