from services import create_passport, search_password, change_name_or_surname, passport_restoration
from database import region, district, passports
from random import randint, choice
from datetime import datetime, timedelta


def main():
    while True:
        action = input("""
        Enter 1 to get passport
        Enter 2 to change the name or surname
        Enter 3 if you loss passport
        Enter 4 to search passport
        Enter 5 to quit
        """).strip()
        if action == '1':
            name = input('Enter your name: ').strip().capitalize()
            surname = input('Enter your surname: ').strip().capitalize()
            middle_name = input('Enter your middle name: ').strip().capitalize()
            date_of_birth = input('Enter your date_of_birth example (22.02.2022): ').strip().capitalize()
            gender = input("""
            Enter 1 if you female
            Enter 2 if you male
            """).strip()
            passport_id = randint(1_000_000, 10_000_000)
            if gender in ['1', '2']:
                inn = int(gender + date_of_birth.replace('.', '') + str(randint(10000, 100000)))
            else:
                break
            start_date = datetime.now()
            end_date = start_date + timedelta(days=3650)
            place_of_issue = 'MKK'+str(choice(region))+str(choice(district))+str(randint(100, 1000))
            if gender == '1':
                gender = 'Female'
            else:
                gender = 'Male'
            create_passport(
                name=name,
                surname=surname,
                middle_name=middle_name,
                date_of_birth=date_of_birth,
                gender=gender,
                passport_id=passport_id,
                inn=inn,
                start_date=start_date,
                end_date=end_date,
                place_of_issue=place_of_issue
            )
        elif action == '2':
            name = input('Enter your name: ').strip().capitalize()
            surname = input('Enter your surname: ').strip().capitalize()
            date_of_birth = input('Enter your date of birth example (22.02.2022): ')
            take_passport = search_password(name=name, surname=surname, date_of_birth=date_of_birth)
            if take_passport[0] is True:
                print('Passport found')
                new_name = input('Enter your new name: ').strip().capitalize()
                new_surname = input('Enter your new surname: ').strip().capitalize()
                change_name_or_surname(
                    take_passport=take_passport,
                    new_name=new_name,
                    new_surname=new_surname)
            else:
                print('Passport not found.')

        elif action == '3':
            name = input('Enter your name: ').strip().capitalize()
            surname = input('Enter your surname: ').strip().capitalize()
            date_of_birth = input('Enter your date of birth example (22.02.2022): ')
            passport_restoration(
                name=name,
                surname=surname,
                date_of_birth=date_of_birth,
                )
        elif action == '4':
            name = input('Enter your name: ').strip().capitalize()
            surname = input('Enter your surname: ').strip().capitalize()
            date_of_birth = input('Enter your date of birth example (22.02.2022): ')
            take_passport = search_password(name=name, surname=surname, date_of_birth=date_of_birth)
            if take_passport[0] is True:
                passport = take_passport[1]
                passports.append(passport)
                print(passport)
            else:
                print('Passport not found')

        elif action == '5':
            break

        else:
            print('Incorrect command!')


if __name__ == '__main__':
    main()
