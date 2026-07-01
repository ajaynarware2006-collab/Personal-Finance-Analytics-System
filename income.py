from connection import connecting

connection,cursor=connecting()

def update_income(user_id):
    try:
        income=int(input("Enter your new Income : "))

    except ValueError:
        print("Please enter integer only.")
        update_income()
    
    sure=input("Are you sure to change income. (Y/N) : ")
    if sure=="Y":
        cursor.execute("UPDATE users SET income=%s WHERE user_id=%s;",(income,user_id))
        connection.commit()
        print(".Successfully Updated")

def view_income(user_id):
    cursor.execute("SELECT income FROM users WHERE user_id=%s;",user_id)
    income=cursor.fetchone()[0]
    print(f"Your Current Income is {income}")
    