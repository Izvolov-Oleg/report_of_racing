import unittest
from unittest import mock
import report
import argparse


class TestReport(unittest.TestCase):

    def setUp(self):
        self.path = './data'

    def test_first(self, mock_parse):
        """ test 'build_report' func"""
        self.assertIsInstance(report.build_report(self.path), list)

    @mock.patch('argparse.ArgumentParser.parse_args')
    def test_second(self, mock_parse):
        """test main func"""
        mock_parse.return_value = argparse.Namespace(
            files=self.path, driver='Petr', asc=True, desc=False)
        self.assertRaises(NameError, report.main)
