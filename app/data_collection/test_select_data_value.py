import unittest,io,sys
from get_stand_in_data import select_data_value

class TestSelectDataValueFunction(unittest.TestCase):
    
    def test_valid_arguments(self):
        valid_arguments = ["test_data_1","test_data_2","test_data_3","test_data_4"]
        final_data_selections = []

        for argument in valid_arguments:
            fake_argv_list = ["main.py", argument]
            final_data_selections.append(select_data_value(fake_argv_list))

        self.assertEqual(valid_arguments,final_data_selections)

    def test_invalid_argument(self):
        invalid_argument = "invalid_argument_name"
        fake_argv_list = ["main.py", invalid_argument, "test"]
        return_string = None
        
        captured_output = io.StringIO()        
        sys.stdout = captured_output

        return_string = select_data_value(fake_argv_list)
        
        sys.stdout = sys.__stdout__

        self.assertEqual(return_string, None)
        self.assertEqual("Please pass a valid test data selection.\n", captured_output.getvalue())

    def test_no_argument(self):
        fake_argv_list = ["main.py"]
        valid_final_selections = ["test_data_1","test_data_2","test_data_3","test_data_4"]
        selected_data_value = select_data_value(fake_argv_list)
        self.assertIn(selected_data_value, valid_final_selections)