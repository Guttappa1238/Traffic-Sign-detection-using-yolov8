# Problem Statement
“ Detect and classify the traffic sign object on image ”
# Solution:
 Data Preprocessing:
Since the dataset(Annotations) i recived was in tensorflow object detection
format, i have to convert it to Yolov8 format.
Why I Used YOLOv8?
Here are a few main reasons why i consider using YOLOv8 for this work:
1. YOLOv8 has a high rate of accuracy measured by COCO and Roboflow 100.
2. YOLOv8 comes with a lot of developer-convenience features, from an easy-to-
use CLI to a well-structured Python package.
3. There is a large community around YOLO and a growing community around
the YOLOv8 model, meaning there are many people in computer vision circles
who may be able to assist you when you need guidance.
# YOLOv8 Architecture:
 Backbone: New CSP-Darknet53
 Neck: SPPF, New CSP-PAN
 Head: YOLOv3 Head
![image](https://user-images.githubusercontent.com/45628395/223023013-dfc0944c-8f43-4e8b-8633-341be131fba3.png)
Figure 1: YOLOv8 Architecture, visualisation made by GitHub user RangeKing
Detection

YOLOv8 is an anchor-free model. This means it predicts directly the center of an
object instead of the offset from a known anchor box.

# Dataset information: 
The dataset consist of 5539 images in total and which has 3
classes ( ADVISORY SPEED MPH, DIRECTIONAL ARROW AUXILIARY, DO NOT ENTER ).
I have Split Dataset into Train, Test and Valid sets with 70, 20 and 10% respectively.Training And Results:
In this work i have used nano pretrained model. And it gave good results in real time
inference.

# How to use this Repo:

In this work i have used nano pretrained model. And it gave good results in real time inference.

for trainig run python3 train_yolov8.py

for testing run python3 test_yolov8.py

# Results:
![image](https://github.com/Guttappa1238/Traffic-Sign-detection-using-yolov8/assets/45628395/0df915f5-4411-4721-a2b7-a58e298c53b9)


![image](https://github.com/Guttappa1238/Traffic-Sign-detection-using-yolov8/assets/45628395/db1abf68-90ef-481e-b291-2e7961b0a4bb)

![image](https://github.com/Guttappa1238/Traffic-Sign-detection-using-yolov8/assets/45628395/9f1d9bf8-4b85-4adc-9a4f-682be4586921)

