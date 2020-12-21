"""
1. Always like and comment on "Lyndall Walker"'s post
2. Like every 2 posts of my follower
3.
"""
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = 'accountforpythonlearning'
insta_password = 'password'
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

# setting
with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=1000000,
                                    min_followers=1,
                                    min_following=1)

    # Interact with specific users
    # set_do_like, set_do_comment, set_do_follow are applicable

    user1Names = ['wmondw']
    user2Names = ['bloodbornegame']
    user1comments = 'Automation is being tested'
    user2comments = 'Awesome picture!'

    def comment(userNames, commentText):
        session.interact_by_users(userNames, amount=3, randomize=True, media='Photo')
        session.set_comments([commentText])
        session.set_do_comment(enabled=True, percentage=100)

    def like(userNames):
        session.interact_by_users(userNames, amount=3, randomize=True, media='Photo')
        session.set_do_like(True, percentage=100)






    comment(user1Names, user1comments)
    comment(user2Names, user2comments)
