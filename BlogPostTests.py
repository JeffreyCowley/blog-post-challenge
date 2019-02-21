import unittest
import configparser
from BlogPost import BlogPostApp


class BlogPostTest(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser(strict=False, interpolation=None)
        config.read('BlogPost.ini')
        database_file = config['Files']['database_file']

        self.blog_post_app = BlogPostApp()

        logging_file = config['Files']['log_file']
        logging_format = config['Logging']['format']
        logging_level = config['Logging']['level']

        self.blog_post_app.setup_logging(logging_file, logging_level, logging_format)

        self.blog_post_app.connect_database(database_file)

    def test_get_all(self):
        result = self.blog_post_app.get_all_entries()
        self.assertTrue(result[0][0] == 1)
        self.assertTrue(result[0][1] == 'hai')
        self.assertTrue(result[0][2] == 'hai')

    def test_set(self):
        set_result = self.blog_post_app.set_entry('hello', 'hello world')
        self.assertTrue(set_result > 0)

        get_result = self.blog_post_app.get_entry(set_result)
        self.assertTrue(get_result[0] == set_result)
        self.assertTrue(get_result[1] == 'hello')
        self.assertTrue(get_result[2] == 'hello world')

    def test_get(self):
        result = self.blog_post_app.get_entry(1)
        self.assertTrue(result[0] == 1)
        self.assertTrue(result[1] == 'hai')
        self.assertTrue(result[2] == 'hai')


if __name__ == '__main__':
    unittest.test_get_all()
    unittest.test_set()
    unittest.test_get()
