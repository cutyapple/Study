import requests
import time
import webbrowser
from bs4 import BeautifulSoup
from datetime import datetime

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
month_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name_list = ['공영길', '김대웅', '김도희', '백서영', '서민준', '손완서', '손정우', '안영준', '유시온', '이진혁']

def ddamamin():
    print('-------------------------------')
    now = get_today()
    bs = set_url()
    times = get_github_time(bs, now)

    set_times(now, times)
    print('-------------------------------')


def get_today():
    now = datetime.now()
    return now


def set_url():
    github_url = 'https://github.com/DDamamin/Study'
    res = requests.get(github_url)
    bs = BeautifulSoup(res.text, 'lxml')

    return bs


def get_github_time(bs, now):
    times = bs.find_all('time-ago')
    times.pop(10)
    print(f'Now : {now.year}년 {now.month}월 {now.day}일 {now.hour}시', end='\n\n')

    return times


def set_times(now, times):
    now_year, now_month, now_day, now_hour = now.year, now.month, now.day, now.hour

    i = 0
    for t in times:
        time = t.get('datetime')
        user_check(time, now_year, now_month, now_day, now_hour, i)
        i+=1



def get_time(time):
    user_year, user_month, user_datedata = time.split('-')
    user_day, user_hour = user_datedata.split(':')[0].split('T')
    user_day = int(user_day)
    user_hour = int(user_hour)+9

    return user_year, user_month, user_day, user_hour


def user_check(time, now_year, now_month, now_day, now_hour, i):
    user_year, user_month, user_day, user_hour = get_time(time)
    user_year, user_month, user_day, user_hour = int(user_year), int(user_month), int(user_day), int(user_hour)

    now_list = [now_year, now_month, now_day, now_hour]
    user_list = [user_year, user_month, user_day, user_hour]

    set_date(now_list, user_list, i)


def set_date(now_list, user_list, i):
    years = get_year(now_list[0], user_list[0])
    years, months = get_month(now_list[1], user_list[1], years)
    months, days = get_day(now_list[2], user_list[2], months, now_list[1])
    days, hours = get_hour(now_list[3], user_list[3], days)

    # print(f'{name_list[i]} : {years} {months} {days} {hours}')

    if days > 2:
        late_user(i, years, months, days, hours)


def late_user(i, year, month, day, hour):
    print(f'{name_list[i]} is Late!')
    if year != 0:
        print(f'{year}year', end=' ')
    if month != 0:
        print(f'{month}month', end=' ')
    if day != 0:
        print(f'{day}day', end=' ')
    if hour != 0:
        print(f'{hour}hour', end=' ago\n')

    webbrowser.open('https://github.com/DDamamin/Study')


def get_year(now_year, user_year):
    return now_year - user_year


def get_month(now_month, user_month, years):
    now_month = int(now_month)
    user_month = int(user_month)
    if now_month < user_month and years > 0:
        years -= 1
        now_month -= 12

    return years, now_month - user_month


def get_day(now_day, user_day, months, user_month):
    if now_day < user_day:
        months -= 1
        return months, month_days_list[user_month-1] - user_day + now_day

    return months, int(now_day) - int(user_day)


def get_hour(now_hour, user_hour, user_day):
    i = user_day * 24
    if now_hour < user_hour:
        hour = user_hour - now_hour
        i -= hour
        user_day -= 1
    else:
        hour = now_hour - user_hour
        i += hour

    hours = i % 24

    return user_day, hours


def is_yoon_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        return True
    return False

while(True):
    ddamamin()
    time.sleep(60)

