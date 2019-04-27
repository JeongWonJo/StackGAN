# StackGAN
## Dependencies<br>
Python 3.6<br>
Pytorch with Cuda 9.0 (```conda install pytorch torchvision cudatoolkit=9.0 -c pytorch```)<br><br>
Add the project folder to PYTHONPATH; write down following command line on the project folder(```export PYTHONPATH="${PYTHONPATH}:/your/home/path/project/folder/StackGAN"```)<br><br>
Install following packages with ```pip install```: 
```
pip install tensorboard==1.0.0a6
pip install theano
pip install python-dateutil
pip install easydict
pip install pandas
pip install torchfile
```
<br>

## Prepare Data
### Prepare Image and Caption Data

Download the preprocessed skip-thoughts embedding for COCO dataset and save it to data/coco/train.
<br>
[Optional] To make embedding for your own dataset, ```python miscc/skipthought_embed.py --caption_path /path/to/your/caption.txt``` 
<br>
Your captions in caption.txt should be in the equivalent order with filenames.pickle. For instance, *x* line in filenames.pickle specifies the path to *x* image, and similarly, *x* line in caption.txt file describes *x* image.
<br><br>
"""write code"""
<br>
Download the '2014 Train Images','2014 Train Images', and '2014 Train/Val annotations' from [coco dataset](http://cocodataset.org/#download). Extract them to *~/StackGAN/data/coco/.*
<br>
<br>

### Prepare Image and Caption Data
[Download](https://github.com/ryankiros/skip-thoughts) vocabularies for skip-thought vectors to *~/StackGAN/data/coco/.*
<br>
<br>
<br>
Now your directories should look like: <br>
```
/StackGAN
  code
  data
    coco
      train
        caption.pickle
        filenames.pickle
        skip-thought-embeddings.pickle
      test
        val_captions.t7
        val_captions.txt
        val_filename.txt
      images
        (place all train images here)
        ...
        COCO_train2014_000000581921.jpg
        ...
      test_image
        (place all test images here)
        ...
        COCO_test2014_000000581923.jpg
        ...
    skipthoughts
      (files necessary for skipthoughts)
      bi_skip.npz
      btable.npy
      uni_skip.npz
      utable.npy
      bi_skip.npz.pkl
      dictionary.txt
      uni_skip.npz.pkl
``` 
<br>

## Training
If you use the COCO dataset and my preprocessed embeddings: <br>
* Stage-I GAN: Go to 'code' folder with ```cd code``` and write down the following command:```python main.py --cfg cfg/coco_s1.yml --gpu 0```. It is set for 120 epochs, and you can alter it by editing 'MAX_EPOCH' argument on coco_s1.yml file, which is in /code/cfg folder. <br><br>
You can see the image and model created during the final epoch in *~/StackGAN/output/coco_stage1/*. If you are using your own dataset, the folder name will be *~/StackGAN/output/**yourdataset**_stage1/*. <br>
There will be three folders created inside the directory, 'Image', 'Log', and 'Model'. <br> <br>

* Stage-II GAN: ```python main.py --cfg cfg/coco_s2.yml --gpu 0``` Just like Stage-I GAN, you can edit the number of epochs and the batch size by editing coco_s2.yml file.
<br>
<br>

## Evaluation
You can evaluate the model by running ```python main.py --cfg cfg/coco_eval.yml```.
It will read the sample captions you have written in *~/StackGAN/data/coco/sample_captions.txt*. <br>
(The code will automatically covert the captions into skip-thought-embedding.)

<br>
<br>
<br>
**You would need to edit paths specified in .yml files when you are working with your own dataset from scratch.**
