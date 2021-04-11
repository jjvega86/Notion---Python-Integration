# Main entry point of application
from notion.client import NotionClient

client = NotionClient(token_v2="281480126b050e8dbd5ba5e81bae40e6179e43e7cac0d2c40f65c18fe0c38580f44eaa7333ed9dcdfb7cbe0896b8943bcfe9ca6fe771276591162790eaf5cbb3662cde822d94c2982eaf9c57ec98")

page = client.get_block("https://www.notion.so/Scratchpad-ed0a396de9ec40d38635f782458736db")

print("The old title is:", page.title)

page.title = "JJ's Scratchpad"

print("The new page title is", page.title)