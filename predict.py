import h5py
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2
from search_model import VGG

j = 1
query = 'test2.jpg'
index = 'feature_database/vgg_featureCNN.h5'
result = 'jdimg/1/'
# read in indexed images' feature vectors and corresponding image names
h5f = h5py.File(index, 'r')
feats = h5f['dataset_1'][:]
imgNames_ = h5f['dataset_2'][:]
imgNames = []
h5f.close()
for name in imgNames_:
    name = name.decode('unicode_escape')
    imgNames.append(name)
    #print(name)
imgNames = np.array(imgNames)

print(feats.shape)
print(imgNames.shape)
print("--------------------------------------------------")
print("               searching starts")
print("--------------------------------------------------")

# read and show query image
#plt.figure()
#ax = plt.subplot(2, 2, j)
queryImg = mpimg.imread(query)
#plt.xticks([])
#plt.yticks([])
plt.imshow(queryImg)
#plt.title('predict', fontsize=16)
plt.show()
# init VGGNet16 model
model = VGG()

# extract query image's feature, compute simlarity score and sort
queryVec = model.get_feature(query)  # 修改此处改变提取特征的网络
# print(queryVec.shape)
# print(feats.shape)
print(queryVec.shape)
print('--------------------------')
# print(queryVec)
# print(feats.T)
print('--------------------------')
scores = np.dot(queryVec, feats.T)
# scores = np.dot(queryVec, feats.T)/(np.linalg.norm(queryVec)*np.linalg.norm(feats.T))
rank_ID = np.argsort(scores)[::-1]
rank_score = scores[rank_ID]
# print (rank_ID)
print(rank_score)

# number of top retrieved images to show
maxres = 3  # 检索出三张相似度最高的图片
imlist = []
for i, index in enumerate(rank_ID[0:maxres]):
    imlist.append(imgNames[index])
    # print(type(imgNames[index]))
    print("image names: " + str(imgNames[index]) + " scores: %f" % rank_score[i])
print("top %d images in order are: " % maxres, imlist)
# show top #maxres retrieved result one by one


for i, im in enumerate(imlist):
    path = result + "/" + str(im)
    print(path)
    image = mpimg.imread(path)

    #plt.title("search output %d" % (i + 1))
    # j += 1
    # ax = plt.subplot(2, 2, j)


    # plt.xticks([])
    # plt.yticks([])
    plt.imshow(image)

    plt.show()