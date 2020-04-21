class Date:

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def format_date(self):
         print(self.__day, self.__month, self.__year, sep='/')
        