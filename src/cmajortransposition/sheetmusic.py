#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import the tools related to the notes
import cmajortransposition.notetools as NoteTools

"""
Description of a sheet music

Tools to handle a sheet music's data and the operations that can be done on it.
"""

class SheetMusic:
    """
    A sheet music is a sequence of different notes

    Methods
    -------
    __init__(self,notes=[])
        Initialize the class

    get_notes_as_int(self)
        Get the notes as a list of integers

    get_notes_as_str(self)
        Get the notes as a list of strings
    """

    def __init__(self,notes=[]):
        """
        Initialize a new SheetMusic

        Parameters
        ----------
        notes: list, optional
            A sequence of int representing the different notes of the sheet music.
            Its default value is an empty list, representing an empty sheet music.

            Currently, the project is focused on the different tones of the notes,
            and not the rhythm. Thus, notes are only defined by their tones.

            In the common Western music, each octave can be divided into 12 tones.
            Based on this twelve-tone equal temperament, each tone of this program
            is represented by an integer.
            Thus, the following equivalences have been set up:

            |  Notes  |  Related integer  |
            | ------- | ----------------- |
            | C       | 0                 |
            | C# / Db | 1                 |
            | D       | 2                 |
            | D# / Eb | 3                 |
            | E       | 4                 |
            | F       | 5                 |
            | F# / Gb | 6                 |
            | G       | 7                 |
            | G# / Ab | 8                 |
            | A       | 9                 |
            | A# / Bb | 10                |
            | B       | 11                |

            Lower or upper integers can represent notes of another octave,
            lower or higher than the octave of reference.

            Examples
            ---------
            The C note of the octave above the octave of reference is annotated `C(1)`
            and corresponds to the integer `12`.
            The C note of the octave below the octave of reference is annotated `C(-1)`
            and corresponds to the integer `-12`.

        Raises
        ------
        ValueError
            If the parameter does not present a correct format.
        """

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
        """
        Get the notes as a list of integers

        Returns
        -------
        list
            A sequence of int representing the different notes of the sheet music.

            Examples
            --------
            C corresponds to the int 1, C# to 2, D to 3, etc.
        """
        return self.notes

    def get_notes_as_str(self):
        """
        Get the notes as a list of strings

        Returns
        -------
        list
            A sequence of string representing the different notes of the sheet music.
            If the note is not contained in the reference octave,
            an octave number is added between parenthesis.

            Examples
            --------
            C# is written C#/Db.
            C(-1) is the C key of the octave below.
        """

        # Initialise the array of note's names
        notes_names = []

        # Format the notes in order to display their names
        for note in self.notes:
            note_description = NoteTools.get_name_and_octave(note)

            if note_description["octave"] == 0:
                note_name = note_description["name"]
            else:
                note_name = "{0}({1})".format(note_description["name"],note_description["octave"])

            # Add the formatted note to the return array
            notes_names.append(note_name)

        # Return the names array
        return notes_names

    def is_transposable_in_c_major(self):
        """
        Check if the sheet music is transposable in C major (ie with no accidental)

        Returns
        -------
        bool
            Whether or not it is transposable:
            True if it is
            False if it is not
        """

        return self.get_transposition_in_c_major_description()["transposable"]

    def get_transposition_in_c_major_description(self):
        """
        Check if the sheet music is transposable in C major (ie with no accidental),
        and if it is, return the number of tone to add

        Returns
        -------
        dict
            A dictionary presenting the following format:
            {
                "transposable": True,
                "tones_added": 3
            }
        """
        # Get a dict of all the different notes in the partition
        reference_notes = []
        for n in self.notes:
            reference_notes.append(n%12)
        all_notes = set(reference_notes)

        return self.get_transposition_in_c_major_description_helper(all_notes)



    def get_transposition_in_c_major_description_helper(self, notes, tones_added=0):
        """
        Helper to check if the sheet music is transposable in C major
        (ie with no accidental), and if it is, return the number of tone to add

        Parameters
        ----------
        tones_added: int
            Number of tones to try to add to each note in order to transpose
            the sheet music in C major

        Returns
        -------
        dict
            A dictionary presenting the following format:
            {
                "transposable": True,
                "tones_added": 3
            }
        """
        # Get all the notes of C major
        c_major_notes = NoteTools.get_c_major_notes()

        # Check if there are accidentals in the notes, if so return True
        if (notes.issubset(c_major_notes)):
            return {"transposable": True, "tones_added": tones_added}

        # If we have done 12 transposition without getting only the C major
        # notes, return False
        if (tones_added > 11):
            return {"transposable": False, "tones_added": 0}

        # Otherwise, try transpositions
        new_notes = []
        for old_note in notes:
            new_notes.append(old_note+1)
        return self.get_transposition_in_c_major_description_helper(set(new_notes), tones_added+1)
