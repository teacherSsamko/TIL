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
`kubectl get pods -o=custom-columns=NAME:.metadata.name,IP:.status.podIP,STATUS:.status.phase,NODE:.spec.nodeName`  
custom column 사용

## pod data 확인하는 방법
`kubectl get pod {pod-name} -o yaml > pod.yaml`  
pod의 세부 정보를 yaml형식으로 출력해서, pod.yaml에 저장한다.  

example of pod.yaml  
```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    cni.projectcalico.org/podIP: 172.16.103.135/32
  creationTimestamp: "2021-10-13T13:51:10Z"
  generateName: echo-hname-7894b67f-
  labels:
    app: nginx
    pod-template-hash: 7894b67f
  managedFields:
  - apiVersion: v1
    fieldsType: FieldsV1
    fieldsV1:
      f:metadata:
        f:annotations:
          .: {}
          f:cni.projectcalico.org/podIP: {}
    manager: calico
    operation: Update
    time: "2021-10-13T13:51:10Z"
  - apiVersion: v1
    fieldsType: FieldsV1
```


## Pod create
1. `kubectl run {podname} --image={image_name}`

    단일 pod 하나만 생성, 관리됨
2. `kubectl create deployment {podname} --image={image_name}`

    deployment라는 그룹내에 pod가 생성됨. podname뒤에 hashcode가 붙음.
3. `kubectl scale deployment {podname} --replicas={n}`

    replicas의 개수를 지정해줌
4. `kubectl apply`

    이미 생성된 object의 변경사항을 적용.  
    create로 생성된 경우 경고메세지가 출력되지만 정상적으로 작동됨.  
    일관성을 유지하기 위해서 변경될 가능성이 있는 경우에는 처음부터 apply로 생성하는 것이 권장됨.

# pod에 명령 전달

1. `kubectl exec -it {podname} -- {commands to execute}`

    pod에서 커맨드를 실행시키기 위한 명령어.  
    bash shell에 접속하고 싶을땐, `kubectl exec -it {podname} -- /bin/bash` 를 입력.

# delete Pod
1. `kubectl delete pod {pod_name}`

    kubectl run으로 생성된 일반 pod를 삭제하는 명령어
2. `kubectl delete deployment {pod_name}`

    deployment를 삭제하기 위한 명령어

# Objects
1. Pod
2. Namespaces
3. Volume
4. Service

# Pods 의 동작 보증
deployment에 속한 pod는 replicas에 의해 일정하게 유지됨.  
삭제해도 상태 보존을 위해 새롭게 pod를 생성

# Cordon
문제가 생길 가능성이 있는 노드를 관리하기 위한 기능. node의 현 상태를 보존하고, 추가로 pod를 배정하지 않는다.  
`kubectl cordon {node-name}`  
`kubectl uncordon {node-name}`  

# drain

