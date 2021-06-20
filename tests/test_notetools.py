#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for "notetools" in cmajortransposition
"""

# Import the testing libraries
import unittest
from nose2.tools import params

# Import the functions to test
import cmajortransposition.notetools as NoteTools

class TestNoteTools(unittest.TestCase):
    """
    A set of tests for notetools
    """

    def test_get_name_and_octave_input(self):
        """ Check if an error occurs if a bad parameter is submitted in the function """
        self.assertRaises(ValueError, NoteTools.get_name_and_octave, "test")

    @params({'in': -25, 'out': {'name': 'B', 'octave': -3}},
            {'in': 0, 'out': {'name': 'C', 'octave': 0}},
            {'in': -12, 'out': {'name': 'C', 'octave': -1}},
            {'in': 2, 'out': {'name': 'D', 'octave': 0}},
            {'in': 13, 'out': {'name': 'C#/Db', 'octave': 1}}
            )
    def test_get_name_and_octave(self,input_dict):
        """ Check the return of the function for different inputs """
        description = NoteTools.get_name_and_octave(input_dict["in"])
        assert description == input_dict["out"]
