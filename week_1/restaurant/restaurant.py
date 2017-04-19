FILENAME = 'restaurant_data.txt'

def get_restaurant_data(filename):
    """
    (file) -> (dict, dict, dict)
    Takes a file and returns three dictionaries:
    - name_to_rating: dict of {str: int}
    - price_to_names: dict of {str: list of str}
    - cuisine_to_names: dict of {str: list of str}
    """

    name_to_rating  = {}
    price_to_names = {'$':[], '$$':[], '$$$':[], '$$$$':[]}
    cuisine_to_names = {}

    with open(filename, 'rU') as f:
        temp = f.read().splitlines()
    x = 0
    for y in range((len(temp)//5)+1):
        name = temp[x]
        rating = temp[x+1]
        price = temp[x+2]
        cuisines = (temp[x+3]).split(',')
        name_to_rating[name] = int(rating[:-1])
        price_to_names[price].append(name)
        for cuisine in cuisines:
            if cuisine not in cuisine_to_names.keys():
                cuisine_to_names[cuisine] = [name]
            else:
                cuisine_to_names[cuisine].append(name)
        x += 5
    return name_to_rating, price_to_names, cuisine_to_names



def recommend_restaurant(file, pricerange, cuisines):
    """
    (file, str, list of str) -> list of lists [int, str]
    Takes a file of restaurants opened for reading, a price range
    (one of $, $$, $$$ or $$$$) and a list of cuisines.
    Returns a list of restautants in that pricerange, serving
    at least one of those quisines, sorted by their ratings from highest
    to lowest.
    """
    name_to_rating, price_to_names, cuisine_to_names = get_restaurant_data(file)
    recommendations = []
    matching_restaurants_by_price = price_to_names[pricerange]
    for cuisine in cuisines:
        for restaurant in cuisine_to_names[cuisine]:
            if restaurant in matching_restaurants_by_price:
                recommendations.append([name_to_rating[restaurant], restaurant])
    recommendations.sort()
    return recommendations

# test
print(recommend_restaurant(FILENAME, "$", ['Thai', 'Chinese']))
