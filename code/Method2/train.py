import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import matplotlib.pyplot as plt
import numpy as np
from model import vgg19



#파라미터 설정
lr=0.01
batch=64
epoch=100
img_size=64
img_c=1 # img channel

# data load
data_dir="D:\study\sugyeong_github\FingerVein-Spoofing\data\images"
save_dir="D:\study\sugyeong_github\FingerVein-Spoofing\model\Method2"

train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=30,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
val_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
        data_dir+'\\train',
        target_size=(64, 64),
        batch_size=64,
        shuffle=True,
        color_mode='grayscale',
        class_mode='binary')
validation_generator = val_datagen.flow_from_directory(
        data_dir+'\\val',
        target_size=(64, 64),
        batch_size=64,
        shuffle=True,
        color_mode='grayscale',
        class_mode='binary')

#model define
# callback 함수 정의 dropout함수
early_stop = EarlyStopping(patience=10, monitor='val_loss')
cb_checkpoint = ModelCheckpoint(filepath=save_dir, monitor='val_loss', verbose=1, save_best_only=True)

model=vgg19(False,None,(img_size,img_size,img_c))
hist=model.fit(
        train_generator,
        steps_per_epoch=len(train_generator),
        epochs=epoch,
        validation_data=validation_generator,
        validation_steps=len(validation_generator),
        callbacks=[early_stop,cb_checkpoint])

# 학습 결과 그래프 그리기

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'b', label='train loss')
loss_ax.plot(hist.history['val_loss'], '--r', label='val loss')
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
loss_ax.legend(loc='upper left')

plt.show()
print('acc: {:.4f}\tloss: {:.4f}'.format(hist.history['val_accuracy'][-11], hist.history['val_loss'][-11]))