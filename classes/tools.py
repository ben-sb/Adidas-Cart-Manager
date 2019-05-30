import discord


class Cart:
    def __init__(self):
        self.id = -1
        self.region = ""
        self.pid = ""
        self.size = ""
        self.email = ""
        self.password = ""
        self.url = ""
        self.mobile_url = ""
        self.image_url = ""
        self.claimed = False


class CartManager:
    def __init__(self):
        self.carts = []
        self.users = []

    def add_cart(self, cart):
        self.carts.append(cart)

    def get_cart_id(self):
        return len(self.carts) + 1

    def get_cart(self, id):
        for cart in self.carts:
            if cart.id == id and not cart.claimed:
                return cart

        return None

    def get_user(self, user):
        for u in self.users:
            if u['user'] == user:
                return u

        return None

    @staticmethod
    def create_cart(cart_manager, original_embed, id):

        e = discord.Embed(title="Cart #" + str(id), color=0x00ff00)
        e.set_thumbnail(url=original_embed.thumbnail.url)
        e.set_footer(text="Sole AIO Cart Manager", icon_url="https://i.imgur.com/ceVbiGI.png")

        cart = Cart()
        cart.id = id
        cart.url = original_embed.url
        cart.pid = original_embed.title.split(' ')[0]
        cart.image_url = original_embed.thumbnail.url

        cart.region = original_embed.fields[0].value
        e.add_field(name='Region', value=cart.region, inline=True)

        cart.pid = original_embed.title.split(' ')[0]
        e.add_field(name='PID', value=cart.pid, inline=True)

        cart.size = original_embed.fields[1].value
        e.add_field(name='Size', value=cart.size, inline=True)

        # fields we don't want to add to the publicly visible embed
        cart.email = original_embed.fields[2].value
        cart.password = original_embed.fields[3].value
        cart.mobile_url = original_embed.fields[5].value

        cart_manager.add_cart(cart)

        e.add_field(name="To Claim", value="React to this message", inline=False)
        return e

    @staticmethod
    def create_cart_embed(cart):

        e = discord.Embed(title="Click to login", color=0x00ff00)
        e.url = cart.url
        e.set_thumbnail(url=cart.image_url)
        e.set_footer(text="Sole AIO Cart Manager",
                     icon_url="https://i.imgur.com/ceVbiGI.png")

        e.add_field(name='Region', value=cart.region, inline=True)
        e.add_field(name='PID', value=cart.pid, inline=True)
        e.add_field(name='Size', value=cart.size, inline=True)
        e.add_field(name='Email', value=cart.email, inline=False)
        e.add_field(name='Password', value=cart.password, inline=False)
        e.add_field(name='Mobile Link', value=cart.mobile_url, inline=False)

        return e

    @staticmethod
    def modify_embed(embed, user):
        embed.title += " - Claimed by %s" % str(user)
        return embed


class Utils:
    @staticmethod
    def get_channel(server, id):
        for channel in server.channels:
            if channel.id == id:
                return channel
        return 'none'
