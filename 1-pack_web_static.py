#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local


def do_pack():
    """generates a .tgz archive from the contents of the
web_static folder
"""
    local("mkdir -p versions")
    timestamp = local('date "+%Y%m%d%H%M%S"', hide=True).stdout.strip()
    archive_name = f"web_static_{timestamp}.tgz"

    result = local(f"tar -czvf versions/{archive_name} web_static")

    if result.succeeded:
        print("OK")
        return f"versions/{archive_name}"
    else:
        print("FAIL")
        return None
