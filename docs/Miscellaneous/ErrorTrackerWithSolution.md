# Here you will get most of the Error with solution what we faced daily day to day life as a Cloud or devOps Engineer

### 1. Error

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

### 2. Error

Error: PythonPipBuilder:ResolveDependencies - {simplejson==3.17.2(sdist), pydantic-core==2.4.0(wheel), awslambdaric==2.0.7(wheel)}

##### Explanation:

We are facing this error while trying to run command `sam build` in AWS while building python application with python3.11 and try to run with eks jenkins cicd with agent having `python3.11, sam cli & AWS cli` .

##### Solution:

Update the archietecture type with respect to `sam-cli` archietecture i.e if its `arm64 or x86_64` in `template.yaml` file

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: An AWS Serverless Application Model template for arn:aws:lambda:ap-south-1:516638134243:function:axaws-cerebro-dev-knowledgebase-function function.
Resources:
  axawscerebrodevknowledgebasefunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: .
      Description: ''
      MemorySize: 128
      Timeout: 60
      Handler: knowledge_base.app.handler
      Runtime: python3.11
      AutoPublishAlias: live
      DeploymentPreference:
        Type: AllAtOnce
      Architectures:
        - x86_64
      EphemeralStorage:
        Size: 512
      EventInvokeConfig:
        MaximumEventAgeInSeconds: 21600
        MaximumRetryAttempts: 2
      PackageType: Zip
      SnapStart:
        ApplyOn: None
      Tags:
        Env: Dev
      VpcConfig:
        SecurityGroupIds:
          - sg-086191bf910edjkh67h
        SubnetIds:
          - subnet-0b23a6d131593977698d
          - subnet-0b383f54de7957e37998
        Ipv6AllowedForDualStack: false
      RuntimeManagementConfig:
        UpdateRuntimeOn: Auto

Outputs:
  axawscerebrodevknowledgebasefunction:
    Description: "Lambda Function ARN"
    Value: !GetAtt axawscerebrodevknowledgebasefunction.Arn
```

### 3. Error

Error: Failed to create changeset for the stack: axaws-cerebro-dev-knowledgebase-function, ex: Waiter ChangeSetCreateComplete failed: Waiter encountered a terminal failure state: For expression "Status" we matched expected path: "FAILED" Status: FAILED. Reason: User: arn:aws:sts::516638134243:assumed-role/axaws-cerebro-jenkins-dev-crossaccount-role/xactarget is not authorized to perform: cloudformation:CreateChangeSet on resource: arn:aws:cloudformation:ap-south-1:aws:transform/Serverless-2016-10-31 because no identity-based policy allows the cloudformation:CreateChangeSet action

##### Explanation:

We are facing error with python-3.11 tech stack application during `sam deploy --capabilities CAPABILITY_IAM`

##### Solution:

We need to add policy in IAM Role

```
 {
    "Version": "2012-10-17",
    "Statement": [{
"Effect": "Allow",
        "Action": "cloudformation:CreateChangeSet",
        "Resource": [
            "arn:aws:cloudformation:us-east-1:123123123123:stack/some-stack-name/*",
            "arn:aws:cloudformation:us-east-1:aws:transform/Serverless-2016-10-31"
    ]
 }]
}
```

[Controlling access with AWS Identity and Access Management - AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html)

### 4. Error

We are facing `slightly delay` in getting `response` from API request around `120 seconds` in `Intermittent connection` specially whenever try to connect after first attempt.

##### Explanation:

We are using `nginx load Balancer as proxy server in ec2 instance`, `Istio service mesh with ingress gateway` which use `Network Load Balancer` in aws and application running in `eks pod` with `Java 21` and `spring boot application` written in `Kotlin`.

###### Solution:

- In `Nginx server ec2 intance` Check telnet for dns name configured with NLB with 443 port and check IP address try 4-5 times and monitor responses.
  
  ```
  telnet test-poc.alb.example.com 443
  ```

- Copy the `IP address` for the telnet output which is working and connecting quickly without delay.

- make an entry in `/etc/hosts` file with with `IP address and DNS Name`
  
  ```
  vi /etc/hosts
  10.0.23.45 test-poc.alb.example.com
  ```

- It will solve problem and everytime request coming nginx will send traffic to specific Network Load Balancer IP only.

- `References:`
  
  ##### TCP connection delays
  
  When both cross-zone load balancing and client IP preservation are enabled, a client connecting to different IPs on the same load balancer may be routed to the same target. If the client uses the same source port for both of these connections, the target will receive what appears to be a duplicate connection, which can lead to connection errors and TCP delays in establishing new connections. You can prevent this type of connection error by disabling cross-zone load balancing. For more information, see [Cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#cross-zone-load-balancing).
  
  ##### Intermittent connection failure when client IP preservation is enabled
  
  When client IP preservation is enabled, you might encounter TCP/IP connection limitations related to observed socket reuse on the targets. These connection limitations can occur when a client, or a NAT device in front of the client, uses the same source IP address and source port when connecting to multiple load balancer nodes simultaneously. If the load balancer routes these connections to the same target, the connections appear to the target as if they come from the same source socket, which results in connection errors. If this happens, clients can retry (if the connection fails) or reconnect (if the connection is interrupted). You can reduce this type of connection error by increasing the number of source ephemeral ports or by increasing the number of targets for the load balancer. You can prevent this type of connection error by disabling client IP preservation or by disabling cross-zone load balancing.
  
  Additionally, when client IP preservation is enabled, connectivity might fail if the clients that are connecting to the Network Load Balancer are also connected to targets behind the load balancer. To resolve this, you can disable client IP preservation on the affected target groups. Alternatively, have your clients connect only to the Network Load Balancer, or only to the targets, but not both.
  
  [Troubleshoot your Network Load Balancer - Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-troubleshooting.html)  

### 5. Error

Error: 

- Application Pods logs : Standard Commons Logging discovery in action with spring-jcl: please remove commons-logging.jar from classpath in order to avoid potential conflicts
  Exception in thread "main" com.amazonaws.SdkClientException: Unable to execute HTTP request: secretsmanager.ap-south-1.amazonaws.com
  
          at com.amazonaws.http.AmazonHttpClient$RequestExecutor.handleRetryableException(AmazonHttpClient.java:1219)
          at com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeHelper(AmazonHttpClient.java:1165)
          at com.amazonaws.http.AmazonHttpClient$RequestExecutor.doExecute(AmazonHttpClient.java:814)
          at com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeWithTimer(AmazonHttpClient.java:781)
          at com.amazonaws.http.AmazonHttpClient$RequestExecutor.execute(AmazonHttpClient.java:755)
          at com.amazonaws.http.AmazonHttpClient$RequestExecutor.access$500(AmazonHttpClient.java:715)
          at com.amazonaws.http.AmazonHttpClient$RequestExecutionBuilderImpl.execute(AmazonHttpClient.java:697)
          at com.amazonaws.http.AmazonHttpClient.execute(AmazonHttpClient.java:561)
          at com.amazonaws.http.AmazonHttpClient.execute(AmazonHttpClient.java:541)
          at com.amazonaws.services.secretsmanager.AWSSecretsManagerClient.doInvoke(AWSSecretsManagerClient.java:2616)
          at com.amazonaws.services.secretsmanager.AWSSecretsManagerClient.invoke(AWSSecretsManagerClient.java:2583)
          at com.amazonaws.services.secretsmanager.AWSSecretsManagerClient.invoke(AWSSecretsManagerClient.java:2572)
          at com.amazonaws.services.secretsmanager.AWSSecretsManagerClient.executeGetSecretValue(AWSSecretsManagerClient.java:1205)
          at com.amazonaws.services.secretsmanager.AWSSecretsManagerClient.getSecretValue(AWSSecretsManagerClient.java:1177)
          at com.axis.thanos.OneGlanceStatementApplication$Companion.getSecret(OneGlanceStatementApplication.kt:64)
          at com.axis.thanos.OneGlanceStatementApplication$Companion.main(OneGlanceStatementApplication.kt:22)
          at com.axis.thanos.OneGlanceStatementApplication.main(OneGlanceStatementApplication.kt)
  
  Caused by: java.net.UnknownHostException: secretsmanager.ap-south-1.amazonaws.com
  
          at java.base/java.net.InetAddress$CachedLookup.get(InetAddress.java:988)
          at java.base/java.net.InetAddress.getAllByName0(InetAddress.java:1818)
          at java.base/java.net.InetAddress.getAllByName(InetAddress.java:1688)
          at com.amazonaws.SystemDefaultDnsResolver.resolve(SystemDefaultDnsResolver.java:27)
          at com.amazonaws.http.DelegatingDnsResolver.resolve(DelegatingDnsResolver.java:38)
          at org.apache.http.impl.conn.DefaultHttpClientConnectionOperator.connect(DefaultHttpClientConnectionOperator.java:112)
          at org.apache.http.impl.conn.PoolingHttpClientConnectionManager.connect(PoolingHttpClientConnectionManager.java:376)
          at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:103)
          at java.base/java.lang.reflect.Method.invoke(Method.java:580)
          at com.amazonaws.http.conn.ClientConnectionManagerFactory$Handler.invoke(ClientConnectionManagerFactory.java:76)
          at com.amazonaws.http.conn.$Proxy10.connect(Unknown Source)
          at org.apache.http.impl.execchain.MainClientExec.establishRoute(MainClientExec.java:393)
          at org.apache.http.impl.execchain.MainClientExec.execute(MainClientExec.java:236)
          at org.apache.http.impl.execchain.ProtocolExec.execute(ProtocolExec.java:186)
          at org.apache.http.impl.client.InternalHttpClient.doExecute(InternalHttpClient.java:185)
          at org.apache.http.impl.client.CloseableHttpClient.execute(CloseableHttpClient.java:83)
          at org.apache.http.impl.client.CloseableHttpClient.execute(CloseableHttpClient.java:56)
          at com.amazonaws.http.apache.client.impl.SdkHttpClient.execute(SdkHttpClient.java:72)
          at com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeOneRequest(AmazonHttpClient.java:1346)
          at com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeHelper(AmazonHttpClient.java:1157)
          ... 15 more

- Istio-Ingress-Gateway logs : lookup istiod.istio-system.svc on 10.96.0.10:53: read udp 10.44.0.4:33126->10.96.0.10:53: read: connection refused"
  2020-09-01T16:48:29.383977Z warn cache resource:default request:e0bdbb01-0c60-47bd-a9e1-e460b8c1da81 CSR failed with error: rpc error: code = Unavailable desc = connection error: desc = "transport: Error while dialing dial tcp: lookup istiod.istio-system.svc on 10.96.0.10:53: read udp 10.44.0.4:33126->10.96.0.10:53: read: connection refused", retry in 3200 millisec
  2020-09-01T16:48:29.384167Z error citadelclient Failed to create certificate: rpc error: code = Unavailable desc = connection error: desc = "transport: Error while dialing dial tcp: lookup istiod.istio-system.svc on 10.96.0.10:53: read udp 10.44.0.4:33126->10.96.0.10:53: read: connection refused"

##### Explanation:

We are using `EKS for application deployment` and `Istio for Service Mesh` for internal communication. So Whenever we deploy application it is successfully deploying in one node where istio-ingress-gateway deployed but whenever application increase replica and deployed in another new node It is giving error in `crashloopbackoff` for all pods in another node and application not deploying after multiple restart.

##### Solution:

1. We need to implement `node intercommunication`.

2. We can allow all the `ports` which used in `istio implementation` in `node security group`.
   
   [Istio Implements Ports]([Istio / Application Requirements](https://istio.io/latest/docs/ops/deployment/requirements/))

3. Allow or Create inbound rule for `node security group`.
   
   ```
   from_port : all
   to_port: all
   protocol: custom
   source: Self Node Security Group
   Description: Allow Intercommunication between nodes 
   ```

### 6. Error

cache: timed out waiting for the condition
  Warning  Failed            23m                  kubelet             Failed to pull image "artifactory.axisb.com/thanos-docker-local/istio/proxyv2:1.20.0": rpc error: code = Unknown desc = failed to pull and unpack image "artifactory.axisb.com/thanos-docker-local/istio/proxyv2:1.20.0": failed to extract layer sha256:256d88da41857db513b95b50ba9a9b28491b58c954e25477d5dad8abb465430b: failed to unmount /var/lib/containerd/tmpmounts/containerd-mount2008772348: failed to unmount target /var/lib/containerd/tmpmounts/containerd-mount2008772348: device or resource busy: unknown

##### Explanation:

We faced this while deploying application in eks version 1.25 with containerd only having installed istio service mesh in AWS with self Managed Node in EKS.

##### Solution:

The issue arises due to there is `DCS security agent` running on all `ec2 worker node` instances in EKS. due to the it will not able to unmount and the path because that agent process holding the path.

- ###### what is `DCS agent`?
  
  In AWS security, a DCS (Distributed Cloud Service) agent refers to the software component that runs on Amazon Elastic Compute Cloud (EC2) instances or other compute resources to enable Amazon GuardDuty, a threat detection service.
  
  The DCS agent collects and analyzes data from various sources on the instance, such as network traffic, system logs, and other runtime behavior data. It then sends this data securely to GuardDuty for further analysis and threat detection.
  
  Some key functions of the DCS agent include:
  
  1. Network Traffic Monitoring: The agent captures network traffic metadata, including source/destination IP addresses, ports, protocols, and packet details.
  2. System Log Collection: It collects and analyzes system logs from the operating system, applications, and AWS services running on the instance.
  3. Runtime Behavior Analysis: The agent monitors the runtime behavior of the instance, such as process execution, file access, and other activities, to detect potential threats or anomalies.
  4. Data Streaming: The collected data is securely streamed to GuardDuty for analysis and threat detection using machine learning and other security analytics techniques.
  
  The DCS agent is designed to have a minimal performance impact on the instance and is regularly updated to support new features and security enhancements. It plays a crucial role in GuardDuty's ability to detect potential threats and security incidents across AWS accounts and resources.

##### To stop `DCS agent` running process in EC2 instances . please run below command

```
ps -ef | grep -i sdcs; 
systemctl stop sisipsdaemon; 
systemctl disable sisipsdaemon; 
systemctl stop sisidsdaemon; 
systemctl disable sisidsdaemon; 
systemctl stop sisanddaemon; 
systemctl disable sisamddaemon; 
systemctl stop sisipsutildaemon; 
systemctl disable sisipsutildaemon;
ps -ef | grep -i sdcs;
```

### 7. Error

docker error "error:0A000086:SSL routines:tls_post_process_server_certificate:certificate verify failed:ssl/statem/statem_clnt.c:1889" in dockerfile while downloading installing packages

##### Explanation:

We faced this while installing package in dockerimage

##### Solution:

```
RUN apk add --no-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/v3.15/main \
    ca-certificates
RUN update-ca-certificates
```

### 8. Error

failed to get cpu utilization: unable to get metrics for resource cpu: unable to fetch metrics from resource metrics API: the server could not find the requested resource (get pods.metrics.k8s.io)

```
kubectl get hpa -n uat-app | grep app-test
app-test               Deployment/app-test              <unknown>/70%, <unknown>/70%   1         3         1          142d
```

##### Explanation:

The error is occurring when trying to get CPU utilization.
It's unable to fetch metrics from the resource metrics API.
The server couldn't find the requested resource, specifically "pods.metrics.k8s.io".
This error typically occurs when the Metrics Server is not properly installed or configured in your Kubernetes cluster. The Metrics Server is responsible for collecting resource metrics from kubelets and exposing them through the Metrics API for use by the Horizontal Pod Autoscaler and other components.

##### Solution:

- Check API resources: List all available API resources in your cluster:
  
  ```
  kubectl api-resources
  ```

- Check API versions: List all available API versions:
  
  ```
  kubectl api-versions | grep metrics.k8s.io
  ```

- `metrics.k8s.io/v1beta1` api missing in eks kubectl api-versions. EKS doesn't come with the Metrics Server pre-installed. You can install it using the following steps: a. Download the Metrics Server manifest:
  
  ```
  wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
  ```

- Edit the file to add the necessary flags for EKS: Open the components.yaml file and find the Metrics Server deployment. Add these flags to the container args:
  
  ```
  --kubelet-insecure-tls
  --kubelet-preferred-address-types=InternalIP
  ```

- Apply the manifest:
  
  ```
  kubectl apply -f components.yaml
  ```

- Verify the installation: After installation, check if the Metrics Server pod is running:
  
  ```
  kubectl get pods -n kube-system | grep metrics-server
  ```

- Wait for the API to become available: It may take a few minutes for the API to become available. You can check its status with:
  
  ```
  kubectl get apiservice v1beta1.metrics.k8s.io
  ```

- Test the metrics API: Once available, try accessing the metrics:
  
  ```
  kubectl top nodes
  kubectl get hpa -n uat-app | grep app-test
  app-test               Deployment/app-test              3%/70%, 23%/70%   1         3         1          142d
  ```
