terraform {
  required_providers {
    render = {
      source  = "registry.terraform.io/render-oss/render"
      version = "~> 1.5.0"
    }
  }
}

provider "render" {
  api_key = var.render_api_key
}

resource "render_service" "flask_app" {
  name                = "flask-api"
  service_type        = "web_service"
  env                 = "docker"
  region              = "oregon"
  docker_image        = "ghcr.io/<YOUR_GITHUB_USERNAME>/flask_api:latest"
  auto_deploy         = true
  instance_type       = "starter"
  env_vars = {
    PORT = "5000"
  }
}
