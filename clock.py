class Clock:
   
    def __init__(self, hour, minute):
        div, self.minutes = divmod(minute, 60)
        self.hours = (hour + div) % 24
    def __repr__(self):
        return f"Clock({self.hours}, {self.minutes})"
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"
    def __eq__(self, other):
        return self.minutes == other.minutes and self.hours == other.hours
    def __add__(self, minutes):
        return Clock(self.hours, self.minutes + minutes)
    def __sub__(self, minutes):
        return Clock(self.hours, self.minutes - minutes)