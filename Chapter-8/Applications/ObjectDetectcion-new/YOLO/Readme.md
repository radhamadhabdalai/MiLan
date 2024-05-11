########################## OM Sree Sree Lokanathay Namoh###########################################################
#Obect Detection using YOLOv3 
Follow these steps to train and test the object detection model YOLO-v3(Version-3)
(Later SSD and RCNN, YOLO-vx object detection model from scratch[custom dataset] will be posted.)
This folder contains a notebook file and a Datsets folder.

First keep dataset ready. You have to download MSCOCO dataset 2017 data


## Download Dataset (file size is = 11gb , you can use mini 2017 data which is 4 gb but annotation and validation file you have to configure)
Create a folder called 'Datasets/yolo' in the root level (where YOLOv3_Fruit_Detection.ipynb file lies ). Inside the dataset folder, follow the 
#option-1
instructions on this page: http://cocodataset.org/#download, download images into 

`Datasets/yolo/train2017`, 
`Datasets/yolo/val2017` ,
`Datasets/yolo/test2017`
# option-2    use gstool but you have to configure gsutil using google cloud , so I have opted option-1 
use command line 
```bash
mkdir val2017
mkdir train2017
mkdir test2017
gsutil -m rsync gs://images.cocodataset.org/val2017 val2017
gsutil -m rsync gs://images.cocodataset.org/train2017 train2017
gsutil -m rsync gs://images.cocodataset.org/test2017 test2017
```
Also, download the annotations
```bash
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
unzip annotations_trainval2017.zip
```

## Creating TF Record
Copy `tfrecords.py` to your newly created `Datasets/yolo/` folder. Run `tfrecords.py` to generate TF Records. 
All dependecies should have been installed (ray, PIL)
```bash
conda activate yolo (your environment name)
python tfrecords.py
```
#copy the class names file `mscoco_2017_names.txt` to `Datasets/yolo/` 
Reference - Deep Learning in Computer Vision (deep-vision)
# Wishing you a good luck 

Copyright (c) 2023, 2024 Radhamadhab Dalai, ITER , Siksha O Aanusandhan University, 
Odisha, India
Author's email address :  radhamadhabdalai@soa.ac.in
