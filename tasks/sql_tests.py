from django.db import connection

# getting tasks


# прописал в каждой функции одинаковый кусок просто для\
# понимания (без вывода этого куска в отдельную функцию)
def get_all_tasks():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, task_name, status FROM tasks_task")
        columns = []  # here we got all names fo the columns (id, name ...)
        for col in cursor.description:
            columns.append(col[0])  # getting the name of the columns (keys)
        rows = cursor.fetchall()  # getting the value of the certain colum
        result = [dict(zip(columns, row)) for row in rows]
        return result


def tasks_in_progress():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, task_name FROM tasks_task WHERE status = 'in_progress'"
        )
        columns = []
        for col in cursor.description:
            columns.append(col[0])
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        return result


def tasks_is_completed():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, task_name FROM tasks_task WHERE status = 'completed'"
        )
        columns = []
        for col in cursor.description:
            columns.append(col[0])
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        return result


# update status


def in_progress_into_completed():
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE  tasks_task SET status = 'completed' WHERE status = 'in_progress'"
        )
        return cursor.rowcount


def new_into_in_progress():
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE  tasks_task SET status = 'in_progress' WHERE status = 'new'"
        )
        return cursor.rowcount


# delete tasks


def delete_all_tasks():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM tasks_task WHERE status = 'completed'")
        return cursor.rowcount()


# count


def tasks_by_user():
    with connection.cursor() as cursor:
        cursor.execute("SELECT user_id, COUNT(*) FROM tasks_task GROUP BY user_id")
        columns = []
        for col in cursor.description:
            columns.append(col[0])
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        return result


def tasks_by_status():
    with connection.cursor() as cursor:
        cursor.execute("SELECT status, COUNT(*) FROM tasks_task GROUP BY status")
        columns = []
        for col in cursor.description:
            columns.append(col[0])
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        return result
