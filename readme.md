
docker run -d docker-ansible --build-arg id_rsa.pub

./ansible-setup.py up

ansible -i hosts all -m ping -u root -i hosts

./ansible-setup.py down