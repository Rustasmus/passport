from models import Passport
from database import passports
from datetime import datetime, timedelta
from random import randint, choice
from database import region, district


def create_passport(name, surname, passport_id,
                    inn, date_of_birth, start_date,
                    end_date, place_of_issue, gender, middle_name=None):
    passport = Passport(
        name=name,
        surname=surname,
        middle_name=middle_name,
        passport_id=passport_id,
        inn=inn,
        date_of_birth=date_of_birth,
        start_date=start_date,
        end_date=end_date,
        place_of_issue=place_of_issue,
        gender=gender
    )
    passports.append(passport)
    print(passport)
    print('Passport create success!')


def search_password(name, surname, date_of_birth):
    for i in passports:
        if name == getattr(i, f'name') and surname == getattr(i, f'surname') \
                and date_of_birth == getattr(i, f'date_of_birth'):
            ind = passports.index(i)
            passport = passports.pop(ind)
            return True, passport
    return False, 0


def change_name_or_surname(take_passport, new_name, new_surname):
    new_passport = take_passport[1]
    new_passport.name, new_passport.surname = new_name, new_surname
    passports.append(new_passport)
    print(new_passport.__str__())
    print('The name and/or surname changes in your passport were successful')


def passport_restoration(name, surname, date_of_birth):
    take_passport = search_password(name=name, surname=surname, date_of_birth=date_of_birth)
    if take_passport[0] is True:
        print('Passport found')
        passport_id = randint(1_000_000, 10_000_000)
        start_date = datetime.now()
        end_date = start_date + timedelta(days=3650)
        place_of_issue = 'MKK' + str(choice(region)) + str(choice(district)) + str(randint(100, 1000))
        new_passport = take_passport[1]
        new_passport.passport_id, new_passport.start_date, new_passport.end_date, new_passport.place_of_issue = \
            passport_id, start_date, end_date, place_of_issue
        passports.append(new_passport)
        print(new_passport)
        print("Your Passport is restoration! Take it. ")
    else:
        print('Passport not found!')
