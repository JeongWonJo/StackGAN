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
Download the preprocessed skip-thoughts embedding for COCO dataset and save it to data/coco/train<br>
* [Optional] To make embedding for your own dataset, ```python miscc/skipthought_embed.py --caption_path /path/to/your/caption.txt``` <br>
Your captions in caption.txt should be in the equivalent order with filenames.pickle. For instance, *x* line in filenames.pickle specifies the path to *x* image, and similarly, *x* line in caption.txt file describes *x* image.<br><br>
"""write code"""<br>
Download the coco image data from: """google drive url""" and extract them to *~/StackGAN/data/coco/.<br> 
Now your directories should look like: <br>
```
/StackGAN
  data
    coco
      train
      test
      images
      
``` 
"""edit directories"""
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
It will read the sample captions you have written in *~/StackGAN/data/coco/sample_captions.txt*.
<br>
<br>
<br>
**You would need to edit paths specified in .yml files when you are working with your own dataset from scratch.**
