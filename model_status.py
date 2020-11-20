'''
from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
project_id = "automl-set-up-task-aj"
dataset_id = "IOD8107419411708641280"
display_name = "roof_segmentation_20201120123026"

client = automl.AutoMlClient()

# A resource that represents Google Cloud Platform location.
project_location = f"projects/{project_id}/locations/us-central1"
# Leave model unset to use the default base model provided by Google
# train_budget_milli_node_hours: The actual train_cost will be equal or
# less than this value.
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#imageobjectdetectionmodelmetadata
metadata = automl.ImageObjectDetectionModelMetadata(
    train_budget_milli_node_hours=24000
)
model = automl.Model(
    display_name=display_name,
    dataset_id=dataset_id,
    image_object_detection_model_metadata=metadata,
)

# Create a model with the model metadata in the region.
response = client.create_model(parent=project_location, model=model)

print("Training operation name: {}".format(response.operation.name))
print("Training started...")
'''

from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
operation_full_id = "projects/479717817760/locations/us-central1/operations/IOD2037187788327092224"
    # "projects/[projectId]/locations/us-central1/operations/[operationId]"

client = automl.AutoMlClient()
# Get the latest state of a long-running operation.
response = client._transport.operations_client.get_operation(
    operation_full_id
)

print("Name: {}".format(response.name))
print("Operation details:")
print(response)