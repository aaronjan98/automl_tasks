project_id = 'automl-set-up-task-aj'
compute_region = 'us-central1'
model_display_name = 'roof_segmentation_20201120123026'
filter = 'good_roof'

from google.cloud import automl_v1beta1 as automl

client = automl.TablesClient(project=project_id, region=compute_region)

# List all the model evaluations in the model by applying filter.
response = client.list_model_evaluations(
    model_display_name=model_display_name
    # model_display_name=model_display_name, filter=filter
)

print("List of model evaluations:")
for evaluation in response:
    print("Model evaluation name: {}".format(evaluation.name))
    print("Model evaluation id: {}".format(evaluation.name.split("/")[-1]))
    print(
        "Model evaluation example count: {}".format(
            evaluation.evaluated_example_count
        )
    )
    print("Model evaluation time: {}".format(evaluation.create_time))
    print("\n")