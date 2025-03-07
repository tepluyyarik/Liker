import sqlite3


con = sqlite3.connect("yunk.db")
cursor = con.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT UNIQUE, 
        password TEXT
    );
""")
con.commit()

def register():
    username = input("Введіть ім'я користувача(найкраще): ")
    password = input("Введи вже цей пароль: ")
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        con.commit()
        print("Реєстрація успішна!Позви друзів до нас!")
    except sqlite3.IntegrityError:
        print("Користувач з таким ім'ям вже має бути на цьому світі!")

def enterac():
    username = input("Введіть ім'я юзера: ")
    password = input("Введіть пароль щоб вижити: ")
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        print(f"Вхід успішний! А вихід грішний, {username}!")
    else:
        print("Неправильне ім'я користувача або пароль.")

while True:
    choice = input("Оберіть варіант входу: reg - Реєстрація, ent - Вхід, ex - Вихід: ")

    if choice == "reg":
        register()
    elif choice == "ent":
        enterac()
    elif choice == "ex":
        print("Ха, тільки ти вийшов!")
        break
    else:
        print("Невірний дум, спробуй ще раз.")


con.close()