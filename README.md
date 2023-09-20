# Mariana: Africas most efficient deepfake neural network for creating amazing videos and images
##

**My method can perform **decent face swapping** on images and videos with **one single trained model, inferenced from a single sample**.**

This project was built and completed as a part of my Capstone thesis for my bachelors degree. It is free for use and has 2 components tested and ready for deployment. The inferencing engine however, does not work in real-time and thus cannot be used on apps and platforms yet. One 2 minute video requires about 15 minutes of GPU processing to make the result.

How it works: My system splits the video into frames that it then executes the identity swapping function on, individually. 

# Training and test code are now available!
- Train: [ <a href="https://colab.research.google.com/github/kudzaijaure-dot/Mariana/blob/main/train.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>](https://colab.research.google.com/github/kudzaijaure-dot/Mariana/blob/main/train.ipynb) 

- Inference with pretrained model:   [ <a href="https://colab.research.google.com/github/kudzaijaure-dot/Mariana/blob/main/Mariana%20colab.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>](https://colab.research.google.com/github/kudzaijaure-dot/Mariana/blob/main/train.ipynb)




**`2022-05-06`**: 
Trained this model with a high quality dataset found here: [VGGFace2-HQ](https://drive.google.com/drive/folders/1ZHy7jrd6cGb2lUa4qYugXe41G_Ef9Ibw?usp=sharing). Attribution for the creation of this data set goes to [Kairui Feng](https://scholar.google.com.hk/citations?user=4N5hE8YAAAAJ&hl=zh-CN), a PhD student from Princeton University.

Read my paper here: 

***We recommend training more than 400K iterations (batch size is 16), 600K~800K will be better, more iterations will not be recommended.***

