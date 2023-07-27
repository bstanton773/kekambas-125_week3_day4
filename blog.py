
class Blog:
    def __init__(self):
        self.users = []
        self.posts = []

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

class Post:
    pass


# Define a function to run the blog!
def run_blog():
    print('Welcome to the blog. I built it myself.')
    # Create an instance of the blog
    my_blog = Blog()
    # Start "running" the blog until the user quits
    while True:
        # Print our menu options
        print("1. Sign Up\n5. Quit")
        # Ask the user which option they would like to do
        to_do = input('Which option would you like to do? ')
        # Keep asking is user does not choose a valid option
        while to_do not in {'1', '5'}:
            to_do = input('Invalid option. Please choose 1 or 5. ')
        # If the user chooses 5, quit the program
        if to_do == '5':
            print('Thanks for checking out the blog!')
            break
        # If they choose option 1, sign the user up
        elif to_do == '1':
            # Call the Blog method to add a new user
            my_blog.create_new_user()


# Call the function to actually start the blog
run_blog()
