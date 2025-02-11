import pyttsx3


class TextToSpeech:
    def __init__(self, language: str):
        self.language = language
        self.engine = pyttsx3.init()

        self.languages_full = {
            "ru": "Russian",
            "en": "English"
        }

    def check_language(self):
        voices = self.engine.getProperty("voices")
        language = self.languages_full[self.language]

        for voice in voices:
            if language in voice.name:
                return True
            else:
                return False

    def say(self, text):
        if not self.check_language():
            raise ValueError("Язык не поддерживается. Для того, чтобы исправить это -> https://тут_ссылка_на_статью.com")
        else:
            self.engine.setProperty("voice", self.languages_full[self.language])
            self.engine.say(text)
            self.engine.runAndWait()

