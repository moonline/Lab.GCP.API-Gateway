variable "region" {
  type        = string
  description = "Google Cloud location / region"
  # API Gateway is not supported in europe-west3
  # https://cloud.google.com/api-gateway/docs/deployment-model#choosing_a_gcp_region
  default     = "europe-west2"
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
