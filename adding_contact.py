from address_book import AddressBook
from dictionary import Record


def add_contact(args: list[str], address_book: AddressBook) -> str:
    try:
        name, phone = args
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)
        return "Contact added."
    except ValueError as e:
        return str(e)


def change_contact(args: list[str], address_book: AddressBook) -> str:
    try:
        name, new_phone = args
        record = address_book.find(name)
        if record:
            record.edit_phone(record.phones[0].value, new_phone)
            return "Contact updated."
        else:
            return "Contact not found."
    except (ValueError, IndexError) as e:
        return str(e)


def show_phone(name: str, address_book: AddressBook) -> str:
    record = address_book.find(name)
    if record:
        return f"{record.name}'s phone number: {record.phones[0]}."
    else:
        return "Contact not found."
