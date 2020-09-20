FROM idock.daumkakao.io/steve_kim/alpine39:python37
## image name naxreo/myaddress:v0.1
## sidecar is naxreo/git-sync:v0.1

COPY requirements.txt /requirements.txt
COPY app /app
WORKDIR /app
CMD ["pip", "install", "-r", "/requirements.txt"]
ENTRYPOINT [ "python", "app.py" ]
