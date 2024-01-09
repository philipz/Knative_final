# Knative with OpenTelemetry

## Create container image

1. `mvn spring-boot:build-image`
2. `docker build -t philipz/otel-logback:agent .`
3. `docker push philipz/otel-logback:agent`

## Deploy Knative Serving with Opentelemetry-collector by sidecar

1. kubectl create configmap collector-config --from-file=config.yaml=otel-grafana.yml
2. kubectl apply -f run-service-knative.yaml
