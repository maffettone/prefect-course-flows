from lab103 import main
from prefect.deployments import Deployment
from prefect.filesystems import GitHub
from prefect.infrastructure.docker import DockerContainer

docker_container_block = DockerContainer.load("test-docker-default")

github_block = GitHub.load("prefect-course")

deploy_docker = Deployment.build_from_flow(
    flow=main, name="Docker Python Deployment", storage=github_block, infrastructure=docker_container_block
)

if __name__ == "__main__":
    deploy_docker.apply()
