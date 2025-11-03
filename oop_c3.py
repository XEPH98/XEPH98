from dataclasses import dataclass, field

class MySubClass(object):
    pass

@dataclass
class Contact:
    all_contacts: List["Contact"] = []

    def __init__(self, name:str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
