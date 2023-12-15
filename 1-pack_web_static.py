#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime


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
