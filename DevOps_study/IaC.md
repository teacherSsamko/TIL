# IaC - Terraform

## To run terraform

1. `terraform init`
2. `terraform plan` show the plan what will apply to the instance
3. `terraform apply` and type `yes` for approving to perform the action
4. `terraform destroy` stop the container
5. `terraform graph` show the dependency graph(order of running)

## with AWS

1. `terraform fmt` update configurations in current directory for readability and consistency
2. `terraform validate`
3. `terraform show` see tfstate

## force-unlock

When you stuck with state lock for some reasons. you can force to unlock by `terraform force-unlock [options] LOCK_ID [DIR]`.

## TODO

[] make custom AMI -> Packer
[] make custom VPC

## Provisioning & Configuration Tools combinations

### Terraform & Ansible

Pros: masterless structure  
Cons: Ansible is precedural code. with mutable servers. maintenance will become difficult when infra gets bigger.

### Packer & Terraform

Pros: immutable infarastructure  
Cons: VMs can take a long time to build and deploy.

### Terraform & kubernetes

Pros: quick build. lots of benefits of k8s
Cons: complexity. k8s is difficult & expensive
