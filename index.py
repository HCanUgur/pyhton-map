import turtle
from utils import alert

ts = turtle.getscreen()

# Load the images
named_img = ts.bgpic("assets/named.gif")
unnamed_img = ts.bgpic("assets/unnamed.gif")

# Cities and their coordinates
cities = {
    "Istanbul": (-100, -100),
    "Kilis": (100, -180),
    "Elazığ": (100,-70),
    "Sivas": (100,70),
     "Ordu": (110,150),
     "Samsun": (15,190),
    "Amasya": (15,145),
     "Yozgat": (10,70),
    "Mersin": (-30,140),
    "çorum":(-80,200),
    "Karabük":(-160,180),
    "Malatya":(150,-21),
    "Van":(500,-18),
    "Mardin":(350, -120),
    "Batman":(360,-80),
    "Siirt":(400.-50),
    "Hakkari":(550,-70),
    "Ağrı":(490,80),
    "Iğdır":(520,100),
    "Kars":(500,140),
    "Ardahan":(465, 200),
    "Artvin":(400, 220),
    "Rize":(340, 180),
    "Erzurum":(340, 100),
    "Bingöl":(340, 30),
    "Mus":(370, 30),
    "Kayseri":(320, -10),
    "Diyarbakir":(320, -40),
    "Erzincan":(280, 70),
    "Tunceli":(280, 50),
    "Trabzon":(270, 150),
    "Gümüşhane":(250, 110),
    "Bayburt":(290, 110),
    "Giresun":(190,160),
    "Urfa":(250,-120),
    "Adiyaman":(150,-100),
    "Maras":(100,-50),
    "Antep":(100,-150),
    "Osmaniye":(40,-100),
    "Hatay":(30,180),
    "Adana":(20,180),
}

# Create the screen and set the mode to "logo"
wn = turtle.Screen()
wn.mode("logo")
wn.bgcolor("lightgreen")

# Hide the default turtle
turtle.hideturtle()

# Load the images
named_img = ts.bgpic("assets/named.gif")
unnamed_img = ts.bgpic("assets/unnamed.gif")
total_wrong_counter = 0
correct_guessed = 0
city_numbers=41

# Create the screen and set the mode to "logo"
wn = turtle.Screen()
wn.mode("logo")

# Hide the default turtle
turtle.hideturtle()

# Set the reference image
wn.bgpic(named_img)
turtle.ontimer(lambda: wn.bgpic(unnamed_img), 3000)

# Create a turtle to draw on the screen
t = turtle.Turtle()

# Move the turtle to the correct position
t.setpos(cities["Istanbul"])

# Draw the image on the screen
t.stamp()

# Set the guessing image
wn.bgpic(unnamed_img)

# Ask for the province name
# province_name = turtle.textinput("Please enter the city name", "City name:")

# check all the cities and their coordinates


def iterate_prv_nxt(my_list):
    prv, cur, nxt = None, iter(my_list), iter(my_list)
    next(nxt, None)

    while True:
        try:
            if prv:
                yield next(prv), next(cur), next(nxt, None)
            else:
                yield None, next(cur), next(nxt, None)
                prv = iter(my_list)
        except StopIteration:
            break


for prv, city_curr, city_next in iterate_prv_nxt(cities):
    # if the province name is in the cities
    print(city_curr)

    while True:
        
        province_name = turtle.textinput("Please enter the city name", "City name:")

        if province_name != city_curr:
            alert.show_alert("error", "Error", "You did not find the city")
            total_wrong_counter += 1
            wn.title(
                "Python Challenge with Turtle Graphics - Correct Guesses: "
                + str(correct_guessed)
                + " Cities Remaining "
                + str(city_numbers)
            )

        else:
            # get the coordinates of the province
            x, y = cities[province_name]
            # move the turtle to the coordinates
            t.setpos(x, y)
            # draw the image on the screen
            t.stamp()
            # show the alert
            correct_guessed += 1
            city_numbers -=1
            alert.show_alert(
                "info",
                "Congratulations🎉",
                "Congratulations🎉 You found the {city}!".format(city=city_curr),
            )
            turtle.write(
                province_name,
                font=("Arial", 15, "normal"),
                align="right",
                move=False,
            )
            wn.title(
               "Python Challenge with Turtle Graphics - Correct Guesses: "
                + str(correct_guessed)
                + " Cities Remaining "
                + str(city_numbers)
            )

            break
    # set the next
    if city_next == None:
        break
    else:
        x, y = cities[city_next]
        # move the turtle to the coordinates
        t.setpos(x, y)
        # draw the image on the screen
        t.stamp()

print("Thanks for playing!")


#! Need refactoring and optimization
if total_wrong_counter == 0:
    alert.show_alert(
        "info",
        "Congratulations🎉",
        "Congratulations🎉 You found all the cities!",
    )
elif total_wrong_counter == 1:
    alert.show_alert(
        "info",
        "Congratulations🎉",
        "Congratulations🎉 You found all the cities with 1 wrong guess!",
    )
elif total_wrong_counter > 1:
    alert.show_alert(
        "info",
        "Congratulations🎉",
        "Congratulations🎉 You found all the cities with "
        + str(total_wrong_counter)
        + " wrong guesses!",
    )
elif total_wrong_counter > 5:
    alert.show_alert(
        "warning",
        "Congratulations⚠️",
        "Congratulations⚠️ You found all the cities with "
        + str(total_wrong_counter)
        + " wrong guesses! You can do better!",
    )
elif total_wrong_counter > 10:
    alert.show_alert(
        "warning",
        "Congratulations❌",
        "Congratulations❌ You found all the cities with "
        + str(total_wrong_counter)
        + " wrong guesses! You can do better! Try again!",
    )


# Wait for the user to press a key
wn.exitonclick()

alert.show_alert("warning", "Bye Bye", "Bye Bye")

# Close the window
turtle.Screen().bye()
