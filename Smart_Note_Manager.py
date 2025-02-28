"""
Task: Build a Smart Notes Manager
"""

from datetime import datetime

# Step 1: Define the base class `Note`
class Note:
    def __init__(self, content):
        """
        Initialize a new note.
        
        :param content: The text content of the note.
        """
        self.content = content  # Store the note content
        self.created_at = datetime.now()  # Store the creation timestamp
        self.id = None  # Initialize the ID as None (will be set by NotesManager)

    def display(self):
        """
        Display the note details.
        """
        print(f"ID: {self.id}")  # Display the note ID
        print(f"Content: {self.content}")
        print(f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")


# Step 2: Create specialized classes
class TextNote(Note):
    def __init__(self, content):
        """
        Initialize a text-based note.
        
        :param content: The text content of the note.
        """
        super().__init__(content)  # Call the parent class constructor

    def display(self):
        """
        Override the display method to show text note details.
        """
        print("=== Text Note ===")
        super().display()  # Call the parent class display method


class ReminderNote(Note):
    def __init__(self, content, reminder_time):
        """
        Initialize a reminder note.
        
        :param content: The text content of the note.
        :param reminder_time: The reminder date and time (as a string in 'YYYY-MM-DD HH:MM:SS' format).
        """
        super().__init__(content)  # Call the parent class constructor
        self.reminder_time = datetime.strptime(reminder_time, '%Y-%m-%d %H:%M:%S')  # Convert string to datetime

    def display(self):
        """
        Override the display method to show reminder note details.
        """
        print("=== Reminder Note ===")
        super().display()  # Call the parent class display method
        print(f"Reminder Time: {self.reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")


# Step 3: Implement the NotesManager class
class NotesManager:
    def __init__(self):
        """
        Initialize the notes manager.
        """
        self.notes = []  # Store all notes in a list
        self.next_id = 1  # Assign unique IDs to notes

    def add_note(self, note_type, content, reminder_time=None):
        """
        Add a new note to the manager.
        
        :param note_type: The type of note ('text' or 'reminder').
        :param content: The text content of the note.
        :param reminder_time: The reminder time (only for reminder notes).
        """
        if note_type == "text":
            note = TextNote(content)  # Create a TextNote
        elif note_type == "reminder":
            note = ReminderNote(content, reminder_time)  # Create a ReminderNote
        else:
            print("Invalid note type. Use 'text' or 'reminder'.")
            return

        note.id = self.next_id  # Assign a unique ID to the note
        self.notes.append(note)  # Add the note to the list
        self.next_id += 1  # Increment the ID counter
        print(f"Note added successfully with ID: {note.id}")

    def delete_note(self, note_id):
        """
        Delete a note by its ID.
        
        :param note_id: The ID of the note to delete.
        """
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)  # Remove the note from the list
                print(f"Note with ID {note_id} deleted successfully.")
                return
        print(f"Note with ID {note_id} not found.")

    def show_notes(self):
        """
        Display all stored notes.
        """
        if not self.notes:
            print("No notes found.")
            return

        for note in self.notes:
            note.display()  # Call the display method of each note
            print("-" * 30)

    def search_notes(self, keyword):
        """
        Search for notes containing a specific keyword.
        
        :param keyword: The keyword to search for.
        """
        found_notes = [note for note in self.notes if keyword.lower() in note.content.lower()]
        if not found_notes:
            print(f"No notes found containing the keyword '{keyword}'.")
            return

        print(f"Found {len(found_notes)} note(s) containing the keyword '{keyword}':")
        for note in found_notes:
            note.display()
            print("-" * 30)


# The user interface that allows you to interanct with th Notes Manager.

# Step 4: Main Program Execution
def main():
    manager = NotesManager()  # Create a NotesManager instance

    while True:
        print("\n=== Welcome to Smart Notes Manager ===")
        print("1. Add a Text Note")
        print("2. Add a Reminder Note")
        print("3. View All Notes")
        print("4. Search Notes")
        print("5. Delete a Note")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            content = input("Enter the note content: ")
            manager.add_note("text", content)  # Add a text note

        elif choice == "2":
            content = input("Enter the note content: ")
            reminder_time = input("Enter the reminder time (YYYY-MM-DD HH:MM:SS): ")
            manager.add_note("reminder", content, reminder_time)  # Add a reminder note

        elif choice == "3":
            manager.show_notes()  # Display all notes

        elif choice == "4":
            keyword = input("Enter the keyword to search: ")
            manager.search_notes(keyword)  # Search for notes

        elif choice == "5":
            note_id = int(input("Enter the ID of the note to delete: "))
            manager.delete_note(note_id)  # Delete a note

        elif choice == "6":
            print("Exiting the Smart Notes Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Step 5: Call the main() function
if __name__ == "__main__":
    main()