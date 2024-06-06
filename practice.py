import sqlite3
from sqlite3 import Error
con = sqlite3.connect('C:/Users/salam/Desktop/github/expense/expense.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS control(id integer PRIMARY KEY , spent_for TEXT, amount_money integer)')
while 1:
    application = int(input('1-add expense \n2-view all expenses \n3-update expenses \n4-delete expense \n5-exit\nenter your application: '))

    if application == 1:

        identify = input('enter the id: ')
        spent = input('that spent for : ')
        amount = int(input('how much money: '))
        expense = (identify, spent, amount)
        cur.execute("INSERT INTO control VALUES(?, ?, ?)", expense)
        con.commit()
    
    elif application == 2:
        
        cur.execute("SELECT * FROM control")
        ls_expenses = cur.fetchall()
        for i in ls_expenses:
            print(f'{i[0]} :\ntitle : {i[1]}\namount : {i[2]}')
    
    elif application == 3:
        
        identify = int(input('what of expenses do you want to change?: '))
        app = input('what do you want to change?: ')
        if app == 'spent':
            new_spent_for = input('enter new : ')
            cur.execute('UPDATE control SET spent_for = ? WHERE id = ?', (new_spent_for, identify) )
        
        elif app == 'amount':
            
            new_amount = int(input('enter new amount: '))
            cur.execute('UPDATE control SET amount_money = ? WHERE id = ?', (new_amount , identify))
        con.commit()

    elif application == 4:

        identify = int(input('enter id of row you want to delete: '))
        cur.execute('DELETE FROM control WHERE id = ?', (identify,))
        con.commit()

    elif application == 5:
        print("bye")
        break
    print("****************\n")        
con.close()
