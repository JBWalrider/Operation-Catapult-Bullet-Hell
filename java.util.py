def setupText(text):
    text.setTextColor("red")
    text.setSize(20)
    text.setStyle("bold")

def error(win):
    errorText = Text(Point(WINDOWSIZE / 2, WINDOWSIZE / 3), "Something went wrong")
    errorText.setSize(30).setTextColor("red").setStyle("bold").draw(win)
    errorImage = Image(Point(WINDOWSIZE / 2, WINDOWSIZE * 2 / 3), "error.gif").draw(win)

def 