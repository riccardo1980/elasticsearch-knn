# Elasticsearch configuration for k-NN enabled search

## Prerequisites
Setup is based on docker-compose. Make sure Linux host matches minimal Elasticsearch requirements. 

### docker-desktop
If you are running docker through docker-desktop, you can modify `max_map_count` VM settings with:
```
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```
**WARNING**: change does not persists across either Windows or VM reboot.

## Setup
Use provided docker compose YAML to setup a 2 nodes cluster, along with dashboard.
```Bash
docker-compose up
```