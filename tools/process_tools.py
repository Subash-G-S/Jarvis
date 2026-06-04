import psutil

def close_app(app_name):

    app_name = app_name.lower()

    for proc in psutil.process_iter(['pid', 'name']):

        try:

            name = proc.info['name']

            if name and app_name in name.lower():

                proc.kill()

                return f"Closed {name}"

        except:
            pass

    return f"{app_name} not running"