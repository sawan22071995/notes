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
