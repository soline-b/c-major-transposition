#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for "sheetmusic" in cmajortransposition
"""

# Import the testing libraries
import unittest
from nose2.tools import params

# Import the functons to test from the cmajortransposition.sheetmusic package
from cmajortransposition import sheetmusic

class TestSheetMusic(unittest.TestCase):
    """
    A set of tests for sheetmusic
    """

    def test_init_wrong_parameter_list(self):
        """ Check if an error occurs if a bad parameter is submitted in the SheetMusic creation """
        self.assertRaises(ValueError, sheetmusic.SheetMusic, ["test"])

    def test_init_wrong_parameter_int(self):
        """ Check if an error occurs if a bad parameter is submitted in the SheetMusic creation """
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

    @params({'notes': [1,5], 'transposable': True},
            {'notes': [0], 'transposable': True},
            {'notes': [0,1,2], 'transposable': False},
            {'notes': [-12,30], 'transposable': True})
    def test_is_transposable_in_c_major(self, notes_description):
        """ Check if a music sheet is transposable in C major """
        a_sheet_music = sheetmusic.SheetMusic(notes_description['notes'])
        assert a_sheet_music.is_transposable_in_c_major() == notes_description['transposable']

    @params({'notes': [1,5], 'out': {'transposable': True, 'tones_added': 4}},
            {'notes': [0], 'out': {'transposable': True, 'tones_added': 0}},
            {'notes': [0,1,2], 'out': {'transposable': False, 'tones_added': 0}},
            {'notes': [-12,30], 'out': {'transposable': True, 'tones_added': 5}})
    def test_get_transposition_in_c_major_description(self, notes_description):
        """
        Check if a music sheet is transposable and the number of tones
        to transpose it if it is
        """
        a_sheet_music = sheetmusic.SheetMusic(notes_description['notes'])
        assert a_sheet_music.get_transposition_in_c_major_description() == notes_description['out']

    def test_get_transposition_in_c_major_description_helper_wrong_param1_int(self):
        """ Check if an error occurs if a bad parameter is submitted """
        a_sheet_music = sheetmusic.SheetMusic([1,2,3])
        with self.assertRaises(ValueError):
            a_sheet_music.get_transposition_in_c_major_description_helper(12)

    def test_get_transposition_in_c_major_description_helper_wrong_param1_set(self):
        """ Check if an error occurs if a bad parameter is submitted """
        a_sheet_music = sheetmusic.SheetMusic([1,2,3])
        with self.assertRaises(ValueError):
            a_sheet_music.get_transposition_in_c_major_description_helper(set(["a","b","b"]))

    def test_get_transposition_in_c_major_description_helper_wrong_param2(self):
        """ Check if an error occurs if a bad parameter is submitted """
        a_sheet_music = sheetmusic.SheetMusic([1,2,3])
        with self.assertRaises(ValueError):
            a_sheet_music.get_transposition_in_c_major_description_helper(set([1,2,2]), 'a')
