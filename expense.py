from connection import connecting
from category_report import view_categories

connection,cursor=connecting()

def user_view(user_id):
    cursor.execute("SELECT expense_id,category_name,amount,expense_date FROM user_view WHERE expenses.user_id=%s",(user_id,))

    user_expenses=cursor.fetchall()

    return user_expenses

def payment_method():
    pay_values={
        "1":"Cash",
        "2":"UPI",
        "3":"Card"
    }
    for values in pay_values:
        print(f"press {values} for {pay_values[values]}")
    choice=input("Enter Your Choice : ")
    if choice not in pay_values:
        print("Please enter Valid input.")
        payment_method()
    else:
        return pay_values[choice]

def get_category():
    print("Choose your category and Enter its Category ID ")
    print()
    all_ids=view_categories()
    category_id=int(input("Enter your category ID : "))
    if category_id not in all_ids:
        print("Please enter a valid ID.")
        get_category()
    else:
        return category_id


def add_expense(user_id):

    try:
        category_id=get_category()
        amount=int(input("Enter Amount you Spend : "))
        description=input("Add Description (OPTIONAL) : ")
        pay_method=payment_method()

        cursor.execute("INSERT INTO expenses (user_id,category_id,amount,description,payment_method) VALUES(%s,%s,%s,%s,%s) RETURNING expense_id;",(user_id,category_id,amount,description,pay_method))
        connection.commit()
        print()
        print("Expense Successfully Added")
        expense_id=cursor.fetchone()[0]

        return expense_id
    
    except Exception as e:
        print(e)



def delete_expense(user_id):

    print(f"{'Expense ID':<12}{'Category':<12}{'Amount':<12}{'Expense Date':<12}")
    user_expenses=user_view(user_id)
    for exp in user_expenses:
        print(f"{exp[0]:<12}{exp[1]:<12}{exp[2]:<12}{str(exp[3]):<12}")

    expense_id=int(input("Enter Expense ID you want to Delete : "))

    cursor.execute("DELETE FROM expenses WHERE expense_id=%s",(expense_id,))

    connection.commit()
    print()
    print("Expense Successfully Deleted.")


def update_expense(user_id):

    print(f"{'Expense ID':<12}{'Category':<12}{'Amount':<12}{'Expense Date':<12}")

    user_expenses=user_view(user_id)
    
    for exp in user_expenses:
        print(f"{exp[0]:<12}{exp[1]:<12}{exp[2]:<12}{str(exp[3]):<12}")

    expense_id=int(input("Enter Expense ID you want to Update : "))
    new_amount=int(input("Enter new amount : "))
    new_category_id=get_category()

    cursor.execute("UPDATE FROM expenses SET amount=%s,category_id= WHERE expense_id=%s",(expense_id,new_amount,new_category_id))

    connection.commit()
    print()
    print("Expense Successfully Update.")


def view_expense(user_id):
    

    print(f"{'Expense ID':<12}{'Category':<12}{'Amount':<12}{'Expense Date':<12}")
    user_expenses=user_view(user_id)
    for exp in user_expenses:
        print(f"{exp[0]:<12}{exp[1]:<12}{exp[2]:<12} {str(exp[3]):<12}")

