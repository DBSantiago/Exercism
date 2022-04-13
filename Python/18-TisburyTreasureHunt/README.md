# Instructions

Azara and Rui are teammates competing in a pirate-themed treasure hunt. One has a list of treasures with map coordinates, the other a list of location names with map coordinates. They've also been given blank maps with a starting place marked YOU ARE HERE.

But things are a bit disorganized: Azara's coordinates appear to be formatted and sorted differently from Rui's, and they have to keep looking from one list to the other to figure out which treasures go with which locations. Being budding pythonistas, they have come to you for help in writing a small program (a set of functions, really) to better organize their hunt information.

## 1. Extract coordinates

Implement the get_coordinate() function that takes a (treasure, coordinate) pair from Azara's list and returns only the extracted map coordinate.

## 2. Format coordinates

Implement the convert_coordinate() function that takes a coordinate in the format "2A" and returns a tuple in the format ("2", "A").

## 3. Match coordinates

Implement the compare_records() function that takes a (treasure, coordinate) pair and a (location, coordinate, quadrant) record and compares coordinates from each. Return True if the coordinates "match", and return False if they do not. Re-format coordinates as needed for accurate comparison.

## 4. Combine matched records

Implement the create_record() function that takes a (treasure, coordinate) pair from Azara's list and a (location, coordinate, quadrant) record from Rui's list and returns (treasure, coordinate, location, coordinate, quadrant) if the coordinates match. If the coordinates do not match, return the string "not a match". Re-format the coordinate as needed for accurate comparison.

## 5. "Clean up" & make a report of all records

Clean up the combined records from Azara and Rui so that there's only one set of coordinates per record. Make a report so they can see one list of everything they need to put on their maps. Implement the clean_up() function that takes a tuple of tuples (everything from both lists), looping through the outer tuple, dropping the unwanted coordinates from each inner tuple and adding each to a 'report'. Format and return the 'report' so that there is one cleaned record on each line.
