from address_book import AddressBook
from inputs import parse_input, add_birthday, show_birthday, show_birthdays_per_week
from adding_contact import add_contact, change_contact, show_phone


def main():
    print("Welcome to the assistant bot!")
    book = AddressBook()
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args[0], book))

        elif command == "all":
            print(book)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args[0], book))

        elif command == "birthdays":
            show_birthdays_per_week(book)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
