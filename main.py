import docker
client = docker.from_env()
image = client.images.build(path='/home/letch/web-projects/digital', dockerfile='Dockerfile', tag='python-runner')
print(image)
# print(image)
print(client.containers.run("python-runner"))
client