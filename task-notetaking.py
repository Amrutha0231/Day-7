import os

def display_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
            else:
                print("No notes available.")
    else:
        print("No notes available.")

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")

def delete_note():
    display_notes()
    try:
        note_number = int(input("Enter the note number to delete: ")) - 1
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if 0 <= note_number < len(notes):
            deleted_note = notes.pop(note_number)
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            print(f"Note deleted: {deleted_note.strip()}")
        else:
            print("Invalid note number.")
    except (ValueError, IndexError):
        print("Invalid input. Enter a valid note number.")

while True:
    print("Note-taking Application")
    print("Choose an action:")
    print("1 - View notes")
    print("2 - Add note")
    print("3 - Delete note")
    print("4 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option.")
