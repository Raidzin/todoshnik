from datetime import datetime

import pytz

MOSCOW_TIMEZONE = 'Europe/Moscow'
TIME_FORMAT = '%H:%M'
DATE_FORMAT = '%d.%m.%Y'


def to_timezone(
    date: datetime,
    timezone_name: str = MOSCOW_TIMEZONE,
) -> datetime:
    return date.astimezone(tz=pytz.timezone(timezone_name))


def format_time(date: datetime) -> str:
    return date.strftime(TIME_FORMAT)


def format_date(date: datetime) -> str:
    return date.strftime(DATE_FORMAT)


templates_globals = {
    'hyperscript_version': '0.9.14',
    'htmx_version': '2.0.4',
}

template_filters = {
    'timezone': to_timezone,
    'time': format_time,
    'date': format_date,
}
