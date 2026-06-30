from connection import connecting

connection,cursor=connecting()

def user_signup():
    name=input("Enter your name : ")
    income=int(input("Enter your mothly income : "))

    password=input("Enter your password : ")
    confirm_pass=input("Enter Password to confirm : ")

    if confirm_pass!=password:
        print("Password don't match.")
        print()
        user_signup()
    
    cursor.execute("INSERT INTO users(name,monthly_income,password) VALUES (%s,%s,%s) RETURNING user_id",(name,income,password))
    connection.commit()
    user_id=cursor.fetchone()[0]

    print("Succesfully Registered.")
    print(f"Your User_id is {user_id}.")



def get_password(password,user):
    if password==user[1]:
        return password
    
    else:
        print("Password is invalid \nTRY AGAIN !") 
        print()
        
        check_password=input("Enter Your Password : ")
        get_password(check_password,user)


def user_login():
    user_id=int(input("Enter your user id : "))
    password=input("Enter Your Password : ")
    
    cursor.execute("SELECT user_id,password FROM users WHERE user_id=%s",(user_id,))
    user=cursor.fetchone()
    if user_id != user[0]:
        print("User not Exists.")
    
    elif password != user[1]:
        get_password()

    else:
        print("Welcome Again.")
        return user_id


def change_password():
    user_id=int(input("Enter your user id : "))
    password=input("Enter Your Password : ")
    
    cursor.execute("SELECT user_id,password FROM users WHERE user_id=%s",(user_id,))
    user=cursor.fetchone()
    if user_id != user[0]:
        print("User not Exists.")
        return
    
    elif password != user[1]:
        print("Invalid Password")
        return

    new_pass=input("Enter New password : ")
    confirm_pass=input("Enter Password to confirm : ")

    if confirm_pass!=new_pass:
        print("Password don't match.")
        return

    cursor.execute("UPDATE users SET password=%s WHERE user_id=%s",(new_pass,user_id))

    connection.commit()
    print("Password Changed.")


def delete_user():
    user_id=int(input("Enter your user id : "))
    password=input("Enter your password : ")

    cursor.execute("SELECT user_id,password FROM users WHERE user_id=%s",(user_id,))

    user=cursor.fetchone()

    if user_id != user[0]:
        print("User not Exists")
    
    elif password != user[1]:
        get_password()
    
    else:
        cursor.execute("DELETE FROM users WHERE user_id=%s",(user_id,))

        connection.commit()
        print("User Deleted Successfully.")