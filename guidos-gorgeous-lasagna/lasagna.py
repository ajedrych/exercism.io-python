EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    s
   :param elapsed_bake_time: int baking time already elapsed
   :return: int remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'
 
   Function that takes the actual minutes the lasagna has been in the oven as
   an argument and returns how many minutes the lasagna still needs to bake
   based on the `EXPECTED_BAKE_TIME`.
   """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int number of layers
    :return: int preparing time in minutes derived from 'PREPARATION_TIME'

    Function that takes the number of layers of lasagne as an argument and
    returns how many minutes is necessary to prepare the lasagne.
    """
    return number_of_layers*PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param number_of_layers: int number of layers
    :param elapsed_bake_time: int bake time already elapsed
    :return: int elapsed time in minutes
    
    Function that takes the number of layers of lasagne as a first argument and baking time already elapsed as a second argument
    and return how many minutes elapsed from the start of baking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time