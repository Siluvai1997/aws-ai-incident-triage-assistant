locals {
  common_tags = {
    Project = var.project_name
    Owner   = "portfolio"
    Managed = "terraform"
  }
}
