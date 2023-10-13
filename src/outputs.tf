output "concerts_api_handler_function_trigger_url" {
  value = google_cloudfunctions2_function.concerts_api_handler_function.url
}

output "concerts_api_hostname" {
  value = google_api_gateway_gateway.concerts_api_gateway.default_hostname
}
