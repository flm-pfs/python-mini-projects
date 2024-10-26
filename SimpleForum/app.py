from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for posts
posts = []


@app.route('/')
def index():
    # Render the index.html template and pass the posts list as a parameter
    return render_template('index.html', posts=posts)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Get the title and content from the form submitted by the user
        title = request.form['title']
        content = request.form['content']

        # Append a new post dictionary to the posts list
        posts.append({'title': title, 'content': content})

        # Redirect the user to the index route after creating the post
        return redirect(url_for('index'))

    # Render the create.html template for GET requests
    return render_template('create.html')


if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
