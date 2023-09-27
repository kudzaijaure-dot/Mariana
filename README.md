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


👨‍🎓 Read my paper here: [Morphizer-1.pdf](https://github.com/kudzaijaure-dot/Mariana/files/12739766/Morphizer-1.pdf)



***We recommend training more than 400K iterations (batch size is 16), 600K~800K will be better, more iterations will not be recommended.***

# Results Experiment 1:
The system was able to perform exceptionally well at extracting the relevant identity information from the target when the facial recognition could work optimally. The mask was able to maintain facial expression very well and the lighting of the room was maintained. The mask did very well transitioning smoothly between frames and maintaining a coherent identity between frames, as each frame is processed individually. 

The system failed to maintain the integrity of the mask with very exxagerated facial expressions and when the target was looking too far to either side, as the facial recognition software would struggle extracting identity information. 

## The faces used as the source identites:

![511469](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/19055f6f-2b5b-4757-bf1d-bb116bfb4d92)

![pac](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/f46e7e56-228d-437b-8f83-6545b3e905fd)

## The target face:
![kenn](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/98d54066-c256-4427-910a-50059715f7c6)


## Results 😁

### 1:


![Screenshot_20230922-091513](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/ff9320bb-7675-4c00-b0e1-47afeec63cc0)


https://github.com/kudzaijaure-dot/Mariana/assets/55686042/e9d3650d-df54-4f97-b36d-226aac9226fc


### 2:
![Screenshot (6)](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/da8c4b47-6f10-442e-87c6-a170b704f032)




https://github.com/kudzaijaure-dot/Mariana/assets/55686042/3e4d1c72-a583-43cb-99d4-72920acac6fe




# Experiment 2:

The software did exceptionally well at extracting the identity of the source images. It did not however, manage to maintain performance regardless of the source image. As seen below, it performs at SOTA when the general facial features such as jawline, nose, and facial structure are similar, in essence performing well within domains. When attempting to use an identity from a source image with different features, it does not manage to perfectly implant the identity information and looks more like a blend between the two images. 
## Target Identity ➡️

https://github.com/kudzaijaure-dot/Mariana/assets/55686042/21efb54e-a3ed-4ed1-add1-9e06458c759e



## Results 😸

### 1:

https://github.com/kudzaijaure-dot/Mariana/assets/55686042/f091eb46-1859-4d6a-9fb1-afa9f9db4503

### 2:

https://github.com/kudzaijaure-dot/Mariana/assets/55686042/27b8a933-c06d-4133-b1f6-ecc484119444




# Future Improvements:
The dataset can very much be fine-tuned to include more exxagerrated and extreme facial conditions so that the end result is iron clad regardless of the task. The software will be improved to take into account facial hair, teeth, ears, head hair and neck, in essence completing a full head swap. 

> This software is free for use, if you're experienced enough to use it without guidance. If you need guidance, or need help adding it to software, buy me a coffee and lets chat! ☕ krjaure556@gmail.com
