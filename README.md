# Python workloads chaos
This repository is aimed to set a k8s testing environment where Pods will be randomly deleted using the python k8s client.

## Usage
Please use the `k8s/chaos-configmap.yaml` file to specify in which namespace will the chaos be applied.

## Compatibility
It has been tested on the following environment:

* Red Hat Enterprise Linux 8.6
* Kind 0.11.1
* Kubernetes 1.21.1
