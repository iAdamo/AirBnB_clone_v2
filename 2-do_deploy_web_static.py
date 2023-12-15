#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy

Usage: fab -f 2-do_deploy_web_static.py
do_deploy:archive_path=versions/archive_name.tgz
-i my_ssh_private_key -u ubuntu
"""


from fabric.api import local, put, run, env
from os.path import exists
from datetime import datetime

env.user = "ubuntu"
env.hosts = ["35.175.134.9", "35.153.33.206"]


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
"""
    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_file = f"versions/web_static_{timestamp}.tgz"

    result = local(f"tar -cvzf {tgz_file} web_static")

    if result.succeeded:
        return tgz_file
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        run(f"mkdir -p {path}{no_ext}")
        run(f"tar -xzf /tmp/{file_name} -C {path}{no_ext}/")
        run(f"rm /tmp/{file_name}")
        run(f"mv {path}{no_ext}/web_static/* {path}{no_ext}/")
        run(f"rm -rf {path}{no_ext}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {path}{no_ext}/ /data/web_static/current")
        run("sudo service nginx restart")
        print("New web version deployed!")
        return True
    except Exception:
        return False
