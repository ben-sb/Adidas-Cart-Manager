# Cart Manager for Sole AIO Adidas carts
# Written by SD
# twitter.com/ciphersuites
# Edited by box
# twitter.com/parcels

from classes.discord_bot import DiscordBot
import discord
import json


try:
    # load the config file
    config = json.loads(open('config.json').read())

    # get specified settings from config
    token = config['token']
    private_channel_id = config['private_channel_id']
    public_channel_id = config['public_channel_id']
    max_num_carts = config['max_num_carts']
    cooldown_time = config['cooldown_time']

    # create instance of DiscordBot and run
    bot = DiscordBot(token, private_channel_id, public_channel_id, max_num_carts, cooldown_time)
    bot.run()


# case where config file is missing
except FileNotFoundError:
    print("FATAL ERROR: Could not find config file")

# case where config file is not valid json
except json.decoder.JSONDecodeError:
    print("FATAL ERROR: Could not read config file, invalid JSON")

# case where we could not login to the Discord application
except discord.errors.LoginFailure:
    print("FATAL ERROR: Failed to connect to Discord application.")

except Exception as e:
    print("Unknown error: " + str(e))
