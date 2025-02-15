from speech_rec import SpeechRecognition
from text_to_speech import TextToSpeech
from commands import Commands

class Assistant:
    def __init__(self):
        self.recognize_engine = SpeechRecognition()
        self.speak_engine = TextToSpeech(language="ru")
        self.commnad_engine = Commands()

        self.is_listening = True

    def start(self):
        while self.is_listening:
            try:
                user_command = self.recognize_engine.recognize()
                if not user_command:
                    continue

                self.commnad_engine.handle_command(user_command)

            except Exception as _err:
                print(f"Произошла ошибка: ({_err}).\nПопробуйте перезапустить программу.\nЕсли это не помогло, то напишите в техподдержку.")
