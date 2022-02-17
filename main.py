username = "user"
password = "password"
server = "server_address"
share = "sharename"
mount_point = "~/mnt"
ssid = ""
sleep_time = 20

import os
import time


def check_ssid():
    pass

def sort_mount_point():
    if not os.path.exists(mount_point):
        os.makedirs(mount_point)
        time.sleep(0.2)

def connect():
    os.system("mount_smbfs //{}:{}@{}/{} {}".format(username, password, server, share, mount_point))

def run():
    while True:
        # if connected to ssid then mount server else sleep
        time.sleep(sleep_time)
