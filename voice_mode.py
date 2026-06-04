# voice_mode.py

from voice.stt import listen
from voice.tts import speak
from gui.gui_manager import set_state

from agent.llm import ask_llm
from agent.router import execute_tool
from agent.analyzer import analyze_result
from gui.gui_manager import go_to_sleep


def run_voice_mode():

    speak("Voice mode activated")

    missed_listens = 0

    while True:

        user_command = listen()

        if not user_command:

            missed_listens += 1

            # roughly 10 seconds if listen timeout is 10 sec
            if missed_listens >= 3:
                set_state("sleeping")
                

                go_to_sleep()

                speak("Going to sleep")

                return

            continue

        missed_listens = 0

        if "exit" in user_command.lower():
            print("EXIT DETECTED")
            go_to_sleep()
            return

        try:
            set_state("thinking")

            llm_response = ask_llm(user_command)
            print("\nLLM RESPONSE:")
            print(llm_response)

            tool_result = execute_tool(llm_response)
            print("\nTOOL RESULT:")
            print(tool_result)

            final_answer = analyze_result(
                user_command,
                tool_result
            )
            set_state("speaking")

            speak(final_answer)
            set_state("listening")

        except Exception as e:

            print("Error:", e)
            set_state("speaking")

            speak("Sorry, something went wrong.")
            set_state("listening")