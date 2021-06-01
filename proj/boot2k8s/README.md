# script to setup an immutable k8s cluster on libvirt IaC
* use talos or k3os.
* boot at least 2 nodes, one server (control plane) and one agent (worker node).
* config all that automatically
* output kubectl config

## TODO
mixed cluster (vm - pinecone, metal - teeny, cloud - ?)
se o pinecone fosse só vmhost escolheria o proxmox. alternatives: 
rhev
ovirt
vsphere
antsle?
virtuozzo?
ou qq coisa private cloud
