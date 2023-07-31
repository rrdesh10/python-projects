import cv2
import pandas as pd

# global variables
clicked = False
r = g = b = xpos = ypos = 0

# reading image with opencv
img = cv2.imread('colorpic.jpg')

# reading csv file using pandas and assigning names to cols
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
csv = pd.read_csv('colors.csv', names=index, header=None)


# function to calculate min distance from all colors and finding most matching color
def getcolorname(R, G, B):
    miminum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, 'R'])) + abs(G - int(csv.loc[i, 'G'])) + abs(B - int(csv.loc[i, 'B']))
        if d <= miminum:
            miminum = d
            cname = csv.loc[i, 'color_name']
    return cname


# function to get x y co-ordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while (1):
    cv2.imshow('image', img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # creating text strings of color name and RGB values
        text = getcolorname(r, g, b) + " R=" + str(r) + " G=" + str(g) + " B=" + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For light colors will display text as black color
        if (r + g + b >= 600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False
    # press Esc key to quit
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
