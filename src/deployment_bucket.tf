resource "google_storage_bucket" "deployment_bucket" {
  name                        = "${var.project}-deployment-${var.environment}"
  location                    = var.region
  uniform_bucket_level_access = true
}
