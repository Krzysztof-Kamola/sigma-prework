from datetime import datetime


def age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


born = datetime.strptime('04-01-1972', '%d-%m-%Y')
print(age(born))
