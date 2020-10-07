import json


class QuizHandler:
    """
        Main Class for Handling quiz
    """

    def __init__(self, question):
        self._question = question
        with open('D:/TriviaBot/ProgrammingTriviaBot/questions/Questions.json', 'r') as json_file:
            data = json.load(json_file)[self._question]
            self._language = data['language']
            self._answer = data['answer']
            self._code = data['code']
            json_file.close()

    def repopulate_properties(self):
        with open('D:/TriviaBot/ProgrammingTriviaBot/questions/Questions.json', 'r') as json_file:
            data = json.load(json_file)[self._question]
            self._language = data['language']
            self._answer = data['answer']
            self._code = data['code']
            json_file.close()

    def is_correct_ans(self, ans):
        return ans == self.answer

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, quest):
        """
        Setter for questions, repopulates properties after setting new question
        :param quest: string
        :return: void
        """
        self._question = quest
        self.repopulate_properties()

    # Not having setters for these, cause these properties should never change
    @property
    def language(self):
        return self._language

    @property
    def answer(self):
        return self._answer

    @property
    def code(self):
        return self._code
