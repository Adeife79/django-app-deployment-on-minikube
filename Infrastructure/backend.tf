terraform {
    backend "s3" {
        bucket = "voters-api-tf-state"
        key    = "terraform.tfstate"
        region = "eu-north-1"
    }
}