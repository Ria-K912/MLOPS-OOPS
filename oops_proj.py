class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to Chatbook!! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5.Press any other key to exit
                           
                           """)
        if user_input =="1":
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input =="3":
            self.write_post()
        elif user_input =="4":
            self.sendmsg()         
        else:
            exit()
            
    def signup(self):
        email = input("Enter username: ")
        pwd = input("Enter password: ")
        self.username = email
        self.password = pwd
        print("Signup successful")
        print("\n")
        self.menu()
        
    def signin(self):
        if self.username == '' and self.password == '':
            print("No user found. Please signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            if self.username == uname and self.password==pwd:
                self.loggedin = True
                print("Signin successful")
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()
        
    def write_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here->")
            print(f"Following content has been posted: {txt}")
        else:
            print("Please signin first to post something")
        print("\n")
        self.menu()
    
    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here ->")
            frnd = input("Whom to send the msg?:")
            print(f"Your message has been sent to {frnd}")
        else:
            print("Please signin first to post something")
        print("\n")
        self.menu()   

            
        
# user1 = chatbook()