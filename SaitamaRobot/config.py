# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("SaitamaRobot".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 3716422  # integer value, dont use ""
    API_HASH = "779c90c42677827af815808dac47244c"
    TOKEN = "5565096928:AAG5ZV21qcBm5BGRDHLIV_9HlEBba71o1Ok"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1208988512  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "@bunny_2021"
    SUPPORT_CHAT = "OnePunchSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001506824512
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001506824512
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
