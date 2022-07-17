from dv_captcha import thaanaGenerator


gen = thaanaGenerator("bruh")

text = "ދާރިސް"
img = gen.generate_image(text,style=5)


img.save("bruh_yes.jpg")

