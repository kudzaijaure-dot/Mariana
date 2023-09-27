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

![511469](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/c5db9cb8-f795-497d-afeb-b9f50ad13c38)

![pac](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/ba4e2569-b8ab-4f63-b0a9-a19d36a0ca4d)

## The target face:
![kenn](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/97f9442e-f615-4f37-b995-d35b77066bd0)

## Results 😁

### 1:

![Screenshot_20230922-091513](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/c2168fad-8e1b-40f0-a518-4b8cfe5bfb64)


https://github.com/kudzaijaure-dot/Mariana/assets/55686042/2edae73d-ddb8-4460-8af5-b9683dc64ea9

### 2:

![Screenshot_20230922-091438](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/fb402ab8-d672-427d-86fe-6408c7ec4a14)

https://github.com/kudzaijaure-dot/Mariana/assets/55686042/b9a38d56-1234-48cd-850b-200cb0a125a0

# Experiment 2:

The software did exceptionally well at extracting the identity of the source images. It did not however, manage to maintain performance regardless of the source image. As seen below, it performs at SOTA when the general facial features such as jawline, nose, and facial structure are similar, in essence performing well within domains. When attempting to use an identity from a source image with different features, it does not manage to perfectly implant the identity information and looks more like a blend between the two images. 
## Target Identity ➡️



https://github.com/kudzaijaure-dot/Mariana/assets/55686042/0f9ecfbf-80b5-4e1d-961e-34ae1d0a9e32


## Results 😸

### 1:
![tom](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/29043871-c641-4f7f-a7cb-31850635d6f7)

https://github.com/kudzaijaure-dot/Mariana/assets/55686042/5ac30dbf-33ed-435c-8780-8870477209ab

### 2:
![Iron_man](https://github.com/kudzaijaure-dot/Mariana/assets/55686042/446031c2-ade9-4bf3-895d-031e35cae1cd)


https://github.com/kudzaijaure-dot/Mariana/assets/55686042/b0e07210-3e9c-4319-8793-561fa9070072


# Future Improvements:
The dataset can very much be fine-tuned to include more exxagerrated and extreme facial conditions so that the end result is iron clad regardless of the task. The software will be improved to take into account facial hair, teeth, ears, head hair and neck, in essence completing a full head swap. 

> This software is free for use, if you're experienced enough to use it without guidance. If you need guidance, or need help adding it to software, buy me a coffee and lets chat! ☕ krjaure556@gmail.com
