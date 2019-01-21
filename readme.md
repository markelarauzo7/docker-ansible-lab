
```bash
    ./create-network.sh
```

As a single container:

docker build -t docker-ansible --build-arg id_rsa_pub=id_rsa.pub .

docker run -d --rm --name docker-test docker-ansible 

As a multi container application:

docker-compose build --build-arg id_rsa_pub=id_rsa.pub

docker-compose up -d --no-build

Ansible execution

./ansible-setup.py check <network>

ansible -i inventory all -m ping -u root

ansible-playbook -i inventory ansible/apache2.yaml

# Ansible

## Ansible terminology

1. Roles: Roles are good for organizing multiple, related Tasks and encapsulating data needed to accomplish those Tasks
2. Task: Actions to carry out in nodes. Tasks can should be executed using modules (but can be executed using shell command for example)
    as modules gather Facts(node status) and act idempotently
3. Facts*: Status of node
4. Playbook: Playbooks can run multiple Tasks and provide some more advanced functionality that we would miss out on using ad-hoc commands
5. Hosts: hosts to act upon. These can be grouped using labels [remote] [docker] for example
6. Handlers: A Handler is exactly the same as a Task (it can do anything a Task can), but it will only run when called by another Task

*Ansible facts all start with anisble_ and are globally available for use any place variables can be used: Variable files, Tasks, and Templates.
ansible -i ./inventory all -m setup -u root

## Roles
Roles have a directory structure like this:
    
    roles
        rolename
        - files
        - handlers
        - meta
        - templates
        - tasks
        - vars

 1. In files directory, we can add files that we'll want copied into our servers.
 2. In handlers directory, we can add all handlers needed by our playbook.
 3. Meta directory contains Role meta data, including dependencies.
 4. Template files can contain template variables, based on Python's Jinja2 template engine. Files in here should end in .j2.
 5. Vars directory contains a main.yml file which simply lists variables we'll use. This provides a convenient place for us to change configuration-wide settings. If you have sensitive information to add into a variable file, you can encrypt the file using ansible-vault.
 6. Include main.yml where all actions to be executed will be listed.

 