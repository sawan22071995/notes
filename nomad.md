# Nomad Notes

## Getting NOMAD Running

### official Documenttation

[Architecture | Nomad | HashiCorp Developer](https://developer.hashicorp.com/nomad/docs/concepts/architecture)

### Introduction to Nomad

- Much simpler alternative for k8s
- It helps to deploy, manage, and scale container for your environment
- It will helps us to deploy container on-prem,at the edge, and any cloud plateform .
- It provide multi-region and multi-datacenter support
- Nomad can scale a thousands node in a single cluster
- It support non-containerized worksload as well such as VM,binaries and more
- Tight integration with hashicorp ecosystem
- Orchestrate any application like
  1. Containarized
  2. Non-Containarized
  3. Batch Application
  4. Java Apps

### Nomad Components

1. Node 
   A physical or VM in the cluster . A node is a machine running in the Nomad Agent.

2. Agent
   
   Long Running daemon running on every member of the Nomad cluster. Agent can run in either client or server mode. This is essentially the binary that downloaded from Hshicorp.
   
   ##### Server : A agent running on a server that holds the global state of the cluster and participate in scheduling decision.
   
   #### Clients : An agent that fingerprints the host to determine the capablities, resources, and available drivers. Responsible for running workloads, such as containers.

3. Jobs  
   
   Defination of how a workloads should be scheduled. The Job specification(spec) is composed of one or more task groups , and each task defines a series of resource configuration and constraints.
   A job is submitted to Nomad and represents a desired state . for example run 3 instances of my application using the Docker image and spread them across three nodes to ensure high availablity.

4. Job Specification(jobspec)
   
   An HCL configuration file on disk which describe how a workload should be scheduled.
   It contains multiple stanza that defines configuration such as jobs, groups, tasks, services and resources for the application.
   
   ![alt text](https://github.com/sawan22071995/notes/blob/main/job-specification-file.png?raw=true)

5. Driver
   
   Pluggable components that executes a task and provide resource isolation.
   It must be installed/available before task can be executed. For example if you submit a job to schedule Docker Container Docker must be available on the Nomad clinets to use.
   For Example docker, java, podman, and raw-exec.

6. Task
   
   A command service application or "set of work" to be executed by Nomad.
   Tasks are executed by their driver.
   Exampls Include:
   Runs these container
   Execute these commands
   Run this Java application from .jar file
   
   ![alt text](https://github.com/sawan22071995/notes/blob/main/task-example.png?raw=true)

7. Task Group
   
   A collection of individual task that should be co-located on the same node.
   Any task within the defined group will be placed on the same Nomad client.
   This is especially useful for applications that require low latency or have high throughput to another application on task group.
   
   ![alt text](https://github.com/sawan22071995/notes/blob/main/task-group-example.png?raw=true)

8. Evaluation
   
   A calculation performed by the Nomad server to determine what action(s) need to take place to execute a job.
   Nomad performs evaluation whenever jobs are submitted or client state changes to determine if what changes need to be made to ensure the desired state.

9. Allocation
   
   The mapping of task in a job to clients is doing using allocations.
   An allocations used to declare that a set of tasks in a job should be run on a particular node.
   Allocation can fail if there are not enough resource to executed the task, a node is down etc.

### Scheduling Workflow in Nomad

![alt text](https://github.com/sawan22071995/notes/blob/main/scheduling-workflow.png?raw=true)

### Nomad Architecture

#### Datacenter

In the context of Nomad, a datacenter typically refers to a physical or virtual location where you run your infrastructure, such as a set of servers or nodes. These nodes can be in the same physical location or distributed across multiple locations.

The primary function of Nomad in a datacenter is to schedule and manage jobs and tasks. Nomad allows for efficient utilization of resources by automatically scheduling tasks on available resources and dynamically scaling the cluster based on demand.

```
-----------------------
nomad.hcl
-----------------------
datacenter "dc1" {
  # Configuration specific to datacenter "dc1"
  name = "Datacenter 1"
  region = "US-East"
  data_dir = "/var/lib/nomad/dc1"
  acl = "management"
  server {
    enabled = true
    bootstrap_expect = 3
  }
}

datacenter "dc2" {
  # Configuration specific to datacenter "dc2"
  name = "Datacenter 2"
  region = "EU-West"
  data_dir = "/var/lib/nomad/dc2"
  acl = "default"
  server {
    enabled = true
    bootstrap_expect = 5
  }
}

server {
  enabled = true
  bootstrap_expect = 3
}

client {
  enabled = true
  servers = ["nomad-server-1:4647", "nomad-server-2:4647", "nomad-server-3:4647"]
}

# Define the default datacenter for nodes that don't specify one
data_dir = "/var/lib/nomad"
```

#### [ Datacenter [ server + Client(Docker) ] ]

### Region

Collection of multiple datacenter often grouped geographically

### Server

The primary component of the Nomad architecture is the server. The servers handle the scheduling and management of the jobs and tasks that are submitted to the Nomad cluster.

### Client

The Nomad client is responsible for running the actual tasks and jobs that are submitted to the Nomad cluster. The client communicates with the servers and agents to request new tasks and jobs and report the status of the tasks and jobs that are running.

### Single Region Architecture

![alt text](https://github.com/sawan22071995/notes/blob/main/single-region-arch.png?raw=true)

### Multi Region Architecture

![alt text](https://github.com/sawan22071995/notes/blob/main/multi-region-arch.png?raw=true)

### Comparing Nomad to Kubernetes

Nomad is primarily task-scheduling plateform and can't orchestrate load balancing , config management and routing etc.

Nomad can scale to millions of containers (check out the 1 million and 2 million
container challenge HashiCorp did)

![alt text](https://github.com/sawan22071995/notes/blob/main/nomad-vs-k8s.png?raw=true)

### Installing Nomad

[Installing Nomad | Nomad | HashiCorp Developer](https://developer.hashicorp.com/nomad/docs/install)

#### Installing Nomad on Linux Using Package Manager

1. Log in to the Linux server
2. Use the following commands to install Nomad (this example will work with
   Amazon Linux)
   
   ```
   $ sudo yum install -y yum-utils
   $ sudo yum-config-manager --add-repo
   https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
   $ sudo yum -y install nomad
   ```
3. Alternatively, you can use this for RHEL
   
   ```
   $ sudo yum install -y yum-utils
   $ sudo yum-config-manager --add-repo
   https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
   $ sudo yum -y install nomad
   ```

   

### Installing Nomad Manually In Linux

1. Log in to the Linux server

2. Download Nomad from https://releases.hashicorp.com/nomad
   
   ```
   $ wget https://releases.hashicorp.com/nomad/<version>
   ```

3. Unzip the downloaded file and delete the zip file:
   
   ```
   $ unzip nomad nomad_1.4.3_linux_amd64.zip
   $ sudo rm nomad_1.4.3_linux_amd64.zip
   ```

4. Move the Nomad binary so it's available on your $PATH:
   
   ```
   $ sudo mv /nomad /usr/local/bin
   ```

5. Create the local Nomad directories:
   
   ```
   $ sudo mkdir /etc/nomad.d
   ```

6. Create the Nomad user:
   
   ```
   $ sudo useradd --system --home /etc/nomad.d --shell
   /bin/false nomad
   ```

7. Set permissions for the new directory:
   
   ```
   $ sudo chown -R nomad:nomad /etc/nomad.d/
   $ sudo chmod 700 /etc/nomad.d
   ```

8. Create the Nomad service file at /etc/system/system/nomad.service
   and copy the configuration to this file.
   
   ```
   $ sudo touch /etc/systemd/system/nomad.service
   ```

  

### Starting the Nomad Services

1. Open /etc/nomad.d/nomad.hcl in a text editor (vi, nano, etc.)
   
   ```
   $ sudo vi /etc/nomad.d/nomad.hcl
   ```

2. Create the file based on the requirenment for example:
   
   ```
   name = "nomad_server_a"
   
   # Directory to store agent state
   data_dir = "/var/lib/nomad"
   
   # Address the Nomad agent should bing to for networking
   # 0.0.0.0 is the default and results in using the default private network interface
   # Any configurations under the addresses parameter will take precedence over this value
   bind_addr = "0.0.0.0"
   
   advertise {
     # Defaults to the first private IP address.
     http = "10.x.x.x" # must be reachable by Nomad CLI clients
     rpc  = "10.x.x.x" # must be reachable by Nomad client nodes
     serf = "10.x.x.x" # must be reachable by Nomad server nodes
   }
   
   ports {
     http = 4646
     rpc  = 4647
     serf = 4648
   }
   
   # TLS configurations
   tls {
     http = true
     rpc  = true
   
     ca_file   = "/etc/certs/ca.crt"
     cert_file = "/etc/certs/nomad.crt"
     key_file  = "/etc/certs/nomad.key"
   }
   
   # Specify the datacenter the agent is a member of
   datacenter = "dc1"
   
   # Logging Configurations
   log_level = "INFO"
   log_file  = "/var/log/nomad.log"
   
   # Server & Raft configuration
   server {
     enabled          = true
     bootstrap_expect = 3
     encrypt          = "Do7GerAsNtzK527dxRZJwpJANdS2NTFbKJIxIod84u0=" 
     license_path     = "/etc/nomad.d/nomad.hclic"
     server_join {
       retry_join = ["10.4.23.44", "10.4.54.112", "10.4.56.33"]
     }
     default_scheduler_config { 
       scheduler_algorithm = "spread" # change from default of binpack
     } 
   }
   
   # Client Configuration - Disable for Server nodes
   client {
     enabled = false
   }
   
   # Enable and configure ACLs
   acl {
     enabled    = true
     token_ttl  = "30s"
     policy_ttl = "60s"
     role_ttl   = "60s"
   }
   
   # [optional] Specifies configuration for connecting to Consul
   consul { 
     address = "consul.example.com:8500"
     ssl = true
     verify_server_hostname = true
   }
   
   # [optional] Specifies configuration for connecting to Vault
   vault {
     enabled     = true
     address     = "https://vault.example.com:8200"
     create_from_role = "nomad-cluster"
   }
   ```

3. Save the file
   
   ```
   ESC:wq
   ```

4. Start the Nomad service
   
   ```
   $ sudo systemctl start nomad
   ```

5. Validate the Nomad service is running
   
   ```
   $ sudo systemctl status nomad
   ```

6. Check to see if Nomad server is responding
   
   ```
   $ nomad server members
   ```

7. Optionally, view the journal logs
   
   ```
   $ sudo journalctl -b -u nomad
   ```

### Starting the Nomad Service – Dev Mode

```
$ nomad agent –dev –bind 0.0.0.0
```

- When Nomad started as development mode It is known as "dev agent & dev mode"
- This quickly start a single agent on your local machine and acts as server and client for testing
- Dev Mode never used for Production...It only for testing
- To start Nomad as client or server we first need a configuration file
- It is written in HCL contains all the information needed for Nomad to run
- configuration file differes for Nomad server vs Nomad Client agent
- Driver/Pre-requisite must be installed on Nomad Clients Such as "Docker"
- Other configuration such as Nomad User, directories, permissions and pre-requsite must be done before starting nomad server
  - systemd config file
  
  - Local Nomad user to run the service
  
  - Directories for storing config and logs

- Nomad Agents COnfiguration files with primary parameters
  
  ```
  name                 - name of the Nomad Agent
  data_dir             - directory where Nomad will store agent state(Data)
  bind_addr            - what IP address the Nomad agent should bind to for networking
  advertise {}         - what IP(s) to use to advertise for network services
  ports {}             - specify ports used for the different services
  tls {}               - TLS configuration
  datacenter           - define what datacenter the local agent is a member of
  log_file             - where does store Nomad Logs
  server {}            - Nomad Server configuration(No need for clients)
  client {}            - Nomad Client configuration(No need for servers) 
  acl {}               - ACL configuration (enable, TTL)
  vault {}             - configuration for vault Integration
  consul {}            - cofiguration for Consul integration
  {}                   = It means stanza
  ```

- However, you can start Nomad agent manually if you want using the
  Nomad command:
  
  ```
  # Start Nomad by point to a config file
  $ nomad agent –config /etc/nomad.d/server.hcl
  # Start Nomad by pointing to a directory
  $ nomad agent –config /etc/nomad.d
  ```

### Nomad agent Configuration file - server.hcl

```
name = "nomad_server_a"

# Directory to store agent state
data_dir = "/var/lib/nomad"

# Address the Nomad agent should bing to for networking
# 0.0.0.0 is the default and results in using the default private network interface
# Any configurations under the addresses parameter will take precedence over this value
bind_addr = "0.0.0.0"

advertise {
  # Defaults to the first private IP address.
  http = "10.x.x.x" # must be reachable by Nomad CLI clients
  rpc  = "10.x.x.x" # must be reachable by Nomad client nodes
  serf = "10.x.x.x" # must be reachable by Nomad server nodes
}

ports {
  http = 4646
  rpc  = 4647
  serf = 4648
}

# TLS configurations
tls {
  http = true
  rpc  = true

  ca_file   = "/etc/certs/ca.crt"
  cert_file = "/etc/certs/nomad.crt"
  key_file  = "/etc/certs/nomad.key"
}

# Specify the datacenter the agent is a member of
datacenter = "dc1"

# Logging Configurations
log_level = "INFO"
log_file  = "/var/log/nomad.log"

# Server & Raft configuration
server {
  enabled          = true
  bootstrap_expect = 3
  encrypt          = "Do7GerAsNtzK527dxRZJwpJANdS2NTFbKJIxIod84u0=" 
  license_path     = "/etc/nomad.d/nomad.hclic"
  server_join {
    retry_join = ["10.4.23.44", "10.4.54.112", "10.4.56.33"]
  }
  default_scheduler_config { 
    scheduler_algorithm = "spread" # change from default of binpack
  } 
}

# Client Configuration - Disable for Server nodes
client {
  enabled = false
}

# Enable and configure ACLs
acl {
  enabled    = true
  token_ttl  = "30s"
  policy_ttl = "60s"
  role_ttl   = "60s"
}

# [optional] Specifies configuration for connecting to Consul
consul { 
  address = "consul.example.com:8500"
  ssl = true
  verify_server_hostname = true
}

# [optional] Specifies configuration for connecting to Vault
vault {
  enabled     = true
  address     = "https://vault.example.com:8200"
  create_from_role = "nomad-cluster"
}
```

### Nomad agent configuration file - client.hcl

```
# Basic Starter Configuration Used for Nomad Course Demonstrations
# This is NOT a Secure Complete Nomad Client Configuration

name = "nomad_client_a"

# Directory to store agent state
data_dir = "/etc/nomad.d/data"

# Address the Nomad agent should bing to for networking
# 0.0.0.0 is the default and results in using the default private network interface
# Any configurations under the addresses parameter will take precedence over this value
bind_addr = "0.0.0.0"

advertise {
  # Defaults to the first private IP address.
  http = "10.0.103.60" # must be reachable by Nomad CLI clients
  rpc  = "10.0.103.60" # must be reachable by Nomad client nodes
  serf = "10.0.103.60" # must be reachable by Nomad server nodes
}

ports {
  http = 4646
  rpc  = 4647
  serf = 4648
}

# TLS configurations
tls {
  http = false
  rpc  = false

  ca_file   = "/etc/certs/ca.crt"
  cert_file = "/etc/certs/nomad.crt"
  key_file  = "/etc/certs/nomad.key"
}

# Specify the datacenter the agent is a member of
datacenter = "dc1"

# Logging Configurations
log_level = "INFO"
log_file  = "/etc/nomad.d/krausen.log"

# Server & Raft configuration
server {
  enabled = false
}

# Client Configuration
client {
  enabled = true
  
  server_join {
    retry_join = ["provider=aws tag_key=nomad_cluster_id tag_value=us-east-1"]
  }
}
```

### Nomad clients with a Nomad server for communication,

To register Nomad clients with a Nomad server for communication, you need to set up a Nomad cluster. Nomad is a cluster manager and scheduler that allows you to manage and deploy applications across a cluster of machines. The Nomad server is responsible for managing the cluster, and Nomad clients are the machines or nodes in the cluster that run your applications.

Here are the general steps to register Nomad clients with a Nomad server:

1. **Install Nomad**:
   
   - First, you need to install Nomad on all the machines that will serve as clients. You can download it from the official website or use a package manager suitable for your operating system.

2. **Configure Nomad Clients**:
   
   - Edit the Nomad client configuration file (`client.hcl`) on each client machine. The configuration file should specify the address of the Nomad server and other client-specific settings. For example:
     
     ```
     datacenter = "dc1"
     data_dir = "/var/lib/nomad"
     client {
       enabled = true
       servers = ["1.2.3.4:4647", "5.6.7.8:4647"]
     }
     
     
     ```

3. **Start the Nomad Client**:
   
   - Start the Nomad client on each machine using the `nomad agent -config client.hcl` command. This registers the client with the specified Nomad server.

4. **Nomad Server Configuration**:
   
   - On the Nomad server, you need to configure the server itself. Create a server configuration file (`server.hcl`) and specify the server settings. For example:
     
     ```
     datacenter = "dc1"
     data_dir = "/var/lib/nomad"
     server {
       enabled = true
       bootstrap_expect = 3
     }
     
     ```

5. **Start the Nomad Server**:
   
   - Start the Nomad server using the `nomad agent -config server.hcl` command. This will bootstrap the server and allow it to coordinate client registrations and job scheduling.

6. **Verify Registration**:
   
   - After starting both Nomad clients and the server, you can verify that the clients have successfully registered by checking the Nomad server logs or using the Nomad CLI. You can use commands like `nomad node status` to view the registered nodes.
   
   
