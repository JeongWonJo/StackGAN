# StackGAN
## Dependencies<br>
Python 3.6<br>

Install following packages with ```pip install```: 
```
pip install tensorflow==0.12.1
pip install torch torchvision
export PYTHONPATH="${PYTHONPATH}:/home/jjw49/StackGAN"
pip install prettytensor==0.7.1
pip install progressbar==2.5
pip install python-dateutil==2.8.0
pip install easydict
pip install torchfile
pip install pandas==0.24.2
pip install scipy==1.1.0
pip install pyyaml==5.1
pip install numpy==1.16.2
pip install scikit-learn
pip install nltk==3.4
pip install theano==1.0.4
```
<br>
<br>

## Prepare Data
### Prepare Image and Caption Data

Download the [birds image](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html) and extract it to ```Data/birds/```.<br>
*command:* 
```
cd Data/birds
wget http://www.vision.caltech.edu/visipedia-data/CUB-200-2011/CUB_200_2011.tgz
tar -zxvf CUB_200_2011.tgz
```

Preprocess images.
```python misc/preprocess_birds.py```


### vocabulary for skip-thought vectors
```
cd Data/skipthoughts/
wget http://www.cs.toronto.edu/~rkiros/models/dictionary.txt
wget http://www.cs.toronto.edu/~rkiros/models/utable.npy
wget http://www.cs.toronto.edu/~rkiros/models/btable.npy
wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz
wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz.pkl
wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz
wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz.pkl
```

<br>
<br>


## Pretrained Model
Download [birds model](https://drive.google.com/open?id=0B3y_msrWZaXLZVNRNFg4d055Q1E) trained from skip-thought text embeddings. Download and save it to ```models/```.

<br>
<br>

## Run Demos
Run ```python birds_skip_thought_demo.py --cfg demo/cfg/birds-skip-thought-demo.yml --gpu 0``` to generate bird samples from sentences. The results will be saved to ```Data/birds/example_captions-skip-thought/```
<br>
Edit sentences in ```Data/birds/example_captions.txt``` to customize sentences.
