import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    
    if not os.path.exists('C:\\Users\\bigse\\Limpiador\\neg'):
        os.makedirs('C:\\Users\\bigse\\Limpiador\\neg')
        
    pic_num = 890
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, 'C:\\Users\\bigse\\Limpiador\\neg\\'+str(pic_num)+".jpg")
            img = cv2.imread('C:\\Users\\bigse\\Limpiador\\neg\\'+str(pic_num)+".jpg", cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite('C:\\Users\\bigse\\Limpiador\\neg\\'+str(pic_num)+".jpg", resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))
            
def find_uglies():
    match = False
    for file_type in ['C:\\Users\\bigse\\Limpiador\\neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('C:\\Users\\bigse\\Limpiador\\Uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('C:\\Users\\bigse\\Limpiador\\Uglies\\'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))
                    
def create_neg():
    for file_type in ['C:\\Users\\bigse\\Limpiador\\neg']:
        
        for img in os.listdir(file_type):            
                    
            if file_type == 'C:\\Users\\bigse\\Limpiador\\neg':
                line = file_type+'\\'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
                    
create_neg()
                    
#find_uglies()           
#store_raw_images()