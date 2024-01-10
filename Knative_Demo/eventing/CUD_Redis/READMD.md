# Use Knative Eventing to Create, Update, or Delete the Redis.

## Prerequisite

* Python 3.7.9
* Docker Desktop
* Kind
* kubectl CLI
* Kn CLI 

## Deploy Redis deployment and service

You need to install Docker, Kind, and kubectl. After downloading Docker, Kind, and kubectl, you must push the image to the Kind (Kubernetes clusters). Then, use the following command to deploy the Redis on your cluster: `kubectl apply -f dep.yaml`. This command deploys the deployment. Next, run `kubectl apply -f service.yaml` to deploy the service on the cluster.

# Create cud-redis container image

Run `docker build -t philipz/cud-redis .` and push `docker push philipz/cud-redis`

## Deploy the deployment, service, and trigger

Run `kubectl apply -f app.yaml` to deploy the CUD_Redis eventing to the cluster and create a trigger to listen on specific borker.

## Check if components are working

1. `kubectl get ns knative-samples --show-labels`
2. `kubectl --namespace knative-samples get deployments cud-redis`
3. `kubectl --namespace knative-samples get svc cud-redis`
4. `kubectl -n knative-samples get trigger cud-redis`

## Send CloudEvent to the Broker

Run the command `kubectl --namespace knative-samples run curl --image=radial/busyboxplus:curl -it` to create a service that allows us to input commands. The command used to check CRUD operations is in [input.txt](./input.txt). After testing, go to the PostgreSQL CLI to see the results.

## Delete all componets

1. Use the command `kubectl delete -f app.yaml` to delete the entire service, including the trigger, and eventing components.

2. Run `kubectl delete -f dep.yaml -f service.yaml` to delete the Redis deployment and service.


