# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_database
resource "google_firestore_database" "concerts_database" {
  project     = var.project
  name        = "concerts-database"
  location_id = var.region
  type        = "FIRESTORE_NATIVE"
}

# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_field
resource "google_firestore_field" "concerts_database_artist_field" {
  project = var.project
  database = google_firestore_database.concerts_database.id
  collection = "concerts_%{random_suffix}"
  field = "artist"

  index_config {
    indexes {
        order = "ASCENDING"
        query_scope = "COLLECTION_GROUP"
    }
    indexes {
        array_config = "CONTAINS"
    }
  }

  ttl_config {}
}
