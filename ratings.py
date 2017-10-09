def get_restaurant_ratings(file_name):
    """Get restaurant ratings from file
    """
    open_file = open(file_name)
    restaurants = {}
    for line in open_file:
        line = line.rstrip()
        name, rating = line.split(':')

        restaurants[name] = int(rating)
    # print restaurants
    return restaurants


def get_user_rating(input_dict):
    """Get user input of restaurant and rating
    If restaurant is in dictionary, assign user rating
    Otherwise, add restaurant with user rating
    """
    user_restaurant = raw_input("Restaurant Name?: ")
    user_rating = ""
    while True:
        user_rating = raw_input("Restaurant Rating?: ")
        try:
            user_rating = int(user_rating)
        except:
            print "Please enter a number"
            continue
        if not (0 < user_rating < 6):
            print "Please enter a number between 1 and 5"
            continue
        else:
            break
    input_dict[user_restaurant] = user_rating


def print_dict_alphabetical(input_dict):
    """Sort restaurants alphabetically by name and print with rating
    """
    alpha_restaurants = sorted(input_dict.items())
    for name, rating in alpha_restaurants:
            print '%s: %d' % (name, rating)

    # print alpha_restaurants


def get_user_choice():
    while True:
        user_input = raw_input("Enter 'rating', 'print, or 'quit': ")
        if user_input == 'rating':
            get_user_rating(ratings)
        elif user_input == 'print':
            print_dict_alphabetical(ratings)
        elif user_input == 'quit':
            break


ratings = get_restaurant_ratings('scores.txt')
get_user_choice()
