import cv2
import os
count=0
creat_folder=0
path="/Users/dabc/Desktop/python tea opencv test"
my_list=os.listdir(path)
print(my_list)
my_list.reverse()
for i in my_list:
    count+=1
    new_list=(i)
    print(new_list)
    img = cv2.imread(new_list)
    crop_img = img[370:1145, 140:1450]
    print("Press Esc...")
    cv2.imshow("cropped", crop_img)
    cv2.imwrite(f"./crop/{count}image.png", crop_img)
    cv2.waitKey(0)

