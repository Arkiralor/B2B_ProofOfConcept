class CalendarMapping:
    day = {
        0: "Invalid Key",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"        
    }

    month = {
        0: "Invalid Key",
        1: "January",
        2: "Febraury",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    @classmethod
    def resolve_day(cls, id:int)->str:
        return cls.day.get(id, cls.day.get(0))

    @classmethod
    def resolve_month(cls, id:int)->str:
        return cls.month.get(id, cls.month.get(0))