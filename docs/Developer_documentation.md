# Developer documentation

## The SheetMusic class
The `SheetMusic` class implementation is located in the file `src/cmajortransposition/sheetmusic`.

### Attributes
#### Notes
In the common Western music, each octave can be divided into 12 tones.
Based on this twelve-tone equal temperament, each tone of this program is represented
by an integer.
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

Lower or upper integers can represent notes of another octave, lower or higher
than the octave of reference.
