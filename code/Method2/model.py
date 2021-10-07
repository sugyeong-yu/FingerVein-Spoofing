from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, GlobalAveragePooling2D, Dense, Activation

def vgg19(show_layers, weights, input_shape):
    base_model = VGG19(include_top=True,weights=None,input_shape=input_shape,classes=1,classifier_activation='sigmoid')
    # x = GlobalAveragePooling2D()(base_model.output)
    # pred = Dense(1, activation='sigmoid')(x)

    #model = Model(inputs=base_model.input, outputs=pred)
    base_model.compile(optimizer=SGD(lr=1e-2, decay=1e-4), loss='binary_crossentropy', metrics=['accuracy'])

    if show_layers:
        for i, layer in enumerate(base_model.layers):
            print(i, layer.name, layer.trainable)
    return base_model
# model=vgg19(True,None,(64,64,1))
# model.summary()