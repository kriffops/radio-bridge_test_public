def on_received_number(receivedNumber):
    radio.write_received_packet_to_serial()
    led.toggle(randint(0, 4), randint(0, 4))
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global group
    group = max(0, group - 1)
    radio.set_group(group)
    led.stop_animation()
    basic.show_number(group)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global group
    group = min(255, group + 1)
    radio.set_group(group)
    led.stop_animation()
    basic.show_number(group)
input.on_button_pressed(Button.B, on_button_pressed_b)

"""

Send all received packets to serial output

"""
"""

Decrement radio group by 1

"""
"""

Increment radio group by 1

"""
"""

Download this code and connect the device to the computer. Press A and B to select the radio group or change it in the code.

"""
group = 0
group = 128
radio.set_group(group)