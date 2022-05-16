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

### Create a Compute Instance

Compute instances inside of Azure Machine Learning are standalone virtual machines which come with preconfigured data science environments that can be used for machine learning development and testing activities. For the purpose of this demo we recommend creating a `Standard_DS3_v2` compute instance and using this to execute the prepared notebooks within this repo.

Navigate to the 'Compute' table along the left sidebar menu and click the '+ New' button under the compute instances panel.

![Compute Instance](img/03.png?raw=true "Compute Instance")

From the 'Create compute instance' tab give your compute instance a globally unique name, and select the `Standard_DS3_v2` option under Virtual machine size. Also, it is recommended to create an automatic shutdown schedule under the 'Advanced Settings' tab which will help avoid any unexpected charges.

![Create Compute Instance](img/04.png?raw=true "Create Compute Instance")

Once your compute instance has been created you should see the state message reflect 'Succeeded' and the VM will be ready for use. To follow along with the pictorial guide in this README, launch the 'JupyterLab' application from applications list.

![Launch JupyterLab](img/05.png?raw=true "Launch JupyterLab")

### Clone this Repo to AML Compute Instance

Inside of JupyterLab, launch a new terminal by clicking the 'Terminal' option from the Launcher menu.

![Open Terminal](img/06.png?raw=true "Open Terminal")

From the newly opened terminal execute the following commands to clone this repo to a folder under your user directory:

```
cd Users/<YOUR-USERNAME>
git clone https://github.com/nickwiecien/AzureML_AutoML_for_Images_Instance_Segmentation
```

After cloning the repo you should see a directory structure that looks like what is shown below:

![Folder Structure](img/07.png?raw=true "Folder Structure")

### Run 01. Notebook to Setup AML Environment

Double-click the `01_Setup_AML_Env.ipynb` notebook from the file explorer to open the environment setup notebook. This notebook contains sample code to create a compute cluster for model training, upload sample street images to an AML-linked datastore, and create/register a labeled dataset that can be used as an input to an AutoML for Images training job.

From the top menubar, click Run and select 'Run All Cells' - this will trigger execution of all cells in the notebook.

![Notebook 1](img/08.png?raw=true "Notebook 1")

After executing all cells (should take ~1 minute) you can validate the setup inside the Azure ML Studio UI. Check that the following assets have been created:

- GPU Compute Cluster named `automlimagescompute`

![Compute Cluster](img/09.png?raw=true "Compute Cluster")

- Blob Datastore named `streetimagestore` compute with sample images

![Image Datastore](img/10.png?raw=true "Image Datastore")

- Registered Test/Train image datasets named `TEST_AML_Labeled_Street_Images` and `TRAIN_AML_Labeled_Street_Images`, respectively. You can explore these datasets to review sample annotations as well.

![Image Datasets](img/11.png?raw=true "Image Datasets")

### Run 02. Notebook to Create AutoML for Images Training Pipeline & Submit Pipeline Run

From JupyterLab, double-click the `02_Create_AML_Model_Training_Pipeline.ipynb` notebook to create a reusable instance segmentation model training pipeline that leverages AutoML for Images under the hood. Again, from the top menubar click Run and then select 'Run All Cells' to trigger all cells in the notebook.


## Sample Images
Sample images used within this repository were retrieved from the [CBCL StreetScenes Challenge Framework](http://cbcl.mit.edu/software-datasets/streetscenes/) which is a collection of images, annotations, software and performance measures for object detection. Each image was taken from a DSC-F717 camera at in and around Boston, MA. For more information on this collection see Stanley Bileschi's Doctoral Thesis cited below.

-----

[StreetScenes: Towards Scene Understanding in Still Images](http://citeseerx.ist.psu.edu/viewdoc/summary;jsessionid=2CC628AB1C394A3FC44C9FC5EF111062?doi=10.1.1.72.3289) –Stanley Michael Bileschi — 2006 — PHD DISSERTATION, MASSACHUSETTES INST. OF TECHNOLOGY

-----
