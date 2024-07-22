# Unit Converter
# Build a unit converter that can convert between different units of measurement
# (e.g., kilometers to miles, Celsius to Fahrenheit). This project will strengthen your
# understanding of functions and user input.

def clear_screen():
    print('\n'*100) # print 100 empty lines to clear screen
def start_program():
    global selected_category
    selected_category = input('''
Select a category to perform conversion:
a. Distance
b. Weight
c. Temperature

Enter choice: ''')
    select_category()

def select_category():
    clear_screen()
    if selected_category == 'a':
        distance_category()
    elif selected_category == 'b':
        weight_category()
    elif selected_category == 'c':
        temperature_category()


def distance_category():
    clear_screen()
    global selected_distance_conversion
    selected_distance_conversion = input('''
Select the unit conversion for distance:
a. kilometer to mile
b. Mile to kilometer

Enter choice: ''')
    select_distance_conversion()

def select_distance_conversion():
    clear_screen()
    if selected_distance_conversion == 'a':
        km_mile_conversion()
    elif selected_distance_conversion == 'b':
        mile_km_conversion()

def km_mile_conversion():
    clear_screen()
    distance_km = float(input('''
Enter distance in km: '''))
    distance_mile = distance_km * 0.621371
    print(f'{distance_km} km = {distance_mile} mile')


def mile_km_conversion():
    clear_screen()
    distance_mile = float(input('''
Enter distance in mile: '''))
    distance_km = distance_mile / 0.621371
    print(f'{distance_mile} mile = {distance_km} km')

""""""""""""""""""""""""""""""""""""""""""
def weight_category():
    clear_screen()
    global selected_weight_conversion
    selected_weight_conversion = input('''
Select the unit conversion for weight:
a. Kilogram to pound
b. Pound to kilogram

Enter choice: ''')
    select_weight_conversion()

def select_weight_conversion():
    clear_screen()
    if selected_weight_conversion == 'a':
        kg_lb_conversion()
    elif selected_weight_conversion == 'b':
        lb_kg_conversion()

def kg_lb_conversion():
    clear_screen()
    weight_kg = float(input('''
Enter weight in kg: '''))
    weight_lb = weight_kg * 2.2046
    print(f'{weight_kg} kg = {weight_lb} lb')


def lb_kg_conversion():
    clear_screen()
    weight_lb = float(input('''
Enter weight in lb: '''))
    weight_kg = weight_lb / 2.2046
    print(f'{weight_lb} lb = {weight_kg} kg')

""""""""""""""""""""""""""""""""""""""""""
def temperature_category():
    clear_screen()
    global selected_temperature_conversion
    selected_temperature_conversion = input('''
Select the unit conversion for temperature:
a. Celsius to Fahrenheit
b. Fahrenheit to Celsius

Enter choice: ''')
    select_temperature_conversion()

def select_temperature_conversion():
    clear_screen()
    if selected_temperature_conversion == 'a':
        C_F_conversion()
    elif selected_temperature_conversion == 'b':
        F_C_conversion()

def C_F_conversion():
    clear_screen()
    temperature_C = float(input('''
Enter temperature in C: '''))
    temperature_F = temperature_C * 9/5 + 32
    print(f'{temperature_C} C = {temperature_F} F')


def F_C_conversion():
    clear_screen()
    temperature_F = float(input('''
Enter temperature in F: '''))
    temperature_C = (temperature_F - 32) * 5/9
    print(f'{temperature_F} F = {temperature_C} C')


start_program()

