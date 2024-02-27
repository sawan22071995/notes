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

##### 2. Error

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

##### 3. Error:

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
