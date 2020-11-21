from google.cloud import automl

project_id = "automl-set-up-task-aj"
model_id = "IOD8107419411708641280"

client = automl.AutoMlClient()
# Get the full path of the model.
model_full_id = client.model_path(project_id, "us-central1", model_id)
model = client.get_model(name=model_full_id)

# Retrieve deployment state.
if model.deployment_state == automl.Model.DeploymentState.DEPLOYED:
    deployment_state = "deployed"
else:
    deployment_state = "undeployed"

# Display the model information.
print("Model name: {}".format(model.name))
print("Model id: {}".format(model.name.split("/")[-1]))
print("Model display name: {}".format(model.display_name))
print("Model create time: {}".format(model.create_time))
print("Model deployment state: {}".format(deployment_state))