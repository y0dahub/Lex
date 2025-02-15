from transformers import pipeline, AutoConfig

class IntentRecognition:
    def __init__(self):
        self.model_name = "DeepPavlov/rubert-base-cased"
        self.config = AutoConfig.from_pretrained(self.model_name)

        self.classifier = pipeline("zero-shot-classification", model=self.model_name, config=self.config)


    def get_intent(self, text):
        """Распознает намерение по входному тексту.

        Args:
            text (str): Текст, который нужно распознать

        Returns:
            intent (str): Возвращает классификацию функции, которую нужно выполнить.
        """
        candidate_labels = ["температура", "время", "приветствие", "неизвестно", "запуск программы", "прощание"]

        result = self.classifier(text, candidate_labels=candidate_labels)

        return result['labels'][0]
