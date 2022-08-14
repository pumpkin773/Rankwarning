#coding:utf-8
from tensorflow.python.keras.layers.core import Dense, Activation
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPool2D, Flatten
from tensorflow.keras import Model
import os
import numpy as np


def extractFeature(path, output_path):
    with open(path, encoding='utf-8') as f:
        data = np.loadtxt(f, delimiter=",")
    f.close()
    data = data.flatten()
    data = data.reshape(-1, 80, 300, 1).astype("float32") / 255.0
    # print(data)


    # 简单cnn的搭建（一个输入层，两个隐藏层，一个全连接层，一个输出层）
    # 是基于序惯式Sequential()搭建网络模型的
    model = Sequential()
    # 第一层卷积层，搭建层c1层，卷积核大小5*5，个数为6
    model.add(Convolution2D(
        filters=20,  # 卷积核个数
        kernel_size=(2, 300),  # 卷积核大小5*5
        strides=1,
        activation="relu",
        input_shape=(80, 300, 1)  # 输入数据28*28*1
    ))
    # model.add(Activation("relu"))
    # 第一层池化层,搭建s2层，池化池化窗口大小2*2
    model.add(MaxPool2D(
        pool_size=(2, 1),  # 池化窗口大小2*2
        strides=2  # 池化步长为2
    ))

    # 第二层隐藏层，搭建c3层，卷积核大小5*5，个数为16
    model.add(Convolution2D(
        filters=50,  # 卷积核的个数
        kernel_size=(2, 1),  # 卷积核的大小
        strides=1,
        activation="relu"
    ))
    # 第二层池化层,搭建s4层，池化窗口大小为2*2
    model.add(MaxPool2D(pool_size=(2, 1),  # 池化窗口大小
                        strides=2,  # 池化步长
                        ))

    # 将卷积层输出为二维数组，全连接层输入为一维数组,Flatten默认按行降维，返回一个一维数组
    model.add(Flatten())
    # 全连接层
    model.add(Dense(300))# 全连接层，该层有120个神经元，一般都是1024,2048,4096个神经元
    model.add(Activation("relu"))
    model.add(Dense(24000))
    model.add(Activation("softmax"))

    # 显示模型摘要
    model.summary()
    # plot_model(model=model, to_file="model_cnn.png", show_shapes=True)

    # 编译
    model.compile(
        optimizer="sgd",
        loss="mean_absolute_error",
        metrics=["accuracy"]
    )

    # 第一步：准备输入数据
    x = data
    # 第二步：加载已经训练的模型
    # model
    # 第三步：将模型作为一个层，输出第7层的输出
    layer_model = Model(inputs=model.input, outputs=model.layers[6].output)
    # 第四步：调用新建的“曾模型”的predict方法，得到模型的输出
    feature = layer_model.predict(x)

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    with open(output_path + '1_CNNoutput.csv', 'w') as f:
        for i in feature:
            j = str(i).replace('[', '').replace(']', '').replace('\n', '').replace(' ', ', ') + '\n'
            print(j, end='')
            f.write(j)


if __name__ == "__main__":
    root_path = 'D:\\data\\'

    # Fixed_violation
    # file_path = root_path + 'FixedViolations\\Types\\'
    # tpye_list = os.listdir(file_path)
    # for i in tpye_list:
    #     extractFeature(file_path + i + '\\vectorizedTokens.csv', file_path + i + "\\LearnedFeatures\\")

    # Edit_script
    # file_path = root_path + 'MiningInput\\'
    # extractFeature(file_path + 'FeatureLearning\\vectorizedEditScripts.csv', file_path + 'ExtractedFeatures\\')

    #Unfixed_violation
    file_path = root_path + 'UnfixedViolations_RQ3\\'
    type_list = os.listdir(file_path)
    for i in type_list:
        extractFeature(file_path + i + '\\selectedData\\vectorizedTokens.csv', file_path + i + '\\LearnedFeatures\\')


