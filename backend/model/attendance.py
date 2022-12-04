
from dataclasses import dataclass

@dataclass
class Attendance():
    name:str
    index:str
    reference:str
    program:str
    date:str
    time_in:str

    