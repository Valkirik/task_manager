from django.db import connection

#getting tasks

def get_all_tasks():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, task_name, status FROM tasks_task")
        return cursor.fetchall()


def tasks_in_progress():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, task_name FROM tasks_task WHERE status = 'in_progress'")
        return cursor.fetchall()

def tasks_is_completed():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, task_name FROM tasks_task WHERE status = 'completed'")
        return cursor.fetchall()


#update status

def in_progress_into_completed():
    with connection.cursor() as cursor:
        cursor.execute("UPDATE  tasks_task SET status = 'completed' WHERE status = 'in_progress'")
        return cursor.rowcount

def new_into_in_progress():
    with connection.cursor() as cursor:
        cursor.execute("UPDATE  tasks_task SET status = 'in_progress' WHERE status = 'new'")
        return cursor.rowcount


#delete tasks

def delete_all_tasks():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM tasks_task WHERE status = 'completed'")
        return cursor.rowcount()

#count

def tasks_by_user():
    with connection.cursor() as cursor:
        cursor.execute("SELECT user_id, COUNT(*) FROM tasks_task GROUP BY user_id")
        return cursor.fetchall()

def tasks_by_status():
    with connection.cursor() as cursor:
        cursor.execute("SELECT status, COUNT(*) FROM tasks_task GROUP BY status")
        return cursor.fetchall()



