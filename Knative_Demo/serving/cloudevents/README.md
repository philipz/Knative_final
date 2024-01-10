`# CloudEvents Player

![Build](https://img.shields.io/github/actions/workflow/status/ruromero/cloudevents-player/build.yaml)
[![amd64](https://img.shields.io/badge/container-amd64-blue)](https://quay.io/repository/ruben/cloudevents-player?tab=tags)
[![arm64](https://img.shields.io/badge/container-arm64-blue)](https://quay.io/repository/ruben/cloudevents-player?tab=tags)

- [Running the container image](#running-the-container-image)
- [Running the binary](#running-the-binary)
- [Running on Kubernetes](#running-on-kubernetes)
  * [Requirements](#requirements)
  * [Use .yaml file to deply application](#Use-yaml-file-to-deply-application)
- [Build](#build)
  * [JVM Build](#jvm-build)
  * [Quarkus dev mode](#quarkus-dev-mode)
  * [Native build](#native-build)
  * [Skip frontend build](#skip-frontend-build)
  * [Build the container image](#build-the-container-image)
- [Configuration](#configuration)
  * [Player Mode](#player-mode)
  * [Broker URI](#broker-uri)
  * [Broker Name and Namespace](#broker-name-and-namespace)
  * [CORS](#cors)

It is an application that can send and receive [CloudEvents](https://cloudevents.io/). Its purpose is to be deployed on a
[Knative Eventing](https://knative.dev/docs/eventing/) environment so that users can monitor received events in the Activity section and
also send events of the desired type to see if it is being forwarded back to the application through
the broker.

It supports both [Structured](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/http-protocol-binding.md#32-structured-content-mode)
and [Binary](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/http-protocol-binding.md#31-binary-content-mode) content mode.

The application has a web interface in which you can define the events you want to send to the broker:

![create event](docs/images/create_event.png)

On the right-hand side all the emitted and received events will be listed. In the image below there are two received 
and one emitted event.

![activity](docs/images/activity.png)

And you will also be able to display the payload of the event.

![event](docs/images/event.png)

## Running the container image

You can expect to have built container images in `arm64` and `amd64` architectures in `quay.io/ruben/cloudevents-player:v1.3`

_Podman_

```bash
podman run -p 8080:8080 -e PLAYER_MODE=LOCAL --rm quay.io/ruben/cloudevents-player:v1.3
```

_Docker_
```bash
docker run -p 8080:8080 -e PLAYER_MODE=LOCAL --rm quay.io/ruben/cloudevents-player:v1.3
```

## Running the binary

First you will have to build the application. See the [Build](#build) section for more details. Then you can
start the application locally with the following command.

```bash
PLAYER_MODE=LOCAL ./target/cloudevents-player-1.3-SNAPSHOT-runner
```

## Running on Kubernetes

### Requirements

- Knative serving
- Knative eventing
- `kubectl`
- `kn`
- `eventing`
### Use .yaml file to deply application
- After apply eventing just go to the deploy folder and run with follwing command.
```bash
kubectl apply -f knative.yaml
```

## Build

It is a Quarkus application with a React frontend. In order to build the application use any of the
following alternatives:

### JVM Build

Build

```shell script
mvn clean package
```

Run

```shell script
$ java -Dplayer.mode=LOCAL -jar target/quarkus-app/quarkus-run.jar
...
2022-06-24 18:39:07,794 INFO  [io.und.websockets] (main) UT026003: Adding annotated server endpoint class com.redhat.syseng.tools.cloudevents.resources.MessagesSocket for path /socket
2022-06-24 18:39:08,130 INFO  [io.qua.sma.ope.run.OpenApiRecorder] (main) Default CORS properties will be used, please use 'quarkus.http.cors' properties instead
2022-06-24 18:39:08,216 INFO  [io.quarkus] (main) cloudevents-player 1.3-SNAPSHOT on JVM (powered by Quarkus 2.16.1.Final) started in 0.879s. Listening on: http://0.0.0.0:8080
2022-06-24 18:39:08,217 INFO  [io.quarkus] (main) Profile prod activated. 
2022-06-24 18:39:08,217 INFO  [io.quarkus] (main) Installed features: [cdi, hibernate-validator, kubernetes-client, rest-client, resteasy-reactive, resteasy-reactive-jackson, smallrye-context-propagation, smallrye-openapi, vertx, websockets, websockets-client] 
```

### Quarkus dev mode

```shell script
$ mvn quarkus:dev -Dplayer.mode=LOCAL
...
Listening for transport dt_socket at address: 5005
...
[INFO] --- quarkus-maven-plugin:1.0.1.Final:dev (default-cli) @ cloudevents-player ---
Listening for transport dt_socket at address: 5005
2022-06-24 18:51:43,172 INFO  [io.und.websockets] (Quarkus Main Thread) UT026003: Adding annotated server endpoint class com.redhat.syseng.tools.cloudevents.resources.MessagesSocket for path /socket

2022-06-24 18:51:43,229 WARN  [org.jbo.res.res.i18n] (Quarkus Main Thread) RESTEASY002155: Provider class io.cloudevents.http.restful.ws.CloudEventsProvider is already registered.  2nd registration is being ignored.
2022-06-24 18:51:43,513 INFO  [io.quarkus] (Quarkus Main Thread) cloudevents-player 1.3-SNAPSHOT on JVM (powered by Quarkus 2.16.1.Final) started in 2.543s. Listening on: http://localhost:8080
2022-06-24 18:51:43,514 INFO  [io.quarkus] (Quarkus Main Thread) Profile dev activated. Live Coding activated.
2022-06-24 18:51:43,515 INFO  [io.quarkus] (Quarkus Main Thread) Installed features: [cdi, hibernate-validator, kubernetes-client, rest-client-reactive, rest-client-reactive-jackson, resteasy-reactive, resteasy-reactive-jackson, smallrye-context-propagation, smallrye-openapi, swagger-ui, vertx, websockets, websockets-client]
```

### Native build

Build

```shell script
mvn clean install -Pnative
```

Run

```shell script
$ ./target/cloudevents-player-1.3-SNAPSHOT-runner -Dplayer.mode=LOCAL
...
2022-06-24 18:48:11,565 INFO  [io.quarkus] (main) cloudevents-player 1.3-SNAPSHOT native (powered by Quarkus 2.16.1.Final) started in 0.022s. Listening on: http://0.0.0.0:8080
2022-06-24 18:48:11,565 INFO  [io.quarkus] (main) Profile prod activated. 
2022-06-24 18:48:11,565 INFO  [io.quarkus] (main) Installed features: [cdi, hibernate-validator, kubernetes-client, rest-client-reactive, rest-client-reactive-jackson, resteasy-reactive, resteasy-reactive-jackson, smallrye-context-propagation, smallrye-openapi, swagger-ui, vertx, websockets, websockets-client]
2022-06-24 18:48:17,028 INFO  [com.git.rur.clo.ser.MessageService] (ForkJoinPool.commonPool-worker-3) Player mode LOCAL - broker: http://localhost:8080/
```

### Skip frontend build

The `skipFrontend` profile will not run npm commands. Useful when you are just changing Java code.

```{bash}
mvn clean package -PskipFrontend
```

### Build the container image

```shell script
mvn clean package -Dcontainer -Dquarkus.native.container-build=true
```

## Configuration

The Cloudevents Player can be configured by:

 - System properties. Usually in lower case and separated by dots e.g. `player.mode` 
 - Environment variables. In upper case and separated by underscores e.g. `PLAYER_MODE`

These are the configuration options provided in the Cloudevents Player.

- `PLAYER_MODE`
- `BROKER_URI`
- `BROKER_NAME`
- `BROKER_NAMESPACE`

In the `KNATIVE` mode it will also look for the `K_SINK` environment variable injected after
defining a `SinkBinding`.

For more configuration options refer to the [Quarkus documentation](https://quarkus.io/guides/all-config)

### Player Mode

Cloudevents Player comes with 2 modes defined in the `PLAYER_MODE` environment variable:

- `LOCAL`: Received events are forwarded to the loopback broker. This mode is just for development and testing 
- `KNATIVE` (default): The application will get the current namespace it is running in and will use the `BROKER_NAME`
 environment variable to decide which broker to connect to (`default` is the default broker).

```bash
# Local Mode
# system property
./target/cloudevents-player-1.3-SNAPSHOT-runner -Dplayer.mode=LOCAL

# environment variable
PLAYER_MODE=LOCAL ./target/cloudevents-player-1.3-SNAPSHOT-runner

# Knative Mode
# system property
./target/cloudevents-player-1.3-SNAPSHOT-runner -Dplayer.mode=KNATIVE

# environment variable
PLAYER_MODE=KNATIVE ./target/cloudevents-player-1.3-SNAPSHOT-runner
```

### Broker URI

Sets the `BROKER_URI` where the messages will be sent to. It will always be `localhost:8080` for `LOCAL` mode.
Overrides the name and namespace properties.

```bash
# with a system property
./target/cloudevents-player-1.3-SNAPSHOT-runner -Dbroker.uri=http://some-broker:1234

# or using an environment variable
BROKER_URI=http://some-broker:1234 ./target/cloudevents-player-1.3-SNAPSHOT-runner
```

### Broker Name and Namespace

Define the broker name and namespace to guess the broker URI. The default broker name is `default` and the default
namespace will be the current namespace.

```bash
# system property
./target/cloudevents-player-1.3-SNAPSHOT-runner -Dbroker.name=example -Dbroker.namespace=other
...
2022-06-24 19:08:53,681 INFO  [com.git.rur.clo.ser.MessageService] (ForkJoinPool.commonPool-worker-3) Player mode KNATIVE - broker: http://broker-ingress.knative-eventing.svc.cluster.local/other/example

# environment variable
BROKER_NAME=example BROKER_NAMESPACE=other ./target/cloudevents-player-1.3-SNAPSHOT-runner
...
2022-06-24 19:08:53,681 INFO  [com.git.rur.clo.ser.MessageService] (ForkJoinPool.commonPool-worker-3) Player mode KNATIVE - broker: http://broker-ingress.knative-eventing.svc.cluster.local/other/example
```

### CORS

By default the cloudevents player will allow all origins but it is possible to defined the allowed origins with the following environment variable:

```
  - name: QUARKUS_HTTP_CORS_ORIGINS
    value: https://cloudevents-player-myns.apps.example.com
```

See the [Quarkus CORS documentation](https://quarkus.io/guides/http-reference#cors-filter) for more configuration parameters.
