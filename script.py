from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# ---------------- WINDOW ----------------
root = Tk()
root.title("Breaking News Template Generator")
root.geometry("500x350")

# ---------------- VARIABLES ----------------
img_path = ""
logo_path = "logo.png"      # apna logo yahan rakhna
template_path = "template.png"

# ---------------- FUNCTIONS ----------------

def select_image():
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")])
    label_img.config(text=img_path.split("/")[-1])

def generate():
    if img_path == "":
        print("Image select karo pehle")
        return

    base = Image.open(template_path).convert("RGBA")

    user_img = Image.open(img_path).convert("RGBA")
    user_img = user_img.resize((850, 750))
    base.paste(user_img, (115, 200), user_img)

    # logo
    try:
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((140, 140))
        base.paste(logo, (base.width - 160, 20), logo)
    except:
        pass

    draw = ImageDraw.Draw(base)

    text = entry.get()

    # bold breaking style font
    try:
        font = ImageFont.truetype("arial.ttf", 55)
    except:
        font = ImageFont.load_default()

    # red breaking box
    draw.rectangle([(0, 0), (base.width, 120)], fill=(200, 0, 0))

    draw.text((30, 35), "BREAKING NEWS", fill="white", font=font)

    # main text
    draw.text((50, 1000), text, fill="white", font=font)

    base.save("output.png")
    print("Generated: output.png")

# ---------------- UI ----------------

Label(root, text="Breaking News Generator", font=("Arial", 16)).pack(pady=10)

Button(root, text="Select Image", command=select_image).pack()

label_img = Label(root, text="No image selected")
label_img.pack(pady=5)

Label(root, text="Enter Text:").pack()

entry = Entry(root, width=50)
entry.pack(pady=5)

Button(root, text="Generate", command=generate, bg="red", fg="white").pack(pady=20)

root.mainloop()
