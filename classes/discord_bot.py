import traceback
import datetime
from classes.tools import *


class DiscordBot:
    def __init__(self, token, private_channel_id, public_channel_id, max_num_carts, cooldown_time):
        self.token = token
        self.private_channel_id = private_channel_id
        self.public_channel_id = public_channel_id
        self.max_num_carts = max_num_carts
        self.cooldown_time = cooldown_time

        self.cart_manager = CartManager()
        self.utils = Utils()
        self.client = discord.Client()

    # method try to send plain text message to a user
    # and return a bool whether it was successful
    async def try_send_message(self, user, msg):
        try:
            await self.client.send_message(user, msg)
            return True
        except:
            return False

    # method try to send an embed to a user
    # return a bool whether it was successful
    async def try_send_embed(self, user, embed):
        try:
            await self.client.send_message(user, embed=embed)
            return True
        except:
            return False

    def run(self):
        @self.client.event
        async def on_ready():
            print("Sole AIO Cart Manager")
            print('Logged in as %s' %self.client.user.name)
            print("Client User ID: %s" %self.client.user.name)
            print('------')


        @self.client.event
        async def on_message(message):
            try:

                if message.channel.id == self.private_channel_id:
                    for embed in message.embeds:

                        if embed['footer'] and embed['footer']['text'] == "Sole AIO Adidas Mode": # detect the cart
                            id = self.cart_manager.get_cart_id()  # get the corresponding cart id

                            # create and send the cart embed to the public
                            # channel and add the reaction
                            e = self.cart_manager.create_cart(self.cart_manager, embed, id)
                            cart_msg = await self.client.send_message(self.utils.get_channel(message.channel.server, self.public_channel_id), embed=e)
                            await self.client.add_reaction(cart_msg, '\N{THUMBS UP SIGN}')

                            cart = self.cart_manager.get_cart(id)  # get correct cart using id

                            # while loop to keep checking for new reactions until the cart is claimed by a suitable user
                            while not cart.claimed:
                                res = await self.client.wait_for_reaction(message=cart_msg, check=self.utils.check_reaction)

                                # get the corresponding user dict and create it
                                # if it does not already exist
                                u = self.cart_manager.get_user(res.user)
                                if u is None:
                                    u = {'user':res.user,
                                         'num':0,
                                         'timestamp':datetime.datetime.now() - datetime.timedelta(seconds=self.cooldown_time + 1)
                                         }
                                    self.cart_manager.users.append(u)


                                if u['num'] >= self.max_num_carts:  # check the user hasn't reached cart limit
                                    await self.try_send_message(res.user, "You have reached the maximum number of carts")

                                # ensure the user isn't spamming carts
                                elif (datetime.datetime.now() - u['timestamp']).total_seconds() < self.cooldown_time:
                                    await self.try_send_message(res.user, "Please wait for the cooldown of %s"
                                                                     " seconds before claiming another cart"%str(self.cooldown_time))


                                elif cart is not None:

                                    # create the cart embed to private message to the user
                                    cart_embed = self.cart_manager.create_cart_embed(cart)

                                    # don't set cart to claimed unless we can successfully message the user
                                    if await self.try_send_embed(res.user, cart_embed):

                                        # edit the public embed to say 'claimed by user'
                                        await self.client.edit_message(cart_msg, embed=self.cart_manager.modify_embed(e, res.user))

                                        # increment user's number of carts and update timestamp
                                        u['num'] += 1
                                        u['timestamp'] = datetime.datetime.now()
                                        self.cart_manager.users[self.cart_manager.users.index(u)] = u

                                        cart.claimed = True  # this breaks out of while loop



            except:
                traceback.print_exc()  # print the traceback for exceptions to terminal


        self.client.run(self.token)  # run the Discord application

