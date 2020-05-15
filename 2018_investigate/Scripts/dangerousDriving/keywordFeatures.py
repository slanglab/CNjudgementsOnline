import re

def genKeywordFeatureVecs(factList, bloodContentBinNumList):
    features = ['无证驾驶','超载','超速','相撞','无号牌','醉酒','碰撞','追尾','饮酒'
            '死亡','重伤','损失','事故','追尾',
            '致人','恶劣','重大','逃逸','自首']
    
    featureVecs = []
    for idx, fact in enumerate(factList):
        factVec = []
        for feature in features:
            if feature in fact:
                factVec.append(1)
            else:
                factVec.append(0)
        factVec.append(bloodContentBinNumList[idx])
        featureVecs.append(factVec)
    return featureVecs