from host.containers import main
import docker 

base_path = main.base_path
instance = main.instance
volumes = main.volumes
service = "nodejs"
settings = main.settings.get_config(service)
name = "cee-tools-%s-%s" % (instance, service)
num_cores = main.settings.get_num_cores(service, get_range=True)

def main(client, network):
   devel_volumes = {
      base_path + "/docker/controller/": {
         "bind": "/home/cee-tools/controller/",
         "mode": "rw",
      },
      base_path + "/scripts/": {
         "bind": "/home/cee-tools/scripts/",
         "mode": "rw",
      },
      base_path + "/source/": {
         "bind": "/home/cee-tools/source",
         "mode": "rw",
      },
      base_path + "/settings/": {
         "bind": "/home/cee-tools/settings",
         "mode": "rw",
      },
      "%s/docker/%s/%s/" % (base_path, service, instance): {
         "bind": "/home/container/daemon",
         "mode": "rw",
      },
   }
   volumes = main.add_volumes(devel_volumes)
   host_config = client.create_host_config(
      port_bindings={str(settings['port']): settings['port']},
      mem_limit="1G",
      binds=volumes,
   )
   kwargs = {
      "image": "cee-tools-%s-%s:latest" % (instance, service),
      "host_config": host_config,
      "name": name,
      "hostname": name,
      "tty": True,
      "stdin_open": True,
   }

   if num_cores != None:
      kwargs['cpuset'] = num_cores

   container = client.create_container(**kwargs)
   client.connect_container_to_network(container=container['Id'], net_id=network['Id'])
   return container

