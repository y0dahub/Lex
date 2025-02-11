from npl.intent_recognition import IntentRecognition
from text_to_speech import TextToSpeech

class Commands:
    def __init__(self):
        self.intent_recognition_engine = IntentRecognition()
        self.speak_engine = TextToSpeech(language="en")

    def hanlde_command(self, command):
        intent = self.intent_recognition_engine.get_intent(command)

        if "greeting" in intent:
            self.speak_engine.say("Hello! How can I help you?")