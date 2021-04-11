from config import settings
import pandas

"""
Link to Admissions => Instruction notes
https://devcodecamp-my.sharepoint.com/:x:/p/carrie/EY3vGDJt73FKsqfdc8GIqvgBJtp-DmKJPs2BpbJf2jFbcA?e=lYJA73 
"""


def change_standup_status_notstarted():
    cv = settings.client.get_collection_view(
        "https://www.notion.so/44aa227ba66f4174b06c0f5a1ddbdb5e?v=26ea1860a39f4aaa9d7b35ceee7e0691")

    for row in cv.collection.get_rows():
        if row.standup_status != "Not Started":
            row.standup_status = "Not Started"


def add_new_class_to_activestudents():
    df = pandas.read_csv(r'/Users/jjvega/Desktop/Admissions to Instruction - April 26 - FT.csv')
    print(df)
