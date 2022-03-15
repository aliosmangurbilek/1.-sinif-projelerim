import turtle
import random
import winsound

winsound.PlaySound('arka müzik.wav', winsound.SND_ASYNC)

oyun_penceresi = turtle.Screen()
oyun_penceresi.bgcolor('black')
oyun_penceresi.title('Ali Versus Emre')
oyun_penceresi.bgpic('uzay.gif')
oyun_penceresi.setup(width=700, height=700)

turtle.register_shape('gemi.gif')
turtle.register_shape('dusman.gif')
turtle.register_shape('ates.gif')

gemi = turtle.Turtle()
gemi.color('blue')
gemi.speed(0)
gemi.shape('gemi.gif')
gemi.setheading(90)
gemi.penup()
gemi.goto(0, -400)
gemi_hizi = 30

mermi = turtle.Turtle()
mermi.color('yellow')
mermi.speed(0)
mermi.shape('ates.gif')
mermi.setheading(90)
mermi.penup()
mermi.goto(0, -400)
mermi_hizi = 70
mermi.hideturtle()
mermi.turtlesize(1, 1)
mermi_kontrol = False

yazi = turtle.Turtle()
yazi.color('white')
yazi.speed(0)
yazi.penup()
yazi.goto(0, 200)
yazi.hideturtle()

dusmanlar = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.hideturtle()
yaz.goto(0, 450)
yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

yapimci = turtle.Turtle()
yapimci.speed(0)
yapimci.shape("square")
yapimci.color("white")
yapimci.penup()
yapimci.goto(0,-200)
yapimci.hideturtle()

yapimci_bir = turtle.Turtle()
yapimci_bir.speed(0)
yapimci_bir.shape("square")
yapimci_bir.color("white")
yapimci_bir.penup()
yapimci_bir.goto(0,-250)
yapimci_bir.hideturtle()

def giden_mermi():
    y = mermi.ycor()
    y = y + mermi_hizi
    mermi.sety(y)

def sola_git():
    x = gemi.xcor()
    x = x - gemi_hizi
    if x < -580:
        x = -580
    gemi.setx(x)

def saga_git():
    x = gemi.xcor()
    x = x + gemi_hizi
    if x > 580:
        x = 580
    gemi.setx(x)

def yukari_git():
    y = gemi.ycor()
    y = y + gemi_hizi
    if y > 400:
        y = 400
    gemi.sety(y)
def asagi_git():
    y = gemi.ycor()
    y = y - gemi_hizi
    if y < -400:
        y = -400
    gemi.sety(y)

def mermi_at():
    global mermi_kontrol
    winsound.PlaySound('lazer.wav', winsound.SND_ASYNC)
    x = gemi.xcor()
    y = gemi.ycor() + 0
    mermi.goto(x, y)
    mermi.showturtle()
    mermi_kontrol = True


for i in range(10):
    dusmanlar.append(turtle.Turtle())
for dusman in dusmanlar:
    dusman.color('red')
    dusman.speed(0)
    dusman.turtlesize(1, 1)
    dusman.shape('dusman.gif')
    dusman.penup()
    dusman.setheading(90)
    x = random.randint(-500, 500)
    y = random.randint(500, 500)
    dusman.goto(x, y)

oyun_penceresi.listen()
oyun_penceresi.onkey(sola_git, 'Left')
oyun_penceresi.onkey(saga_git, 'Right')
oyun_penceresi.onkey(yukari_git, 'Up')
oyun_penceresi.onkey(asagi_git, 'Down')
oyun_penceresi.onkey(mermi_at, 'space')



while True:
    if mermi_kontrol:
        giden_mermi()

    for dusman in dusmanlar:
        y = dusman.ycor()
        y = y - 2
        dusman.sety(y)

        if dusman.distance(mermi) < 50:
            puan = puan + 10
            yaz.clear()
            yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 30, "normal"))
            dusman.hideturtle()
            mermi.hideturtle()
            dusmanlar.pop(dusmanlar.index(dusman))
            winsound.PlaySound('patlama.wav', winsound.SND_ASYNC)

        if dusman.ycor() < -500 or dusman.distance(gemi) < 50:
            yazi.write('Maalesef Kaybettiniz', align='center', font=('Courier', 40, 'bold'))
            yapimci.write('Hazırlayanlar:', align='center', font=('Courier', 30, 'bold'))
            yapimci_bir.write("Ali ve Emre", align='center', font=('Courier', 30, 'bold'))
    if len(dusmanlar) == 0:
        yazi.write('Tebrikler, Kazandınız', align='center', font=('Courier', 40, 'bold'))
        yapimci.write('Hazırlayanlar:', align='center', font=('Courier', 30, 'bold'))
        yapimci_bir.write('Ali ve Emre', align='center', font=('Courier', 25, 'bold'))





