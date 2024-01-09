# If toy want to modify the code you need to install python3.7.9!
# If you  jsut want to run the experiment.
You need to install docker and kind,kubectl,after download docker and kind,kubectl,you need to pull the image to the kind(kubernetes cklusters),use bellow command to deploy the Redis Database on you cluster,cmd:"kubectl apply -f redis_dep.yaml" to deploy deploymet,nedt run cmd:"kubectl apply -f redis_sev.yaml" to deploy service on the cluster.
# After create a redis service.
run cmd: kubectl get pods  -n knative-samples to check the pods name,in this part my id is:redis-deployment-55b654cbc9-6l4hk
# After get pod id.
run cmd:"kubectl exec -it redis-deployment-55b654cbc9-6l4hk -n knative-samples  -- /bin/sh" to go to Redis bash.
# After create databse and table.
run cmd:"kubectl apply -f app.yaml to deploy the CUD_Redis eventing to our cluster and create a trigger to listen on specific borker.
# Verify execute bellow code from top to down to  check you eventing is work.
"kubectl get ns knative-samples --show-labels"
"kubectl --namespace knative-samples get deployments cud-redis"
"kubectl --namespace knative-samples get svc cud-redis"
# Check trigger.
"kubectl -n knative-samples get trigger cud-redis"
# Run the Test.
First,run "kubectl --namespace knative-samples run curl --image=radial/busyboxplus:curl -it" to create a service to let'us to input command,
the command which use for check CUD is in input.txt,after testing go to 
the redis-cli to see the result.
# Delete the service
use cmd:"kubectl delete -f app.yaml" can delete whole service include broker and trigger and eventing.


