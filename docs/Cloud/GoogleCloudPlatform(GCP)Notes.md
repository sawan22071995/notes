# Google Cloud Platform (GCP) Notes

<img src="https://github.com/sawan22071995/notes/blob/main/docs/Cloud/GCP.jpg?raw=true" title="" alt="alt text" data-align="center">

**Google Cloud Platform (GCP)** is a suite of cloud computing services offered by Google that provides a variety of infrastructure and platform services for building, deploying and scaling applications and services.

Some of the key services and products offered by Google Cloud Platform include:

1. **Compute Services**: Google Compute Engine (Virtual Machines), Google Kubernetes Engine (Managed Kubernetes), Google App Engine (PaaS), Google Cloud Functions (Serverless execution).

2. **Storage Services**: Google Cloud Storage, Cloud Bigtable, Cloud Datastore, Persistent Disk.

3. **Networking Services**: Virtual Private Cloud (VPC), Cloud Load Balancing, Cloud CDN, Cloud Interconnect.

4. **Big Data and Machine Learning**: BigQuery, Cloud Dataflow, Cloud Dataproc, Cloud Dataprep, Cloud ML Engine, Vertex AI.

5. **Management Tools**: Google Cloud Console, Cloud Deployment Manager, Cloud Monitoring, Cloud Logging.

6. **Security and Identity**: Cloud Identity and Access Management (IAM), Cloud Key Management Service, Cloud Security Scanner.

7. **Databases**: Cloud SQL, Cloud Spanner, Cloud Bigtable, Cloud Datastore.

8. **Internet of Things (IoT)**: Cloud IoT Core.

9. **API Management**: Cloud Endpoints, Apigee.

10. **Developer Tools**: Cloud Source Repositories, Cloud Build, Cloud Tasks, Cloud Scheduler.

Google Cloud Platform provides a global infrastructure with data centers around the world, enabling customers to deploy their applications and services closer to their users. It also offers a range of pricing models, including pay-as-you-go, sustained use discounts, and committed use discounts, allowing customers to optimize their costs based on their usage patterns.

### Regions and Zones

- **Availablity Region(DR)** : East US x West US (For disaster Recovery or Region geographical Failure)
- **Availablity Zone(99.99% SLA)** : Zone 1 x Zone 2 x Zone 3 (For Data centre Recovery or Data Centre Zone failure)
- **Availablity Set(99.95% SLA)** : Fault Domain x 3 and Update Domain x 20( for upgrade or maintenance phyiscal Hardware)
- **Single VM (99.9% SLA)** : Configuration of Machine in Single centre only

### GCP is organized into Regions and zones.

### Any Resource in GCP either be Regional, Zonal or Global.

### In a single region there will be 1,2,3 and 4 zones.

```
us-central1 [Region] 
   |__us-central1-a____
   |__us-central1-b    |
   |__us-central1-c    |-Zones
   |__us-central1-f____|
```

### RPO (Recovery Points Objective)

- Data loss due to accident and recovering 
- Maximum time for which system can be down

### RTO (Recovery Time Objective)

- Downtime due to System recovering
- Maximum time for which organization can tolerate Dataloss

### sustain user discount

- Automatic Discount upto 30% on workloads that run for a significant portion of billing month. i.e.
- As long as the resource will sustain google will provide more discount on resource billing.
- If you terminate machine in 10 days - 5% discount given by Google on Billing Amount
- If you terminate machine in 20 days - 10% discount given by Google on Billing Amount
- If you terminate machine in 30 days - 30% discount given by Google on Billing Amount
- **Preemptible VM** - Upto 80% off on Workload. But workload can be interrupted.
- **ColdLine Storage** - Archival Storage at very Cheap rate.
- **Custom Machines** - Pick any Configuration of CPU & Memory and Save Up to 48% on Compute Engine resources.
- **Committed Use Discount** - Save up to 57% on Lock-In resources.

### Google Pricing Calculator - To Calculate the Business Budget of your Project

https://cloud.google.com/products/calculator

### The service account must be created before you create a firewall rule that relies on it.

### Firewall rules that use service accounts to identify instances apply to both new instances created and associated with the service account and existing instances if you change their service accounts.

### User can associate service accounts with individual instances and with instance templates used by managed instance groups.

### GCP default vpc have subnet like this

- Each subnet for each 1 region
  
  ```
  Total no. of subnets = Regions available in GCP
  ```

### Managing cloud infrastructure from k8s

- we can do it by using crossplane
  
  https://docs.crossplane.io/v1.14/getting-started/
  
  https://docs.crossplane.io/v1.14/getting-started/provider-gcp/
  
  https://doc.crds.dev/github.com/crossplane/provider-gcp@v0.22.0
  
  https://github.com/crossplane-contrib/provider-gcp/tree/master/examples

### Migration to Google Cloud

1. What does google cloud do, that we can't do right Now?

2. Why should we migrate our resources to GCP?

3. What is ROI if we move to Google cloud?

4. Things care about migration as leader/Architect?
   
   - Costs
   
   - Future-proof infrastructure
   
   - Scale to meet demands
   
   - Data Analytics
   
   - Greater Businness agility
   
   - Managed Services
   
   - Global Reach
   
   - Secuirty at scale

### Five Phases of Cloud Migration

```
[1]Assess ==>
   [2]Pilot ===>
      [3]Move Data ====>
         [4]Move App =====>
            [5]Optimize
```

### Principles of Good Cloud Design

- High Availablity
- Scalablity
- Security
- Disaster Recovery
- Cost Control

## Migration Services end to end migrate

| *Services Types* | *Own Data Center*                  | *GCP(Google Cloud Platform)*               |
| ---------------- | ---------------------------------- | ------------------------------------------ |
| Compute          | Physical\|Virtualize Hardware      | **Compute Engine**                         |
| Storage          | SAN, NAS, DAS                      | **Persistant Disk, Cloud Storage**         |
| Network          | MPLN, VPN, DNS, H/W Load Balancing | **Cloud VPN, Cloud LB, CDN**               |
| Security         | Firewall, Route Table etc.         | **Firewall, Encryption etc**.              |
| Identity         | Active Directory, LDAP             | **IAM, LDAP**                              |
| Management       | Configuration Service, CICD tools  | **GCP Deployment Manager, CI,Cloud Build** |

### Data tranfer by Gsutil

- Multi Threaded Transfer Copy using `gsutil`
  
  ```
  - Use -m Option
  gsutil -m cp -r [SOURCE] gs://[BUCKET_NAME]
  ```

- Parallel Uploads
  
  ```
  - Break Single File into Chunks
  - Don’t use for Nearline/Coldline Buckets - Extra Charge for
  ‘Modifying’ files on upload
  gsutil -o GSUtil:parallel_composite_uplaod_threashold=200M cp
  [SOURCE] gs://[BUCKET_NAME]
  ```

### Removing old replicasets is part of the Deployment object, but it is optional. You can set .spec.revisionHistoryLimit to tell the Deployment how many old replicasets to keep around.Here is a YAML example:

```
apiVersion: apps/v1
kind: Deployment
# ...
spec:
  # ...
  revisionHistoryLimit: 0 # Default to 10 if not specified
  # ...
```

### Execute trigger from cloudbuild.yaml file

```
- name: gcr.io/cloud-builders/gcloud
    args:
      - builds
      - triggers
      - run
      - MY-TRIGGER
      - '--region=asia-south1'
```

### Install gke-auth plugin in private VM

```
sudo apt-get install google-cloud-sdk-gke-gcloud-auth-plugin
```

### Create cloudbuild trigger with the help of shell script

```
#!/bin/bash
ms_name =("test1" "test2" "test3") 
for n in ${ms_name[@]}; 
do
  gcloud builds triggers create cloud-source-repositories --name=tyh-$n-microservice-docker-image-puild-push-uat --repo=tyh-$n-microservice-uat  --branch-pattern=^development$ --build-config=cloudbuild-docker-build-push.yaml --region=asia-south1 --description="This trigger used to build and push docker images in artifact repositories"

  gcloud builds triggers create cloud-source-repositories --name=tyh-$n-microservice-gke-deploy-uat --repo=tyh-$n-microservice-uat  --branch-pattern=^development$ --build-config=cloudbuild-k8s-deploy-uat.yaml --region=asia-south1 --description="This trigger used to deploy microservice in gke k8s engine"
done
```

### gcloud cli login

```
gcloud auth login --no-launch-browser
```

### Resize disk in VM

https://cloud.google.com/compute/docs/disks/resize-persistent-disk

### attach mount non-boot disk in VM

- **WINDOWS** : https://cloud.google.com/compute/docs/disks/format-mount-disk-windows

- **LINUX**   : https://cloud.google.com/compute/docs/disks/format-mount-disk-linux

### Mount disk to the Linux VM

- Create a directory that serves as the mount point for the new disk on the VM. You can use any directory. The following example creates a directory under /mnt/disks/
  
  ```
  sudo mkdir -p /mnt/disks/MOUNT_DIR
  ```

- Use the mount tool to mount the disk to the instance, and enable the discard option:
  
  ```
  sudo mount -o discard,defaults /dev/DEVICE_NAME /mnt/disks/MOUNT_DIR
  ```

- Configure read and write permissions on the disk. For this example, grant write access to the disk for all users
  
  ```
  sudo chmod a+w /mnt/disks/MOUNT_DIR
  ```

- Configure automatic mounting on VM restart, Create a backup of your current /etc/fstab file.
  
  ```
  sudo cp /etc/fstab /etc/fstab.backup
  ```

- Use the blkid command to list the UUID for the disk.
  
  ```
  sudo blkid /dev/DEVICE_NAME
  Output: 
  /dev/DEVICE_NAME: UUID="a9e1c14b-f06a-47eb-adb7-622226fee060" BLOCK_SIZE="4096"
  TYPE="ext4" PARTUUID="593b3b75-108f-bd41-823d-b7e87d2a04d1"
  ```

- Open the /etc/fstab file in a text editor and create an entry that includes the UUID. For example:
  
  ```
  UUID=UUID_VALUE /mnt/disks/MOUNT_DIR ext4 discard,defaults,MOUNT_OPTION 0 2
  ```

- Use the cat command to verify that your /etc/fstab entries are correct:
  
  ```
  cat /etc/fstab
  ```

- If you detach this disk or create a snapshot from the boot disk for this VM, edit the /etc/fstab file and remove the entry for this disk. Even with MOUNT_OPTION set to nofail or nobootwait, keep the /etc/fstab file in sync with the devices that are attached to your VM and remove these entries before you create your boot disk snapshot or detach the disk.

### cloudbuild trigger names list

```
gcloud alpha builds triggers list --region=asia-south1 --format="value(name)"
```

### Give your account permissions to perform all administrative actions needed in k8s

```
kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=<GOOGLE-EMAIL-ACCOUNT>
```

### rollout deployment in GKE

```
kubectl rollout undo deployment/tyh-test-uat --to-revision=<revision No>
kubectl set image deployment/tyh-test-uat tyh-test-uat=asia-south1-docker.pkg.dev/tyh-uat-svc-poc/tyh-poc/test-microservice:2188c4b
```

### insecure-skip-tls-verify in .kube/config file for connecting GKE (*NOT Recommended*)

[ssl - helm: x509: certificate signed by unknown authority - Stack Overflow](https://stackoverflow.com/questions/48119650/helm-x509-certificate-signed-by-unknown-authority)

```
apiVersion: v1
clusters:
- cluster:
    server: https://192.168.0.3
    insecure-skip-tls-verify: true
  name: gke_my_k8s
```

### check tls through nmap for ssl certificates

```
nmap --script ssl-enum-ciphers -p 443 poc-dev.test.com
nmap --script ssl-enum-ciphers -p 80 34.45.667.8
```

### update SSL policy in gcp for compute resources or Load Balancer in GKE ingress

```
- Create an SSL policy with desired settings
gcloud compute ssl-policies create my-ssl-policy \
  --profile=MODERN \
  --min-tls-version=1.2\
  --custom-features=TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_256_GCM_SH

- Create front end config yaml for ssl-policy
apiVersion: networking.gke.io/v1beta1
kind: FrontendConfig
metadata:
  name: my-frontend-config
  namespace: poc-dev
spec:
  sslPolicy: my-ssl-policy

- create ingress file with ssl policy gke
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    networking.gke.io/v1beta1.FrontendConfig: "my-frontend-config"
```

### disable tls in gcloud

```
gcloud config set auth/disable_ssl_validation  True
```

### remove file start `--` in linux

```
rm ./--02102023-2005PM.log
```

### you can check here if any service getting issue from gcp side

https://status.cloud.google.com/

### cloudbuild default variable list

[Substituting variable values &nbsp;|&nbsp; Cloud Build Documentation &nbsp;|&nbsp; Google Cloud](https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values)

### nginx annotation ingress

https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/nginx-configuration/annotations.md

### kubectl logs with tail in GKE

```
kubectl logs --tail=50 <pod_name>
```

### install telnet in alpind linux docker images

```
apk update install
apk add busybox-extras
```

### replace subsitute variable in yaml file in cloudbuild

```
steps:
  - name: 'gcr.io/cloud-builders/gcloud'
    id: commit
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        echo ${_VERSION}
        sed -i "s/latest/${_VERSION}/g" k8/deploymentprod.yaml
        cat k8/deploymentprod.yaml
```

### Spin K8s Self Managed Cluster on GCP

- Set Project in gcloud
  
  ```
  gcloud config set project <myProject>
  ```
- Set the zone property in the compute section
  
  ```
  gcloud config set compute/zone us-east1-b
  ```
- Create the VPC
  
  ```
  gcloud compute networks create k8s-cluster --subnet-mode custom
  ```
- Create the k8s-nodes subnet in the k8s-cluster VPC network
  
  ```
  gcloud compute networks subnets create k8s-nodes \
  --network k8s-cluster \
  --range 10.240.0.0/24
  ```
- Create a firewall rule that allows internal communication across TCP, UDP, ICMP and IP in IP.
  
  ```
  gcloud compute firewall-rules create k8s-cluster-allow-internal \
  --allow tcp,udp,icmp,ipip \
  --network k8s-cluster \
  --source-ranges 10.240.0.0/24
  ```
- Create a firewall rule that allows external SSH, ICMP, and HTTPS
  
  ```
  gcloud compute firewall-rules create k8s-cluster-allow-external \
  --allow tcp:22,tcp:6443,icmp \
  --network k8s-cluster \
  --source-ranges 0.0.0.0/0
  ```
- Create the controller VM (Master Node)
  
  ```
  gcloud compute instances create master-node \
    --async \
    --boot-disk-size 200GB \
    --can-ip-forward \
    --image-family ubuntu-1804-lts \
    --image-project ubuntu-os-cloud \
    --machine-type n1-standard-2 \
    --private-network-ip 10.240.0.11 \
    --scopes compute-rw,storage-ro,service-management,service-control,logging-write,monitoring \
    --subnet k8s-nodes \
    --zone us-east1-b \
    --tags k8s-cluster,master-node,controller
  ```
- Create Two worker VMs
  
  ```
  for i in 0 1; do
  gcloud compute instances create workernode-${i} \
    --async \
    --boot-disk-size 200GB \
    --can-ip-forward \
    --image-family ubuntu-1804-lts \
    --image-project ubuntu-os-cloud \
    --machine-type n1-standard-2 \
    --private-network-ip 10.240.0.2${i} \
    --scopes compute-rw,storage-ro,service-management,service-control,logging-write,monitoring \
    --subnet k8s-nodes \
    --zone us-east1-b \
    --tags k8s-cluster,worker
  done
  ```
- Install Docker on the controller VM and each worker VM.
  
  ```
  sudo apt update
  sudo apt install -y docker.io 
  sudo systemctl enable docker.service
  sudo apt install -y apt-transport-https curl
  ```
- Install kubeadm, kubelet, and kubectl on the controller VM and each worker VM.
  
  ```
  curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
  cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
  deb https://apt.kubernetes.io/ kubernetes-xenial main
  EOF
  sudo apt-get update
  sudo apt-get install -y kubelet kubeadm kubectl
  sudo apt-mark hold kubelet kubeadm kubectl
  ```
- Create the controller node of a new cluster. On the controller VM, execute:
  
  ```
  sudo kubeadm init --pod-network-cidr 192.168.0.0/16
  ```
- To set up kubectl for the ubuntu user, run:
  
  ```
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
  ```
- On Worker Nodes Execute the Join Command
  
  ```
  kubeadm join --discovery-token abcdef.1234567890abcdef --discovery-token-ca-cert-hash sha256:1234..cdef 1.2.3.4:6443
  ```
- Verify the Cluster Status
  
  ```
  kubectl get nodes
  ```
- On the controller, install Calico from the manifest:
  
  ```
  curl https://docs.projectcalico.org/manifests/calico.yaml -O kubectl apply -f calico.yaml
  ```

### Add custom header through yaml in Load Balancer for GKE Ingress

https://cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#1.16-gke.3+

- Create BackendConfig.yaml as mentioned below
  
  ```
  apiVersion: cloud.google.com/v1
  kind: BackendConfig
  metadata:
  name: my-backendconfig
  spec:
  customResponseHeaders:
    headers:
    - "server: hide"
    - "X-Content-Type-Options: nosniff"
    - "X-Frame-Options: DENY"
    - "X-XSS-Protection: 1; mode=block"
    - "Strict-Transport-Security: max-age=31536000; includeSubDomains; preload"
    - "Content-Security-Policy: default-src 'self';script-src 'self';style-src 'self';font-src 'self';img-src 'self' data:;base-uri 'self';form-action 'self';frame-ancestors 'none';block-all-mixed-content;upgrade-insecure-requests;-cache--control no-cache no-store;no-store;object-src 'none';script-src-attr 'none'"
    - "Referrer-Policy: strict-origin-when-cross-origin"
  ```

- apply the BackendConfig yaml in k8s
  
  ```
  kubectl apply -f BackendConfig.yaml
  ```

- Add above Backend annotation to application servivce.yaml
  
  ```
  kind: Service
  apiVersion: v1
  metadata:
  name: tyh-webui-uat
  annotations:
    cloud.google.com/backend-config: '{"ports": {"3000":"my-backendconfig"}}'
  spec:
  type: NodePort
  ports:
  - name: http
    port: 3000
    targetPort: 3000
    protocol: TCP
  selector:
    app: tyh-webui-uat
  ```

- apply the application service.yaml
  
  ```
  kubectl apply -f service.yaml
  ```

- traffic Routing workflow to application in gke
  
  ```
  User request-->
              DNS-->
                 ALB Front End-->
                              GKE Ingress Route-->
                                               GKE Application Backend service-->
                                                                              GKE Application Pod-->Application Running
  ```

- All backend service in GCP ALB created through GKE ingress didn't update or delete until you will not change or delete GKE application service exposed internet through Ingress.

### add request header to gcp alb backend by gcloud command

```
gcloud compute backend-services update <Backend Name> --global --custom-request-header <Headers>

gcloud compute backend-services update k8s-be-30314--8b39b28cb6b1eb84 --global --custom-request-header "X-Frame-Options:DENY" --custom-request-header "X-Content-Type-Options: nosniff" --custom-request-header "server: hide" --custom-request-header "X-XSS-Protection: 1; mode=block" --custom-request-header "Strict-Transport-Security: max-age=31536000; includeSubDomains; preload"
```

### add response header to gcp alb backend by gcloud command

```
gcloud compute backend-services update <Backend Name> --global --custom-response-header <Headers>

gcloud compute backend-services update k8s-be-30314--8b39b28cb6b1eb84 --global --custom-response-header "X-Frame-Options:DENY" --custom-response-header "X-Content-Type-Options: nosniff" --custom-response-header "server: hide" --custom-response-header "X-XSS-Protection: 1; mode=block" --custom-response-header "Strict-Transport-Security: max-age=31536000; includeSubDomains; preload"
```

### remove header form backend gcp alb

```
gcloud compute backend-services update <Backend Name> --global --no-custom-request-headers
gcloud compute backend-services update k8s-be-30314--8b39b28cb6b1eb84 --global --no-custom-request-headers

gcloud compute backend-services update <Backend Name> --global --no-custom-response-header
gcloud compute backend-services update k8s-be-30314--8b39b28cb6b1eb84 --global --no-custom-response-headers
```

### security annotation in nginx lb deployed in GKE

```
nginx.ingress.kubernetes.io/configuration-snippet: |
      more_set_headers "server: hide";
      more_set_headers "X-Content-Type-Options: nosniff";
      more_set_headers "X-Frame-Options: DENY";
      more_set_headers "X-XSS-Protection: 1; mode=block";
	  more_set_headers "Strict-Transport-Security: max-age=31536000; includeSubDomains; preload"
```

### logs explorere query for specific time to find logs

- Time must be in Container Pod timezone UTC
  
  ```
  resource.type="k8s_container"
  resource.labels.project_id="tyh-dev-svcprj"
  resource.labels.location="asia-south1"
  resource.labels.cluster_name="tyhpockubernetes"
  resource.labels.namespace_name="default"
  labels.k8s-pod/app="tyh-prescription-dev" severity>=DEFAULT
  timestamp>="2023-09-08T22:00:00Z" AND timestamp<="2023-09-08T23:45:00Z"
  ```

### Variablized default GCP compute engine service account for automation

```
SVC_ACCOUNT="${PROJECT_NUM//\'/}-compute@developer.gserviceaccount.com"
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT --member serviceAccount:$SVC_ACCOUNT --role roles/storage.objectAdmin
```

### GCP AI & ML Demo Service online

```
https://cloud.google.com/?hl=en
--> Products
-->AI and Machine Learning 
-->Speech-To-Text
```

### Cloud Run

- Deploy containerized application through serverless services just like AWS fargate, Azure container etc.
  
  ```
  gcloud run deploy translate --source . --allow-unauthenticated --platform
  ```

### search google API

```
[GCP Console] --> [API & Services] --> [library,Enabled API's & Services, Credentials]
gcloud services enable artifactregistry.googleapis.com 
```

### deploy application in AppEngine Service by app.yaml file

```
- deploy application
gcloud app deploy

- stream logs 
gcloud app logs tail -s deafult

- To view application in web browser run
gcloud app browse
```

### run docker application in cloud shell and access it using another cloudshell with curl http://localhost:8080/

```
docker run --rm -p 8080:8080 gcr.io/{PROJECT_ID}/hello-app:v1
```

### Submit cloudbuild.yaml by gcloud command

```
gcloud builds submit --config cloudbuild.yaml
```

### Build docker image and push to GCR with the help of gcloud

```
gcloud builds submit --tag gcr.io/{google_cloud_project_id}/hello-world .
```

### mount filestore in VM with server address

```
sudo apt-get -y update && sudo apt-get -y install nfs-common
sudo mkdir -p /mnt/test
sudo mount 10.0.134.23:/filshareName /mnt/test
sudo chmod go+rw /mnt/test
```

### Policy role inherit from top to download

- `Organization-->Folder-->Project-->Resource`
  i.e Sawan has "viewer" role in organinzation. Then it will automatically inherit to all child folder,project,resource.
  
  ```
  {
  	"binding": [
  	{
  		members: [
  			"user:raha@example.com"
  		],
  		"role": "roles/storage.objectViewer"
  	  }
  	]
  	"etag": "wjehqoi"
  	"version": 1
  }
  ```

### gcsfuse command for mount to gcp bucket with gke with alpine linux images i.e. node with GKE application pod

- Create startup.sh
  
  ```
  MOUNT_DIR_PATH="/app/logs"
  BUCKET_NAME="tyh-dev-pharmacy-001"
  BUCKET_DIR_NAME="tyh-poc-logs"
  GCP_CREDENTIALS_JSON_PATH="/app/tyh-dev-1234567890.json"
  mkdir ${MOUNT_DIR_PATH} && /root/go/bin/gcsfuse --key-file=${GCP_CREDENTIALS_JSON_PATH} --only-dir=${BUCKET_DIR_NAME} ${BUCKET_NAME} ${MOUNT_DIR_PATH}
  ```

- Create Dockerfile
  
  ```
  FROM node:16.17-alpine3.15
  
  # add required tools and dependencies
  RUN apk add --no-cache ca-certificates fuse openssl wget curl go git && update-ca-certificates
  WORKDIR /app
  RUN git clone https://github.com/GoogleCloudPlatform/gcsfuse.git
  WORKDIR /app/gcsfuse
  RUN go install .
  RUN ["chmod", "+x", "/root/go/bin/gcsfuse"]
  WORKDIR /app
  COPY ["package.json", "package-lock.json","./"]
  COPY ["tyh-dev-1234567890.json","./"]
  RUN npm add
  COPY . /app
  RUN ["chmod", "+x", "/app/startup.sh"]
  ENTRYPOINT ["/app/startup.sh"]
  ```

- Create k8s-deployment.yaml
  
  ```
  lifecycle:
            preStop:
              exec:
                command:
                - fusermount
                - -u
                - /app/logs
  ```

### `Policy analyzer` in IAM

- It is used to create query from template `who access what resources etc`

### Zero downtime with rolling update in GKE deployed application

```
spec:
  replicas: 1
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
kubectl rollout restart deployment $app_name -n $namespace --message="version upgrade"
```

### Access private rdp VM through IAP tunnel user

- use IAP-Desktop application
- Create Firewall rule
  
  ```
  Name : iap-tcp
  source: rdp-VM-IP
  destination: 3389
  ```

### find and fetch service account key with gcloud command

```
gcloud beta iam service-accounts keys get-public-key KEY_ID \
    --iam-account=SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
    --output-file=FILENAME
```

### add custom compte machine `Worker pool`  for execute build steps as cloudbuild privately which defined in Cloudbuil.yaml .

```
steps:
  - name: 'gcr.io/cloud-builders/kubectl'
    args: ['apply', '-f', 'k8/deploymentprod.yaml']
    id: apply-deployment
    env:
    - 'CLOUDSDK_COMPUTE_ZONE=${_ZONE}'
    - 'CLOUDSDK_CONTAINER_CLUSTER=${_GKE_CLUSTER}'
    waitFor: ['delete-deployment']
substitutions:
    #GCP Specific configuration. Please DON'T change anything
    _PROJECT: tyh-prd-svc-poc
    _ZONE: asia-south1
    _GKE_CLUSTER: tyh-poc-prod-gke    
options:
    substitution_option: 'ALLOW_LOOSE'
    workerPool:
      'projects/tyh-prd-svc-poc/locations/asia-south1/workerPools/gke-private-pool'
```

### GCP storage bucket mount to GKE application pod

https://cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver

https://chimbu.medium.com/access-cloud-storage-buckets-as-volumes-in-gke-c2e405adea6c

- To enable the driver on an existing Standard cluster
  
  ```
  gcloud container clusters update tyhpockubernetes --update-addons GcsFuseCsiDriver=ENABLED --region=asia-south1
  ```
- Create service account
  
  ```
  kubectl create serviceaccount k8s-gcs --namespace default
  ```
- Create an IAM service account for your application or use an existing IAM service account instead
  
  ```
  gcloud iam service-accounts create k8s-gcs-bucket --project=tyh-dev-tyolpo
  ```
- You can grant the role to your IAM service account to only access a specific Cloud Storage bucket
  
  ```
  gcloud storage buckets add-iam-policy-binding gs://tyh-dev-response-001 --member "serviceAccount:k8s-gcs-bucket@tyh-dev-tyolpo.iam.gserviceaccount.com" --role "editor"
  ```
- Allow the Kubernetes service account to impersonate the IAM service account by adding an IAM policy binding between the two service accounts
  
  ```
  gcloud iam service-accounts add-iam-policy-binding k8s-gcs-bucket@tyh-dev-tyolpo.iam.gserviceaccount.com --role roles/iam.workloadIdentityUser --member "serviceAccount:tyh-dev-tyolpo.svc.id.goog[default/k8s-gcs]"
  ```
- Annotate the Kubernetes service account with the email address of the IAM service account
  
  ```
  kubectl annotate serviceaccount k8s-gcs --namespace default iam.gke.io/gcp-service-account=k8s-gcs-bucket@tyh-dev-tyolpo.iam.gserviceaccount.com
  ```
- Configure resources for the sidecar container overwrite deafult value
  
  ```
  apiVersion: v1
  kind: Pod
  metadata:
  annotations:
    gke-gcsfuse/volumes: "true"
    gke-gcsfuse/cpu-limit: 500m
    gke-gcsfuse/memory-limit: 100Mi
    gke-gcsfuse/ephemeral-storage-limit: 50Gi
  ```
- Consume the CSI ephemeral storage volume in a Pod
  
  ```
  apiVersion: v1
  kind: Pod
  metadata:
  name: gcs-fuse-csi-example-ephemeral
  namespace: NAMESPACE
  annotations:
    gke-gcsfuse/volumes: "true"
  spec:
  terminationGracePeriodSeconds: 60
  containers:
  - image: busybox
    name: busybox
    volumeMounts:
    - name: gcs-fuse-csi-ephemeral
      mountPath: /app/logs
      readOnly: false
  serviceAccountName: KSA_NAME
  volumes:
  - name: gcs-fuse-csi-ephemeral
    csi:
      driver: gcsfuse.csi.storage.gke.io
      readOnly: true
      volumeAttributes:
        bucketName: tyh-dev-response-001
        mountOptions: "implicit-dirs"
  ```
- Disable the Cloud Storage FUSE CSI driver
  
  ```
  gcloud container clusters update CLUSTER_NAME --update-addons GcsFuseCsiDriver=DISABLED
  ```

### FileStore mount in GKE deployed application pod
