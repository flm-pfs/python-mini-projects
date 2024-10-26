import json


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content):
        # Create a dictionary representing a post
        post = {
            "title": title,
            "content": content
        }
        # Append the post to the list of posts
        self.posts.append(post)
        print(f"Post '{title}' added successfully.")

    def list_posts(self):
        if not self.posts:
            print("No posts found.")
        else:
            for post in self.posts:
                print(f"Title: {post['title']}\nContent: {post['content']}\n")

    def save_posts(self, filename):
        # Save the posts to a JSON file
        with open(filename, 'w') as file:
            json.dump(self.posts, file)
        print(f"Posts saved to {filename}.")

    def load_posts(self, filename):
        try:
            # Load the posts from a JSON file
            with open(filename, 'r') as file:
                self.posts = json.load(file)
            print(f"Posts loaded from {filename}.")
        except FileNotFoundError:
            print("File not found.")

    def menu(self):
        while True:
            print("\nSimple Blog Menu:")
            print("1. Add Post")
            print("2. List Posts")
            print("3. Save Posts")
            print("4. Load Posts")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter title: ")
                content = input("Enter content: ")
                self.add_post(title, content)
            elif choice == '2':
                self.list_posts()
            elif choice == '3':
                filename = input("Enter filename to save: ")
                self.save_posts(filename)
            elif choice == '4':
                filename = input("Enter filename to load: ")
                self.load_posts(filename)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    blog = Blog()
    blog.menu()
