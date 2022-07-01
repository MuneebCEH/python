from instabot import Bot
bot=Bot()
bot.login(username="userdemo", password="demo")
#bot.follow('muneeb_ceh')
#bot.upload_photo("C:/user/demo")
#bot.unfollow("muneeb_ceh")
#bot.send_message("i love python",["muneeb_ceh","muneeb_ceh2"])
# followers=bot.get_user_followers("userdemo")
# for follower in followers:
#     print(bot.get_user_info(follower))
following=bot.get_user_following("userdemo")
for Following in following:
    print(bot.get_user_info(Following))