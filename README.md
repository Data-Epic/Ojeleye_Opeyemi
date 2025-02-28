# Note_Ojeleye_Opeyemi
Task1 submission

# Task: Build a Smart Notes Manager


## The task is to build a Smart Notes Manager that can help users to create, organize, and manage different types of notes.

The Notes Manager: NotesManager
This is the organizer for all the notes. It helps you:

Add new notes.

Delete notes.

Show all notes.

Search for notes.

Key Features:
notes: A list that stores all the notes.

next_id: A counter to give each note a unique ID.

Methods:

add_note(): Adds a new note (either TextNote or ReminderNote).

delete_note(): Removes a note by its ID.

show_notes(): Displays all notes.

search_notes(): Finds notes containing a specific keyword.


How Everything Fits Together Creating a Note:

When you add a note, the NotesManager creates either a TextNote or ReminderNote object and stores it in the notes list.

Each note gets a unique ID.

Displaying Notes:

The display() method of each note is called to show its details.

Searching Notes:

The program looks through all the notes and checks if the keyword is in the content.

Deleting Notes:

The program finds the note with the given ID and removes it from the notes list.
