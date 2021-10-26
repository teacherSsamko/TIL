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

## Service
외부에서 쿠버네티스 클러스터에 접속하는 방법

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

    `--record` 옵션을 사용하면, 배포한 정보의 히스토리를 기록함  


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
유지보수를 위해 노드를 꺼야 하는 경우, 지정된 노드의 파드를 전부 다른 곳으로 이동시켜주는 기능  
`kubectl drain {node-name}`  
하지만 daemonset은 각 노드에 1개만 존재하는 파드여서 drain으로 삭제할 수 없습니다. 이 daemonset을 무시하려면, `--ignore-daemonsets` 옵션을 함께 사용해야 한다.  
drain이 적용된 node는 cordon을 수행했을때와 같이 'SchedulingDisabled'상태가 된다.  
보수가 끝났다면, `uncordon`으로 다시 스케쥴을 받을 수 있는 상태로 복귀시킨다.  

# rollout history
`--record` 옵션으로 기록된 히스토리를 확인 가능.  
`kubectl rollout historydeployment {pod name}`  

# set image
container의 버전을 변경할 수 있다.
`kubectl set image deployment {pod name} {image}={image}:{version}`  
예) `kubectl set image deployment ssam-nginx nginx=nginx:1.16.0`  
이렇게 하면 기존 pod들을 하나씩 지우고 변경된 이미지를 가진 파드를 새로 생성하는 방식으로 버전을 변경한다.  

# rollout status
현재 진행중인 상태 확인  
`kubectl rollout status deployment {pod name}`  

# describe
쿠버네티스 상태를 자세히 살펴볼 때 사용  
`kubectl describe deployment {pod name}`  

# rollout undo
rollout revision을 한단계 뒤로 되돌린다
`kubectl rollout undo deployemnt {pod name}`  
  
- `--to-revision` 특정 시점으로 돌아가고 싶을때 사용하는 옵션  

# serviece
`kubectl get services`  
사용중인 서비스 보기

# NodePort
NodePort를 이용해서 Service를 생성하면 외부에서 접속이 가능하다.  
이때, scale을 이용해 pod를 늘려주면 자동으로 load balancer의 역할도 수행한다.  
  
## expose
Object Spec 파일이 아닌 커맨드로 NodePort를 사용하고자 할 때 사용하는 커맨드.  
`kubectl expose deployment {pod name} --type=NodePort --name={service name} --port={port}`  
이렇게 커맨드로 NodePort를 사용할 경우에는 외부해서 접속할 Port는 선택할 수 없다. 30000~32767사이의 포트번호가 임의로 배정된다.  


# Ingress
여러 개의 deployment가 있을 때 고유한 주소를 제공해 사용 목적에 따른 다른 응답을 제공하고, 트래픽에 대한 L4/L7 로드밸런서와 보안 인증서를 처리하는 기능을 제공함

# HPA (Horizantal Pod Autoscaler)
부하량에 따라 deployment pods 수를 유동적으로 관리하는 기능

