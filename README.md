# Azure ML - AutoML for Images: Instance Segmentation

Auzre Machine Learning's AutoML for Images functionality can be used to train custom image classification, object detection, and instance segmentation models. The notebooks contained within this sample repository demonstrate an end-to-end sample for: 

- Creating compute resources for training and inferencing operations
- Uploading sample images to an AML datastore 
- Creating and registering a labeled image dataset
- Building and publishing a reusable model training pipeline which submits an AutoML for Images training job
- Registering a trained instance segmentation model to the AML workspace
- Deploying a trained model to a real-time endpoint (Azure Kubernetes)
- Submitting HTTP requests to consume a deployed instance segmentation model 

![Azure ML - AutoML for Images: Instance Segmentation](img/01.png?raw=true "Azure ML - AutoML for Images: Instance Segmentation")

Follow the 'Getting Started' guide below for step-by-step instructions for executing this sample.

## Getting Started

Following the instructions below to deploy and run this demo.

### Required Resources

In order to run this demo you will need access to an Azure Machine Learning workspace. If you do not have access to an existing Azure Machine Learning workspace, you can provision and new instance by following [the quickstart guide linked here](https://docs.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources).

Sign into your AML workspace by navigating to [ml.azure.com](https://ml.azure.com/) and selecting the target workspace you aim to run this demo inside of.

![Azure ML Workspace](img/02.png?raw=true "Azure ML Workspace")


### Sample Images
Sample images used within this repository were taken from the [CBCL StreetScenes Challenge Framework](http://cbcl.mit.edu/software-datasets/streetscenes/) which is a collection of images, annotations, software and performance measures for object detection. Each image was taken from a DSC-F717 camera at in and around Boston, MA. For more information on this collection see Stanley Bileschi's Doctoral Thesis cited below.

-----

[StreetScenes: Towards Scene Understanding in Still Images](http://citeseerx.ist.psu.edu/viewdoc/summary;jsessionid=2CC628AB1C394A3FC44C9FC5EF111062?doi=10.1.1.72.3289) –Stanley Michael Bileschi — 2006 — PHD DISSERTATION, MASSACHUSETTES INST. OF TECHNOLOGY

-----
