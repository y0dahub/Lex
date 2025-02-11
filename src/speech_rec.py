import speech_recognition as sr


class SpeechRecognition:
    def listen(self):
        recognise = sr.Recognizer()

        with sr.Microphone() as source:
            print("Слушаю...")
            audio = recognise.listen(source)

        return audio


    def recognize(self, audio):
        recognizer = sr.Recognizer()

        try:
            command = recognizer.recognize_vosk(audio, language="ru-RU")

            return command

        except sr.UnknownValueError:
            return "Ваша команда не содержится в моей базе."
        
        except sr.RequestError:
            return "Ошибка подключения."