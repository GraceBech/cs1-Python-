#Author : Grace Bech
# Date  : 01/15/2023
#purpose: Using Cs1lib to draw the cover of a children's book

from cs1lib import*

def cover():
    clear()
    set_stroke_color(0, 0, 0)
    enable_stroke()
    set_fill_color(0, 1, 1, 1)
    #Back book cover
    draw_rectangle(70, 80, 180, 289)
    #front book cover
    draw_rectangle(80, 90, 200, 290)
    #center of the book.
    set_fill_color(0.2, 0.5, 0)
    draw_rectangle(70, 80, 10, 290)
    # Ground
    draw_rectangle(80, 260, 200, 120)
    #The sun
    set_fill_color(1, 1, 0)
    draw_circle(240, 150, 40)
    set_fill_color(1, 1, 1)
    #head
    draw_circle(150, 260, 40)
    draw_circle(150, 220, 30)
    #Eyes
    r = 5
    x = 150
    set_fill_color(1, 1, 1)
    draw_circle(x-10, 204, r)
    draw_circle(x+13, 204, r)

    set_fill_color(0, 0, 0)
    draw_circle(x+16, 204, r-3)
    draw_circle(x-8, 204, r-3)
    #Hat
    draw_ellipse(150, 190, 22, 10)
    set_fill_color(1, 0, 0)
    draw_ellipse(150, 230, 8, 3)
    disable_stroke()
    set_fill_color(1, 1, 1)
    #Snow man's body
    set_stroke_color(0, 0, 0)
    draw_circle(150, 320, 50)
    set_font_size(12)
    #Snow man's arm
    enable_stroke()
    #Right Hand
    draw_line(230, 240, 160, 190)
    #Right Hand Elbow
    draw_line(230, 240, 180, 250)
    #left arm
    draw_line(115, 240, 90, 290)
    #Nose
    set_fill_color(1, 0.5, 0)
    draw_triangle(150, 212, 220, 210, 220, 220)
def drawing():
    cover()
    set_fill_color(1, 1, 1, )
    #Melted ice
    draw_rectangle(190, 340, 20, 20)
    draw_rectangle(240, 330, 20, 20)
    enable_stroke()
    set_stroke_color(0,0,0)
    set_font_size(15)
    draw_text("SNOWMAN", 100, 120)
    draw_text("AND THE SUN", 90, 140)
    draw_text("A book by", 210, 290)
    draw_text("Grace B.", 210, 310)
start_graphics(drawing)