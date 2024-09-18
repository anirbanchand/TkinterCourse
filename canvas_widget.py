from tkinter import *

root = Tk()

canvas_width = 500
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)

# Create a vertical line from (x=0, y=0) to (x=0, y=400), spanning the entire height
can_widget.create_line(0, 0, 500, 400, fill="red")
can_widget.create_line(0, 400, 500, 0, fill="red")

# To create a rectangle, specify the top-left and bottom-right coordinates:
can_widget.create_rectangle(3, 5, 500, 300, fill="blue")


# for text
can_widget.create_text(200, 200, text="Python")

# for oval
can_widget.create_oval(455, 355, 5, 5)


can_widget.pack()
root.mainloop()
