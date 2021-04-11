from config import settings

lutetium = settings.client.get_block(
    "https://www.notion.so/Lutetium-1d399afb9aa1406ca97e2e81a822be97")  # By getting an instance of the Lutetium block, I can set the value of a relation property to this object
