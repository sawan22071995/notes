# ♾️ DevOps CI/CD Project with Jenkins, Ansible and Kubernetes(AKS) ♾️

![diagram](https://media.licdn.com/dms/image/D4D22AQHIULO9fciOzA/feedshare-shrink_800/0/1691052203983?e=1695254400&v=beta&t=rBTtYe9-EFqLSkGhlTMBVVb7F6gJJBrJapypU05t-sw)

### ✍Create new Ubuntu Virtual Machine and install Jenkins in it.

## ✍ Create new Ubuntu Virtual Machine and install Ansible in it.

## ✍ Create new user ansibleadmin and generate SSH key for it.

## ✍ On Jenkins dashboard install new plugin "Publish over SSH" and integrate Ansible with Jenkins.

## ✍ Install Docker on Ansible server and provide full rights to ansibleadmin on Docker.

## ✍ Create ansible host group in file /etc/ansible/host.

## ✍ Add self ssh key(ssh-copy-id localhost) so that Ansible playbook can connect to local host.

## ✍ Create Ansible playbook to create Docker image and push that Image to Docker-Hub.

## ✍ Create Jenkins job(CI_Job) to run the Ansible playbook.

## ✍ Create new Ubuntu Virtual Machine(Kube-Server) and install Azure CLI in it.

## ✍ Create AKS cluster on Azure Portal, login through Azure CLI and install aks cli.

## ✍ Create Deployment and Service Manifest files.

## ✍ Create group called kubernetes in /etc/ansible/hosts file.

## ✍ On Kube-Server enable password based authentication for "root" and set password for root.

## ✍ Copy ssh key of ansibleadmin of Ansible server to root user of Kube-Server so that playbook can interact with kubernetes as we have connected kubernetes via root user of Kube-Server.

## ✍ Create Ansible playbook to run Deployment and Service Manifest files.

## ✍ Create Jenkins deployment job(CD_Job) for Kubernetes.

## ✍ Modify CI_Job to trigger CD_Job after completion. Set build trigger in CI_Job using PollSCM.

## ✅ Verify the CI/CD by making change on GitHub Repo and confirm the changes on Application.
