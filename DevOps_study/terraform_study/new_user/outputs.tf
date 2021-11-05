output "user_arn" {
    value = "${aws_iam_user.example.0.arn}"
}

output "ec2_id" {
    value = "${aws_instance.app_server.id}"
}