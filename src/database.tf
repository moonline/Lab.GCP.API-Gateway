# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_database
resource "google_firestore_database" "concerts_database" {
  project = var.project

  # Currently the only name supported by firebase_admin is "(default)"
  name        = "(default)"
  location_id = var.region
  type        = "FIRESTORE_NATIVE"
}
