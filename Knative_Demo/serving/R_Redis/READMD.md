# Use Knative Serving to Read the Redis.

## Prerequisite

* Python 3.7.9
* Docker Desktop
* Kind
* kubectl CLI
* Kn CLI 

# Create r-redis container image

Run `docker build -t /philipz/r-redis .` and push `docker push /philipz/r-redis`

## Deploy the service

Run `kubectl apply -f app.yaml` to deploy the CUD_Redis eventing to the cluster and create a trigger to listen on specific borker.

# Check if components are working

1. `kubectl get ksvc r-redis -n knative-samples` or `kubectl get ksvc r-redis -n knative-samples --output=custom-columns=NAME:.metadata.name,URL:.status.url`

# Check Serving.
use  curl to send "GET" to this link:
http://r-redis.knative-samples.127.0.0.1.sslip.io/read/<your_key>

# Delete the serving

Use the command `kubectl delete -f app.yaml` to delete the service.


