from lab103 import main
from prefect.deployments import Deployment
from prefect.filesystems import GitHub

github_block = GitHub.load("prefect-course")

deploy_gh = Deployment.build_from_flow(flow=main, name="GH Python Deployment", storage=github_block)

if __name__ == "__main__":
    deploy_gh.apply()
