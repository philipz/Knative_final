# Use Knative Eventing to Create, Update, or Delete the PostgreSQL Database.

A simple web app written in Python that you can use to test knative eventing. It shows how to consume a CloudEvent in Knative eventing, and optionally how to respond back with another CloudEvent in the http response, by adding the Cloud Eventing headers outlined in the Cloud Events standard definition.

## Prerequisite

* Python 3.7.9
* Docker Desktop
* Kind
* kubectl CLI
* Kn CLI 

## Deploy PostgreSQL deployment and service

You need to install Docker, Kind, and kubectl. After downloading Docker, Kind, and kubectl, you must push the image to the Kind (Kubernetes clusters). Then, use the following command to deploy the PostgreSQL database on your cluster: `kubectl apply -f dep.yaml`. This command deploys the deployment. Next, run `kubectl apply -f service.yaml` to deploy the service on the cluster.

## Create a PostgreSQL table and insert data

Run the command `kubectl get pods -n knative-samples` to check the names of the pods. In this part, the pod name is: *postgres-deployment-58cdc49bc9-zddbw*.

Then, run `kubectl exec -it postgres-deployment-58cdc49bc9-zddbw -n knative-samples -- /bin/sh` to access the PostgreSQL bash. Once in the bash, you need to create a table using the command provided in the file [create_db.txt](./create_db.txt).

## Create cud-postgres container image

Run `docker build -t philipz/cud-postgres .` and push `docker push philipz/cud-postgres`

## Deploy the Knative broker, deployment, service, and trigger

Run `kubectl apply -f app.yaml` to deploy the CUD_Postgres eventing to the cluster and create a trigger to listen on specific borker.

## Check if components are working

1. `kubectl get ns knative-samples --show-labels`
2. `kubectl --namespace knative-samples get deployments cud-postgres`
3. `kubectl --namespace knative-samples get svc cud-postgres`
4. `kubectl -n knative-samples get trigger cud-postgres`

## Send CloudEvent to the Broker

Run the command `kubectl --namespace knative-samples run curl --image=radial/busyboxplus:curl -it` to create a service that allows us to input commands. The command used to check CRUD operations is in [input.txt](./input.txt). After testing, go to the PostgreSQL CLI to see the results.

## Delete all componets

1. Use the command `kubectl delete -f app.yaml` to delete the entire service, including the broker, trigger, and eventing components.

2. Run `kubectl delete -f dep.yaml -f service.yaml` to delete the PostgreSQL deployment and service.