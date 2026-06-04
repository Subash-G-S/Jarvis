from gui.jarvis_window import JarvisWindow

window = None


def set_window(win):

    global window

    window = win


def set_state(state):

    if window:

        window.set_state(state)
def wake_up():

    if window:

        window.wake_up()


def go_to_sleep():

    if window:

        window.go_to_sleep()