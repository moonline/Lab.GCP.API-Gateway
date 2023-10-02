variable "region" {
  type        = string
  description = "Google Cloud location / region"
  default     = "europe-west3"
}

variable "environment" {
  type        = string
  description = "Environment like dev, test, prod"
  default     = "dev"
}

variable "project" {
  type        = string
  description = "GCP project"
  default     = "concerts-2023"
}
