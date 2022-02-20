import requests
import time
import datetime


def get_questions_python(_url):
    current_date = datetime.datetime.now()
    date_from = current_date.replace(hour=00, minute=00, second=00, microsecond=0) - datetime.timedelta(days=2)
    timestamp_from = int(time.mktime(date_from.timetuple()))
    timestamp_to = int(time.mktime(current_date.timetuple()))

    params = {'fromdate': timestamp_from, 'todate': timestamp_to, 'tagged': 'Python', 'order': 'desc',
              'site': 'stackoverflow', 'sort': 'creation'}
    resp = requests.get(url=_url, params=params, timeout=20)
    return resp['items']


if __name__ == '__main__':
    url = 'https://api.stackexchange.com/2.3/questions'
    posts = get_questions_python(url)

    for post in posts:
        print(f'Дата создания: {datetime.datetime.fromtimestamp(post["creation_date"])}   Заголовок : {post["title"]}')
