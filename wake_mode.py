# wake_mode.py

from voice.stt import listen
from voice.tts import speak

from voice_mode import run_voice_mode
from tools.app_discovery import build_app_cache
from gui.gui_manager import set_state
from gui.gui_manager import wake_up

print("Building app cache...")
build_app_cache()
def start_wake_mode():
    while True:

        print("\nWaiting for wake word...")

        text = listen()

        if not text:
            continue

        text = text.lower()

        if "jarvis" in text:
            wake_up()
            set_state("listening")

            speak("I'm listening")

            run_voice_mode()
            print("VOICE MODE FINISHED")

            print("Returned to sleep mode")