#!/bin/bash
virsh undefine --nvram k3os-s1
virsh undefine --nvram k3os-n1
virsh undefine --nvram k3os-n2
virsh destroy k3os-s1
virsh destroy k3os-n1
virsh destroy k3os-n2
