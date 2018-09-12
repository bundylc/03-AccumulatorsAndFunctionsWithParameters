"""
This module demonstrates simple LOOPS of the form:
   for k in range(blah):
      ... k ...

and also USING OBJECTS.

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Landon Bundy.
"""  # TODOne: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    #test_print_sequence1()
    #draw_circles1()
    #draw_circles2()
    #draw_circles3()
    #print_cosines()
    draw_cosines_and_sines()

    """
    Prints:
       0
       10
       20
       30
       40
       ...
       200
    """


def test_print_sequence1():
    # ------------------------------------------------------------------
    # TODOne: 2. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------

    print()
    print('--------------------------------------------------')
    print('Running print_sequence1:')
    print('--------------------------------------------------')

    expected = 10
    answer = print_sequence1(2)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 20
    answer = print_sequence1(3)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 30
    answer = print_sequence1(4)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)


def print_sequence1(n):
    for k in range(n):
        total = 10 * k

    return total


def draw_circles1():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws 21 rg.Circle objects such that:
         -- Each is centered at (200, 200)
         --j They have radii:  0  10  20  30  40 ... 200, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODOne: 3. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # HINT: You might find a prior module useful when 'writing' this code.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles1:  See graphics window')
    print('--------------------------------------------------')

    window = rg.RoseWindow(400, 400)

    for k in range(21):
        center_point = rg.Point(200, 200)
        radius = k * 10
        circle1 = rg.Circle(center_point, radius)
        circle1.attach_to(window)
        window.render()

    window.close_on_mouse_click()

    """
    Prints:
      50
      70
      90
      110
      130
      ...
      390.
    """
    # ------------------------------------------------------------------
    # TODOne: 4. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence2:')
    print('--------------------------------------------------')

    expected = 70
    answer = print_sequence2(2)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 90
    answer = print_sequence2(3)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 110
    answer = print_sequence2(4)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)


def print_sequence2(n):
    for k in range(n):
        total = 50 + 20 * k

    return total


def draw_circles2():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- Each has fill_color 'blue'.
         -- They are centered at, respectively:
               (50, 100)   (70, 100)   (90, 100)  (110, 100) ... (390, 100)
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODOne: 5. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles2:  See graphics window')
    print('--------------------------------------------------')

    window = rg.RoseWindow(400, 400)

    for k in range(17):
        ball = 50 + 20 * k
        center_point = rg.Point(ball, 200)
        radius = 10
        circle2 = rg.Circle(center_point, radius)
        circle2.fill_color = 'blue'
        circle2.attach_to(window)
        window.render()

    window.close_on_mouse_click()

    """
    Prints:
      1
      2
      3 
      4
      ...
      100.
    """
    # ------------------------------------------------------------------
    # TODOne: 6. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_sequence3:')
    print('--------------------------------------------------')

    expected = 10
    answer = print_sequence3(10)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 30
    answer = print_sequence3(30)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 60
    answer = print_sequence3(60)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)


def print_sequence3(n):
    total = 0
    for k in range(n):
        total = 1 + k

    return total


def draw_circles3():
    """
    -- Constructs an rg.RoseWindow whose width and height are both 300.
    -- Constructs and draws 100 rg.Circle objects such that:
         -- Each is centered at (200, 150)
         -- They have radii:  1  2  3  4  ... 100, respectively.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODOne: 7. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_circles3:  See graphics window')
    print('--------------------------------------------------')

    window = rg.RoseWindow(300, 300)

    for k in range(100):
        center_point = rg.Point(200, 150)
        radius = k
        circle3 = rg.Circle(center_point, radius)
        circle3.attach_to(window)
        window.render()

    window.close_on_mouse_click()

    """
    For each of the integers 0  1  2  ... 100,
    prints 80 times the cosine of that integer.
    Thus, the numbers printed should be about:
       80.0
       43.224184469451174
       -33.29174692377139
       -79.19939972803563
       -52.29148966908895
       22.6929748370581
       76.81362293202928
       60.31218034746437
         ...
       -65.54305962331674
       3.185670431451112
       68.9855097830147
    """
    # ------------------------------------------------------------------
    # TODOne: 8. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    #
    # HINT: You need to   import math   at the top of this file
    #       to use math functions like the ones for cosine and sine.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the cosine function is.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running print_cosines:')
    print('--------------------------------------------------')


def print_cosines():
    for k in range(101):
        total = 80 * math.cos(k)
        print(total)

    """
    -- Constructs a window whose width and height are both 400.
    -- Constructs and draws rg.Circle objects such that:
         -- Each has radius 10.
         -- They are centered at, respectively:
               ( 200 + (80 * cos(0)), 200 + (80 * sin(0) )
               ( 200 + (80 * cos(1)), 200 + (80 * sin(1) )
               ( 200 + (80 * cos(2)), 200 + (80 * sin(2) )
               ( 200 + (80 * cos(3)), 200 + (80 * sin(3) )
                   ...
               ( 200 + (80 * cos(100)), 200 + (80 * sin(100) )
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODOne: 9. Implement this function, per its doc-string above.
    # Put a statement in  main  to test this function.
    # REQUIREMENT: You must use a   RANGE  statement to solve this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Running draw_cosines_and_sines:  See graphics window')
    print('--------------------------------------------------')


def draw_cosines_and_sines():
    window = rg.RoseWindow(400, 400)

    for k in range(100):
        base = (200 + (80 * math.cos(k)))
        ball = (200 + (80 * math.cos(k)))
        center_point = rg.Point(base, ball)
        radius = 10
        circle3 = rg.Circle(center_point, radius)
        circle3.attach_to(window)
        window.render()

    window.close_on_mouse_click()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
