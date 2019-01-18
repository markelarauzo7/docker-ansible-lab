
```bash
    ./create-network.sh
```

As a single container:

docker build -t docker-ansible --build-arg id_rsa_pub=id_rsa.pub .

docker run -d docker-ansible 

As a multi container application:

docker-compose build --build-arg id_rsa_pub=id_rsa.pub

docker-compose up -d --no-build


./ansible-setup.py up

ansible -i hosts all -m ping -u root -i hosts

./ansible-setup.py down
