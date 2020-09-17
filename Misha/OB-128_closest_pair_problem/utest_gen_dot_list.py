import unittest
from main import generate_dot_list


class GeneratingDotsTest(unittest.TestCase):

    def test_generate_dot_list_with_right_parameter(self):
        dot_list = generate_dot_list(5)
        expected_result = [5, 2]
        self.assertEqual(expected_result, [len(dot_list), len(dot_list[0])])

    def test_generate_dot_list_with_wrong_input_as_string_parameter(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, generate_dot_list('5'))
        the_exception = str(context.exception)
        self.assertEqual('TypeError', the_exception)

    def test_generate_dot_list_with_wrong_input_as_non_type_parameter(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, generate_dot_list(None))
        the_exception = str(context.exception)
        self.assertEqual('TypeError', the_exception)

    def test_generate_dot_list_with_wrong_input_as_list_parameter(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, generate_dot_list([1, 2, 3]))
        the_exception = str(context.exception)
        self.assertEqual('TypeError', the_exception)


if __name__ == '__main__':
    unittest.main()
