class car(object):
    def __init__(self, registrations, color):
        self._reg_number = registrations
        self._color = color
        
    @property
    def get_registration_number(self):
        return self._reg_number
    
    @property
    def get_color(self):
        return self._color
    
    
        