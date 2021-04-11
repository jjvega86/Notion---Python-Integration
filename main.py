# Main entry point of application
from config import settings

client = settings.client

page = client.get_block("https://www.notion.so/Scratchpad-ed0a396de9ec40d38635f782458736db")
lutetium = client.get_block(
    "https://www.notion.so/Lutetium-1d399afb9aa1406ca97e2e81a822be97")  # By getting an instance of the Lutetium block, I can set the value of a relation property
# to this object
cv = client.get_collection_view(
    "https://www.notion.so/44aa227ba66f4174b06c0f5a1ddbdb5e?v=26ea1860a39f4aaa9d7b35ceee7e0691")

for row in cv.collection.get_rows():
    if row.standup_status != "Not Started":
        row.standup_status = "Not Started"
