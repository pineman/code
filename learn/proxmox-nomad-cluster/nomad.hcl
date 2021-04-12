data_dir = "/var/lib/nomad"
bind_addr = "0.0.0.0"
region = "lisboa"
datacenter = "rato"
server {
  enabled = true
  bootstrap_expect = 3
}
client {
  enabled = true
}
plugin "nomad-driver-podman" {
  config {
    socket_path = "unix://run/user/1000/podman/podman.sock"
  }
}
