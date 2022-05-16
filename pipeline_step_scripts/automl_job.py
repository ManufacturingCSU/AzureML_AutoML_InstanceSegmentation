from azureml.core import Run, Dataset, Environment
import argparse
from azureml.core.compute import ComputeTarget
import os


#Parse Input Arguments
parser = argparse.ArgumentParser("Retrieve AML Dataset and Launch AutoML for Images Job")
parser.add_argument("--model_name", type=str, required=True)
parser.add_argument("--dataset_name", type=str, required=True)
parser.add_argument("--compute_name", type=str, required=True)
args, _ = parser.parse_known_args()
model_name = args.model_name
dataset_name = args.dataset_name
compute_name = args.compute_name

#Get current run and AML workspace
current_run = Run.get_context()
ws = current_run.experiment.workspace
experiment_name = current_run.experiment.name

compute_target = ComputeTarget(workspace=ws, name=compute_name)

from azureml.automl.core.shared.constants import ImageTask
from azureml.train.automl import AutoMLImageConfig
from azureml.train.hyperdrive import BanditPolicy, RandomParameterSampling
from azureml.train.hyperdrive import choice, uniform

from azureml.core import Dataset
dataset = Dataset.get_by_name(ws, name=dataset_name)
formatted_datasets = [('Training_Data', dataset)]


from azureml.train.automl import AutoMLImageConfig
from azureml.train.hyperdrive import GridParameterSampling, choice
from azureml.automl.core.shared.constants import ImageTask

tuning_settings = {
    "iterations": 20,
    "max_concurrent_iterations": 5,
    "hyperparameter_sampling": GridParameterSampling({'model_name': choice('maskrcnn_resnet18_fpn', 'maskrcnn_resnet34_fpn', 'maskrcnn_resnet50_fpn','maskrcnn_resnet101_fpn','maskrcnn_resnet152_fpn', 'yolov5'), 'number_of_epochs': 50, 'img_size': 640}),
    "enable_early_stopping": False
}

image_automl_config = AutoMLImageConfig(
    task=ImageTask.IMAGE_INSTANCE_SEGMENTATION,
    compute_target=compute_target,
    training_data=dataset,
    **tuning_settings
)

new_run = current_run.submit_child(image_automl_config)
new_run.wait_for_completion()

best_child_run = new_run.get_best_child()
metrics = best_child_run.get_metrics()

updated_tags = metrics

os.makedirs('tmp')

best_child_run.download_files(prefix='./outputs', output_directory='tmp',append_prefix=True)
best_child_run.download_files(prefix='./train_artifacts', output_directory='tmp',append_prefix=True)

current_run.upload_folder('automl_outputs', 'tmp')

model = current_run.register_model(model_name, model_path='automl_outputs', model_framework='Azure ML - AutoML for Images (Instance Segmentation)', tags=updated_tags, datasets=formatted_datasets, sample_input_dataset = dataset)

scoring_env = Environment.from_conda_specification('AutoMLImages_ScoringEnv', './tmp/outputs/conda_env_v_1_0_0.yml')
scoring_env.register(ws)
