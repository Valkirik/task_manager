from django.db import connection

#getting tasks

def get_all_tasks():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, task_name, status FROM tasks_task")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def tasks_in_progress():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, task_name FROM tasks_task WHERE status = 'in_progress'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def tasks_is_completed():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, task_name FROM tasks_task WHERE status = 'completed'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)


#update status

def in_progress_into_completed():
    with connection.cursor() as cursor:
        cursor.execute("UPDATE  tasks_task SET status = 'completed' WHERE status = 'in_progress'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def new_into_in_progress():
    with connection.cursor() as cursor:
        cursor.execute("UPDATE  tasks_task SET status = 'completed' WHERE status = 'in_progress'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)


#delete tasks

def delete_all_tasks():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM tasks_task WHERE status = 'completed'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

#count

def tasks_by_user():
    with connection.cursor() as cursor:
        cursor.execute("SELECT user_id, COUNT(*) FROM tasks_task GROUP BY user_id")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def tasks_by_status():
    with connection.cursor() as cursor:
        cursor.execute("SELECT status, COUNT(*) FROM tasks_task GROUP BY status")
        rows = cursor.fetchall()
        for row in rows:
            print(row)



