import unittest
from unittest.mock import patch
import comparison

class test_emissions_comparison_calculation(unittest.TestCase):

    @patch('comparison.random.choice')
    def test_tree_comparison(self, mock_choice):
        mock_choice.return_value = "tree_comparison"
        jet_emission = 5.5
        output = comparison.emissions_comparison_calculation(jet_emission)
        self.assertEqual(output, "It will take 275 trees approximately 1 year to remove this CO2 from the atmosphere.")