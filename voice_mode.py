from voice.stt import listen
from voice.tts import speak

from gui.gui_manager import (
    set_state,
    go_to_sleep
)

from agent.planner import (
    create_plan
)

from agent.executor import (
    execute_plan
)

from agent.analyzer import (
    analyze_result
)


def run_voice_mode():

    speak("Voice mode activated")

    missed_listens = 0

    while True:

        user_command = listen()

        if not user_command:

            missed_listens += 1

            if missed_listens >= 3:

                set_state(
                    "sleeping"
                )

                go_to_sleep()

                speak(
                    "Going to sleep"
                )

                return

            continue

        missed_listens = 0

        if "exit" in user_command.lower():

            print(
                "EXIT DETECTED"
            )

            go_to_sleep()

            return

        try:

            set_state(
                "thinking"
            )

            plan = create_plan(
                user_command
            )

            print(
                "\nPLAN:"
            )

            print(
                plan
            )

            results = execute_plan(
                plan
            )

            print(
                "\nRESULTS:"
            )

            print(
                results
            )

            final_answer = analyze_result(
                user_command,
                results
            )

            set_state(
                "speaking"
            )

            speak(
                final_answer
            )

            set_state(
                "listening"
            )

        except Exception as e:

            print(
                "Error:",
                e
            )

            set_state(
                "speaking"
            )

            speak(
                "Sorry, something went wrong."
            )

            set_state(
                "listening"
            )