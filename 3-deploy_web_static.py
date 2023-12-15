#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""a Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""

from fabric.api import put, run, env, local
from os.path import exists
from datetime import datetime

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
        path = f"/data/web_static/releases/{file_name.split('.')[0]}"
        run(f"mkdir -p {path}")
        run(f"tar -xzf /tmp/{file_name} -C {path}/")
        run(f"rm /tmp/{file_name}")
        run(f"mv {path}/web_static/* {path}/")
        run(f"rm -rf {path}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {path}/ /data/web_static/current")
        run("sudo service nginx restart")
        print("New web version deployed!")
        return True
    except BaseException:
        return False


def deploy():
    """creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
