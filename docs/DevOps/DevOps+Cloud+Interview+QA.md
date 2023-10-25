# DevOps & Cloud & Python Basic & Interview & QA

##### Q. How can you access services or details with login through Azure Portal?

- By using **Microsoft Graph API **
- **Microsoft Graph** is a RESTful web API that enables you to access Microsoft Cloud service resources. After you register your app and get authentication tokens for a user or service, you can make requests to the Microsoft Graph API.
  https://learn.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http

##### Q. What is plane or data migration strategy for cloud migration?

1. Problem and requirment.
2. Check ROI(Return on Investment), CapEx and Zero Downtime.
3. Make complete stretegy and Infrastructure Plan with Cost
4. Convince the customer or client with respect to stretegy and plans.
5. Check Infrastructure pre-requisite and start migration.

##### Q. what is keywords used for exception handling?

try     : Something Thats might Cause Exception 
catch   : Do this if there was an exception 
else    : Do this if there were NO exception
finally : Do this no matter what happens

##### Q. What is *args stands for in function def sum(*args)?

Any number of Argument we can pass without any restriction.

"*" takes all arguments as tuple.

##### Q. What is **kargs stands in function def sum(**kargs)?

Any number of Argument we can pass without any restriction.

"*" takes all arguments as keywords dictionary. and order not matters in argument in **kwargs.

##### Q. What is list comprehension?

```
1. Copy listA to listB with adding 1 in each item
-----------------------
Normal Solution
-----------------------
listA = [ 1, 2, 3]
listB = []
for n in listA:
    add_1 = n + 1
    listB.append(add_1)
-----------------------
By List Comprehension
-----------------------
listB = [ n + 1 for n in listA ]
----------------------------------
List Comprehension with condition
----------------------------------
l1 = ['sawan' , 'muskan', 'srajan', 'vasu' ]
l2 = [name.upper() for name in l1 if len(name) > 5 ]
```

##### Q. Leap years condition check?

1. It must be divisible by 4.
2. It shouldn't divisible by 100.
3. It must be divisible by 400.

##### Q. can you define block scope in python?

Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.

##### Q. Output of the code print(734_529.678)?

734529.678

##### Q. what is availability zone in Azure?

Azure availability zones are physically and logically separated datacenters.
their have own independent power source, network, and cooling. 
Connected with an extremely low-latency network, they become a building block to delivering high availability applications.

##### Q. what is availability set and how to achieve it in Azure?

- Availability Sets takes the virtual machine and configures multiple copies of it. 
- Each copy is isolated within a separate physical server, compute rack, storage units and network switches within one datacentre within an Azure Region.
- Availability Sets only apply to virtual machines
- In the Azure Service Management (ASM) portal, we have two Fault domains and 5 update domains.
- In the Azure Resource Manager(ARM) portal, we have 3 Fault domains and 5 update domains but we can upgrade our update domains from 5 to 20.

##### Q. docker exec default directory when login inside container?

```
/       - root directory
/workdir- defined in dockerfile
```

##### Q. docker exec inside conatiner with other user?

```
docker exec -it --user sawan <container_name_or_id> /bin/bash
```

##### Q. docker exec inside container with specific directory?

```
docker exec -w /path/to/directory <container_name_or_id> /bin/bash
```

##### Q. what is workflow for 'kubectl get pod' command?

```
kubectl-->kubeconfig-->kubeApiServer-->ETCD
```

##### Q. How communication happended inside the docker between conatiner?

Docker creates a virtual network called bridge by default, and connects your containers to it.

##### Q. How to find the IP of docker conatiner?

```
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
```

##### Q. What is the difference between replicaset and daemonset?

- ReplicaSets should be used when your application is completely decoupled from the node and you can run multiple copies on a given node without special consideration. 
- DaemonSets should be used when a single copy of your application must run on all or a subset of the nodes in the cluster.

##### Q. How many types of volume in docker?

1. **Host volumes** : A host volume can be accessed from within a Docker container and is stored on the host, as per the name. To create a host volume.
   docker run -v /path/on/host:/path/in/container
   Pros:
   Offers direct access to the file system of the host machine.
   Can be used to share data between the host and the container.
   Allows for easy debugging of container applications.
   Cons:
   The volume’s data can be modified or deleted accidentally by the host or another container.
   Can have compatibility issues with different host systems.

2. **Anonymous volumes** : The location of anonymous volumes is managed by Docker. Note that it can be difficult to refer to the same volume when it is anonymous.
   docker run -v /path/in/container ...
   Pros:
   Easier to use since Docker handles their creation.
   Automatically deleted when the container is removed.
   Provides a level of isolation between the container and the host machine.
   Cons:
   Cannot be shared between containers.
   Cannot be backed up or restored.
   Difficult to manage and track.

3. **Named volumes** and anonymous volumes are similar because Docker manages where they are located. However, named volumes can be referred to by name.
   docker volume create somevolumename
   docker run -v somevolumefileName:/path/in/container
   Pros:
   Easier to manage and share between containers.
   Provides a clear separation of concerns between the container and the storage.
   Can be backed up, restored, and migrated
   Cons:
   Requires creating the volume ahead of time.

##### Q. Difference between --mount vs --volume in docker?

```
-v or --volume: Consists of three fields, separated by colon characters (:). The fields must be in the correct order, and the meaning of each field is not immediately obvious.
--volume $(pwd):/backup/user:rw

--mount: Consists of multiple key-value pairs, separated by commas and each consisting of a <key>=<value> tuple with verbose.
--mount 'type=volume,src=<VOLUME-NAME>,dst=<CONTAINER-PATH>,volume-driver=local,volume-opt=type=nfs'
```

##### Q. How to get list of volume in docker?

```
docker volume ls
output:
    local               my-vol
```

##### Q. Get details of attached volume?

```
docker volume inspect my-vol
output:
[
    {
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/my-vol/_data",
        "Name": "my-vol",
        "Options": {},
        "Scope": "local"
    }
]
```

##### Q. reverse string in Python?

```
#By slicing the string
txt = "Hello World"[::-1]
print(txt)
---
#by for loop because charcter arrange in revrse order [right<--left]
def reverse(s):
    str = ""
    for i in s:
        print("i :", i)
        str = i + str
        print("str :", str)
    return str

s = "Comapany"
print(reverse(s))
```

##### Q. What is the default Code Coverage Percentage defined in Default SonarCloud Quality Gate?

80%

##### Q. What is Branching stretegies in GIT?

Main <-- Hotfix <-- Release <-- Development <-- Feature1,Feature2
The overall flow of Gitflow is:

- A develop branch is created from main
- A release branch is created from develop
- Feature branches are created from develop
- When a feature is complete it is merged into the develop branch
- When the release branch is done it is merged into develop and main
- If an issue in main is detected a hotfix branch is created from main
  Once the hotfix is complete it is merged to both develop and main
  https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

##### Q. what is sidecar container in AKS?

- A sidecar is just a container that runs on the same Pod as the application container. It shares the same volume and network as the main container, it can “help” or enhance how the application operates.
- A Sidecar container is a second container to add the pod. Why sidecar container added to the pod or main container? because it needs to use the same resources that use by the main container.
- A sidecar is independent from its primary application in terms of runtime environment and programming language, so you don't need to develop one sidecar per language. The sidecar can access the same resources as the primary application.

##### Q. Create Azure front door with + WAF policy?

- Create azure fornt door.
- Create WAF policy by defining some rules, custom policy(deny traffic from Country by [ Geo Location ]and associate at Front Door created earlier.
- Go to front door and check WAF section it will be associated.

##### Q. diffrence between Traffic manager and Front Door?

- **Traffic Manager** — Any protocol: Because Traffic Manager works at the DNS layer, you can route any type of network traffic; HTTP, TCP, UDP, etc.
  On-premises routing : With routing at a DNS layer, traffic always goes from point to point. Routing from your branch office to your on premises datacenter can take a direct path; even on your own network using Traffic Manager.

- **Front Door** — With Front Door traffic is proxied at the Edge of Microsoft’s network. Because of this, HTTP(S) requests see latency and throughput improvements reducing latency for SSL negotiation and using hot connections from AFD to your application.
  Independent scalability: Because Front Door works with the HTTP request, requests to different URL paths can be routed to different backend / regional service pools (microservices) based on rules and the health of each application microservice.

##### Q. How to know who commit the code with 1000 line with author in file?

The **git blame** command is used to examine the contents of a file line by line and see when each line was last modified and who the author of the modifications was.

##### Q. How to upgrade and renew ssl certificate in Azure Application Gateway?

- To renew a listener certificate from the portal, navigate to your application gateway listeners. 
- Select the listener that has a certificate that needs to be renewed.
- select Renew or edit selected certificate. Upload your new PFX certificate, give it a name, type the password, and then select Save.

##### Q. Types of Subnet ?

- Public  - Instances can directly access the internet. Through Public IP access.

- Private - Instances can access the Internet with NAT (Network Address Translation) gateway that is present in the public subnet.

##### Q. Nested list sorting in python?

```
lst = [['1', 'A', 2, 5, 7],['2', 'B', 8, 15, 65,],['3', 'C', 32, 35, 25],['4', 'D', 82, 305],['5', 'E', 39, 43, 89, 55]]
lst = sorted(lst, key=lambda x: x[2], reverse=True)
print(lst)
```

##### Q. Pass mutiple docker file in build docker images?

```
docker build -f wildfly.Dockerfile ./wildfly
docker build -f mysql.Dockerfile ./mysql
docker build -f other.Dockerfile ./other
```

##### Q. How many types of Deployment Model in AKS?

- **Recreate Deployment**
  A recreate deployment strategy is an all-or-nothing process that lets you update an application immediately, with some downtime. 

        Downside downtime of Environment as well as complete delete the old version. Can't rollback until you don't have Previous version backup.

- **Rolling Deployment**
  Rolling deployment is a deployment strategy that updates a running instance of an application to a new version. All nodes in the target environment are incrementally updated to a new version; the update occurs in pre-specified batches. This means rolling deployments requires two versions of a Service—one for the old version and another for the new version of the application

        The downsides are that it can be slow, and there is no easy way to roll back to the previous version if something goes wrong. 

- **Blue/Green Deployment (Red/Black Deployment)**
  A blue/green (or red/black) deployment strategy enables you to deploy a new version while avoiding downtime. Blue represents the current version of the application, while green represents the new version. 

        Downside are the strategy requires double resources for both deployments and can incur high costs. Furthermore, it requires a way to switch over traffic rapidly from blue to green version and back.

- **Canary Deployment**
  A canary deployment strategy enables you to test a new application version on a real user base without committing to a full rollout. It involves using a progressive delivery model that initiates a phased deployment. Canary deployment strategies encompass various deployment types, including A/B testing and dark launches.

        there are two downside are the application needs to be able to run multiple versions at the same time, and you need to have a smart traffic mechanism that can route a subset of requests to the new version.

- **Shadow Deployment**
  Shadow deployments are another type of canary deployments where you test a new release on production workloads. A shadow deployment splits traffic between a current and a new version, without end users noticing the difference. When the stability and performance of the new version meets predefined requirements, operators trigger a full rollout

       The downside is that shadow deployments are complex to manage and require twice the resources to run compared to a standard deployment.

##### Q. print a line conatining "sawan" in file.txt

```
grep -n "sawan" file.txt
```

##### Q. How to Upgrade Kubernetes Cluster Zero Downtime?

```
https://platform9.com/blog/kubernetes-upgrade-the-definitive-guide-to-do-it-yourself/
- Login into the first node and upgrade the kubeadm tool only
The reason why we run apt-mark unhold and apt-mark hold is because if we upgrade kubeadm then the installation will automatically upgrade the other components like kubelet to the latest version (which is v1.15) by default, so we would have a problem. To fix that, we use hold to mark a package as held back, which will prevent the package from being automatically installed, upgraded, or removed.
> ssh admin@10.0.11.1
> apt-mark unhold kubeadm && \
> apt-get update && apt-get install -y kubeadm=1.13.0-00 && apt-mark hold kubeadm

- Verify the upgrade plan
COMPONENT            CURRENT AVAILABLE
API Server           v1.13.0 v1.14.0
Controller Manager   v1.13.0 v1.14.0
Scheduler            v1.13.0 v1.14.0
Kube Proxy           v1.13.0 v1.14.0
> kubeadm upgrade plan

- Apply the upgrade plan
> kubeadm upgrade plan apply v1.14.0

- Update Kubelet and restart the service
> apt-mark unhold kubelet && apt-get update && apt-get install -y kubelet=1.14.0-00 && apt-mark hold kubelet
> systemctl restart kubelet

- Apply the upgrade plan to the other master nodes
> ssh admin@10.0.11.2
> kubeadm upgrade node experimental-control-plane
> ssh admin@10.0.11.3
> kubeadm upgrade node experimental-control-plane

- Upgrade kubectl on all master nodes
> apt-mark unhold kubectl && apt-get update && apt-get install -y kubectl=1.14.0-00 && apt-mark hold kubectl

- Upgrade kubeadm on first worker node
> ssh worker@10.0.12.1
> apt-mark unhold kubeadm && apt-get update && apt-get install -y kubeadm=1.14.0-00 && apt-mark hold kubeadm

- Login to a master node and drain first worker node
> ssh admin@10.0.11.1
> kubectl drain worker --ignore-daemonsets

- Upgrade kubelet config on worker node
> ssh worker@10.0.12.1
> kubeadm upgrade node config --kubelet-version v1.14.0

- Upgrade kubelet on worker node and restart the service
> apt-mark unhold kubelet && apt-get update && apt-get install -y kubelet=1.14.0-00 && apt-mark hold kubelet
> systemctl restart kubelet

- Restore worker node
> ssh admin@10.0.11.1
> kubectl uncordon worker
Step 12: Repeat steps 7-11 for the rest of the worker nodes.
Step 13: Verify the health of the cluster:
> kubectl get nodes

#Migration With Node Pools
- Create all required Node pool with new version and migrate all workload one by one in new node pools.
- Cordon all old node it will prevent from scheduling new pod in old node.
kubectl cordon <node-name>
- Drain each node it will help to delete all existing pod in node and schedule in new node.
kubectl drain node <node-name> --force 
- Delete the old node After successfull rollout migration of all workload. 
```

##### Q. How to upgrade Azure Kubernates Services with zero downtime process?

```
-----------------------
Pre-Upgrading Planning
-----------------------
1. Standalone Pod
Identify the standalone pods and plan the downtime for those.

2. Setup Pod Disruption Budget
If the drain operation fails, the upgrade operation will fail by design to ensure that the application are not disrupted.

3. Customize node surge upgrade
The max surge value may be customized per node pool to enable a trade-off between upgrade speed and upgrade disruption. 
By increasing the max-surge value the upgrade process completes faster, but setting large value for max surge may cause disruption during the upgrade process.
----------------------------------------------------------------
AKS Upgrading Process ( [NODE] ~ [SURGE] + [CORDON] + [DRAIN] )
----------------------------------------------------------------
Control Plane = Control Manager + ETCD + API Server + Scheduler
Node Pool(VM) = Containerd + Kubelet + Pods + OS
- Get the current version and latest version
az aks get-upgrade --resource-group rg1 --name aks1
- Get the running Pod and PDB policy and deployment
- Update the node pool with node surge
az aks nodepool update -n NodePoolName -g rg1 -n aks1 --max-surge 50% (out of 5 total node 50% will be 2 node evicted together)
- Perform the upgrade cluster operation
az aks upgrade -r rg1 -n aks1 --kubernetes-version 1.22.4
- Provide the input as requested
are you sure you want to perform this operation?(y/N): y
- We can define the control plane argument seprately or upgrade all master(control plane) and worker(node pool) to upgrade
Since control-plane-only argument is not specified, this will upgrade the control plane AND all nodepool to version 1.22.4. Continues (y/N): y
- check the upgrade process by events
kubectl get events
Remark : Upgrading Control Plane alone doesn't impact anything on application level.
```

##### Q. what is PDB(Pod disruption Budget)?

```
PDB policy is help to run minimum pod must be running for application.Even if some volutry disruption happened i.e. Draining node for repair or upgrade.
PDB always make sure minimum number of pod must be run for a application anyhow.
---
api/version: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: pdbName
spec:
    minAvailable: 2
    selector:
        matchLabels:
            run: nginx
---
```

##### Q. Difference between PDB and Replica?

- PodDisruptionBudget with minAvailable are useful in such scenarios to achieve zero downtime. Replicaset will only ensure that the replicas number of pods will be created on other nodes during the process.

- If you just have a Replicaset with one replica and no PodDisruptionBudget specified, the pod will be terminated and a new pod will be created on other nodes. This is where PDBs provide the added advantage over the Replicaset.

##### Q. Is it possible to schedule pod in taint node?

- When we places a taint on node node1. The taint has key key1, value value1, and taint effect NoSchedule. 
- This means that no pod will be able to schedule onto node1 unless it has a matching toleration.
- Tolerations allow the scheduler to schedule pods with matching taints. Tolerations allow scheduling but don't guarantee scheduling: the scheduler also evaluates other parameters as part of its function.

##### Q. What is availability set fault domain and update domain?

```
FD-1        |          FD-2         |         FD-3
--------------------------------------------------------
VM1         |          VM2          |         VM3
UD-1        |          UD-2         |         UD-3
--------------------------------------------------------
VM4         |          VM5          |         VM6
UD-4        |          UD-5         |         UD-6
--------------------------------------------------------
```

##### Q. Autoscaling in Cloud services type and what?

- **Horizontal scaling** means scaling by adding more machines to your pool of resources (also described as “scaling out”), 
- **vertical scaling** refers to scaling by adding more power (e.g. CPU, RAM) to an existing machine (also described as “scaling up”).

##### Q. Process to follow Azure DevOps migration from one tenant to another tenant?

- Prepare the users in the new tenant
- Change the AAD connection for DevOps (https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/change-azure-ad-connection?vie...)
- UserMapping after migration in DevOps
- Document all RBAC, Roles, ecc. as described here: https://learn.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription
- Migration of the subscription to the new tenant
- Restore RBAC, KeyVault, StorageAccount accesses in the new tenant
- Re-create all ServicePrincipals in DevOps and adjust the pipelines

##### Q. Change your organization connection to a different Azure AD?

[Switch to another Azure Active Directory - Azure DevOps Services | Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/change-azure-ad-connection?view=azure-devops)

##### Q. What is Azure Service connection?

**Service Connection** represent a Service Principal in Azure AD. An identity which uses Headless authentication. Since it's represent a Azure AD service principal, Yes you could obtain an access token using that

##### Q. what is azure hybrid benefits?

**Azure Hybrid Benefit** is a licensing offer that helps you migrate and save to Azure. 
To apply this benefit you must be paying for either:
Windows Server or SQL Server core licences with Software Assurance or a subscription to these products.
An active Linux subscription, including Red Hat Enterprise Linux or SUSE Linux Enterprise Server running in Azure.

1. **cost savings**
2. **modernise and**
3. **maintain a flexible hybrid environment while optimising business applications.**

##### Q. Terraform remote backend create dynamically to store .tfstate file?

- No, Its not possible to configure it first you need to create remote backened with local .tfstate file.
- you can then do "terraform state push" and it will push the backup to the remote.

##### Q. Terraform .tfststate restore?

To do that, you restore the last working state backup file you had before you ran into this issue. If you have frequent state backups in place, you can sort by the date and time before you ran into the issue.

you can then do "terraform state push" and it will push the backup to the remote.

LOCALLY:
if you're running Terraform locally, a terraform.tfstate.backup file is generated before a new state file is created. You can use that as your new state file and see if that works for you.
To make an old backup state file your new one, all you need do is to move your current one to a different (safe) folder/directory (in case anything goes wrong), then rename the backup file as your new terraform.tfstate file, and run terraform plan again.

REMARK :
your old state file might be a couple of versions behind your current infra setup so you might need to recreate or re-import the additional resources/config.

##### Q. Terraform .tfstate delete So, what happened with resources if you re-apply?

It will give error resource already exist. 

1. We will re-apply the "terraform apply" command.
2. then we can use "terraform import" to all resource already exist error.

##### Q. sgid, sgid, stickbit, acl and special group permission command?

```
The red highlighted area indicate that the file is possessed with suid.
---(user)---(Group)---(others) : rwxrwxrwx
SUID - means set user ID.
SUID - Run programs as owner of the file.
SUID - have a value of 4 or use u+s.
SUID - chmod 4775 um.sh  | chmod +s um.sh 

SGID - means set group ID.
SGID - Assign authority to run programs as owner of file.Inherit group ownership of all the item created beneath that directory
SGID - has value of 2 or use g+s. 
SGID - chown 2775 /data | chown g+s /data

Sticky Bit - Only owner of the file can delete the file e.g. /tmp
Sticky Bit - has a value of 1 or use +t to apply the value.
Sticky Bit - chmod 1775 /tmp | chmod +t /example

ACL - Access control list(ACL) is used to give permissions to more then one user or group on a directory, using acl you can give less permission to one group for a file and more permission to anther file for the same file.
#Command to check ACL permission
getfacl
#Command to set ACL permission
setfacl -R -m d:g:marketing:rw acl/
-R for recursive option
-m to modify default permissions
-g for group i.e marketing
-d we need to define default acl
-rw to read write permission
acl/ directory name
setfacl -R -m user:geeko:rwx,group:mascots:rwx mydir/
```

##### Q. what is ansible ad-hoc commands?

Command used in ansible without playbook is called ad-hoc command.

##### Q. What is Dynamic Block in Terraform?

```
- You can dynamically construct repeatable nested block like setting using a specific dynamic block type , which is supported inside resources, data, providors and provisioner block.
local {
    ports = [22,80,8080,8081]
}

dynamic "security_rule"{
    for_each = local.port
    content{
    name                   = "Inbound-rule-${security_rule.key}"   //0,1,2,3         - keyIndexForEachLoop
    priority               = sum([100, security_rule.key])         //100,101,102,103 - 100 + KeyIndexForEachLoop
    source_port_range      = security_rule.value                   //22,80,8080,8081 - ValueForEachLoop
    destination_port_range = security_rule.value                   //22,80,8080.8081 - ValueForEachLoop
    }
}
```

##### Q. deploy conatiner on the basis of specific label-defined or not in AKS?

```
https://kubernetes.io/blog/2019/08/06/opa-gatekeeper-policy-and-governance-for-kubernetes/
Azure & Kubernates Policy definition Kubernetes cluster pods should use specified labels.
{
  "displayName": "Kubernetes cluster pods should use specified labels",
  "policyType": "BuiltIn",
  "mode": "Microsoft.Kubernetes.Data",
  "description": "Use specified labels to identify the pods in a Kubernetes cluster. This policy is generally available for Kubernetes Service (AKS), and preview for Azure Arc enabled Kubernetes. For more information, see https://aka.ms/kubepolicydoc.",
  "metadata": {
    "version": "7.0.1",
    "category": "Kubernetes"
  },
  "parameters": {
    "effect": {
      "type": "String",
      "metadata": {
        "displayName": "Effect",
        "description": "'Audit' allows a non-compliant resource to be created, but flags it as non-compliant. 'Deny' blocks the resource creation. 'Disable' turns off the policy.",
        "portalReview": true
      },
      "allowedValues": [
        "audit",
        "Audit",
        "deny",
        "Deny",
        "disabled",
        "Disabled"
      ],
      "defaultValue": "Deny"
    },
    "excludedNamespaces": {
      "type": "Array",
      "metadata": {
        "displayName": "Namespace exclusions",
        "description": "List of Kubernetes namespaces to exclude from policy evaluation. System namespaces \"kube-system\", \"gatekeeper-system\" and \"azure-arc\" are always excluded by design."
      },
      "defaultValue": [
        "kube-system",
        "gatekeeper-system",
        "azure-arc"
      ]
    },
    "namespaces": {
      "type": "Array",
      "metadata": {
        "displayName": "Namespace inclusions",
        "description": "List of Kubernetes namespaces to only include in policy evaluation. An empty list means the policy is applied to all resources in all namespaces."
      },
      "defaultValue": []
    },
    "labelSelector": {
      "type": "Object",
      "metadata": {
        "displayName": "Kubernetes label selector",
        "description": "Label query to select Kubernetes resources for policy evaluation. An empty label selector matches all Kubernetes resources."
      },
      "defaultValue": {}
    },
    "labelsList": {
      "type": "Array",
      "metadata": {
        "displayName": "List of labels",
        "description": "The list of labels to be specified on Pods in a Kubernetes cluster.",
        "portalReview": true
      }
    }
  },
  "policyRule": {
    "if": {
      "field": "type",
      "in": [
        "Microsoft.Kubernetes/connectedClusters",
        "Microsoft.ContainerService/managedClusters"
      ]
    },
    "then": {
      "effect": "[parameters('effect')]",
      "details": {
        "templateInfo": {
          "sourceType": "PublicURL",
          "url": "https://store.policy.core.windows.net/kubernetes/pod-enforce-labels/v1/template.yaml"
        },
        "apiGroups": [
          ""
        ],
        "kinds": [
          "Pod"
        ],
        "excludedNamespaces": "[parameters('excludedNamespaces')]",
        "namespaces": "[parameters('namespaces')]",
        "labelSelector": "[parameters('labelSelector')]",
        "values": {
          "labels": "[parameters('labelsList')]"
        }
      }
    }
  }
}
```

##### Q. What is managed identities used in Application gateway to communicate with Azure Key Vault?

User Assigned Identity

##### Q. Kubernates solution for PVC autogrow?

```
# Method - 1 
kubernates version >=1.11
- Make sure the storageClass used by the PVC (gp2 in this case) has allowVolumeExpansion set to true

- Any PVC created from this StorageClass can be edited to request more space. Kubernetes will interpret a change to the storage field as a request for more space, and will trigger an automatic volume resizing.
---------------------------------------------------------
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
  name: gp2
parameters:
  fsType: ext4
  type: gp2
provisioner: kubernetes.io/aws-ebs
reclaimPolicy: Delete
volumeBindingMode: Immediate
-----------------------------------------------------------
- We need to edit PVC and resize it and recreate application and StatefulSet.

# Method - II
Using Autopilot to Autogrow PVCs
An AutopilotRule that has 4 main parts:
- PVC Selector : Matches labels on the PVCs.
- Namespace Selector : Matches labels on the Kubernetes namespaces the rule should monitor. This is optional, and the default is all namespaces.
- Metric conditions : on the PVC to monitor.
- PVC resize action : to perform once the metric conditions are met.
--------------------
postgres-sc.yaml
--------------------
##### Portworx storage class
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: postgres-pgbench-sc
provisioner: kubernetes.io/portworx-volume
parameters:
  repl: "2"
allowVolumeExpansion: true
------------------------
postgres-pv.yaml
------------------------
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: pgbench-data
  labels:
    app: postgres
spec:
  storageClassName: postgres-pgbench-sc
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: pgbench-state
spec:
  storageClassName: postgres-pgbench-sc
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
--------------------------
Postgres-app.yaml
--------------------------
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pgbench
  labels:
    app: pgbench
spec:
  selector:
    matchLabels:
      app: pgbench
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  replicas: 1
  template:
    metadata:
      labels:
        app: pgbench
    spec:
      schedulerName: stork
      containers:
        - image: postgres:9.5
          name: postgres
          ports:
          - containerPort: 5432
          env:
          - name: POSTGRES_USER
            value: pgbench
          - name: POSTGRES_PASSWORD
            value: superpostgres
          - name: PGBENCH_PASSWORD
            value: superpostgres
          - name: PGDATA
            value: /var/lib/postgresql/data/pgdata
          volumeMounts:
          - mountPath: /var/lib/postgresql/data
            name: pgbenchdb
        - name: pgbench
          image: portworx/torpedo-pgbench:latest
          imagePullPolicy: "Always"
          env:
            - name: PG_HOST
              value: 127.0.0.1
            - name: PG_USER
              value: pgbench
            - name: SIZE
              value: "70"
          volumeMounts:
          - mountPath: /var/lib/postgresql/data
            name: pgbenchdb
          - mountPath: /pgbench
            name: pgbenchstate
      volumes:
      - name: pgbenchdb
        persistentVolumeClaim:
          claimName: pgbench-data
      - name: pgbenchstate
        persistentVolumeClaim:
          claimName: pgbench-state
--------------------------------
postgres-autopilotRule.yaml
--------------------------------
apiVersion: autopilot.libopenstorage.org/v1alpha1
kind: AutopilotRule
metadata:
  name: volume-resize
spec:
  ##### selector filters the objects affected by this rule given labels
  selector:
    matchLabels:
      app: postgres
  ##### namespaceSelector selects the namespaces of the objects affected by this rule
  namespaceSelector:
    matchLabels:
      type: db
  ##### conditions are the symptoms to evaluate. All conditions are AND'ed
  conditions:
    # volume usage should be less than 50%
    expressions:
    - key: "100 * (px_volume_usage_bytes / px_volume_capacity_bytes)"
      operator: Gt
      values:
        - "50"
  ##### action to perform when condition is true
  actions:
  - name: openstorage.io.action.volume/resize
    params:
      # resize volume by scalepercentage of current size
      scalepercentage: "100"
      # volume capacity should not exceed 400GiB
      maxsize: "400Gi"
---------------------------------------------------------
#command apply order
kuberctl apply -f postgres-autopilotRule.yaml 
kubectl apply -f postgres-sc.yaml
kubectl apply -f postgres-vol.yaml
kubectl apply -f postgres-app.yaml
---------------------------------------------------------
```

##### Q. Storage account access disabled at networking level? How to access it without any chnages in storage account with contributors role?

- Add 'My Cleint Ip Address' in Firewall networking rule to access container.

If the public network access to your Azure storage account has been disabled and you have only the Contributor role on the subscription, you may not be able to access the storage account blobs directly.

However, you can still access the blobs by using Azure virtual network service endpoints, which allow you to limit network access to your storage account to only specific subnets in a virtual network. This will enable you to access the storage account and its blobs while keeping the public network access disabled.

Here's how you can configure virtual network service endpoints for your storage account:

- Go to the Azure portal and navigate to the storage account that you want to configure.
- In the storage account, click on "Service Endpoints" in the left-side menu.
- Click on the "+ Add" button to add a new service endpoint.
- Select "Microsoft.Storage" as the service, and select the virtual network that you want to use.
- Select the subnet that you want to use for the endpoint, and click on the "Add" button.

Once you have created the virtual network service endpoint, you can access the storage account and its blobs from the virtual network. You will need to follow the steps outlined in my previous answer to access the blobs, depending on the method that you choose.

##### Q. what is CI-CD?

**Continuous integration (CI)** is the process of automatically integrating code changes from multiple developers into a shared repository. Automated tests are utilized to verify and affirm the additional codes generate no conflict with the existing codebase. Ideally, code changes should be merged multiple times a day, at every commit, with the help of CI tools.

**Continuous delivery (CD)**, together with CI makes a complete flow for deliverable code packages. In this phase, automated building tools are applied to compile artifacts (e.g., source code, test scripts, configuration files, and environments) and have them ready to be delivered to the end user. With that in mind, in a CD environment, new releases are just one click away from being published with fully functional features and minimal human intervention

Continuous deployment takes CD to the next level by having new changes in code integrated and delivered automatically into the release branch.

##### Q. what is DevOps?

In general, DevOps is the gray area between development (Dev) and operations (Ops) teams in a product development process. DevOps is a culture in which communication, integration, and collaboration in the product development cycle are emphasized. Thus, it eliminates the silos between software development and operations teams, allowing them to focus on rapid and continuous product deployment.

##### Q. What is kubernates architecture?

Kubernetes follows a client-server architecture. It’s possible to have a multi-master setup (for high availability), but by default there is a single master server which acts as a controlling node and point of contact. The master server consists of various components including a kube-apiserver, an etcd storage, a kube-controller-manager, a cloud-controller-manager, a kube-scheduler, and a DNS server for Kubernetes services. Node components include kubelet and kube-proxy on top of Docker.

##### Q. what is terraform lifecycle?

```
Lifecycle arguments help control the flow of your Terraform operations by creating custom rules for resource creation and destruction. Instead of Terraform managing operations in the built-in dependency graph, lifecycle arguments help minimize potential downtime based on your resource needs as well as protect specific resources from changing or impacting infrastructure.

#Prevent resource deletion
To prevent destroy operations for specific resources, you can add the prevent_destroy attribute to your resource definition. This lifecycle option prevents Terraform from accidentally removing critical resources.
--------------------------------------------------------------------
resource "aws_instance" "example" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.sg_web.id]
  user_data              = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y apache2
              sed -i -e 's/80/8080/' /etc/apache2/ports.conf
              echo "Hello World" > /var/www/html/index.html
              systemctl restart apache2
              EOF
  tags = {
    Name          = "terraform-learn-state-ec2"
    drift_example = "v1"
  }

+ lifecycle {
+   prevent_destroy = true
+ }
}
----------------------------------------------------------------------

#Create resources before they are destroyed
For changes that may cause downtime but must happen, use the create_before_destroy attribute to create your new resource before destroying the old resource.
----------------------------------------------------------------------
resource "aws_instance" "example" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.sg_web.id]
  user_data              = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y apache2
-             sed -i -e 's/80/8080/' /etc/apache2/ports.conf
              echo "Hello World" > /var/www/html/index.html
              systemctl restart apache2
              EOF
  tags = {
    Name          = "terraform-learn-state-ec2"
    Drift_example = "v1"

  }

  lifecycle {
-   prevent_destroy = true
+   create_before_destroy = true
  }
}
------------------------------------------------------------------------

#Ignore changes
For changes outside the Terraform workflow that should not impact Terraform operations, use the ignore_changes argument.
------------------------------------------------------------------------
resource "aws_instance" "example" {
##...
  lifecycle {
    create_before_destroy = true
+   ignore_changes        = [tags]
  }
}
-------------------------------------------------------------------------

#Custom Condition Checks
You can add precondition and postcondition blocks with a lifecycle block to specify assumptions and guarantees about how resources and data sources operate. The following examples creates a precondition that checks whether the AMI is properly configured.
-------------------------------------------------------------------------
resource "aws_instance" "example" {
  instance_type = "t2.micro"
  ami           = "ami-abc123"

  lifecycle {
    # The AMI ID must refer to an AMI that contains an operating system
    # for the `x86_64` architecture.
    precondition {
      condition     = data.aws_ami.example.architecture == "x86_64"
      error_message = "The selected AMI must be for the x86_64 architecture."
    }
  }
}
--------------------------------------------------------------------------
```

##### Q. what is jenkins?

- Jenkins is an open source continuous integration (CI) server written in Java that can be self-hosted to automate the build cycle of any project. - - Jenkins provides CI services for a software project, which can be started via command line or web application server.
- Jenkins is open-source (free) and has a large community
- There are many plugins available that make Jenkins easier to use
- Jenkins is written in Java, which means it is portable
- Developers can spend more time elsewhere: Most of the integration and testing is managed by an automated build and testing system.
- Speeds up development: Most of the integration work is done automatically, which results in fewer integration issues. In the long run, this saves both time and money over the lifespan of the project.
- Higher quality software: Issues are detected early and resolved almost right away. This keeps the software in a state where it can be released at any time safely

##### Q. what are the plugin in jenkins?

Plugins are the primary means of enhancing the functionality of a Jenkins environment to suit organization- or user-specific needs.

##### Q. how to connect jenkins with azure cloud without using any user credentials?

with the help or system managed identity.System managed identity exist till resource exist.

##### Q. How to add exciting Resources from cloud to terraform file?

```
This example will import an AWS instance into the aws_instance resource named foo:
terraform import aws_instance.foo i-abcd1234

The example below will import an AWS instance into the aws_instance resource named bar into a module named foo:
terraform import module.foo.aws_instance.bar i-abcd1234
```

##### Q. what is terraform state file?

Terraform stores information about your infrastructure in a state file. This state file keeps track of resources created by your configuration and maps them to real-world resources.

##### Q. what are places we can store terraform state file?

The state file is commonly stored either on a local machine, in a remote storage location (like a storage account in Azure, or S3 bucket in AWS), or in Terraform cloud.
By default, it is stored on the local machine and is named “terraform.tfstate”.

##### Q. what is gitlab runner?

GitLab Runner is an application that works with GitLab CI/CD to run jobs in a pipeline.

##### Q. what is command to delete and apply specific resource in terraform ?

```
terraform destroy -target=resource_type.resource_name
terraform apply -target=resource_type.resource_name
```

##### Q. How many types of docker network in docker?

There are three common Docker network types  

1. **bridge networks** - used within a single host, 
2. **overlay networks** - for multi-host communication, 
3. **macvlan networks** - which are used to connect Docker containers directly to host network interfaces.

##### Q. what is default network in docker?

**Bridge** is the default network driver. If you don't specify a driver, this is the type of network you are creating. Bridge networks are usually used when your applications run in standalone containers that need to communicate.

##### Q. How to control communication between pods in kubernates?

```
with the help of defined network policy
---------------------------------------------------------------------
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
---------------------------------------------------------------------
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: simple-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: target-app-who-is-applied-the-policy
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - ipBlock:
        cidr: 172.17.0.0/16
    - namespaceSelector:
        matchLabels:
          name: namespace-that-can-talk-to-my-app
    - podSelector:
        matchLabels:
          app: pod-that-can-talk-to-my-app
    ports:
    - protocol: TCP
      port: 6379
  egress:
  - to:
    - ipBlock:
        cidr: 10.0.0.0/24
    - namespaceSelector:
        matchLabels:
          name: namespace-my-app-can-talk-to
    - podSelector:
        matchLabels:
          app: pod-my-app-can-talk-to
    ports:
    - protocol: TCP
      port: 5978
--------------------------------------------------------------------------
```

##### Q. what is ingress controller in kubernates?

- An ingress controller is a piece of software that provides reverse proxy, configurable traffic routing, and TLS termination for Kubernetes services. 
- Kubernetes ingress resources are used to configure the ingress rules and routes for individual Kubernetes services.

##### Q. what is trigger in Azure devOps?

A trigger help to perform specifies task with respect to some events. i.e. push code and which branches cause a continuous integration build to run.

Continuous deployment triggers help you start classic releases after a classic build or YAML pipeline completes.

##### Q. what is difference between statefulset and deployment in kubernates?

**A Deployment** is a Kubernetes resource object used for declarative application updates. Deployments allow you to define the lifecycle of applications, including the container images they use, the number of pods and the manner of updating them
Deployment is used to deploy stateless applications

**A stateless** application is one which depends on no persistent storage. The only thing your cluster is responsible for is the code, and other static content, being hosted on it. That’s it, no changing databases, no writes and no left over files when the pod is deleted.

**A StatefulSet** is a workload API object for managing stateful applications. Usually, Kubernetes users are not concerned with how pods are scheduled, although they do require pods to be deployed in order, to be attached to persistent storage volumes, and to have unique, persistent network IDs that are retained through rescheduling. StatefulSets can help achieve these objectives.
StatefulSets is used to deploy stateful applications

**Stateful applications** save data to persistent disk storage for use by the server, by clients, and by other applications. An example of a stateful application is a database or key-value store to which data is saved and retrieved by other applications.

##### Q. what is daemonset?

A DaemonSet ensures that all (or some) Nodes run a copy of a Pod. As nodes are added to the cluster, Pods are added to them. As nodes are removed from the cluster, those Pods are garbage collected. Deleting a DaemonSet will clean up the Pods it created.

#Some typical uses of a DaemonSet are:
running a cluster storage daemon on every node

running a logs collection daemon on every node

running a node monitoring daemon on every node

##### Q. what are the section & element in Yaml manifest in Kubernates?

```
#yaml element & section
1.apiVersion: Group_Name/VERSION
  apiVersion: apps/v1
  apiVersion: batch/v1
  apiVersion: batch/v1beta1
  apiVersion: extensions/v1beta1
  apiVersion: v1(by default Core group)
  apiVersion: rbac.authorization.k8s.io/v1
2.Kind
  Pod Replicaset ReplicationController Deployment Service Daemonset Secret StatefulSet ServiceAccount Role PersistentVolume
  RoleBinding PersistentVolumeClaim ClusterRole ConfigMap ClusterRoleBinding Namespace Job ComponentStatus CronJob
3.Metadata
4.Spec
```

##### Q. How many types of VM in Azure?

Types of Virtual Machine Available in Azure Cloud:

- General purpose
- Compute optimized
- Memory optimized
- Storage optimized
- GPU
- High performance compute

##### Q. what is secured way to store secret and certificate in azure?

Azure key vault

##### Q. How to access secured password from Azure Key Vault by terraform?

```
Use this data source to access information about an existing Key Vault Secret.
------------------------------------------------------------------------------
data "azurerm_key_vault_secret" "example" {
  name         = "secret-sauce"
  key_vault_id = data.azurerm_key_vault.existing.id
}

output "secret_value" {
  value     = data.azurerm_key_vault_secret.example.value
  sensitive = true
}
-------------------------------------------------------------------------------
```

##### Q. what is webhook in git?

When a subscribed event occurs on GitHub, GitHub triggers an HTTP POST request to the defined destination. This destination is specified as an HTTP URL, which is the endpoint that is to be called whenever the event occurs. This is known as the webhook URL.

##### Q. What are the steps to create 100 servers by using ansible?(Trick Question)

Configuration management tools such as Ansible are typically used to streamline the process of automating server setup by establishing standard procedures for new servers while also reducing human error associated with manual setups.

##### Q. Can Ansible create servers?Can Ansible provision servers?

Ansible can provision the latest cloud platforms, virtualized hosts and hypervisors, network devices and bare-metal servers. After bootstrapping, nodes can be connected to storage, added to a load balancer, security patched or any number of other operational tasks by separate teams.

##### Q. what is taint and toleration?

- Taints - are the opposite to node affinity they allow a node to repel a set of pods.
- Tolerations - are applied to pods. Tolerations allow the scheduler to schedule pods with matching taints.
  Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes. 
  One or more taints are applied to a node; this marks that the node should not accept any pods that do not tolerate the taints.

##### Q. what is way to assign pod to specific node?

- nodeselector by label
- nodename
- nodeaffinity
- podaffinity

##### Q. how you will stop your pod schedule to specific node?

by specifying taint to node. or taint a node.

##### Q. how can you manage high availablity of pod?

Replicaset create automatically new pod for manage HA.

##### Q. What is service endpoint and private endpoint?

Private Link is superior to Service Endpoint in Security.
------------------------------------------

- Azure Private Link (Private Endpoint) 

------------------------------------------

allows you to access Azure PaaS services over Private IP address within the VNet. 

It gets a new private IP on your VNet. 

When you send traffic to PaaS resource, it will always ensure traffic stays within your VNet.

It is a private IP in the address space of the virtual network where the private endpoint is configured.

It has an inbuilt data protection.

Easily extensible for On-premises network traffic via ExpressRoute or VPN tunnels.

Need to manage another resource.

It costs can quickly grow depending on total ingress and egress traffic and runtime of the link.

Use a private endpoint, if you want to be able to block all internet traffic to a target resource.

------------------------------------------

- Azure Service Endpoint 

------------------------------------------

provides secure and direct connectivity to Azure PaaS services over an optimized route over the Azure backbone network.

Traffic still left your VNet and hit the public endpoint of PaaS service.

It remains a publicly routable IP address.

Traffic need to be passed through an NVA/Firewall for exfiltration protection.

it is not easily restrict on-premise traffic. They can only be secured to Azure VNet.

It’s much simpler to implement and significantly reduce complexity of your architecture design.

There is no additional cost for using VNet service endpoints.

##### Q. What is load balancer in azure?

Service                                  : Network load balancer
Network Protocols              : Layer 4 (TCP or UDP) 
Type                                       : Internal and Public
Routing                                  : Hash-based,Source IP affinity
Global/Regional Service      : Global
Recommended Traffic         : Non-HTTP(S)
Endpoints                               : NIC (VM/VMSS), IP address
Endpoint Monitoring            : Health probes
Redundancy                           : Zone redundant and Zonal
SSL/TLS Termination             : Not Supported
Web Application Firewall      : Not Supported
Sticky Sessions                       : Supported
VNet Peering                           : Supported
SKU                                           : Basic and Standard
Pricing                                      : Basic - free , Standard Load Balancer – charged based on the number of rules and processed data.

##### Q. What is application gateway in Azure?

Service                                          : Web traffic load balancer
Network Protocols                     : Layer 7 (HTTP/HTTPS)
Type                                              : Standard and WAF
Routing                                         : Path-based
Global/Regional Service             : Regional
Recommended Traffic                : HTTP(S)
Endpoints                                      : IP address/FQDN, Virtual machine/VMSS, App services
Endpoint Monitoring                   : Health probes
Redundancy                                  : Zone redundant
SSL/TLS Termination                    : Supported
Web Application Firewall             : Supported
Sticky Sessions                              : Supported
VNet Peering                                  : Supported
SKU                                                  : Standard and WAF (v1 & v2)
Pricing                                             : Charged based on Application Gateway type, processed data, outbound data transfers, and SKU

##### Q. What is traffic manager in Azure?

Service                                           : DNS-based traffic load balancer.
Network Protocols                       : Layer 7 (DNS)
Type                                               : Not Supported
Routing                                          : Performance, Weighted, Priority, Geographic, MultiValue, Subnet
Global/Regional Service              : Global
Recommended Traffic                 : Non-HTTP(S)
Endpoints                                       : Cloud service, App service/slot, Public IP address
Endpoint Monitoring                    : HTTP/HTTPS GET requests
Redundancy                                   : Resilient to regional failures
SSL/TLS Termination                    : Not Supported
Web Application Firewall             : Not Supported
Sticky Sessions                              : Not Supported
VNet Peering                                 : Not Supported 
SKU                                                 : Not Supported
Pricing                                             : Charged per DNS queries, health checks, measurements, and processed data points.

##### Q. What is Front Door in azure?

Service                                           : Global application delivery
Network Protocols                       : Layer 7 (HTTP/HTTPS)
Type                                                : Standard and Premium
Routing                                           : Latency, Priority, Weighted, Session Affinity
Global/Regional Service               : Global
Recommended Traffic                  : HTTP(S)
Endpoints                                        : App service, Cloud service, Storage, Application Gateway, API Management, Public IP address, Traffic Manager, Custom Host
Endpoint Monitoring                     : Health probes
Redundancy                                    : Resilient to regional failures
SSL/TLS Termination                      : Supported
Web Application Firewall               : Supported
Sticky Sessions                                : Supported
VNet Peering                                   : Not Supported
SKU                                                   : Standard and Premium
Pricing                                              : Charged based on outbound/inbound data transfers, and incoming requests from client to Front Door POPs

##### Q. what is service pricipal?

An Azure service principal is an identity created for use with applications, hosted services, and automated tools to access Azure resources

##### Q. what is managed identities in azure?

A Managed Identity is an Enterprise Application (so a Service Principal) within Azure AD, which is linked to an Azure resource (the virtual machine from the example). You can then log in within the Azure resource (VM) as this Enterprise Application without storing any credentials on the Azure resource (VM). With this account, you can then authenticate against other Azure resources (the SQL database from the example) that support Azure AD authentication.

Managed Identity is a feature of Azure Active Directory. It is used for communications among cloud services that support Azure Active Directory (Azure AD) authentication. Using this feature, we can eliminate password complexity and its all drawback.

There are two types of managed identities:

- **System-assigned** - You need to enable a system-assigned managed identity for an Azure resource. The life cycle of a system-assigned managed identity is tied to the life cycle of the Azure resource it represents.

- **User-assigned** - You can Create a user-assigned managed identity and assign it to one or more Azure resources. The life cycle of the user-assigned managed Identity is independent of the Azure resources.

##### Q. what is azure key vault?

**Azure Key Vault** is a cloud service for securely storing and accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, or cryptographic keys. Key Vault service supports two types of containers: vaults and managed hardware security module(HSM) pools.

##### Q. how you will copy azure key vault secret from one subscription to another which are mostly active?

```
#!/bin/bash

SOURCE_KEYVAULT="keyvaultold"
DESTINATION_KEYVAULT="keyvaultnewtest"

SECRETS+=($(az keyvault secret list --vault-name $SOURCE_KEYVAULT --query "[].id" -o tsv))

for SECRET in "${SECRETS[@]}"; do

SECRETNAME=$(echo "$SECRET" | sed 's|.*/||')

SECRET_CHECK=$(az keyvault secret list --vault-name $DESTINATION_KEYVAULT --query "[?name=='$SECRETNAME']" -o tsv)

if [ -n "$SECRET_CHECK" ]
then
    echo "A secret with name $SECRETNAME already exists in $DESTINATION_KEYVAULT"
else
    echo "Copying $SECRETNAME to KeyVault: $DESTINATION_KEYVAULT"
    SECRET=$(az keyvault secret show --vault-name $SOURCE_KEYVAULT -n $SECRETNAME --query "value" -o tsv)
    az keyvault secret set --vault-name $DESTINATION_KEYVAULT -n $SECRETNAME --value "$SECRET" >/dev/null
fi

done
```

##### Q. give one use case of Azure managed identities?

- Access Resources from AKS - system-assigned Identity
- Perform Aks operation on agent by user - User-assigned Identity

##### Q. what is logic app?

Azure Logic Apps helps you orchestrate and integrate different services by providing hundreds of ready-to-use connectors, ranging from SQL Server or SAP to Azure Cognitive Services. The Logic Apps service is "serverless", so you don't have to worry about scale or instances. All you have to do is define the workflow with a trigger and the actions that the workflow performs. The underlying platform handles scale, availability, and performance. Logic Apps is especially useful for use cases and scenarios where you need to coordinate actions across multiple systems and services.

Every logic app starts with a trigger, and only one trigger, which starts your logic app workflow and passes in any data as part of that trigger. Some connectors provide triggers, which come in these types:

- Polling triggers: Regularly checks a service endpoint for new data. When new data exists, the trigger creates and runs a new workflow instance with the data as input.

        Recurrence trigger lets you set the start date and time plus the recurrence for firing your logic app. For example, you can select the days of the week and times of day for triggering your logic app. For more information, see these topics:

        Schedule and run recurring automated tasks, processes, and workflows with Azure Logic Apps
        Tutorial: Create automated, schedule-based recurring workflows by using Azure Logic Apps
        The When an email is received trigger lets your logic app check for new email from any mail provider that's supported by Logic Apps, for example, Office 365 Outlook, Gmail, Outlook.com, and so on.

- Push triggers: Listens for data at a service endpoint and waits until a specific event happens. When the event happens, the trigger fires immediately, creating and running a new workflow instance that uses any available data as input.

        The Request trigger can receive incoming HTTPS requests.    

        The HTTP Webhook trigger subscribes to a service endpoint by registering a callback URL with that service. That way, the service can just notify the trigger when the specified event happens, so that the trigger doesn't need to poll the service.

##### Q. write or create logic app for scenerios?

to start and stop azure kubernates cluster.

##### Q. what is kubernates components?

```
# MASTER NODE configuration used for control all cluster. There are 4 component in master node or control plane
1. API Server       - Used to communicate between all other component with each other  
   port-6443          All the configuration like CRUD operation goes through it only.
                      It is also manage authentication and validate yaml configuration also.
2. ETCD             - It is know as the key-value pair database for Kubernates.
   port-2379          It is stored all kubernates configuration,app configuration and secret etc.
3. Controll Manager - There is used to controller for controllers. Their are 4 controllers component
   port-10252         a. node controller
                      b. replication controller
                      c. end-point controller
                      d. token and service token controllers
                      It manage overall health of kubernates cluster like evrything is up and running state
4. Schedular        - It helps to task schedule and check pod configuration and assign configuration to node as respect to pod
   port-10251         It have task to find approriate worker node and assign to pod 

#  WORKER NODE is used to perform task and deployed application in it.There are 3 component for worker node
1. Kubelet          - it is agent inside every worker node.
   port-10250         it always check api sever in master node to assign task to worker node
                      It is also responsible for reporting working node status and pod running on it
2. Kube-Proxy       - It is network agent running in every worker node
   services port-     It is used to maintain all network configuration.
   (30000-32767)      Jobs like Service configuration , routing and load balancing task 
3. CRI              - It is know as Container Runtime Interfaces
                      It is responsible for running and downloading images in node
                      Kubernates support various CRI like docker,containers.d and others
                      Docker is default CRI in Kubernates
```

##### Q. How to authenticate terraform with azure?

Terraform needs the following information to authenticate with Azure by service principal:

- subscription_id
- client_id
- client_secret
- tenant_id

```
# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}

  subscription_id             = "00000000-0000-0000-0000-000000000000"
  client_id                   = "00000000-0000-0000-0000-000000000000"
  client_certificate_path     = var.client_certificate_path
  client_certificate_password = var.client_certificate_password
  tenant_id                   = "00000000-0000-0000-0000-000000000000"
}

#When storing the credentials as Environment Variables, for example:
export ARM_CLIENT_ID="00000000-0000-0000-0000-000000000000"
export ARM_CLIENT_CERTIFICATE_PATH="/path/to/my/client/certificate.pfx"
export ARM_CLIENT_CERTIFICATE_PASSWORD="Pa55w0rd123"
export ARM_SUBSCRIPTION_ID="00000000-0000-0000-0000-000000000000"
export ARM_TENANT_ID="00000000-0000-0000-0000-000000000000"
```

##### Q. What is Kubernetes and why it is important?

- Kubernetes is an open-source platform used to automate the deployment, scaling, and management of containerized applications. It is like a traffic controller for containerized applications. It ensures that these applications are running efficiently and reliably, by managing their deployment, scaling, and updating processes.

- Kubernetes is important because it makes much easier to deploy and manage complex applications across different environments and infrastructures. By providing a consistent platform for containerized applications, Kubernetes allows developers to focus on building and improving their applications, rather than worrying about the underlying infrastructure. Additionally, Kubernetes helps organizations to achieve greater efficiency, scalability, and flexibility, which can result in significant cost savings and faster time-to-market.

##### Q. How does Kubernetes handle network communication between containers?

Kubernetes defines a network model called the container network interface (CNI), but the actual implementation relies on network plugins. The network plugin is responsible for allocating internet protocol (IP) addresses to pods and enabling pods to communicate with each other within the Kubernetes cluster.
When a pod is created in Kubernetes, the CNI plugin is used to create a virtual network interface for the pod. Each container in the pod is then assigned its own unique IP address within the pod's network namespace. This enables containers within the pod to communicate with each other via localhost, as if they were running on the same host.
To enable communication between pods, Kubernetes sets up a virtual network overlay using the selected network plugin. Each node in the cluster runs a network agent that communicates with other agents on other nodes to establish the overlay network. This enables communication between containers running in different pods, even if they are running on different nodes.

##### Q. How does Kubernetes handle scaling of applications?

Kubernetes provides built-in mechanisms for scaling applications horizontally and vertically, allowing you to meet changing demands for your application.
Horizontal scaling, also known as scaling out, involves adding more instances of an application to handle increased traffic. Kubernetes can manage this automatically through the use of ReplicaSet,
which ensure that a specified number of identical pods are running at all times. We can configure the ReplicaSet to automatically create additional replicas when demand increases, and scale back down when demand decreases.
Vertical scaling, also known as scaling up, involves increasing the resources (such as CPU or memory) available to an existing instance of an application. Kubernetes can handle this through the use of a feature called the Horizontal Pod Autoscaler (HPA), which automatically adjusts the number of replicas based on CPU or memory utilization. When the utilization exceeds a specified threshold, the HPA will increase the number of replicas, and when it falls below a certain threshold, it will decrease the number of replicas.

##### Q. What is a Kubernetes Deployment and how does it differ from a ReplicaSet?

In Kubernetes, a deployment is a higher-level object that provides declarative updates for replica sets and pods. A deployment is responsible for managing the desired state of a set of pods, ensuring that the current state matches the desired state.
A deployment creates and manages replica sets, which in turn manage pods. A replica set ensures that a specified number of replicas of a pod are running at any given time. If a pod fails or is deleted, the replica set replaces it with a new pod.
In short, deployment is a higher-level object that manages the desired state of a set of pods, while a replica set is a low-level object that manages the scaling and lifecycle of pods. Deployments provide declarative updates, rolling updates, and rollbacks, while replica sets are primarily used for scaling and ensuring the desired number of replicas of a pod are running.

##### Q. Can you explain the concept of rolling updates in Kubernetes?

In Kubernetes, a rolling update is a strategy for updating a deployment or a replica set without causing any downtime or interruption to the application. It works as follows:

- First, Kubernetes creates a new version of the desired deployment or replica set.
- Next, Kubernetes gradually replaces the old pods with new ones, one at a time, until all the pods have been updated.
- During the update process, both old and new pods are running simultaneously. This ensures that the application remains available throughout the update process.
- Once all the new pods are running, Kubernetes deletes the old pods.
  This gradual replacement process is a way to update an application without taking it offline or causing any disruption to users. Rolling updates also provide the ability to roll back to the previous version in case something goes wrong during the update process.
  Overall, rolling updates are a powerful and essential feature of Kubernetes that help keep applications up-to-date and available to users.

##### Q. How does Kubernetes handle network security and access control?

Kubernetes has a several built-in features for managing network security and access control. Some of these features are
Network policies: Kubernetes allows administrators to define Network Policies that specify rules for traffic flow within the cluster. These policies can be used to restrict traffic between pods, namespaces, or even entire clusters, based on IP addresses, ports, or other attributes.
Role-Based Access Control (RBAC): Kubernetes supports RBAC, which enables administrators to define granular permissions for users and services based on their roles and responsibilities. This feature allows administrators to control access to Kubernetes resources, including pods, nodes, and services.
Container Network Interface (CNI): Kubernetes supports CNI, which is a plugin-based interface that allows third-party network providers to integrate with the cluster. This feature allows administrators to use their preferred networking solution to provide additional network security and access control.

##### Q. Can you give an example of how Kubernetes can be used to deploy a highly available application?

Let's say you have a web application that needs to be highly available, meaning it can't go down if one or more of its components fail. You can use Kubernetes to deploy this application in a highly available manner by doing the following:

- Create a Kubernetes cluster with multiple nodes (virtual or physical machines) that are spread across multiple availability zones or regions.
- Create a Kubernetes Deployment for your application, which specifies how many replicas (copies) of your application should be running at any given time.
- Create a Kubernetes Service for your application, which provides a stable IP address and DNS name for clients to access your application.
- Use a Kubernetes Ingress to route traffic to your application's Service, and configure the Ingress to load-balance traffic across all the replicas of your application.
  By following these steps, Kubernetes will automatically monitor your application and ensure that the specified number of replicas are always running, even if one or more nodes fail. Clients will be able to access your application through the stable IP address and DNS name provided by the Service, and the Ingress will distribute traffic across all available replicas to ensure that the application remains highly available.

##### Q. What is namespace is Kubernetes? Which namespace any pod takes if we don't specify any namespace?

Namespace can be recognised as a virtual cluster inside your Kubernetes cluster. We can have multiple namespaces inside a single Kubernetes cluster, and they are all logically isolated from each other. They can help us and our teams with organization, security, and even performance!
There are two types of Kubernetes namespaces: Kubernetes system namespaces and custom namespaces.
If we don't specify a namespace for a pod, it will be created in the default namespace by default. This is the namespace that Kubernetes creates automatically when we set up a cluster, and it is used for objects that do not have a specific namespace specified.
Here are four default namespaces Kubernetes creates automatically

- default
- Kube-system
- Kube-public
- Kube-node-lease

##### Q. How ingress helps in Kubernetes?

Ingress is a Kubernetes resource that provides a way to manage incoming traffic to your cluster. It acts as a layer 7 (application layer) load balancer and provides advanced routing and path-based rules for HTTP and HTTPS traffic.
Here are a few ways that Ingress helps in Kubernetes:

- Load balancing: Ingress can be used to distribute traffic to different services in the cluster, based on the URL or hostname specified in the incoming request. This helps to balance the load on the different services and ensure that the traffic is routed to the correct backend service.
- Routing: Ingress can route traffic to different services based on the URL path or hostname specified in the request. This makes it easy to manage multiple services running on the same cluster.
- Access control: Ingress can be used to restrict access to services based on IP addresses, HTTP headers, or other criteria. This helps to improve the security of the cluster by preventing unauthorized access to the services.
  TLS termination: Ingress can terminate SSL/TLS encryption, allowing you to use a single certificate for multiple services and domains.

##### Q. Explain different types of services in Kubernetes?

There are four types of services in Kubernetes:

- **ClusterIP** (default): ClusterIP service is responsible for providing a stable IP address for a set of pods in the cluster. This IP address is only accessible within the cluster, and it allows other services and pods to access the pods that belong to the ClusterIP service.

- **NodePort**: This type of service exposes a set of pods to the outside world. A NodePort service maps a port on each node in the cluster to a specific port on the pod. This service type is used when you need to access a service from outside the cluster or from a different namespace within the same cluster.

- **LoadBalancer**: This type of service is used to expose a set of pods to the outside world through a load balancer. The LoadBalancer service type is used in cloud environments, and it is responsible for automatically creating a cloud load balancer and configuring it to route traffic to the pods in the service.

- **ExternalName**: This type of service maps a service to an external DNS name, allowing you to use the DNS name to access the service instead of the IP address. This service type is useful when you have a service running outside of the cluster, and you want to access it from within the cluster.

##### Q. Can you explain the concept of self-healing in Kubernetes and give examples of how it works?

Self-healing is a feature provided by the Kubernetes open-source system. If a containerized app or an application component fails or goes down, Kubernetes re-deploys it to retain the desired state. Kubernetes provides self-healing by default.
Ex: Suppose we have a web application deployed in Kubernetes with 2 replicas. Each replica runs in its own container. Kubernetes monitors the health of each container by sending periodic requests to the application's endpoints.
If one of the replicas fails, Kubernetes detects it by monitoring the responses to the health check requests. It then terminates the failed container and starts a new one to replace it, ensuring that the total number of replicas is always maintained. The replacement container is created from the same image and configuration as the original, which helps to ensure consistency across replicas.
Kubernetes also supports rolling updates, which allow you to update your application without causing downtime. When you update your application, Kubernetes creates a new set of replicas with the updated code and configuration. It then gradually replaces the old replicas with the new ones, ensuring that the application remains available during the update process.

##### Q. How does Kubernetes handle storage management for containers?

Kubernetes provides various ways to manage storage for containers, including:
volumes, persistent volumes, and storage classes.

- **Volumes**: A volume is a directory accessible to containers in a pod. Volumes are used to store data that needs to persist beyond the lifetime of a container. Kubernetes supports several types of volumes, such as emptyDir, hostPath, configMap, secret, and more. Each type of volume has its own properties and behaviour.
- **Persistent Volumes**: Persistent volumes (PVs) are storage resources provisioned by an administrator that can be used by a pod. A PV is a piece of storage in the cluster that has been provisioned by an administrator. It is not tied to any specific pod, and can be used by any pod that requests it. PVs can be dynamically provisioned by a storage class or statically provisioned by an administrator.
- **Storage Classes**: A storage class is used to define the types of storage that can be dynamically provisioned in the cluster. Storage classes provide a way to abstract the underlying storage infrastructure, making it easier to manage and use storage resources in a consistent way. A storage class defines the provisioner that will be used to provision the storage, along with other parameters like the access mode, reclaim policy, and more.

##### Q. How does the NodePort service work?

NodePort service in Kubernetes allows you to expose a container running in a Kubernetes cluster to the outside world by mapping a specific port of the Kubernetes node to the container's port.

- First, you create a NodePort service by defining it in a Kubernetes manifest file. In this manifest file, you specify the target port on which your container is listening and the port on which you want to expose the service to the outside world.
- When you create the service, Kubernetes assigns a random port in the range of 30000-32767 to the service. This port is the "NodePort" that gives the service its name.
- Kubernetes then creates a mapping between the NodePort and the target port of your container.
- When you want to access your container from outside the Kubernetes cluster, you can use the IP address of any node in the cluster along with the NodePort to access the service. For example, if the NodePort assigned to your service is 32000 and you have a node with IP address 10.0.0.100, you can access the service at http://10.0.0.100:32000.
- The node that you use to access the service will route the traffic to the correct pod based on the mapping that Kubernetes created between the NodePort and the target port of your container.

##### Q. What is a multinode cluster and single-node cluster in Kubernetes?

In Kubernetes, a node is a worker machine that runs containerized applications. A cluster is a group of nodes that work together to run and manage these applications.
**A single-node cluster** in Kubernetes consists of only one node, which means that all the applications and services are running on the same node. This configuration is useful for testing and development purposes, but it is not recommended for production environments.
On the other hand, **a multinode cluster** consists of multiple nodes that work together to distribute the workload and provide high availability. In a multinode cluster, if one node fails, the applications can be automatically moved to another node, ensuring that the applications remain available.

##### Q. Difference between create and apply in Kubernetes?

In Kubernetes, "create" and "apply" are two different commands used to manage Kubernetes resources.

- "**Create**" command:
  The "create" command is used to create a new Kubernetes resource from a YAML or JSON file. When you create a resource using the "create" command, Kubernetes will create a new resource object based on the specification provided in the file. If a resource with the same name already exists, the "create" command will return an error.

- "**Apply**" command:
  The "apply" command is used to create or update a Kubernetes resource based on a YAML or JSON file. When you apply a resource using the "apply" command, Kubernetes will update the existing resource object if it already exists, or create a new resource object if it doesn't exist.
  The main difference between the two commands is that "create" always creates a new resource, while "apply" can create or update an existing resource.

### Key-Points

- Only 1 agent used for run 1 pipeline parallel.
- Yaml file will available for CI pipeline from class editor created pipeline in Azure DevOps not CD pipelines.
- Online debugger for python : https://pythontutor.com/visualize.html#mode=edit

##### Q. what is the diffrence between COPY and ADD command in dockerfile?

1. Functionality:
   COPY: The COPY command is a straightforward way to copy files and directories from your host system to the image. It copies files or directories as-is without extracting or processing them. It's a simple file transfer mechanism.
   ADD: The ADD command has additional functionality. It not only copies files from the host to the image but also allows you to use URLs or extract compressed archives (e.g., .tar, .zip) directly into the image. Docker will automatically handle the extraction and copying of files.

2. Caching:
   COPY: The COPY command is cacheable. Docker will cache the results of the COPY command, which can lead to faster build times when the source files have not changed. If the source files haven't changed, Docker will use the cached layer, and the subsequent builds will be faster.
   ADD: The ADD command is not cacheable in the same way as COPY. Since it can involve complex operations such as decompression of archives or downloading from URLs, Docker doesn't cache the results in the same manner. This can lead to slower builds if the source files haven't changed.

3. URLs and Archives:
   COPY: The COPY command is designed primarily for copying local files and directories into the image. It does not support URLs or extracting compressed archives directly.
   ADD: The ADD command, on the other hand, allows you to copy files from URLs or automatically extract compressed archives. For example, you can use ADD to download a file from the internet and place it in your image, or you can use it to add a compressed archive that will be extracted during the build process.
- Best Practices:
  It is generally recommended to use the COPY command when you only need to copy local files or directories and have no need for the additional features of ADD. This is because COPY is more explicit and predictable in its behavior.
  Use the ADD command when you specifically require its additional functionality, such as extracting archives or downloading files from URLs.

##### Q. Explain the typical lifecycle of a docker container?

There can be many combinations of stages in the life cycle of a docker container but here is one of the most common one is given below.

- Pull or create a docker image
- Create a container from the image
- Run the container
- Stop the container 
- Restart the container
- Kill the container (if needed)
- Prune or reclaim the resources used by the container

##### Q. What are the two ways to download the docker images?

There are two ways i.e. explicit and implicit. We can download image explicitly using command ‘docker pull’. Implicitly, when we execute ‘docker run’ then Docker daemon searches the image locally and if not found, it downloads the image.

##### Q. How to transfer docker images from one machine to another without intenret?

docker save -o images.tar image1 image2 image3
docker load -i image.tar

##### Q. Import and export docker containers?

docker export -o container.tar container_name
docker import container.tar

##### Q. How to check steps executed in docker images?

```
$ docker image history  acme/my-final-image:1.0
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
8bd85c42fa7f   3 minutes ago   CMD ["/bin/sh" "-c" "/app/hello.sh"]            0B        buildkit.dockerfile.v0
<missing>      3 minutes ago   RUN /bin/sh -c chmod +x /app/hello.sh # buil…   39B       buildkit.dockerfile.v0
<missing>      3 minutes ago   COPY . /app # buildkit                          222B      buildkit.dockerfile.v0
<missing>      4 minutes ago   RUN /bin/sh -c apk add --no-cache bash # bui…   2.15MB    buildkit.dockerfile.v0
<missing>      7 weeks ago     /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
<missing>      7 weeks ago     /bin/sh -c #(nop) ADD file:f278386b0cef68136…   5.6MB
```

##### Q. What does the following command do "docker inspect –format ‘{{ .NetworkSettings.IPAddress }}’ hfgdh67868"?

This will extract the exact private IP address of the container

##### Q. How can you override the ENTRYPOINT at runtime?

You can override the ENTRYPOINT at runtime using ‘–entrypoint’.

##### Q. What are the two types of registries used in Docker?

The two types of registry used in Docker system are Public Registry and Private Registry. Docker’s public registry is called Docker hub where you can store millions of images. You can also build a private registry for your in-premise use.

##### Q. How does  Docker client and Docker Daemon communicate?

Docker client and Docker Daemon communicate using a mix of Restful API, socket I/O, and TCP.

##### Q. Can we add mutiple machine in docker swarn without installing docker swarn in each machine?

NO

##### Q. what is the difference between docker create and docker run command?

**Create** command create the conatiner but doesn't start it. the docker daemon creates a writeable container layer over the specified image and prepares it for running the specified command. The container ID is then printed to STDOUT. This is similar to docker run -d except the container is never started.

**Run** command create as well as start the conatiner from docker image.

##### Q. What is “null” network driver and what is its use?

“null” network driver gets activated when the container is started with

```
$ docker run –net none …
```

The “null” here simply means that no IP address would be configured for the container. Also the container will not have any access to the external network as well as to other containers. It is generally used for running local batch tyep of jobs.

##### Q. How do you ensure that container 1 runs before container 2 while using Docker Compose?

Docker Compose doesn’t wait for containers to be ready before moving forward with the next container. 
In order to control our order of execution, we can use the “depends on” condition, depends_on. Here’s an example of it being used in a docker-compose.yml file:

```
version: "2.4"
services:
 backend:
   build: .
   depends_on:
     - db
 db:
   image: postgres
```

The docker-compose up command will start and run the services in the dependency order that we specify.

##### Q. Can you explain the “ship the application” part of Docker?

A modern-day application is structured as a set of independent microservices with well-defined access points. They are converted to images along with their dependencies and shipped. Each image is a set of layers and only changes in layers are shipped (and not the entire layer). This way, we can save on disk usage, reduce network load and minimize memory usage.

##### Q. Who owns the Docker control socket?

Docker control socket is owned by docker group.

##### Suppose you are inside a container say container_1. You exit the container by typing exit on the command prompt. What happens to container_1?

root@container_1:/# exit
Ans. Container_1 goes to stop state and all its compute resources get freed. However, it remains on the system’s disk storage.

##### Q. Can an ARG variable be used by the running container?

No, an ARG variable cannot be used by the running container as it is exclusively reserved for use by dockerfile.

##### Q. The launchable, configured unit of an application is called a container. Is this statement true or false?

This statement is false. Image is the launchable and configured unit of an application.

##### Q. How can one see the logs of a container in real time?

```
We can see the logs of a container in real time using –follow option of logs command. E.g.
$ docker logs –follow <containerid>
```

##### Q. Normal user in host machine can read files mounted by docker container with root user?

NO

##### Q.  What is Checkpoint? / Does Nomad call home?

Nomad makes use of a HashiCorp service called Checkpoint which is used to check for updates and critical security bulletins. Only anonymous information, which cannot be used to identify the user or host, is sent to Checkpoint. An anonymous ID is sent which helps de-duplicate warning messages. This anonymous ID can be disabled. Using the Checkpoint service is optional and can be disabled.

##### Q. Is Nomad eventually or strongly consistent?

Nomad makes use of both a consensus protocol and a gossip protocol. The consensus protocol is strongly consistent, and is used for all state replication and scheduling. The gossip protocol is used to manage the addresses of servers for automatic clustering and multi-region federation. This means all data that is managed by Nomad is strongly consistent.

##### Q. Is Nomad's datacenter parameter the same as Consul's?

No. For those familiar with Consul, Consul's notion of a datacenter is more equivalent to a Nomad region. Nomad supports grouping nodes into multiple datacenters, which should reflect nodes being colocated, while being managed by a single set of Nomad servers.
Consul on the other hand does not have this two-tier approach to servers and agents and instead relies on federation to create larger logical clusters.

##### Q. What is "bootstrapping" a Nomad cluster?

Bootstrapping is the process when a Nomad cluster elects its first leader and writes the initial cluster state to that leader's state store. Bootstrapping will not occur until at least a given number of servers, defined by bootstrap_expect, have connected to each other. Once this process has completed, the cluster is said to be bootstrapped and is ready to use.
Certain configuration options are only used to influence the creation of the initial cluster state during bootstrapping and are not consulted again so long as the state data remains intact. These typically are values that must be consistent across server members. For example, the default_scheduler_config option allows an operator to set the SchedulerConfig to non-default values during this bootstrap process rather than requiring an immediate call to the API once the cluster is up and running.
If the state is completely destroyed, whether intentionally or accidentally, on all of the Nomad servers in the same outage, the cluster will re-bootstrap based on the Nomad defaults and any configuration present that impacts the bootstrap process.


