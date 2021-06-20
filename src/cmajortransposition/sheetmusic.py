#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import warnings library to write warning messages
import warnings

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

    set_notes(self, new_notes)
        Modify all the notes of the sheet music

    is_transposable_in_c_major(self)
        Check if the sheet music is transposable in C major (ie with no accidental)

    transpose_in_c_major(self)
        Transpose the sheet music in C major if it is possible

    get_transposition_in_c_major_description(self)
        Check if the sheet music is transposable in C major (ie with no accidental),
        and if it is, return the number of tones to add

    def get_transposition_in_c_major_description_helper(self, notes, tones_added=0)
        Helper to check if the sheet music is transposable in C major
        (ie with no accidental), and if it is, return the number of tone to add
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

    def set_notes(self, new_notes):
        """
        Modify all the notes of the sheet music

        Parameters
        ----------
        new_notes: list
            A list of int representing the new notes of the sheet music

        Raises
        ------
        ValueError
            If the parameter does not present a correct format.
        """

        # Check if the notes are integers
        if isinstance(new_notes, list):
            for note in new_notes:
                if not isinstance(note, int):
                    raise ValueError("The new_notes argument is not an int array")
        else:
            raise ValueError("The new_notes argument is not an int array")

        self.notes = new_notes

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

    def transpose_in_c_major(self):
        """
        Transpose the sheet music in C major if it is possible

        Returns
        -------
        list
            A list of integers representing notes: the transposed sheet music if
            the latter is transposable, the original sheet music otherwise
        """
        # Get if the transposition is possible, and if so, get the number of
        # tones to add to the notes
        transposition_description = self.get_transposition_in_c_major_description()

        # If the sheet music is not transposable in C major, print a warning
        if not transposition_description["transposable"]:
            warnings.warn("The sheet music can not be transposed in C major.", UserWarning)
            return self.notes

        # If the sheet music is transposable in C major, transpose it
        tones_to_add = transposition_description['tones_added']
        new_notes = []
        for note in self.notes:
            new_notes.append(note+tones_to_add)
        return new_notes

    def get_transposition_in_c_major_description(self):
        """
        Check if the sheet music is transposable in C major (ie with no accidental),
        and if it is, return the number of tones to add

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
        notes: set
            A set of notes to transpose

        tones_added: int
            Number of tones to try to add to each note in order to transpose
            the sheet music in C major (Default: 0)

        Returns
        -------
        dict
            A dictionary presenting the following format:
            {
                "transposable": True,
                "tones_added": 3
            }
            (In this one, for instance, 3 tones are added to the notes to
            transpose the sheet music in C major)

            If the transposition is impossible, the returned dictionary is:
            {
                "transposable": False,
                "tones_added": 0
            }

        Raises
        ------
        ValueError
            If the parameter does not present a correct format.
        """

        # Check if the notes are integers
        if isinstance(notes, set):
            for note in notes:
                if not isinstance(note, int):
                    raise ValueError("The notes argument is not a set of integers")
        else:
            raise ValueError("The notes argument is not a set of integers")

        # Check if tones_added is an integers
        if not isinstance(tones_added, int):
            raise ValueError("The notes argument is not a set of integers")

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
            new_notes.append((old_note+1)%12)
        return self.get_transposition_in_c_major_description_helper(set(new_notes), tones_added+1)
