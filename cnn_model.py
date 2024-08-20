import tensorflow as tf
from tensorflow.keras import layers, models

def create_cnn_model(
    input_shape,
    num_classes,
    c_layers=3,
    filters=32,
    d_layers=1,
    d_units=128,
    dropout_rate=0.5
):
    """
    Create CNN model for image classification.
    
    Parameters:
    - input_shape: tuple, shape of the input images (height, width, channels)
    - num_classes: int, number of classes for classification
    - c_layers: int, number of convolutional layers (default = 3)
    - filters: int, number of filters in the first convolutional layer (default = 32)
    - d_layers: int, number of dense layers after convolutional layers (default = 1)
    - d_units: int, number of units in each dense layer (default = 128)
    - dropout_rate: float, dropout rate applied after dense layers (default = 0.5)
    
    Returns:
    - model: tf.keras.Model, the CNN model
    """
    
    model = models.Sequential()
    
    # Add layers
    for i in range(c_layers):
        if i == 0:
            model.add(layers.Conv2D(filters, (3, 3), activation='relu', input_shape=input_shape))
        else:
            model.add(layers.Conv2D(filters, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2))) # After each c_layer
        filters *= 2  # Double filters with each additional layer

    model.add(layers.Flatten())
    
    # Add dense layers
    for _ in range(d_layers):
        model.add(layers.Dense(d_units, activation='relu'))
        model.add(layers.Dropout(dropout_rate))
    
    # Add output layer
    model.add(layers.Dense(num_classes, activation='softmax'))
    
    # Compile model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model