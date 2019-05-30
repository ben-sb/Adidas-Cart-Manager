# Adidas-Cart-Manager

A Python program for protecting Sole AIO Adidas carts. It adds a claiming system to the carts and stops users seeing each others details. Instructions for use are below.

## Creating Discord Application

First, you need a Discord bot/application.

A tutorial on creating a Discord application, getting the token and adding the bot to your server is here https://github.com/SinisterRectus/Discordia/wiki/Setting-up-a-Discord-application 

You can get the IDs for your Discord channels by following this guide https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-


## Config

The settings for the Cart Manager are found in config.json. Open this up with an editor of your choice and change the following attributes:

* **token** - the token for your Discord bot - get it from the Discord applications page
* **private_channel_id** - ID of the private channel where the carts are sent to by Sole AIO (the channel which you entered the webhook into Sole AIO)
* **public_channel_id** - ID of the public channel where the users can react to claim carts
* **max_num_carts** - the maximum number of carts one user can claim
* **cooldown_time** - how long a user has to wait between claiming carts (in seconds)


## To Run

Download and install Python 3.6 (won't work on 3.7)

Install discordpy:
* py -3 -m pip install -U discord.py

Run cart_manager.py (a server is a good idea)


## Credits

Written by:
* Twitter - https://twitter.com/ciphersuites
* Discord - sd#1000

Edited by:
* Twitter - https://twitter.com/parcels
* Discord - box#9447


*Please note that the concept was not my idea, I wrote this as no publically available cart managers supported Sole AIO at the time*
