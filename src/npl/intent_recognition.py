class IntentRecognition:
    def get_intent(self, text):
        """_summary_

        Args:
            text (str): Текст, который нужно распознать

        Returns:
            intent (str): Возвращает классификацию функции, которую нужно выполнить. НА АНГЛ!!
        """
        intents = {
            "weather": ["погода", "температура"],
            "time": ["сколько время", "который час"],
            "greeting": ["привет", "здравствуй"]
        }

        for intent, keywords in intents.items():
            if any(word in text.lower() for word in keywords):
                return intent
            
        return "unknown"
