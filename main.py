username = "user"
password = "password"
server = "server_address"
share = "sharename"
mount_point = "~/mnt"
ssid = ""
sleep_time = 20


import os
import time
import subprocess


def ssid_connected():
    wifi_info = subprocess.check_output(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-I']).decode("UTF-8")
    if ssid in wifi_info:
        print("On correct wifi network")
        return True
    print("Not on required wifi network")
    return

def sort_mount_point():
    if not os.path.exists(mount_point):
        print("mount point doesn't exist, creating...")
        os.makedirs(mount_point)
        time.sleep(0.2)

def is_mounted():
    try:
        mnts = subprocess.check_output(['mount']).decode("UTF-8")
        if mount_point in mnts:
            return True
        return
    except Exception as e:
        print(e)

def connect():
    try:
        os.system("mount_smbfs //{}:{}@{}/{} {}".format(username, password, server, share, mount_point))
    except Exception as e:
        print(e)

def run():
    while True:
        if ssid_connected() and not is_mounted():
            sort_mount_point()
            time.sleep(0.2)
            connect()
        # if connected to ssid then mount server else sleep
        time.sleep(sleep_time)


if __name__ == "__main__":
    run()