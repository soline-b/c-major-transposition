#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description of a sheet music

Tools to handle a sheet music's data and the operations that can be done on it.
"""

# Store the equivalence between integers and notes'names
_notes_equivalences = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

class SheetMusic:
    """
    A sheet music is a sequence of different notes

    Attributes
    ----------
    notes: list
        A sequence of int representing the different notes of the sheet music.
        C corresponds to the int 1, C# to 2, D to 3, etc.
    """

    def __init__(self,notes=[]):
        """ Initialization of a new SheetMusic """

        # Check if the notes are integers
        if isinstance(notes, list):
            for note in notes:
                if not isinstance(note, int):
                    raise ValueError("The notes argument is not an int array")
        else:
            raise ValueError("The notes argument is not an int array")

        # Set the notes
        self.notes = notes

    def get_notes_as_int(self):
        """ Get the notes as a list of integers """
        return self.notes

    def get_notes_as_str(self):
        """ Get the notes as a list of strings """

        # Initialise the array of note's names
        notes_names = []

        # Format the notes in order to display their names
        for note in self.notes:
            # If the note is from lower octaves
            if note < 0:
                octave_number = int(note/12)-1
                note_name = "{0}{1}".format(_notes_equivalences[note%12],octave_number)
            # If the note is from the current octave
            elif note < 12:
                note_name = _notes_equivalences[note%12]
            # If the node is from higher octaves
            else:
                octave_number = int(note/12)
                note_name = "{0}{1}".format(_notes_equivalences[note%12],octave_number)

            notes_names.append(note_name)

        # Return the names array
        return notes_names
