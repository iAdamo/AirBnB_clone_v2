#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from invoke import run as local, task

@task
def do_pack(c):
    """generates a .tgz archive from the contents of the web_static folder
"""
    local("mkdir -p versions")
    timestamp = local('date "+%Y%m%d%H%M%S"', hide=True).stdout.strip()
    archive_path = f"versions/web_static_{timestamp}.tgz"

    result = local(f"tar -czvf {archive_path} web_static")

    if result.ok:
        print("OK")
        return archive_path
    else:
        print("FAIL")
        return None
