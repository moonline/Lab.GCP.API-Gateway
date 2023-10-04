# https://cloud.google.com/api-gateway/docs/passing-data
# x-google-backend:
#   address: https://${var.region}-${var.project}.cloudfunctions.net/concerts_api_handler
#   address: ${concerts_api_handler_function_uri} ???

# https://registry.terraform.io/modules/GoogleCloudPlatform/cloud-functions/google/latest -> ???

# https://cloud.google.com/api-gateway/docs/get-started-cloud-functions
# https://cloud.google.com/api-gateway/docs/secure-traffic-gcloud


# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/api_gateway_api
resource "google_api_gateway_api" "concerts_api" {
  provider = google-beta
  api_id = "concerts-api-${var-environment}"
  project = var.project
  labels {
    application = "concerts"
    environment = var.environment
  }
}

# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/api_gateway_api_config
resource "google_api_gateway_api_config" "concerts_api_config" {
  provider = google-beta
  api = google_api_gateway_api.concerts_api.api_id
  api_config_id = "concerts-api-config-${var-environment}"

  openapi_documents {
    document {
      path = "spec.yaml"
       # contents = filebase64("${path.module}/api/concerts.yaml")
      contents = base64encode(templatefile(
        "${path.module}/api/concerts.yaml",
        {
          concerts_api_handler_function_uri = cloud_functions2.concerts_api_handler_function.uri
        }
      ))
    }
  }
  lifecycle {
    create_before_destroy = true
  }
  project = var.project
  labels {
    application = "concerts"
    environment = var.environment
  }
}

# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/api_gateway_gateway
resource "google_api_gateway_gateway" "concerts_api_gateway" {
  provider = google-beta
  api_config = google_api_gateway_api_config.concerts_api_config.id
  gateway_id = "concerts-api-gateway-${var-environment}"
  project = var.project
  labels {
    application = "concerts"
    environment = var.environment
  }
}
