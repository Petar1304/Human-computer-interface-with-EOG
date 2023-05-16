import mouse

mouse.get_position()
# mouse.click('left/right/middle')
mouse.is_pressed('left')
mouse.drag(0, 0, 100, 100, absolute=False, duration=0.1)
mouse.move(100, 100, absolute=False, duration=0.2)

