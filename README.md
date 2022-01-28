# security-notebooks

Lab# 2- To launch a jupyter stack datascience notebook

```bash
docker run --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work jupyter/datascience-notebook:b418b67c225b
```

Note: the above will be accessible on localhost:10000, not 8888!

Do the same with a `docker-compose.yml` file:

```bash
docker-compose up -d
```
