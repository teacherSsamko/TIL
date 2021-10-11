# Pod create
1. `kubectl run {podname} --image={image_name}`

    단일 pod 하나만 생성, 관리됨
2. `kubectl create deployment {podname} --image={image_name}`

    deployment라는 그룹내에 pod가 생성됨. podname뒤에 hashcode가 붙음.