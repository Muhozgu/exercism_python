print("Lasagna Module Loaded")

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(actual_time):
    return EXPECTED_BAKE_TIME - actual_time

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

print(elapsed_time_in_minutes(3, 20))

#---------------------------------------------------------------------------------- FINAL -----------------------------------------------------------------------------------
