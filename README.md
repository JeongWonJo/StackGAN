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
* [Optional] To make embedding for your own dataset, ```python miscc/skipthought_embed.py --caption_path /path/to/your/caption.txt``` <br> """write code"""<br>
Download the coco image data from: """google drive url""" and extract them to data.<br> 
Now your directories should look like: <br>
```
/StackGAN
  data
    coco
      train
      test
``` 
"""edit directories"""
<br>

## Training
If you use the COCO dataset and my preprocessed embeddings: <br>
* Stage-I GAN: Go to 'code' folder with ```cd code``` and write down the following command:```python main.py --cfg cfg/coco_s1.yml --gpu 0```. It is set for 120 epochs, and you can alter it by editing 'MAX_EPOCH' argument on coco_s1.yml file, which is in /code/cfg folder. <br>
* Stage-II GAN: ```python main.py --cfg cfg/coco_s2.yml --gpu 0``` Similarly, you can edit the number of epoch by editing coco_s2.yml file.
<br>
You can either skip the training process by downloading the pretrained model."""gdrive url"""
<br>

## Evaluation
You can evaluate the model by running ```python main.py --cfg cfg/coco_eval.yml```.
<br>
<br>
<br>
**You would need to edit paths specified in .yml files when you are working with your own dataset from scratch.**
