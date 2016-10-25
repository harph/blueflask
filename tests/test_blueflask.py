#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_blueflask
----------------------------------

Tests for `blueflask` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from blueflask import cli


class TestBlueFlask(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        self.assertEqual(result.exit_code, 0)
        help_result = runner.invoke(cli.main, ['--help'])
        self.assertEqual(help_result.exit_code,0)
        self.assertTrue(
            '--help  Show this message and exit.' in help_result.output)


if __name__ == '__main__':
    unittest.main()
