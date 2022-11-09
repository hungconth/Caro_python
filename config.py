# screen config

# from main import *

screen_size = (800, 800)
screen_color = (14,41,60)
n = 4
dosau = 2
# board config
# 0 = ô đang trống, 1 = X, -1 = O

border_thickness = 4
square_size = 40
# tic-tac config

X_color = (192, 250, 255)
O_color = (255,0,0)
tic_tac_thickness = 9
from_border = 12

# analyze points
connect_multiple_four1 = 1e9 + 500
connect_four_has_obstacles1 = 1e9
connect_four1 = 1e9
connect_multiple_three1 =  1e7
connect_three_has_obstacles1 = 1e6
connect_three1 = 1e6
connect_multiple_two1 = 300
connect_two_has_obstacles1 = 50
connect_two1 = 200

connect_multiple_four2 = 1e8
connect_four_has_obstacles2 = 1e9
connect_four2 = 1e9
connect_multiple_three2 = 1e7-1
connect_three_has_obstacles2 = 1e5-1
connect_three2 = 1e6-1
connect_multiple_two2 = 10-1
connect_two_has_obstacles2 = 20-1
connect_two2 = 150
dict = {
    'connect_multiple_four1' : connect_multiple_four1,
    'connect_four_has_obstacles1' : connect_four_has_obstacles1,
    'connect_four1' : connect_four1,
    'connect_multiple_three1' :  connect_multiple_three1,
    'connect_three_has_obstacles1' : connect_three_has_obstacles1,
    'connect_three1' : connect_three1,
    'connect_multiple_two1' : connect_multiple_two1,
    'connect_two_has_obstacles1' : connect_two_has_obstacles1,
    'connect_two1' : connect_two1,

    'connect_multiple_four2' : connect_multiple_four2,
    'connect_four_has_obstacles2' : connect_four_has_obstacles2,
    'connect_four2' : connect_four2,
    'connect_multiple_three2' :  connect_multiple_three2,
    'connect_three_has_obstacles2' : connect_three_has_obstacles2,
    'connect_three2' : connect_three2,
    'connect_multiple_two2' : connect_multiple_two2,
    'connect_two_has_obstacles2' : connect_two_has_obstacles2,
    'connect_two2' : connect_two2
}

# text config
win_text = " win."
lose_text = " lost."
# win_text = "Congratulations! You win."
# lose_text = "You lost. Try Again?"
text_size = 70
text_color = (251, 255, 0)
text_font = 'freesansbold.ttf'