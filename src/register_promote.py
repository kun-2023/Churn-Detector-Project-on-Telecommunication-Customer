import mlflow
import sys
from mlflow import MlflowClient
from src.config import (TRACKING_URI, EXPERIMENT_NAME,
                        REGISTERED_MODEL_NAME, 
                        CANDIDATE_ALIAS, CHAMPION_ALIAS)

def register_model():
    mlflow.set_tracking_uri(TRACKING_URI)
    experiment=mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    if experiment is None:
        raise ValueError("Experiment not found.")
    
    # find the latest logged model
    models=mlflow.search_logged_models(
        experiment_ids=[experiment.experiment_id],
        filter_string="name='churn_model'",
        order_by=[{"field_name":"creation_time", "ascending": False}],
        max_results=1,
        output_format="list")
    if not models:
        raise ValueError("No logged churn model found.")
    
    # get model_uri
    model_uri=f"models:/{models[0].model_id}"
    # register model
    model_info=mlflow.register_model(
        model_uri=model_uri,
        name=REGISTERED_MODEL_NAME
    )

    # Assign candidate alias to model
    client=MlflowClient()
    client.set_registered_model_alias(
    name=REGISTERED_MODEL_NAME,
    alias=CANDIDATE_ALIAS,
    version=model_info.version
)
    print("model_uri: ", model_uri)
    print("Run_id: ", models[0].source_run_id)
    print("Registered_model_version: ",model_info.version)

def promote_model():
    mlflow.set_tracking_uri(TRACKING_URI)
    client=MlflowClient()
    
    # get candidate model
    candidate=client.get_model_version_by_alias(
        name=REGISTERED_MODEL_NAME,
        alias=CANDIDATE_ALIAS
    )

    # Promote candidate to champion
    client.set_registered_model_alias(
        name=REGISTERED_MODEL_NAME,
        alias=CHAMPION_ALIAS,
        version=candidate.version
    )

    print("Promoted model version:", candidate.version)
    print("Champion alias:", CHAMPION_ALIAS)
if __name__=="__main__":
    
    if sys.argv[1]=="register":
        register_model()

    elif sys.argv[1]=="promote":
        promote_model()
