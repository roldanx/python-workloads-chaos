import os, random
from kubernetes import client, config

config.load_incluster_config()
chaos_namespace=os.environ.get('CHAOS_NAMESPACE')

v1=client.CoreV1Api()
print("Pod to be deleted:")
pods = v1.list_namespaced_pod(namespace=chaos_namespace)
pods_list=[]

for i in pods.items:
    pods_list.append(i.metadata.name)

pod_to_be_deleted=random.choice(pods_list)
print(pod_to_be_deleted)

v1.delete_namespaced_pod(name=pod_to_be_deleted, namespace="workloads")
