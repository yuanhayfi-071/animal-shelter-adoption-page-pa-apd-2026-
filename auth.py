from data import users_data

def login_menu():
    print("""
    Silahkan masuk ke akun anda!
    Sudah punya akun -> 1. Login
    Belum punya akun -> 2. Sign up
""")
    opsi = input("> ")
    if opsi == "1":
        login()
    elif opsi == "2":
        sign_up()
    else:
        print("\nOpsi tidak ditemukan!")

def login():
    pass

def sign_up():
    pass