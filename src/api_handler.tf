resource "google_storage_bucket" "deployment_bucket" {
  name                        = "${var.project}-deployment-${var.environment}"
  location                    = var.region
  uniform_bucket_level_access = true
}

resource "google_storage_bucket_object" "concerts_api_handler_source_object" {
  name   = "concerts_api_handler.zip"
  bucket = google_storage_bucket.deployment_bucket.name
  source = "./functions/concerts_api_handler.zip"
}

/**
curl -m 40 -X POST https://europe-west3-concerts-2023.cloudfunctions.net/concerts-api-handler-dev?artist=Madonna \
    -H "Authorization: bearer $(gcloud auth print-identity-token)" \
    -H "Content-Type: application/json" -d '{}'
*/
# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions2_function
resource "google_cloudfunctions2_function" "concerts_api_handler_function" {
  name        = "concerts-api-handler-${var.environment}"
  description = "Concerts API Gateway request handler function"
  location    = var.region

  build_config {
    runtime     = "python39"
    entry_point = "get_concerts"

    source {
      storage_source {
        bucket = google_storage_bucket.deployment_bucket.name
        object = google_storage_bucket_object.concerts_api_handler_source_object.name
      }
    }
  }

  service_config {
    max_instance_count = 1
    available_memory   = "128Mi"
    available_cpu = 0.083
    timeout_seconds    = 30
    # ingress_settings = "ALLOW_INTERNAL_ONLY"
    all_traffic_on_latest_revision = true

    # environment_variables = {
    #     TABLE_NAME = "TODO"
    # }
  }

  labels = {
    application = "concerts"
    environment = var.environment
  }
}
