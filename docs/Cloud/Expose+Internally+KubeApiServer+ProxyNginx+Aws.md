# Provide developers with secure access to the Kubernetes API server of a private Amazon EKS cluster for the purpose of troubleshooting and debugging cloud-deployed applications.

![RequestFlowDiagram](https://github.com/sawan22071995/notes/blob/main/docs/Cloud/Nginx+KubeAPi.png?raw=true)

### Context:

- The EKS cluster is configured with private endpoints, meaning the Kubernetes API server is not directly accessible from the public internet.

- Developers need to access the API server to debug and troubleshoot issues that cannot be resolved through other means.

### Use Case Description:

- **Actors**: Developers, DevOps Engineers

- **Precondition**: Developers have appropriate permissions to access the cluster and perform troubleshooting.

- **Trigger**: Need to diagnose issues within the EKS cluster that require direct interaction with the Kubernetes API server.

### Scenario:

- **Authentication**: Developers authenticate through a secure method to gain temporary access to the Kubernetes API server.

- **Access Method**: Developers access the API server via a secure channel, such as a bastion host or VPN.

- **Debugging**: Developers perform necessary debugging and troubleshooting tasks.

- **Termination**: Access is terminated when the troubleshooting session is complete.

### Pre-Requisite

1. EC2 Computer Instance

2. Elastic Kubernetes Service(eks)

3. AWS Account with admin access (or with minimum required permission IAM,EKS,Route53,LB,EC2 etc.)

4. Nginx Software installed in EC2 Instance

5. Automation Script | Automation Job - Optional

6. Jenkins - Optional

7. VPN access to Nginx Server from System

### Steps to be Peformed for Installation and Setup

### Support Me

**If you find my content useful or enjoy what I do, you can support me by buying me a coffee. Your support helps keep this website running and encourages me to create more content.**

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/sawanchokso)

**Your generosity is greatly appreciated!**

##### Thank you for your support!💚
 