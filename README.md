## Emotion Detection - Team Arcane


welcome to Team Arcane's Emotion Detection repository! <br />
<br />

## Our Motivation
Mental health is an essential aspect of our lives as it affects our emotional, psychological, and social well-being. Maintaining proper mental health can benefit us as it increases productivity, promotes self-confidence, and even improves relationships. Conversely, having bad mental health may lead to mental illnesses and may even be harmful to our bodies. <br />
<br />
Through this project, we aim to aid and enable professionals, experts, and maybe even ordinary people to analyze and hopefully assist in diagnosing people with mental health problems before it gets too severe.<br />


##Best Parameter:
Crop          224 <br />
Batch Size    128 <br />
Epoch         90 <br />
Learning Rate 0.001 <br />
Converted     True #convert 1000 classes classification to 7 classes classification <br />
Pre-trained   True <br />

##Result:
**training accuracy:** 86% <br />
**Validation accuracy:** 69% <br />

**How to validate our result?**
python ImageNetMain.py -a resnet18 ckplus_add/Emotion_image_Dataset --gpu 0 --batch-size 128 --lr 0.001 --pretrained --epoch 90 | tee log.txt <br />

**Dataset:** FER2013  https://paperswithcode.com/dataset/fer2013 <br />
**Model:**  ResNet-18 https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf

**Member:** <br />
Fuwei Zhuang (Elina): 19fz2@queensu.ca :) <br />
Benjamin Hui (Ben): 18bh13@queensu.ca <br />
Hudson Chen (Hudson): 18hc41@queensu.ca <br />
Wanqing Li (Wanqing): wanqing.li@queensu.ca <br />
E Ching Kho (Noon): 17eck3@queensu.ca <br />

**Mentor:** <br />
Tristan Sylvain <br />
