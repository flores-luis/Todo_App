from flask_app.config.dbconnect import connectToMySQL
#from datetime import datetime
#from flask import flash

class Task:

    #database name
    db_name = 'luis52$todo'

    #since only 1 table in database, mimic TASKS table's data
    def __init__(self,db_data):
        self.id = db_data['id']
        self.task_name = db_data['task_name']
        self.notes = db_data['notes']
        self.due_date = db_data['due_date']
        self.priority_level = db_data['priority_level']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_all_tasks(cls):
        query = "SELECT * FROM tasks ORDER BY due_date ASC;"
        results = connectToMySQL(cls.db_name).query_db(query)
        task_list = []
        for row in results:
            task_list.append(cls(row))
        return task_list


##############################################################################
    @classmethod
    def save(cls,data):
        query = "INSERT INTO tasks (task_name,notes,due_date,priority_level) VALUES (%(task_name)s,%(notes)s,%(due_date)s,%(priority_level)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE tasks SET task_name=%(task_name)s, notes=%(notes)s, due_date=%(due_date)s, priority_level=%(priority_level)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM tasks WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print(results)
        one_task = cls( results[0])
        print(one_task)
        return one_task

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM tasks WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    # @staticmethod
    # def validate_sightings(sightings):
    #     is_valid = True
    #     if len(sightings['Location']) < 1:
    #         is_valid = False
    #         flash("Location must be at least 1 characters","add")
    #     if len(sightings['Comments']) < 10:
    #         is_valid = False
    #         flash("Comments must be at least 3 characters","add")
    #     if int(sightings['sasquatch_number']) < 1:
    #         is_valid = False
    #         flash("# of Sasquatches must be at least 1 character","add")
    #     if sightings['sighting_date'] == "":
    #         is_valid = False
    #         flash("Please enter a date","add")
    #     return is_valid
