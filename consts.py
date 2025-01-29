"""
Filename: consts.py
Purpose: Constants for the Hydrogen Rocket UI
"""
import os
import pygame

FPS = 100

# arduino
BAUDRATE = 115200
SERIAL_ERROR = -1
RECONNECT_INTERVAL = 1  # seconds

# voltage, charge, and capacitor values
MIN_VOLTAGE = 0.0  # in volts
MAX_VOLTAGE = 350.0  # in volts
MIN_CHARGE = 0.0  # in coulombs
MAX_CHARGE = 1.6  # in coulombs
MIN_ENERGY = 0.0  # in joules
MAX_ENERGY = 250.0  # in joules
CAPACITANCE = 0.00457  # in farads

# languages
HEBREW = 0
ENGLISH = 1
ARABIC = 2
LANGUAGES = [HEBREW, ENGLISH, ARABIC]

#states (only one state for this project)
# OPENING = 0
MEASURE = 1
STATES = [MEASURE]

# logging values
LOG_FOLDER = os.path.join(os.path.dirname(__file__), "logs")  # get the path of the logs folder
MAX_SIZE_PER_LOG_FILE = 1 * 1024 * 1024  # 1MB
BACKUP_COUNT = 10  # max number of log files, if all 10 are full, the first one will be deleted, rotating the rest 

# pictures
pygame.init()
VIEW_PORT = pygame.display.Info().current_w, pygame.display.Info().current_h  # get the screen resolution
VIEW_PORT = (607.5, 1080)  # for testing
# VIEW_PORT = (1080, 1920)  # for testing

PICTURES = os.path.join(os.path.dirname(__file__), "pictures")  # get the path of the pictures folder
# OPEN_HEB = os.path.join(PICTURES, "0_heb.png")  # no opening screen
# OPEN_ENG = os.path.join(PICTURES, "0_eng.png")  # no opening screen
# OPEN_ARB = os.path.join(PICTURES, "0_arb.png")  # no opening screen
MEASURE_HEB = os.path.join(PICTURES, "1_heb.png")
MEASURE_ENG = os.path.join(PICTURES, "1_eng.png")
MEASURE_ARB = os.path.join(PICTURES, "1_arb.png")
# BAR_EMPTY_ENERGY = os.path.join(PICTURES, "bar_empty_left.png")
BAR_FULL_ENERGY = os.path.join(PICTURES, "bar_full_left.png")
# BAR_EMPTY_CHARGE = os.path.join(PICTURES, "bar_empty_middle.png")
BAR_FULL_CHARGE = os.path.join(PICTURES, "bar_full_middle.png")
# BAR_EMPTY_VOLTAGE = os.path.join(PICTURES, "bar_empty_right.png")
BAR_FULL_VOLTAGE = os.path.join(PICTURES, "bar_full_right.png")


# load the pictures
# open_heb = pygame.image.load(OPEN_HEB)  # no opening screen
# open_eng = pygame.image.load(OPEN_ENG)  # no opening screen
# open_arb = pygame.image.load(OPEN_ARB)  # no opening screen
measure_heb = pygame.image.load(MEASURE_HEB)
measure_eng = pygame.image.load(MEASURE_ENG)
measure_arb = pygame.image.load(MEASURE_ARB)
# bar_empty_energy = pygame.image.load(BAR_EMPTY_ENERGY)
bar_full_energy = pygame.image.load(BAR_FULL_ENERGY)
# bar_empty_charge = pygame.image.load(BAR_EMPTY_CHARGE)
bar_full_charge = pygame.image.load(BAR_FULL_CHARGE)
# bar_empty_voltage = pygame.image.load(BAR_EMPTY_VOLTAGE)
bar_full_voltage = pygame.image.load(BAR_FULL_VOLTAGE)


# transform the pictures to the screen resolution
# open_heb = pygame.transform.scale(open_heb, VIEW_PORT)  # no opening screen
# open_eng = pygame.transform.scale(open_eng, VIEW_PORT)  # no opening screen
# open_arb = pygame.transform.scale(open_arb, VIEW_PORT)  # no opening screen
measure_heb = pygame.transform.scale(measure_heb, VIEW_PORT)
measure_eng = pygame.transform.scale(measure_eng, VIEW_PORT)
measure_arb = pygame.transform.scale(measure_arb, VIEW_PORT)
# bar_empty_energy = pygame.transform.scale(bar_empty_energy, VIEW_PORT)
bar_full_energy = pygame.transform.scale(bar_full_energy, VIEW_PORT)
# bar_empty_charge = pygame.transform.scale(bar_empty_charge, VIEW_PORT)
bar_full_charge = pygame.transform.scale(bar_full_charge, VIEW_PORT)
# bar_empty_voltage = pygame.transform.scale(bar_empty_voltage, VIEW_PORT)
bar_full_voltage = pygame.transform.scale(bar_full_voltage, VIEW_PORT)


# positions
CURRENT_TEXT_POS = (int(0.5 * VIEW_PORT[0]), int(0.487 * VIEW_PORT[1]))  # the position of the current text on the screen
CHARGE_TEXT_POS = (int(0.51 * VIEW_PORT[0]), int(0.92 * VIEW_PORT[1]))  # the position of the charge text on the screen
BAR_GRAPH_BOTTOM_HEIGHT = int(0.71 * VIEW_PORT[1])  # the bottom of the bar graphs (same for all 3)

# colors
BLACK = (0, 0, 0)
CURRENT_TEXT_COLOR = BLACK
CHARGE_TEXT_COLOR = BLACK

# sizes
CURRENT_TEXT_SIZE = int(50 * VIEW_PORT[0] / 1080)
CHARGE_TEXT_SIZE = int(80 * VIEW_PORT[0] / 1080)
BAR_SIZE = (int(781 * VIEW_PORT[0] / 4500), int(2238 * VIEW_PORT[1] / 8000))