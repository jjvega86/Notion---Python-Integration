from config import settings
import pandas

"""
Link to Admissions => Instruction notes
https://devcodecamp-my.sharepoint.com/:x:/p/carrie/EY3vGDJt73FKsqfdc8GIqvgBJtp-DmKJPs2BpbJf2jFbcA?e=lYJA73 
"""


def get_active_students_collection():
    return settings.client.get_collection_view(
        "https://www.notion.so/44aa227ba66f4174b06c0f5a1ddbdb5e?v=26ea1860a39f4aaa9d7b35ceee7e0691")


def get_copy_active_students_collection():
    return settings.client.get_collection_view(
        "https://www.notion.so/05954b4edb354043803b8a49fabfa4f5?v=971140e72618440aa2d578c4e688b838")


def change_standup_status_notstarted():
    cv = get_active_students_collection()

    for row in cv.collection.get_rows():
        if row.standup_status != "Not Started":
            row.standup_status = "Not Started"


def add_new_class_to_activestudents():
    cv = get_copy_active_students_collection()
    students = pandas.read_csv(r'/Users/jjvega/Desktop/Admissions to Instruction - April 26 - FT.csv')
    students_list = students.to_dict(
        'records')  # creates a List of dictionary items containing key-value pairs representing column -> value
    for student in students_list:
        row = cv.collection.add_row()
