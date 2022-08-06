#!/usr/bin/python3

from rich import print, pretty, traceback
import docker
import re
import os

pretty.install()
traceback.install()

def atoi(text):
    return int(text) if text.isdigit() else text

def naturalKeys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

account = "lgili"

images = [    
    "sqlcipher"
]


def printBuildLogs(buildLogs):
    for logEntry in buildLogs:
        if "stream" in logEntry:
            print(logEntry["stream"], end="")

def buildImages():
    client = docker.from_env()
    for imageName in images:
        for root, directories, files in os.walk(imageName):
            directories[:] = [d for d in directories if not d[0] == '.']
            directories.sort(key=naturalKeys)
            try:
                directories.remove("scripts")
            except:
                print("not removed yet")
            print(directories)
            for imageVersion in directories:
                imagePath = os.path.join(imageName, imageVersion)
                imageRepository = "{}/{}".format(account, imageName)
                imageFullTag = "{}:{}".format(imageRepository, imageVersion)

                print("=" * 100)
                print(f"[green]Building image:[/green] [yellow]{imageFullTag}[/yellow]")
                print("=" * 100)

                (image, logs) = client.images.build(path=imagePath, tag=imageFullTag, rm=True)
                printBuildLogs(logs)

                if imageVersion == directories[-1]:
                    image.tag(imageRepository, tag="latest")

                image.reload()

                print("=" * 100)
                print("[green]Done:[/green] [yellow]{}[/yellow]".format(*image.tags))
                print("=" * 100, end="\n\n")

    client.images.prune(filters={"dangling": 1})
    client.images.prune(filters={"dangling": 1})

def pushImages():
    client = docker.from_env()
    print("=" * 100)

    for imageName in images:
        imageRepository = "{}/{}".format(account, imageName)
        print(f"[green]Pushing repository:[/green] [yellow]{imageRepository}[/yellow]")
        client.images.push(imageRepository)

        print("=" * 100)

buildImages()
# pushImages()
