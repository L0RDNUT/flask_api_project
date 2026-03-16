output "app_url" {
  value = render_service.flask_app.service_details[0].url
}
