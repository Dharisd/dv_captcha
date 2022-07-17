import pickle
import numpy as np
from PIL import Image


'''
Generate hand written thaana text 
'''

class thaanaGenerator:
    def __init__(self, data_path):
        self.cons_map = {'ހ':0,'ށ':1,'ނ':2,'ރ':3,'ބ':4,'ޅ':5,'ކ':6,'އ':7,'ވ':8,'މ':9,'ފ':10,'ދ':11,'ތ':12,'ލ':13,'ގ':14,'ޏ':15,'ސ':16,'ޑ':17,'ޒ':18,'ޓ':19,'ޔ':20,'ޕ':21,'ޖ':22,'ޗ':23,'ޘ':24,'ޙ':25,'ޚ':26,'ޛ':27,'ޜ':28,'ޝ':29,'ޞ':30,'ޟ':31,'ޠ':32,'ޡ':33,'ޢ':34,'ޣ':35,'ޤ':36,'ޥ':37,}
        self.vow_map = {'ަ':0,'ާ':1,'ި':2,'ީ':3,'ު':4,'ޫ':5,'ެ':6,'ޭ':7,'ޮ':8,'ޯ':9,'ް':10,}

        with open(data_path,"rb") as f:
            self.data = pickle.load(f)



    def to_con_vow_pairs(self,text):
        n = 2
        pairs = []
        text_list = list(text)

        return [text_list[i:i + n] for i in range(0, len(text_list), n)]
        
    
    def to_mapping(self,pair_list):
        gen_list = []

        for pair in pair_list:
            cons = pair[0]
            vow = pair[1]

            if cons in self.cons_map and vow in self.vow_map:
                gen_list.append((self.cons_map[cons],self.vow_map[vow]))

        return gen_list

            
    def pair_to_image(self,map_pair,style=1):
        cons = map_pair[0]
        vowel = map_pair[1]


        img_data = self.data[cons][vowel][style]

        return img_data.reshape(40,40)

    
    def generate_image(self,text,style=1):

        imgs = []
        t = self.to_con_vow_pairs(text)
        pairs = self.to_mapping(t)

        for pair in pairs:
            img = self.pair_to_image(pair,style)
            imgs.append(img)

        imgs = imgs[::-1]
        imgs_comb = np.hstack(imgs).astype('uint8')
        imgs_comb = np.invert(imgs_comb)
        imgs_comb = Image.fromarray(imgs_comb)

        return imgs_comb
