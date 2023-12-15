#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy

Usage: fab -f 2-do_deploy_web_static.py
do_deploy:archive_path=versions/archive_name.tgz
-i my_ssh_private_key -u ubuntu
"""


from fabric.api import put, run, env
from os.path import exists

env.hosts = ["35.175.134.9", "35.153.33.206"]


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