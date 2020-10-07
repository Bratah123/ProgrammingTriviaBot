import json


class DatabaseHandler:

    @staticmethod
    def add_points(author_id, point_amount):
        db = open('D:/TriviaBot/ProgrammingTriviaBot/database/database.json', 'r')
        json_data = json.load(db)
        db.close()
        db = open('D:/TriviaBot/ProgrammingTriviaBot/database/database.json', 'w')
        json_data[str(author_id)][0]["quizPoints"] += point_amount
        try:
            json.dump(json_data, db)
        except Exception as e:
            print(e)
        db.close()

    @staticmethod
    def add_user(author_id):
        db = open('D:/TriviaBot/ProgrammingTriviaBot/database/database.json', 'r')
        json_data = json.load(db)
        db.close()
        new_user = {"quizPoints": 0}
        json_data[str(author_id)] = [new_user]
        db = open('D:/TriviaBot/ProgrammingTriviaBot/database/database.json', 'w')
        try:
            json.dump(json_data, db)
        except Exception as e:
            print(e)
        db.close()

    @staticmethod
    def is_already_user(author_id):
        db = open('D:/TriviaBot/ProgrammingTriviaBot/database/database.json', 'r')
        json_data = json.load(db)
        db.close()
        try:
            return json_data[str(author_id)] is not None
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_points(author_id):
        db = open('D:/TriviaBot/ProgrammingTriviaBot/database/database.json', 'r')
        json_data = json.load(db)
        db.close()
        return json_data[str(author_id)][0]["quizPoints"]
