# Run the project locally

```bash
docker-compose up --build
```
* Type Ctrl-C or just exit the terminal
```bash
docker-compose down -v
docker-compose up -d
```
* Create admin user first
```bash
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
* Go to 127.0.0.1:8000 or 20.52.185.205:8000 (VM IP)

# Deploy the project to a kubernetes cluster

* connect to cluster

## persistent volumes
```bash
kubectl apply -f k8s/db/postgres-pvc.yml
```
## configmaps
### create fastapi configmap
```bash
kubectl create configmap django-config --from-env-file=k8s/django/django.env
```

## deployments
```bash
kubectl apply -f k8s/db/postgres-deployment.yml
kubectl apply -f k8s/django/django-deployment.yml
```

## services
```bash
kubectl apply -f k8s/db/postgres-clip.yml
kubectl apply -f k8s/django/django-clip.yml

```
## secrets
* pg secret

```bash
kubectl create secret generic pg-user \
--from-literal=PGUSER=<put user name here> \
--from-literal=PGPASSWORD=<put password here>
```
* tls secret
```bash
cd nginx/certs
kubectl create secret generic tls-secret \ 
 --from-file=tls.crt=server.crt \             
 --from-file=tls.key=server.key\             
 --from-file=ca.crt=ca_bundle.crt
```

## ingress

* allow routing. Get the name of your network interface, e.g. eth0 and run
```bash
sudo ufw allow in on eth0 && sudo ufw allow out on eth0
sudo ufw default allow routed
```

* apply ingress yml file(s)
```bash
kaf k8s/ingress/django-ingress-.yml # for http only
kaf k8s/ingress/django-ingress-ssl.yml # for https
```

## Application overview

![Image of Yaktocat](assets/img/fastapi-lab.png)
# Links
* [Control startup and shutdown order in Compose](https://docs.docker.com/compose/startup-order/)

* [Github: create a personla access token for packages](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

* [Configure docker to use with github packages](https://docs.github.com/en/packages/guides/configuring-docker-for-use-with-github-packages)

* [create kubernetes secret to access github packages](https://stackoverflow.com/questions/61912589/how-can-i-use-github-packages-docker-registry-in-kubernetes-dockerconfigjson)

* [kubernetes ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
