import random

def fakeUserAgent():
    # list of browser names
    browsers = ['Mozilla', 'AppleWebKit', 'Chrome', 'Safari', 'Firefox']

    # list of operating system names
    platforms = ['Windows NT', 'Macintosh', 'X11', 'Linux']

    # list of fake user agent string elements
    elements = ['Version', 'Build', 'x86_64', 'rv', 'like Gecko']

    # create a fake user agent string by randomly selecting elements from the lists
    random_user_agent = ' '.join(random.choice(browsers) + '/' + random.choice(elements) for _ in range(5))

    # append a random platform to the fake user agent string
    random_user_agent += ' (' + random.choice(platforms) + '; rv:' + str(random.randint(1, 99)) + '.' + str(random.randint(1, 99)) + ')'

    return random_user_agent
