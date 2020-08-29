# Pyconcrete-Python
- Example of encrypting a python script using the pyconcrete
- I recommend that you should ignore the commented instructions with an octothorpe, #.
- Modified date: July 26, 2020.


## Table of contents
0.  [Summarized environments about the Pyconcrete-Python](#envs)
1.  [Create a virtualenv for python3 and activate it.](#pip3_virtualenv)
2.  [Install python packages.](#pip3_pkgs)
3.  [Run a demo code without encyrption](#demo_wo_enc)
4.  [Encrypt a python source code using the pyconcrete and run a demo code with encryption.](#demo_w_enc)
5.  [Encrypt all python source codes using the pyconcrete and run a demo code with encryption.](#demo_w_enc_full)


## 1. Summarized environments about the Pyconcrete-Python <a name="envs"></a>
- Operating System (OS): Ubuntu MATE 18.04.3 LTS (Bionic)
- Graphics Processing Unit (GPU): NVIDIA TITAN Xp, 1ea
- GPU driver: Nvidia-440.100
- CUDA toolkit: CUDA 10.2
- cuDNN: cuDNN v7.6.5


## 2. Create a virtualenv for python3 and activate it. <a name="pip3_virtualenv"></a>
- The root directory for the virtualenv: /home/usrname/pip3_virtualenv
- The name of new virtualenv to be created: pyconcrete
- Please note that the python version (e.g. python3.6) to be installed should be equal to the default python3 version for a python3 package, pyconcrete.
```bash
usrname@hostname:~/curr_path$ mkdir -p /home/usrname/pip3_virtualenv/pyconcrete
usrname@hostname:~/curr_path$ virtualenv /home/usrname/pip3_virtualenv/pyconcrete/ --python=python3.6
usrname@hostname:~/curr_path$ source /home/usrname/pip3_virtualenv/pyconcrete/bin/activate
(pyconcrete) usrname@hostname:~/curr_path$
```


## 3. Install python packages. <a name="pip3_pkgs"></a>
- The name of activated virtualenv: pyconcrete
- I recommend that you should install the python package, pyconcrete from source, not pip3. 
- Thus, the provided requirements.txt does not include the python3 package, pyconcrete.
```bash
(pyconcrete) usrname@hostname:~/curr_path$ git clone https://github.com/vujadeyoon/Pyconcrete-Python
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ pip3 install -r requirements.txt
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ mkdir -p /home/usrname/pip3_packages
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ git clone https://github.com/Falldog/pyconcrete /home/usrname/pip3_packages/pyconcrete
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ cd /home/usrname/pip3_packages/pyconcrete
(pyconcrete) usrname@hostname:~/pyconcrete$ python setup.py install
(pyconcrete) usrname@hostname:~/pyconcrete$ cd ~/Pyconcrete-Python
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$
```


## 4. Run a demo code without encyrption <a name="demo_wo_enc"></a>
- Please note that you should download a checkpoint for the pretrained model, resnet18 (i.e. resnet18-5c106cde.pth) from the Facebook torchvision using the wget.
- Please note that you should prepare an image to ./Pyconcrete-Python/image.png.
```bash
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ wget "https://download.pytorch.org/models/resnet18-5c106cde.pth"
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ python3 main.py
torch.Size([1000])
tensor(800, device='cuda:0')
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$
```


## 5. Encrypt a python source code using the pyconcrete and run a demo code with encryption. <a name="demo_w_enc"></a>
- If you have not prepared the checkpoint and image, please refer to the section 4 and prepare them.
- The path for a python source code to be encrypted: ~/Pyconcrete-Python/resnet.py
```bash
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ cd /home/usrname/pip3_packages/pyconcrete
(pyconcrete) usrname@hostname:~/pyconcrete$ pyconcrete-admin.py compile --source=~/Pyconcrete-Python/resnet.py --pye
(pyconcrete) usrname@hostname:~/pyconcrete$ rm -rf ~/Pyconcrete-Python/resnet.py
(pyconcrete) usrname@hostname:~/pyconcrete$ cd ~/Pyconcrete-Python
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ python3 main.py
torch.Size([1000])
tensor(800, device='cuda:0')
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$
```


## 6. Encrypt all python source codes using the pyconcrete and run a demo code with encryption. <a name="demo_w_enc_full"></a>
- If you have not prepared the checkpoint and image, please refer to the section 4 and prepare them.
- The path for a python source code to be encrypted: ~/Pyconcrete-Python/*.py
```bash
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ cd /home/usrname/pip3_packages/pyconcrete
(pyconcrete) usrname@hostname:~/pyconcrete$ pyconcrete-admin.py compile --source=~/Pyconcrete-Python/ --pye
(pyconcrete) usrname@hostname:~/pyconcrete$ find ~/Pyconcrete-Python/ -name "*.py" -exec rm -rf {} \;
(pyconcrete) usrname@hostname:~/pyconcrete$ cd ~/Pyconcrete-Python
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$ pyconcrete main.pye
torch.Size([1000])
tensor(800, device='cuda:0')
(pyconcrete) usrname@hostname:~/Pyconcrete-Python$
