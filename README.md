# Lab.GCP.API-Gateway

A basic API with API Gateway, Cloud Functions, Firestore and Deployment Manager


## Development

### Dependencies

1. Install latest gcloud CLI https://cloud.google.com/cli and login with `gcloud init`
2. Install Python 3.9


### Recommended Visual Studio Code plugins

* https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml
* https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one
* https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja


## Deployment

```sh
# Create a new gcloud project
gcloud projects create "concerts-2023"
gcloud config set project "concerts-2023"
# Enable services
gcloud services enable artifactregistry.googleapis.com cloudapis.googleapis.com cloudbuild.googleapis.com cloudfunctions.googleapis.com logging.googleapis.com monitoring.googleapis.com pubsub.googleapis.com run.googleapis.com storage-api.googleapis.com storage-component.googleapis.com storage.googleapis.com deploymentmanager.googleapis.com
```

```sh
# Create a deployment bucket
gcloud storage buckets create "gs://concerts-deployment" --project "concerts-2023" --location "europe-west3"
```

```sh
cd src
```

```sh
# Zip & deploy code to deployment bucket
(cd functions/concerts_api_handler; zip -FSr "../concerts_api_handler.zip" *)
gcloud storage cp "./functions/concerts_api_handler.zip" "gs://concerts-deployment/"
```

```sh
# Deploy template
gcloud deployment-manager deployments create "concerts-api-dev" --config jinja/concerts_api.yaml
# redeploy template
gcloud deployment-manager deployments update "concerts-api-dev" --config jinja/concerts_api.yaml
```


## WIP deploy function by CLI

```sh
gcloud functions deploy "api-handler" \
--gen2 \
--runtime=python39 \
--region=europe-west3 \
--source=./functions/concerts_api_handler \
--entry-point=get_concerts \
--trigger-http \
--allow-unauthenticated \
--project=concerts-2023
```

## Cleanup

```sh
# Manual deployment
gcloud functions delete "api-handler" --gen2 --region europe-west3
# Template deployment
gcloud deployment-manager deployments delete "concerts-api-dev"
```

* Delete all the build artifacts:
https://console.cloud.google.com/storage/browser?project=concerts-2023&prefix=&forceOnBucketsSortingFiltering=true
* Delete deployment bucket


## Resources

* [Create a 2nd gen Cloud Function by using the Google Cloud CLI](https://cloud.google.com/functions/docs/create-deploy-gcloud#functions_quickstart_helloworld-python)
* [Snippets: Cloudfunctions v1](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/google/resource-snippets/cloudfunctions-v1)
* [Cloud Deployment Manager: Creating a Basic Template](https://cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template#jinja_1)