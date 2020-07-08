import os

import h5py
import numpy as np

from search_model import VGG

path = 'jdimg/1/'
index = 'feature_database/vgg_featureCNN.h5'


img_list = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


print("--------------------------------------------------")
print("         feature extraction starts")
print("--------------------------------------------------")

feats = []
names = []
#classes = ['西红柿炒鸡蛋',]
model = VGG()
for i, img_path in enumerate(img_list):
    norm_feat = model.get_feature(img_path)  # 修改此处改变提取特征的网络
    print(norm_feat.shape)
    img_name = os.path.split(img_path)[1]
    feats.append(norm_feat)
    name = img_name.encode("unicode_escape")
    #print('img_name:',img_name)
    #print(name.decode('unicode_escape'))
    names.append(name)
    print("extracting feature from image No. %d , %d images in total" % ((i + 1), len(img_list)))

feats = np.array(feats)
# print(feats)
# directory for storing extracted features
# output = args["index"]
output = index
print("--------------------------------------------------")
print("      writing feature extraction results ...")
print("--------------------------------------------------")

h5f = h5py.File(output, 'w')
h5f.create_dataset('dataset_1', data=feats)
# h5f.create_dataset('dataset_2', data = names)
h5f.create_dataset('dataset_2', data=np.string_(names))
h5f.close()