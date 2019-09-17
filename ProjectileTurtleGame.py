# Gra polegająca na trafieniu w cel
import turtle

# Stałe nazwane
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

# Konfigurowanie okna.
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

# Narysowanie celu.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()
success = False
while(success == False):
    # Umieszczenie żółwia na środku ekranu.
    turtle.goto(0,0)
    turtle.setheading(EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)

    # Pobranie od gracza wartości określających kąt i siłę.
    angle = float(input("Podaj kąt pocisku: "))
    force = float(input("Podaj siłę początkową (1-10): "))

    # Obliczenie odległości
    distance = force*FORCE_FACTOR

    # Określenie kierunku.
    turtle.setheading(angle)

    # Wystrzelenie pocisku.
    turtle.pendown()
    turtle.forward(distance)

    # Czy cel został trafiony?
    if(turtle.xcor() >= TARGET_LLEFT_X and
       turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
       turtle.ycor() >= TARGET_LLEFT_Y and
       turtle.ycor() <= (TARGET_LLEFT_Y+TARGET_WIDTH)):
        print("Cel został trafiony!")
        success = True;
    else:
        print("Cel nie został trafiony.")
        success = False;
        if(force <= 9.8):
            print("Powinieneś zwiększyć siłę.")
        elif(force >= 9.9):
            print("Powinieneś zmniejszyć siłę.")
        if(angle <= 67):
            print("Powinieneś zwiększyć kąt.")
        elif(angle>=69):
            print("Powinieneś zmniejszyć kąt")
turtle.done()
