# Service

## ClusterIP

Default of ServiceType. Only accessible from the same cluster.

## NodePort

Expose service on a specific(fixed) port(NodePort) on each node. Accessble from outside of the cluster via \<NodeIP>:\<NodePort>

## LoadBalancer

Expose service using a load balancer of Cloud Provider.

## ExternalName

Return CNAME record with the value of it.
> Note: ExternalName need kube-dns:1.7+ or CoreDNS:1.7+
