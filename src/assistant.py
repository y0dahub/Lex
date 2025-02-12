from speech_rec import SpeechRecognition
from text_to_speech import TextToSpeech
from commands import Commands

class Assistant:
    def __init__(self):
        self.recognize_engine = SpeechRecognition()
        self.speak_engine = TextToSpeech(language="en")
        self.commnad_engine = Commands()

        # self.config = config
        self.is_listening = True

        # self.api_keys = [
        #     config.get("API_KEYS"),
        # ]

    def start(self):
        self.speak_engine.say("Привет! Чем могу помочь?")

        while self.is_listening:
            try:
                # user_audio = self.recognize_engine.listen()
                # if not user_audio:
                #     continue ------ Раскомментируй код, при тесте - это нужно для микрофона, а 26 строчку - удали
                user_audio = input()
                print(f"Вы сказали: '{user_audio}'. Веду обработку")

                self.commnad_engine.hanlde_command(user_audio)

            except Exception as _err:
                print(f"Произошла ошибка: ({_err}).\nПопробуйте перезапустить программу.\nЕсли это не помогло, то напишите в техподдержку.")
