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
<br>

## Training
Download the pretrained skip-thoughts embedding for COCO dataset and save it to data/coco/train
* [Optional] To make embedding for your own dataset, ```python miscc/skipthought_embed.py --caption_path /path/to/your/caption.txt
