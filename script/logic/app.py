from interface.ui import UI 

class App():
    def __init__(self):
        self.ui = UI(self)
        self.identity = None
    
    def present_identity(self, identity):
        self.identity = identity
        self.ui.add_info("Name", self.identity.first_name)
        self.ui.add_info("Surname", self.identity.last_name)
        self.ui.add_info("Date of Birth", self.identity.date_of_birth)
        self.ui.add_info("Place of Birth", self.identity.place_of_birth)
