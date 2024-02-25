import unittest
from unittest.mock import patch
import comparison

# since this function randomly chooses a comparison, we need to force which one is picked so we can test and output. We use 'mock'
# to define which case is chosen
class test_emissions_comparison_text(unittest.TestCase):

    @patch('comparison.random.choice')
    def test_tree_comparison(self, mock_choice):
        mock_choice.return_value = 'tree_comparison' #using mock the say that 'tree_comparison' was "randomly chosen"
        metric_tons_co2_emitted = 5.5
        output = comparison.get_emissions_comparison_text(metric_tons_co2_emitted)
        self.assertEqual(output, "It will take 275 trees approximately 1 year to remove this CO2 from the atmosphere.") #this is the expected output assuming that the jet trip emitted 5.5 mt CO2

    @patch('comparison.random.choice')
    def test_LA_NY_comparison(self, mock_choice):
        mock_choice.return_value = 'LA_NY_drive_comparison' #using mock the say that 'LA_NY_drive_comparison' was "randomly chosen"
        metric_tons_co2_emitted = 5.5
        output = comparison.get_emissions_comparison_text(metric_tons_co2_emitted)
        self.assertEqual(output, "You would have to drive from LA to NY 5 times to emit this same amount.") #expected output given a 5.5 mt co2 jet trip emission

    @patch('comparison.random.choice')
    def test_average_american_comparison_less_than_one_year(self, mock_choice):
        mock_choice.return_value = 'average_american_emissions_comparison' #using mock the say that 'average_american_emissions_comparison' was "randomly chosen"
        metric_tons_co2_emitted = 5.5
        output = comparison.get_emissions_comparison_text(metric_tons_co2_emitted)
        self.assertEqual(output, "It would take an average American 4 months to emit the same amount.") #expected output given a 5.5 mt co2 jet trip emission, confirming output is in months

    @patch('comparison.random.choice')
    def test_average_american_comparison_one_year(self, mock_choice):
        mock_choice.return_value = 'average_american_emissions_comparison' #using mock the say that 'average_american_emissions_comparison' was "randomly chosen"
        metric_tons_co2_emitted = 14.5
        output = comparison.get_emissions_comparison_text(metric_tons_co2_emitted)
        self.assertEqual(output, "It would take an average American 1.0 years to emit the same amount.") #confirming correct output in years for 1 year worth of emissons

    @patch('comparison.random.choice')
    def test_average_american_comparison_more_than_one_year(self, mock_choice):
        mock_choice.return_value = 'average_american_emissions_comparison' #using mock the say that 'average_american_emissions_comparison' was "randomly chosen"
        metric_tons_co2_emitted = 20
        output = comparison.get_emissions_comparison_text(metric_tons_co2_emitted)
        self.assertEqual(output, "It would take an average American 1.38 years to emit the same amount.") #confirming output for > 1 years worth of emissions
