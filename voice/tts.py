import asyncio
import edge_tts
import tempfile
import pygame
import os


VOICE = "en-US-GuyNeural"


def speak(text):

    async def generate():

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        filename = temp_file.name
        temp_file.close()

        communicate = edge_tts.Communicate(
            str(text),
            VOICE
        )

        await communicate.save(filename)

        return filename

    filename = asyncio.run(generate())

    pygame.mixer.init()

    pygame.mixer.music.load(filename)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()

    os.remove(filename)