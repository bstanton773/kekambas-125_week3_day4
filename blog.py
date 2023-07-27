
class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None

    # Method to create a new user instance and add to the Blog's users
    def create_new_user(self):
        # Get user info from input
        username = input('Please enter a username: ')
        # Check if a user already has that username
        if username in [u.username for u in self.users]:
            print(f"User with username {username} already exists")
        else:
            password = input('Please enter a password: ')
            # Create a new instance of User with the input info
            new_user = User(username, password)
            # Add the new user to the users list
            self.users.append(new_user)
            print(f"{new_user} has been created")

    # Method will log a user in by setting the current_user to a User instance
    def log_user_in(self):
        # Get user credentials via input
        username = input('What is your username? ')
        password = input('What is your password? ')
        # Loop through each user in the blog
        for user in self.users:
            # Check if the user has that username AND the user's password is correct
            if user.username == username and user.check_password(password):
                # If credentials are correct, set the blog's current_user to that user instance
                self.current_user = user
                print(f"{user} has logged in")
                break
        # If no users in the blog have that username/password, flash invalid credentials message
        else:
            print("Username and/or password is incorrect")



class User:
    id_counter = 1
    
    def __init__(self, username, password):
        self.username = username
        self.password = hash(password)
        self.id = User.id_counter
        User.id_counter += 1

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<User {self.id}|{self.username}>"

    def check_password(self, password_attempt):
        return self.password == hash(password_attempt)

class Post:
    pass


# Define a function to run the blog!
def run_blog():
    print('Welcome to the blog. I built it myself.')
    # Create an instance of the blog
    my_blog = Blog()
    # Start "running" the blog until the user quits
    while True:
        # If there is currently nobody logged in to the blog (aka the current_user is None)
        if my_blog.current_user is None:
            # Print our menu options
            print("1. Sign Up\n2. Log In\n5. Quit")
            # Ask the user which option they would like to do
            to_do = input('Which option would you like to do? ')
            # Keep asking is user does not choose a valid option
            while to_do not in {'1', '5', '2'}:
                to_do = input('Invalid option. Please choose 1, 2, or 5. ')
            # If the user chooses 5, quit the program
            if to_do == '5':
                print('Thanks for checking out the blog!')
                break
            # If they choose option 1, sign the user up
            elif to_do == '1':
                # Call the Blog method to add a new user
                my_blog.create_new_user()
            # If they choose option 2, log the user in
            elif to_do == '2':
                # Call the blog method to log user in
                my_blog.log_user_in()
        # If there is a logged in user (aka current_user is not None, it is a user instance)
        else:
            # Ask the user for an input and then quit.
            print('Quit')
            to_do = input('Which option would you like to do? ')
            if to_do == 'quit':
                break


# Call the function to actually start the blog
run_blog()
