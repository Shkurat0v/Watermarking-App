import tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = Tk()
window.title("Watermaking App")

# Insert path to your image below

im = Image.open("sample.jpg")
if im.size > (500, 500):
    image_big = True
    image_alt = Label(text="Image is too big, but it will be downloaded anyways!")
    image_alt.grid(column=1, row=1)
# Insert path to your image above
else:
    image_big = False
    image = ImageTk.PhotoImage(im)
    actual_image = tkinter.Label(image=image)
    actual_image.grid(column=1, row=1)
    canvas = Canvas(width=500, height=500)


app = Label(text="Imported image:")
app.grid(column=1, row=0)


watermark = Label(text="Enter a text for your watermark:")
watermark.grid(column=2, row=0)

watermark_position = Label(text="Enter coordinates for your watermark (x, y):")
watermark_position.grid(column=2, row=1)

watermark_size = Label(text="Enter a size for watermark font (recommended is 30):")
watermark_size.grid(column=1, row=2)

watermark_input = Entry(width=20)
watermark_input.grid(column=3, row=0)

watermark_input_position = Entry(width=20)
watermark_input_position.grid(column=3, row=1)

watermark_input_size = Entry(width=35)
watermark_input_size.grid(column=1, row=3)



def make_watermark():
  global im, image, actual_image
  try:
     x, y = map(int, watermark_input_position.get().split(','))
     font = ImageFont.load_default(float(watermark_input_size.get()))
  except ValueError:
     app.configure(text="Enter valid entries!", fg="red")
     return

  Im = ImageDraw.Draw(im)
  Im.text(((x, y)), watermark_input.get(), fill=(255, 255, 255), font=font)

  if not image_big:
      image = ImageTk.PhotoImage(im)
      actual_image.configure(image=image)
      actual_image.image = image
      app.configure(text="Watermarked Image is saved! To import original image, restart the app.", fg="white")
      im.save("Watermarked.png")
  else:
      image_alt.configure(text="Watermarked Image is saved! To import original image, restart the app.", fg="white")
      im.save("Watermarked.png")

watermark_button = Button(text="Submit", width=20, height=3, command=make_watermark)
watermark_button.grid(column=3, row=2, rowspan=2)

window.mainloop()