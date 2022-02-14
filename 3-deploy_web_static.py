#!/usr/bin/python3
from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os.path import exists
env.hosts = ["3.84.104.13", "35.237.21.147"]
file_path = None


def do_pack():
    """This will create a package with web_static"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    compressed = ("versions/web_static_{}.tgz".format(date))
    local("tar -cvzf {} web_static".format(compressed))
    return compressed


def do_deploy(archive_path):
    """This function will deploy the web static to the servers"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(filename)
        run("sudo mkdir -p {}/".format(path))
        run("sudo tar -zxf /tmp/{}.tgz -C {}/".format(filename, path))
        run("sudo rm /tmp/{}".format(archive_path.split("/")[1]))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(filename, filename))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(filename))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Full deployment"""
    global file_path
    if file_path is None:
        file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)
