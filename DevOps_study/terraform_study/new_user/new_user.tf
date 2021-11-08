resource "aws_iam_user" "backend_dev" {
  count = length(var.username)
  name  = element(var.username, count.index)
  path  = "/dev/"
}

resource "aws_iam_access_key" "newemp" {
  count = length(var.username)
  user  = element(var.username, count.index)

  depends_on = [
    aws_iam_user.backend_dev
  ]
}

resource "aws_iam_user_group_membership" "developer" {
  count = length(var.username)
  user  = element(var.username, count.index)

  groups = [
    "developer",
  ]

  depends_on = [
    aws_iam_user.backend_dev
  ]
}
