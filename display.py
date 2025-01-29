"""
Filename: display.py
Purpose: Display functions for the Jumping Ring UI
"""
from consts import *


def display_state(screen, state=MEASURE, language=HEBREW, voltage=MIN_VOLTAGE):
    """
    Display the state screen
    :param screen: the screen to display the state screen on
    :param language: the language to display the state screen in
    :param state: the state to display
    """
    # if state == OPENING:  # no opening screen for this exhibit
    #     display_opening(screen, language=language)

    if state == MEASURE:
        display_measure(screen, language=language, voltage=voltage)

# no opening screen for this exhibit
# def display_opening(screen, language):
#     """
#     Display the opening screen
#     :param screen: the screen to display the opening screen on
#     :param language: the language to display the opening screen in
#     """
#     if language == HEBREW:
#         screen.blit(open_heb, (0,0))

#     elif language == ENGLISH:
#         screen.blit(open_eng, (0,0))

#     elif language == ARABIC:
#         screen.blit(open_arb, (0,0))


def display_measure(screen, language=HEBREW, voltage=MIN_VOLTAGE):
    """
    Display the measurement screen
    :param screen: the screen to display the measurement screen on
    :param language: the language to display the measurement screen in
    """
    if language == HEBREW:
        screen.blit(measure_heb, (0,0))

    elif language == ENGLISH:
        screen.blit(measure_eng, (0,0))

    elif language == ARABIC:
        screen.blit(measure_arb, (0,0))

    # sub function to calculate the current, charge and energy from the voltage and capacitance
    # def calculate_charge_and_energy(voltage):
    #     """
    #     Calculate the charge and energy from the voltage and capacitance
    #     :param voltage: the voltage
    #     :return: the charge and the energy
    #     """
    #     charge = voltage * CAPACITANCE
    #     energy = 0.5 * CAPACITANCE * voltage ** 2
    #     return charge, energy
    # write the same as lambda function
    calculate_charge_and_energy = lambda voltage: (max(min(voltage * CAPACITANCE, MAX_CHARGE), MIN_CHARGE), max(min(0.5 * CAPACITANCE * voltage ** 2, MAX_ENERGY), MIN_ENERGY))

    charge, energy = calculate_charge_and_energy(voltage)
    display_bars(screen, voltage, charge, energy)
    
    # display_current(screen, current)
    # display_charge(screen, charge)


def display_bars(screen, voltage=MIN_VOLTAGE, charge=MIN_CHARGE, energy=MIN_ENERGY):
    """
    Display the bar on the screen according to the values
    :param screen: the screen to display the bar on
    :param voltage: the voltage to display
    :param charge: the charge to display
    :param energy: the energy to display
    """

    # sub function to reduce code duplication
    def display_bar_from_values(screen, value, max, min, bar_image):
        """
        sub function to display the bar on the screen according to the value and the max and min values
        """
        height = int((value - min) / (max - min) * BAR_SIZE[1])
        crop_rect = pygame.Rect(0, BAR_GRAPH_BOTTOM_HEIGHT - height, VIEW_PORT[0], VIEW_PORT[1] - BAR_GRAPH_BOTTOM_HEIGHT + height)
        cropped_bar = bar_image.subsurface(crop_rect).copy()
        screen.blit(cropped_bar, (0, BAR_GRAPH_BOTTOM_HEIGHT - height))


    display_bar_from_values(screen, voltage, MAX_VOLTAGE, MIN_VOLTAGE, bar_full_voltage)
    display_bar_from_values(screen, charge, MAX_CHARGE, MIN_CHARGE, bar_full_charge)
    display_bar_from_values(screen, energy, MAX_ENERGY, MIN_ENERGY, bar_full_energy)


def display_current(screen, current):
    """
    Display the current on the screen
    :param screen: the screen to display the current on
    :param current: the current to display
    """
    font = pygame.font.Font(None, CURRENT_TEXT_SIZE)
    text = font.render(f"{current:.2f}", True, CURRENT_TEXT_COLOR)
    text_rect = text.get_rect(center=CURRENT_TEXT_POS)
    screen.blit(text, text_rect)


def display_charge(screen, charge):
    """
    Display the charge on the screen
    :param screen: the screen to display the charge on
    :param charge: the charge to display
    """
    font = pygame.font.Font(None, CHARGE_TEXT_SIZE)
    text = font.render(f"{charge:.2f}", True, CHARGE_TEXT_COLOR)
    text_rect = text.get_rect(center=CHARGE_TEXT_POS)
    screen.blit(text, text_rect)
