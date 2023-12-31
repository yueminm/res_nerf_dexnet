# Modified Version of Berkeley AUTOLAB's GQCNN Package
<p>
   <a href="https://travis-ci.org/BerkeleyAutomation/gqcnn/">
       <img alt="Build Status" src="https://travis-ci.org/BerkeleyAutomation/gqcnn.svg?branch=master">
   </a>
   <a href="https://github.com/BerkeleyAutomation/gqcnn/releases/latest">
       <img alt="Release" src="https://img.shields.io/github/release/BerkeleyAutomation/gqcnn.svg?style=flat">
   </a>
   <a href="https://github.com/BerkeleyAutomation/gqcnn/blob/master/LICENSE">
       <img alt="Software License" src="https://img.shields.io/badge/license-REGENTS-brightgreen.svg">
   </a>
   <a>
       <img alt="Python 3 Versions" src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-yellow.svg">
   </a>
</p>

## Package Overview
The gqcnn Python package is for training and analysis of Grasp Quality Convolutional Neural Networks (GQ-CNNs). It is part of the ongoing [Dexterity-Network (Dex-Net)](https://berkeleyautomation.github.io/dex-net/) project created and maintained by the [AUTOLAB](https://autolab.berkeley.edu) at UC Berkeley.

## Installation and Usage of the Original Package
Please see the [docs](https://berkeleyautomation.github.io/gqcnn/) for installation and usage instructions.

## Installation and Usage of this Modified Package
Step 1: Get a docker container
```
docker pull nvidia/cuda:11.8.0-devel-ubuntu22.04
```

Step 2: Run the docker container
``` 
docker run --gpus "device=1" -it  -v /home/username/dexnet:/dexnet nvidia/cuda:11.8.0-devel-ubuntu22.04
```

Step 3: Clone this repo
```
git clone https://github.com/yueminm/res_nerf_dexnet.git
```

Step 4: Install python 3.10 and required packages. Note: Update numpy to version 1.24 <br />

Step 5: Create a folder named "models" to store the GQCNN-2.0 model downloaded from [Dexterity-Network (Dex-Net)](https://berkeleyautomation.github.io/dex-net/) project page. <br />

Step 6: Create a folder named "data" to store depth maps in .npy format. <br />

## Run the code
```
 ./scripts/policies/run_dex_net_2.0.sh
```

## Citation
If you use any part of this code in a publication, please cite [the appropriate Dex-Net publication](https://berkeleyautomation.github.io/gqcnn/index.html#academic-use).

