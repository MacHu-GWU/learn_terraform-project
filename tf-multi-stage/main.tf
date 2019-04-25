provider "aws" {
  region = "${var.region}"
  profile = "${var.profile}"
}

resource "aws_s3_bucket_object" "example" {
  bucket = "enquizit-skymap-explore-test"
  key = "example.txt"
  source = "example.txt"
}
