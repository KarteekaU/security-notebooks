# Project Title
This is a short description of the project. E.g., "This repo is my custom jupyter datascience image..."

[![Binder](https://mybinder.org/badge_logo.svg)](your-mybinder-link)

The built image is [hosted on Docker-Hub](https://hub.docker.com/layers/kaup1074/my-datascience-notebook/latest/images/sha256-48f8e3077ff6573b3e4bd42849da4a70bbe8cae555536febb10f80c2932ad486?context=repo).

## Using this repo
### With `docker`
Build:

```bash
docker build fill-in-the-rest
# Should explain how to build the image, including tagging it
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
# - It should publish port 8888
# - It should mount the local directory as a volume in the container's
#   home directory
```
