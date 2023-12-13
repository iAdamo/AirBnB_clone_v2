#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""

from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
"""
    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    target_tgz_file = "versions/web_static_{}.tgz".format(timestamp)

    result = local("tar -cvzf {} web_static".format(target_tgz_file))

    if result.ok:
        return target_tgz_file
    else:
        return None
