# Concept

## EKS - Amazon Elastic Kubernetes
관리형 쿠버네티스

## Solutions
구성형 쿠버네티스
- kubeadm

## CNI - Container Network Interface

- flannel
    - L2 Network
        MAC 주소 기반 switching
- calico
    - L3 Network
        protocol 주소 기반 switching

## CoreDNS

쿠보너테스 클러스터에서 도메인 이름을 이용해 통신할 때 사용.  
[공식홈페이지](https://coredns.io)

# kubectl
`kubectl get nodes`  
node 연결상태 확인  
`kubectl get pods --all-namespaces`  
모든 namespace에서 pod 수집

## Pod create
1. `kubectl run {podname} --image={image_name}`

    단일 pod 하나만 생성, 관리됨
2. `kubectl create deployment {podname} --image={image_name}`

    deployment라는 그룹내에 pod가 생성됨. podname뒤에 hashcode가 붙음.

# Objects
1. Pod
2. Namespaces
3. Volume
4. Service