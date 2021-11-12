resource "aws_iam_user" "dev" {
  for_each = toset(var.dev_team)
  name     = each.key
  path     = "/dev/"
}

resource "aws_iam_access_key" "newemp" {
  for_each = toset(var.dev_team)
  user     = each.key

  depends_on = [
    aws_iam_user.dev
  ]
}

resource "aws_iam_user_group_membership" "developer" {
  for_each = toset(var.dev_team)
  user     = each.key

  groups = [
    "Dev",
  ]

  depends_on = [
    aws_iam_user.dev
  ]
}

resource "aws_iam_user_login_profile" "developer" {
  for_each = toset(var.dev_team)
  user     = each.key
  pgp_key  = "keybase:ssamko"
}
