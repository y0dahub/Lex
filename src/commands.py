from npl.intent_recognition import IntentRecognition
from text_to_speech import TextToSpeech

class Commands:
    def __init__(self):
        self.intent_recognition_engine = IntentRecognition()
        self.speak_engine = TextToSpeech(language="ru")

    def _recognize_intent(self, command):
        return self.intent_recognition_engine.get_intent(command)
    
    def _respond_to_intent(self, intent):
        print(intent)
        if "приветствие" in intent:
            self.speak_engine.say("Привет! Чем могу помочь?")

        elif "прощание" in intent:
            self.speak_engine.say("До свидания! Хорошего дня!")
            
        else:
            self.speak_engine.say("Извините, я не понял команду.")

    
    def handle_command(self, command):
        intent = self._recognize_intent(command)
        self._respond_to_intent(intent)