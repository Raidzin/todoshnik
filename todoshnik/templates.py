from datetime import datetime

import pytz

MOSCOW_TIMEZONE = pytz.timezone('Europe/Moscow')
TIME_FORMAT = '%H:%M'
DATE_FORMAT = '%d.%m.%Y'


def format_time(date: datetime) -> str:
    return date.astimezone(tz=MOSCOW_TIMEZONE).strftime(TIME_FORMAT)


def format_date(date: datetime) -> str:
    return date.astimezone(tz=MOSCOW_TIMEZONE).strftime(DATE_FORMAT)


templates_globals = {
    'hyperscript_version': '0.9.14',
    'htmx_version': '2.0.4',
}

template_filters = {
    'time': format_time,
    'date': format_date,
}
