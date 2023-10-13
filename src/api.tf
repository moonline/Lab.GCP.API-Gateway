# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/api_gateway_api
resource "google_api_gateway_api" "concerts_api" {
  provider = google-beta
  project  = var.project

  api_id       = "concerts-api-${var.environment}"
  display_name = "Concerts API ${upper(var.environment)}"

  labels = {
    application = "concerts"
    environment = var.environment
  }
}

# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/api_gateway_api_config
resource "google_api_gateway_api_config" "concerts_api_config" {
  provider = google-beta
  project  = var.project

  api           = google_api_gateway_api.concerts_api.api_id
  api_config_id = "concerts-api-config-${var.environment}"
  display_name  = "Concerts API ${upper(var.environment)} Config"

  # https://cloud.google.com/api-gateway/docs/openapi-overview
  openapi_documents {
    document {
      path = "spec.yaml"
      contents = base64encode(templatefile(
        "${path.module}/api/concerts.yaml",
        {
          concerts_api_handler_function_url = google_cloudfunctions2_function.concerts_api_handler_function.url
        }
      ))
    }
  }

  lifecycle {
    create_before_destroy = true
  }

  labels = {
    application = "concerts"
    environment = var.environment
  }
}

# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/api_gateway_gateway
resource "google_api_gateway_gateway" "concerts_api_gateway" {
  provider = google-beta
  project  = var.project

  api_config = google_api_gateway_api_config.concerts_api_config.id
  gateway_id = "concerts-api-gateway-${var.environment}"

  labels = {
    application = "concerts"
    environment = var.environment
  }
}
