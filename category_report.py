from connection import connecting

connection,cursor=connecting()

def add_category():
    try:

        category=input("Enter Category you want to add : ")

        cursor.execute("INSERT INTO category(category_name) VALUES (%s) RETURNING category_id",(category,))

        connection.commit()
        print("Successfully Created.")

        category_id=cursor.fetchone()[0]
        print(f"Category ID is {category_id}")

    except Exception as e:
        print(e)


def view_categories():
    cursor.execute("SELECT * FROM category ORDER BY category_id")
    data=cursor.fetchall()

    print(f"{'Category ID': <12}{'Category Name'}")
    for category in data:
        print("-------------------------------")
        print(f"     {category[0]:<12}{category[1]}")

def delete_category():
    try:
        category_id=int(input("Enter category ID tO DELETE: "))
    except ValueError:
        print("Please enter integer only.")
        delete_category()
    cursor.execute("DELETE FROM category WHERE CATEGORY_ID=%s",(category_id,))

    connection.commit()
    print("Category Deleted Successfully")

# add_category()
delete_category()
