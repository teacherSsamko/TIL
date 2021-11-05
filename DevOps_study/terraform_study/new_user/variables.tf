variable "ec2_name" {
  type = string
}

variable "username" {
    type = list
    default = ["es-a", "es-b", "es-c"]
}