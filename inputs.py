from address_book import AddressBook


def parse_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_birthday(args: list[str], address_book: AddressBook) -> str:
    name, birthday = args
    record = address_book.find(name)
    if record:
        try:
            record.add_birthday(birthday)
            return "Birthday added."
        except ValueError as e:
            return str(e)
    else:
        return "Contact not found."


def show_birthday(name: str, address_book: AddressBook) -> str:
    record = address_book.find(name)
    if record and record.birthday:
        return f"{record.name}'s birthday is on {record.birthday}."
    elif record and not record.birthday:
        return "No birthday set for this contact."
    else:
        return "Contact not found."


def show_birthdays_per_week(address_book: AddressBook) -> None:
    address_book.get_birthdays_per_week()
