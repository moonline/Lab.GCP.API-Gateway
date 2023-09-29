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
gcloud services enable artifactregistry.googleapis.com cloudapis.googleapis.com cloudbuild.googleapis.com cloudfunctions.googleapis.com logging.googleapis.com monitoring.googleapis.com pubsub.googleapis.com run.googleapis.com storage-api.googleapis.com storage-component.googleapis.com storage.googleapis.com
```

```sh
cd src
```

### WIP deploy function by CLI

```sh
gcloud functions deploy "api-handler" \
--gen2 \
--runtime=python39 \
--region=europe-west3 \
--source=./functions/concerts_api_handler \
--entry-point=get_concerts \
--trigger-http \
--allow-unauthenticated
```

### Cleanup

```sh
gcloud functions delete "api-handler" --gen2 --region europe-west3
```

* Delete all the build artifacts:
  https://console.cloud.google.com/storage/browser?project=concerts-2023&prefix=&forceOnBucketsSortingFiltering=true
