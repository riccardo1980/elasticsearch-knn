# Elasticsearch configuration for k-NN enabled search

## Prerequisites
Setup is based on docker-compose. Make sure Linux host matches minimal Elasticsearch requirements. 

## Setup
This setup is based on [Start the Elastic Stack with Docker Compose](https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-stack-docker.html#run-docker-secure) official HowTo.  
Place your `.env` file in `knn-es_cluster_config` folder, then issue: 
```Bash
docker-compose up
```

# docker-desktop
If you are running docker through docker-desktop, you can modify max_map_count VM settings from a powershell commandline prompt with:
```Bash
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```

To run notebooks in Jupyter, install and configure notebook package
```Bash
pip install -r notebooks/requirements.txt
ipython kernel install --user --name=.venv
```