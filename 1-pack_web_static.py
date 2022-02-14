#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive.
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Fabric script that generates a .tgz archive """
    local('mkdir -p versions')
    v_name = 'versions/web_static_{}\
.tgz'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    arch = local('tar -vczf {} web_static'.format(v_name))
    if arch.failed:
        return None
    else:
        return (v_name)
