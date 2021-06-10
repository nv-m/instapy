"""
Coded By nv

follow me on instagram : https://www.instagram.com/this_is_nv_/

follow me on github : https://github.com/nv-m

"""
print("Coded By nv","follow me on instagram : https://www.instagram.com/this_is_nv_/","follow me on github : https://github.com/nv-m",sep='\n')

print('this code is meant for linux based systems only')
print('this wont work in windows')
from instapy import InstaPy
from instapy import smart_run

insta_username = input('enter your username : ')
insta_password = input('enter your password : ')


# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=6000,
                                    max_following=3000,
                                    min_followers=30,
                                    min_following=30)
    session.set_user_interact(amount=2, randomize=True, percentage=30,
                              media='Photo')
    session.set_do_like(enabled=True, percentage=97)
    session.set_do_comment(enabled=True, percentage=25)
    session.set_comments(
        ['Nice shot! @{}', 'I love your profile! @{}', '@{} Love it!',
        '@{} :heart::heart:',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
         '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:'],
        media='Photo')



    accs = ['this_is_nv_']
    session.follow_by_list(accs, times=1, sleep_delay=600, interact=False)


    # follow activity
    ammount_number = 500
    fu=input('enter the username of a user to follow their followers:  ')
    session.follow_user_followers([fu],
                                  amount=ammount_number, randomize=False,
                                  interact=True, sleep_delay=30)
        # unfollow activity
    
    session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM",
                           unfollow_after=42 * 60 * 60, sleep_delay=300)
    

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='entertainment', engagement_mode='no_comments')
