class Date:

    def __init__(self):
        from datetime import date
        self.__day = date.today().day
        self.__month = date.today().month
        self.__year = date.today().year

    def format_date(self):
         print(self.__day, self.__month, self.__year, sep='/')