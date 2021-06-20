#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for "sheetmusic" in c-major-transposition
"""

import unittest
from nose2.tools import params

# Import the functons to test from the cmajortransposition.sheetmusic package
from cmajortransposition import sheetmusic

# This is a temporary class in order to test the structure of the project
class TestSheetMusic(unittest.TestCase):

    def test_init_wrong_attribute_list(self):
        """ Check if an error occurs if a bad attribute is submitted in the SheetMusic creation """
        self.assertRaises(ValueError, sheetmusic.SheetMusic, ["test"])

    def test_init_wrong_attribute_int(self):
        """ Check if an error occurs if a bad attribute is submitted in the SheetMusic creation """
        self.assertRaises(ValueError, sheetmusic.SheetMusic, 12)

    @params([3,5,9,0,15], [])
    def test_get_notes_as_int(self, initial_notes):
        """ Check if the notes stored then returned by a SheetMusic stay the same """
        a_sheet_music = sheetmusic.SheetMusic(initial_notes)
        assert a_sheet_music.get_notes_as_int() == initial_notes


    @params({'in': [0,2,4,5,7,9,11], 'out': ['C','D','E','F','G','A','B']},
            {'in': [], 'out': []},
            {'in': [-25,3,2,0,-12,-6,-4,5,8,24,12,0,2,1,1], 'out': ['B(-3)','D#/Eb','D','C','C(-1)','F#/Gb(-1)','G#/Ab(-1)','F','G#/Ab','C(2)','C(1)','C','D','C#/Db','C#/Db']})
    def test_display_notes(self, notes):
        """ Check the return of the notes as strings """
        a_sheet_music = sheetmusic.SheetMusic(notes['in'])
        assert a_sheet_music.get_notes_as_str() == notes['out']
