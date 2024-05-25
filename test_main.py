import unittest
from unittest.mock import patch
from nltk.chat.util import Chat, reflections
from main import pairs, my_dummy_reflections

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.chat = Chat(pairs, reflections)

    def test_greeting(self):
        response = self.chat.respond("hello")
        self.assertIn(response, ["Hello", "Hey there"])

    def test_name_query(self):
        response = self.chat.respond("what is your name?")
        self.assertEqual(response, "My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .")

    def test_location_query(self):
        response = self.chat.respond("where are you located?")
        self.assertEqual(response, "Cairo, egypt")

    def test_quit(self):
        response = self.chat.respond("quit")
        self.assertIn(response, ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"])

    @patch('builtins.print')
    def test_print_statements(self, mock_print):
        from main import __name__
        with self.assertLogs() as captured:
            __name__ == "__main__"
        self.assertEqual(captured.output, ['{}', "Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave "])
        mock_print.assert_any_call(reflections)

    def test_reflections(self):
        response = self.chat.respond("I go to the park")
        self.assertEqual(response, "That is nice to hear")

    def test_dummy_reflections(self):
        self.chat.reflections.update(my_dummy_reflections)
        response = self.chat.respond("hello")
        self.assertEqual(response, "hey there")

if __name__ == '__main__':
    unittest.main()
