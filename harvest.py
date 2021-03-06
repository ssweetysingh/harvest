############
# Part 1   #
############
import sys

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_havest = code
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', '1998', 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', '2003', 'orange', True, False, 'Casaba')
    casaba.add_pairing('mint')
    casaba.add_pairing('strawberry')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', '1996', 'green', False, False, 'crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', '2013', 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)






    # debug print
    print(all_melon_types)
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        pairings = melon.pairings
        print(f'{melon.name} pairs with')
        for i in range(len(pairings)):
            print(f'- {pairings[i]}')
    return None
    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}
    # Fill in the rest
    for melon in melon_types:
        melon_dict[melon.code] = melon
    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvest_location, harvested_by):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_location = harvest_location
        self.harvested_by = harvested_by

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons = []
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id["yw"], "8", "7", "2", "Sheila")
    melons.append(melon_1)

    melon_2 = Melon(melons_by_id["yw"], "3", "4", "2", "Sheila")
    melons.append(melon_2)

    melon_3 = Melon(melons_by_id["yw"], "9", "8", "3", "Sheila")
    melons.append(melon_3)

    melon_4 = Melon(melons_by_id["cas"], "10", "6", "35", "Sheila")
    melons.append(melon_4)

    melon_5 = Melon(melons_by_id["cren"], "8", "9", "35", "Michael")
    melons.append(melon_5)

    melon_6 = Melon(melons_by_id["cren"], "8", "2", "35", "Michael")
    melons.append(melon_6)

    melon_7 = Melon(melons_by_id["cren"], "2", "3", "4", "Michael")
    melons.append(melon_7)

    melon_8 = Melon(melons_by_id["musk"], "6", "7", "4", "Michael")
    melons.append(melon_8)

    melon_9 = Melon(melons_by_id["yw"], "7", "10", "3", "Sheila")
    melons.append(melon_9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if is_sellable(melon):
            print(f"Havested by {melon.harvested_by} from {melon.harvest_location} (CAN BE SOLD)")
        else:
            print(f"Havested by {melon.harvested_by} from {melon.harvest_location} (NOT SELLABLE)")


def is_sellable(melon):
    sellable = False
    rating = int(melon.shape_rating)
    color = int(melon.color_rating)
    loc = int(melon.harvest_location)
    if rating > 5 and color > 5 and loc != 3:
        sellable = True


def open_harvest_log(log_file):
    with open(log_file) as f:
        for line in f:
            line = line.rstrip()


open_harvest_log('harvest_log.txt')

