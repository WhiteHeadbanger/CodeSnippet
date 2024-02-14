from enum import Enum, auto

class SessionType(Enum):
    USER = auto()
    ANON = auto()

class Session:

    def __init__(self):
        self.session_type: SessionType = SessionType.ANON

    def get_user(self):
        return self.session_type
    
    def set_user(self):
        self.session_type = SessionType.USER