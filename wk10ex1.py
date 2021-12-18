#
# wk10ex1.py
#
# naam:
#

# Eerst de klassedefinitie
# Hieronder definiëren we een aantal handige objecten van het type Date
#  +++ bewaar die en/of voeg je eigen toe! +++


class Date:
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # de constructor heet altijd __init__ !
    def __init__(self, day, month, year):
        """Construct a Date with the given day, month, and year."""
        self.day = day
        self.month = month
        self.year = year

    # de "afdruk"-functie heet altijd __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}-{:02d}-{:04d}".format(self.day, self.month, self.year)
        return s

    # Hier is een voorbeeld van een "methode" van de klasse Date:
    def is_leap_year(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same day, month, year
            as the calling object (self).
        """
        dnew = Date(self.day, self.month, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def __eq__(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        return self.equals(d2)

    def is_before(self, d2):
        """ Check if self is before d2
        """
        if self.year != d2.year:
            return self.year < d2.year

        if self.month != d2.month:
            return self.month < d2.month

        return self.day < d2.day

    def __lt__(self, d2):
        """ checks if self is smaller than d2 
        """
        return self.is_before(d2)

    def is_after(self, d2):
        """ Checks if self is greater than d2
        """
        if self.year != d2.year:
            return self.year > d2.year

        if self.month != d2.month:
            return self.month > d2.month

        return self.day > d2.day

    def __gt__(self, d2):
        """ checks if self is greater than d2
        """
        return self.is_after(d2)

    def tomorrow(self):
        """ Adds one day 
        """
        fdays = 28 + self.is_leap_year()
        dim = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day += 1
        if self.day > dim[self.month]:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

    def yesterday(self):
        """ Removes one day
        """
        fdays = 28 + self.is_leap_year()
        dim = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day -= 1
        if self.day <= 0:
            self.month -= 1
            if self.month <= 0:
                self.year -= 1
                self.month = 12
            self.day = dim[self.month]

    def add_n_days(self, amount):
        """ Add n days to the date
        """
        for _ in range(amount):
            self.tomorrow()
            print(self)

    def sub_n_days(self, amount):
        """ Subtracks n days from the date
        """
        for _ in range(amount):
            self.tomorrow()
            print(self)

    def __iadd__(self, n):
        """ Add n days to the date
        """
        self.add_n_days(n)

    def __isub__(self, n):
        """ Subtracks n days form the date
        """
        self.sub_n_days(n)

    def diff(self, d2):
        """ Calculates the difference between self and d2
        """
        curr = self.copy()
        after = self.is_after(d2)
        counter = 0
        while not curr.equals(d2):
            if after:
                counter += 1
                curr.yesterday()
            else:
                counter -= 1
                curr.tomorrow()
        return counter

    def __sub__(self, d2):
        """ Calculates the difference between self and d2
        """
        return self.diff(d2)

    def dow(self):
        """ returns the day of the week
        """
        sunday = Date(10, 10, 2010)
        diff = self.diff(sunday)
        day = diff % 7 - 1
        if abs(diff) != diff:
            day = 6 - abs(diff) % 7
        week = ['Monday', 'Tuesday', 'Wednessday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
        return week[day]

#
# vergeet niet je code voor de klasse Date HIERBOVEN toe te voegen; in de klassedefinitie
#

#
# een aantal datums om mee te werken...
#
# Het handige van ze hier plaatsen is dat ze elke keer dat de software uitgevoerd
#   wordt ze opnieuw gedefinieerd worden (en dat is nodig om te testen!)
#


d = Date(2, 12, 2020)    # Vandaag?
d2 = Date(21, 12, 2020)   # Kerstvakantie
ny = Date(1, 1, 2021)   # Nieuwjaar
nd = Date(1, 1, 2030)   # Nieuw decennium
nc = Date(1, 1, 2100)   # Nieuwe eeuw
graduation = Date(12, 7, 2024)   # Pas dit zelf aan!
vacation = Date(19, 7, 2021)     # Dit ook ~ zomervakantie!
sm1 = Date(28, 10, 1929)    # Krach aandelenbeurs
# Nog een beurskrach: Maandagen in okt. zijn gevaarlijk...
sm2 = Date(19, 10, 1987)
