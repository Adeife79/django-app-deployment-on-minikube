terraform {
    backend "s3" {
        bucket = "<bucket_name>"
        key    = "terraform.tfstate"
        region = "<aws_region>"
    }
}