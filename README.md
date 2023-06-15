# MultiModal-Eval

This is the official implementation of the paper _Disentangling the Performance Puzzle of Multimodal-aware Recommender Systems_, under review as full paper at EvalRS’23@KDD.

## Table of Contents
- [Pre-requisites](#pre-requisites)
- [Installation](#installation)
  - [Local](#local)
  - [Docker](#docker)
- [Datasets](#datasets)
- [Training](#training)
- [Evaluation](#evaluation)

## Pre-requisites

We implemented and tested our models in `PyTorch==1.12.0`, with CUDA `10.2` and cuDNN `8.0`. Additionally, some of graph-based models require `PyTorch Geometric`, which is compatible with the versions of CUDA and `PyTorch` we indicated above.

## Installation

### Local
If you have the possibility to install CUDA on your workstation (i.e., `10.2`), you may create the virtual environment with the requirement files we included in the repository, as follows:

```sh
# PYTORCH ENVIRONMENT (CUDA 10.2, cuDNN 8.0)

python3.8 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements_torch_geometric.txt
```

### Docker
A more convenient way of running experiments is to instantiate a docker container having CUDA `10.2` already installed. Make sure you have Docker and NVIDIA Container Toolkit installed on your machine (you may refer to this [guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installing-on-ubuntu-and-debian)). Then, you may use the following Docker image to instantiate the container equipped with CUDA `10.2` and cuDNN `8.0`: [link](https://hub.docker.com/layers/nvidia/cuda/10.2-cudnn8-devel-ubuntu18.04/images/sha256-3d1aefa978b106e8cbe50743bba8c4ddadacf13fe3165dd67a35e4d904f3aabe?context=explore).

## Datasets

We provide already processed and split datasets in the ```./data/``` folder. Just unzip the files and you are done!

Each dataset folder comes with the following files/subfolders:

```
<dataset_name>/
  image_feat/
    0.npy
    1.npy
    ...
  text_feat/
    0.npy
    1.npy
    ...
  train.txt
  test.txt
  val.txt
```

## Training

To train all baselines on a specific dataset, run the following command:

```sh
python3.8 start_experiments.py --dataset <dataset_name>
```

Please consider that this may take some time depending on the machine you are running the experiments on.

## Evaluation
