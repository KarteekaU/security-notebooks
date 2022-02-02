# Security notebooks- Python Data Science lab
This repo has all the labs and class work from MSBX 5500

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/KarteekaU/security-notebooks/HEAD)

The built image is [hosted on Docker-Hub](https://hub.docker.com/layers/kaup1074/my-datascience-notebook/latest/images/sha256-48f8e3077ff6573b3e4bd42849da4a70bbe8cae555536febb10f80c2932ad486?context=repo).

## Using this repo
### With `docker`
Build:

```bash
docker build --rm -t kaup1074/my-datascience-notebook
# Built an image on dockerhub in the my data science notebook repo

docker tag jupyter/my-datascience-notebook kaup1074/my-datascience-notebook
# Tagged as above
```

Run:

```bash
docker run fill-in-the-rest
# - Should publish port 8888
# - Should mount the local directory as a volume in the
#   container's home directory
# - Should `--rm` container when done
# - Should use `-it` mode
```

### With `docker-compose`
Build and run:

```bash
docker-compose up
# - This command publishes port 8888 and mounts the local directory as a volume in the container's home directory
# pushes to my Dockerhub repository
```
