from unittest import TestCase
from unittest.mock import patch
import blog.tests.app as app
from blog import Blog




class AppTest(TestCase):

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            pp.menu()
            mocked_input.assert_called_with("aoo.MENU_PROMPT")

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:  
            app.menu()
            mocked_print_blogs.assert_called()
        

    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')


