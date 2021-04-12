from notion.collection import NotionDate
from datetime import datetime, timedelta


def create_date(course_type):
    user_input = input('Enter start date in format: YYYY-MM-DD')
    start = datetime.strptime(user_input, "%Y-%m-%d").date()
    days = None
    if course_type == 'Full Time':
        days = 91
    elif course_type == 'Part Time':
        days = 98
    end = start + timedelta(days=days)
    date = NotionDate(start, end=end)
    return date
