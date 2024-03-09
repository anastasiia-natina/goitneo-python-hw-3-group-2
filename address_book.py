from collections import defaultdict
from datetime import datetime


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def find(self, name):
        return self.data.get(name)

    def get_birthdays_per_week(self):
        birthdays = defaultdict(list)
        today = datetime.now().date()

        for record in self.data.values():
            if record.birthday:
                bday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                days_until_bday = (bday_date - today).days
                if 0 <= days_until_bday < 7:
                    weekday = bday_date.strftime("%A")
                    birthdays[weekday].append(record.name.value)

        for weekday, names in birthdays.items():
            print(f"{weekday}: {', '.join(names)}")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
