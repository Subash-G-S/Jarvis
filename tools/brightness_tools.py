import screen_brightness_control as sbc


def get_brightness():

    brightness = sbc.get_brightness()

    return f"Brightness is {brightness[0]}%"


def set_brightness(percent):

    percent = max(
        0,
        min(100, percent)
    )

    sbc.set_brightness(percent)

    return f"Brightness set to {percent}%"
def increase_brightness(step=10):

    current = sbc.get_brightness()[0]

    new = min(
        current + step,
        100
    )

    sbc.set_brightness(new)

    return f"Brightness increased to {new}%"
def decrease_brightness(step=10):

    current = sbc.get_brightness()[0]

    new = max(
        current - step,
        0
    )

    sbc.set_brightness(new)

    return f"Brightness decreased to {new}%"