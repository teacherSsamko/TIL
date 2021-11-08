resource "aws_iam_account_password_policy" "strict" {
  minimum_password_length        = 8
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = false
  allow_users_to_change_password = true
}

resource "aws_iam_user_policy" "newemp_policy" {
  count = length(var.username)
  name  = "es_test_policy"
  user  = element(var.username, count.index)


  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : [
          "es:Describe*"
        ],
        "Resource" : [
          "*"
        ]
      }
    ]
  })
}
