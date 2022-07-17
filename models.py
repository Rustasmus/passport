
from datetime import date


class Passport:
    def __init__(self, name: str, surname: str, passport_id: int, inn: int, date_of_birth: date,
                 start_date: date, end_date: date, place_of_issue, gender: int,  middle_name=None):
        self.__name = name
        self.__surname = surname
        self.__middle_name = middle_name
        self.__passport_id = passport_id
        self.__date_of_birth = date_of_birth
        self.__inn = inn
        self.__start_date = start_date
        self.__end_date = end_date
        self.__place_issue = place_of_issue
        self.__gender = gender

    @property
    def inn(self):
        return self.__inn

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.isalpha():
            self.__name = name.strip().capitalize()
        else:
            print('Incorrect name!')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if surname.isalpha():
            self.__surname = surname.strip().capitalize()
        else:
            print('Incorrect surname!')

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        if middle_name.isalpha():
            self.__middle_name = middle_name.strip().capitalize()
        else:
            print('Incorrect middle name!')

    @property
    def passport_id(self):
        return self.__passport_id

    @passport_id.setter
    def passport_id(self, passport_id):
        try:
            passport_id = int(passport_id)
            self.__passport_id = passport_id
        except TypeError:
            print('Incorrect passport id!')

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        if type(start_date) == date:
            self.__start_date = start_date
        else:
            print('Incorrect start date!')

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):
        if type(end_date) == date:
            self.__end_date = end_date
        else:
            print('Incorrect end date!')

    @property
    def place_of_issue(self):
        return self.__place_issue

    @place_of_issue.setter
    def place_of_issue(self, place_of_issue):
        if len(place_of_issue) == 9 and place_of_issue[:4] == 'MKK-' and place_of_issue[4:].isdigit():
            self.__place_issue = place_of_issue
        else:
            print('Incorrect place of issue! Example : MKK - 11223')

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender in ['1', '2', '0']:
            self.__gender = gender
        else:
            print('Incorrect gender')

    def __str__(self):
        return f""" 
Name: {self.__name}
Surname: {self.__surname}
Middle name: {self.__middle_name}
Date of birth: {self.__date_of_birth}
Gender: {self.__gender}
ID: {self.__passport_id}
INN: {self.__inn}
Start Date: {self.__start_date}
End Date: {self.__end_date}
"""
