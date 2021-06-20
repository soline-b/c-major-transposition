#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tools for operations relative to musical notes
"""

# Store the equivalence between integers and notes'names through a sequence
# presenting the names of the 12 tones composing an octave.
notes_equivalences = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

def get_name_and_octave(note):
    """
    Retrieve the note name and the octave corresponding to an integer
    representing a note

    Parameters
    ----------
    note: int
        The integer representing the note

    Returns
    -------
    dict
        A dictionary presenting the following format:
        {
            "name": "C",
            "octave": 2
        }

    Raises
    ------
    ValueError
        If the parameter does not present a correct format.
    """

    # Check the parameter
    if not isinstance(note, int):
        raise ValueError("The note parameters is not an integer")

    # Initialize the values
    note_name = notes_equivalences[note%12]
    octave_number = 0

    # Extract name and octave from the note
    # If the note is from lower octaves
    if note < 0:
        if note_name == 'C':
            octave_number = int(note/12)
        else:
            octave_number = int(note/12)-1

    # If the note is from the current octave
    elif note < 12:
        octave_number = 0

    # If the node is from higher octaves
    else:
        octave_number = int(note/12)

    # Return the corresponding dictionary
    return {"name": note_name, "octave": octave_number}
