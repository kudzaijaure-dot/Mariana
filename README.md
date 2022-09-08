# Mariana: Africas most efficient deepfake neural network for creating amazing videos and images
## Kudzai Jaure in collaboration with Group 2 Computer Science, Africa University

**Our method can realize **arbitrary face swapping** on images and videos with **one single trained model**.**

# Training and test code are now available!
- Train: [ <a href="https://colab.research.google.com/github/kudzaijaure-dot/Mariana/blob/main/train.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>](https://colab.research.google.com/github/neuralchen/SimSwap/blob/main/train.ipynb) 

- Inference with pretrained model:   [ <a href="https://colab.research.google.com/github/kudzaijaure-dot/Mariana/blob/main/Mariana%20colab.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>](https://colab.research.google.com/github/neuralchen/SimSwap/blob/main/train.ipynb)


## Attention
***This project is for academic use as a capstone project and is not meant to be used in a commercial applications except where authorized by K. R. Jaure***

***This code is not open to contribution until the license has been finalized and declared.***


**`2022-05-06`**: 
Trained this model with a high quality dataset found here: [VGGFace2-HQ](https://drive.google.com/drive/folders/1ZHy7jrd6cGb2lUa4qYugXe41G_Ef9Ibw?usp=sharing). Attribution for the creation of this data set goes to [Kairui Feng](https://scholar.google.com.hk/citations?user=4N5hE8YAAAAJ&hl=zh-CN), a PhD student from Princeton University.

## ***Our Group Members:***
- Thabani Masukume
- Marc Signe Aurele
- Kudzai Jaure

## Dependencies
- python3.6+
- pytorch1.5+
- torchvision
- opencv
- pillow
- numpy
- imageio
- moviepy
- insightface


***We recommend training more than 400K iterations (batch size is 16), 600K~800K will be better, more iterations will not be recommended.***

