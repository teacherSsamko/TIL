resource "aws_iam_account_password_policy" "strict" {
  minimum_password_length        = 8
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = false
  allow_users_to_change_password = true
}


data "aws_iam_policy_document" "ec2_instance_connect" {

  statement {
    effect    = "Allow"
    actions   = ["ec2-instance-connect:*"]
    resources = ["arn:aws:ec2:us-west-2::instance/*"]
    condition {
      test     = "StringEquals"
      values   = ["eunsub"]
      variable = "ec2:osuser"
    }
  }
  statement {
    effect    = "Allow"
    actions   = ["ec2:DescribeInstances"]
    resources = ["*"]
  }

}


data "aws_iam_policy_document" "dev_policy" {
  source_policy_documents = [
    data.aws_iam_policy_document.ec2_instance_connect.json,
  ]
}
