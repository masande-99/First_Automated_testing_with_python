from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):

    def setUp(self):
        blog = Blog('Test', 'Test author')
        app.blogs = {'Test': blog}

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.PROMPT_MENU)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input :
            mocked_input.side_effect = ('Test', 'Test author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value = 'Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test post', 'Test content')
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])


    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = '''
---Post title---

Post content

'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)


