# Knative experiment sample

Knative with serving and eventing

## Prerequisite

* OS:osx
* CPU:darwin/arm64 m2
* Python:3.7.9
* Docker version 24.0.6
* kubernetes version:kind v0.20.0 go1.21.1 darwin/arm64
* Knative quickstart:lastest
* kubectl:latestest

## Create local environment

1. Create Kind cluster
```
cat <<EOF | kind create cluster --name knative --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
    ## expose port 31080 of the node to port 80 on the host
  - containerPort: 31080
    hostPort: 80
    ## expose port 31443 of the node to port 443 on the host
  - containerPort: 31443
    hostPort: 443
EOF
```

2. Install Knative
```
kn quickstart kind --registry
```

## To run this experiment you must run eventing first!!

For [Knative eventing](./Knative_Demo/eventing/): Refer to the **README.md** file located in the 'eventing' folder of each directory. Follow each step outlined in the file.

For [Knative serving](./Knative_Demo/serving/): After deploying the eventing components, you need to deploy the serving components to the same namespace in Kubernetes. The steps for this process are also detailed in the **README.md** file located in the 'serving' folder. Follow the instructions provided in the file.

## Knative with OpenTelemetry

## CloudEvents player input 
* Event Source: dev.knative.samples.helloworld //please see in file Knative_Demo/eventing/CUD_Postgres/app.yaml arrtribute: source
* Event Type : dev.knative.samples/helloworldsource //please see in file Knative_Demo/eventing/CUD_Postgres/app.yaml arrtribute: type
* Message: Create:{"cmd":"POST","key":1,"value":{"id":"1","name":"redis","price":"2000"}}
* Message: Change:{"cmd":"PUT","key":1,"value":{"id":"1","name":"python","price":"1500"}}
* Message: Delete:{"cmd":"DELETE","key":1,"value":{"id":"1"}}


