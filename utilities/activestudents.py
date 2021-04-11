from config import settings


def change_standup_status():
    cv = settings.client.get_collection_view(
        "https://www.notion.so/44aa227ba66f4174b06c0f5a1ddbdb5e?v=26ea1860a39f4aaa9d7b35ceee7e0691")

    for row in cv.collection.get_rows():
        if row.standup_status != "Not Started":
            row.standup_status = "Not Started"
