from blog import Blog

POST_TEMPLATE ='''
---{}---

{}

'''
PROMPT_MENU =('Enter "c" to create blog, "l" to list blog, "r" to read one, "p" to crate post, or "q" to quit')
blogs = dict()      # Blog name : Blog object


def menu():

    print_blogs()
    selection = input(PROMPT_MENU)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(PROMPT_MENU)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def ask_create_blog():
    title = input('Enter your title :')
    author = input('Enter your name')

    blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input('Enter the blog title you want to read :')

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    pass
