from turtle import update
import mysql.connector

'''
State your group member name and id here:
1. 2022132Uong Uong SovanDara
2. 2022079cheung Cheung Sok Panha
3. 2022076doch Doch Chanthida
'''

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cat_db",
    port="3306"
)


cursor = mydb.cursor()
# print(mydb)


def register_cat(cat_info):

    sql = "INSERT INTO cats (name, gender, breed, dob, description) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, cat_info)
    mydb.commit()

    print("Registration completed!\n")


# test_cat = ("rose", "f", "Siberian", "2020-03-08", "smart one")
# register_cat(test_cat)


def get_cats():

    sql = "SELECT * from cats"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# print(get_cats())


def get_cat(id):
    sql = f"SELECT * FROM cats WHERE id={id}"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


# print(get_cat(1))


def update_cat(cat_info):
    id, name, gender, breed, dob, description = cat_info
    sql = f"UPDATE cats SET name='{name}', gender='{gender}', breed='{breed}', dob='{dob}', description='{description}' WHERE id={id}"
    cursor.execute(sql)
    mydb.commit()

    print("Update completed!\n")

# test_cat_1 = (1, "jacky", "m", "ferry", "2020-03-08", "smart one")
# update_cat(test_cat_1)


def remove_cat(id):
    sql = f"DELETE FROM cats WHERE id={id}"
    cursor.execute(sql)
    mydb.commit()
    print("Remove completed!\n")


# remove_cat(2)
