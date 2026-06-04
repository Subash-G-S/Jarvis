# tools/system_tools.py

import psutil

def get_ram_usage():

    ram = psutil.virtual_memory()

    used = ram.used / (1024 ** 3)

    total = ram.total / (1024 ** 3)

    return f"{used:.1f} GB used out of {total:.1f} GB"

def get_disk_space():

    disk = psutil.disk_usage("C:\\")

    free = disk.free / (1024**3)
    total = disk.total / (1024**3)

    return f"{free:.1f} GB free out of {total:.1f} GB"
import platform
import GPUtil

def get_system_info():

    cpu = platform.processor()

    ram = psutil.virtual_memory()

    total_ram = ram.total / (1024 ** 3)

    disk = psutil.disk_usage("C:\\")

    total_disk = disk.total / (1024 ** 3)

    free_disk = disk.free / (1024 ** 3)
    gpus = GPUtil.getGPUs()

    gpu_name = "Not Found"

    if gpus:
        gpu_name = gpus[0].name

    info = f"""
CPU: {cpu}

GPU: {gpu_name}

RAM: {total_ram:.1f} GB

Disk Total: {total_disk:.1f} GB

Disk Free: {free_disk:.1f} GB

"""

    return info
def get_battery_status():

    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information not available."

    percent = battery.percent

    charging = battery.power_plugged

    status = "Charging" if charging else "Not Charging"

    return f"Battery: {percent}% | {status}"
def get_cpu_usage():

    cpu = psutil.cpu_percent(interval=1)

    return f"CPU Usage: {cpu}%"
def list_running_apps():

    apps = []

    for proc in psutil.process_iter(['name']):

        try:

            name = proc.info['name']

            if name:
                apps.append(name)

        except:
            pass

    apps = sorted(set(apps))

    return "\n".join(apps[:50])
