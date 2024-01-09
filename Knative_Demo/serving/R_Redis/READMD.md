# If toy want to modify the code you need to install python3.7.9!
# If you  jsut want to run the experiment.
You need to install docker and kind,kubectl,after download docker and kind,kubectl,you need to push the image to the kind(kubernetes cklusters)
# Create serving
use command below can deploy serving to your kind cluster
cmd:kubectl apply -f app.yaml
# Verification
use below command:
"kubectl get ksvc r-redis -n knative-samples  --output=custom-columns=NAME:.metadata.name,URL:.status.url"
# Check Serving.
use  curl to send "GET" to this link:
http://r-redis.knative-samples.127.0.0.1.sslip.io/read/<your_key>
# Delete the serving
use cmd:"kubectl delete -f app.yaml"


