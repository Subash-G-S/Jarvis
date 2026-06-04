import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        try:

            audio = recognizer.listen(
                source,
                timeout=3,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:

            return None

    try:

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text

    except sr.UnknownValueError:

        return None

    except sr.RequestError:

        return None