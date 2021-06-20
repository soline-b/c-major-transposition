# User documentation

## Overview

## Quick start

## Examples

In this example, we learn to create a sheet music.

### Create a sheet music

In this project, a sheet music contains notes presenting a specific tone, regardless of their rhythms. Thus, it can be constructed from a notes array.

The notes are here presented as integers, such as presented in the following array:

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

For our example, we consider the following partition:
![Partition](images/partition.png)

It can be translated as follows:
```
[-3,5,-3,4,-3,5,7,4,-3,7,5,4,2,4,9,9,10,7,0,0,9,10,7,9,10,9,7,5]
```

Thus, the partition can be written by the following lines:

```
# Import the package
from cmajortransposition import sheetmusic

# Initialize the array of notes as int
notes_int = [-3,5,-3,4,-3,5,7,4,-3,7,5,4,2,4,9,9,10,7,0,0,9,10,7,9,10,9,7,5]

# Create the sheet music with the notes as parameters
my_sheetmusic = sheetmusic.SheetMusic(notes_int)

# Return the notes as strings
notes_str = my_sheetmusic.get_notes_as_str()

# Print the notes
print(notes_str)
```

The printed result is:

```
['A(-1)', 'F', 'A(-1)', 'E', 'A(-1)', 'F', 'G', 'E', 'A(-1)', 'G', 'F', 'E', 'D', 'E', 'A', 'A', 'A#/Bb', 'G', 'C', 'C', 'A', 'A#/Bb', 'G', 'A', 'A#/Bb', 'A', 'G', 'F']
```
