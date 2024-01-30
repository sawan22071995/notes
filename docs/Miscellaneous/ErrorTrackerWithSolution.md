# Here you will get most of the Error with solution what we faced daily day to day life as a Cloud or devOps Engineer

##### 1. Error:

*Error syncing load balancer: failed to ensure load balancer: Multiple untagged security groups found for instance
i-0580321e00235d0f9: ensure the k88 security group is tagged*

##### Explaination:

We are facing these issue normally using same VPC, secuirty group for mutiple Eks. During creating Service type `LoadBalancer` specially i.e. `creating istio-gteway-loadbalancer-service`.

##### Solution:

We need to Check and add few tags in `node security group` and `subnets`  as well

Multiple eks in same VPC

- The "shared" value allows more than one cluster to use the subnet or security group.
- The "Owned" value allows more than one cluster to use the subnet or security group.

All `subnet` must have tag if `same` subnet used in both eks worker node

```
"Key": "kubernetes.io/cluster/<Cluster-Name> ","Value": "shared"
```

All `subnet` must have tag if `different` subnet used in both eks worker node

```
"Key": "kubernetes.io/cluster/<Cluster-Name> ","Value": "owned"
```

All `secuirty group` must have tag if same `secuirty group` used in both eks worker node

```
"Key": "kubernetes.io/cluster/<Cluster-Name> ","Value": "shared"
```

All `secuirty group` must have tag if different `secuirty group` used in both eks worker node

```
"Key": "kubernetes.io/cluster/<Cluster-Name> ","Value": "owned"
```
