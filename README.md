# DV_CAPTCHA

This generates images of dhivehi handwritten and text, this is generated using data from (https://github.com/dash8x/Thaana-Dataset) 

### Usage
First download the pickled python dictionary from releases.

```
from dv_captcha import thaanaGenerator

gen = thaanaGenerator("pickeled_data_path")

text = "ދާރިސް"

img = gen.generate_image(text,style=5)
img.save("bruh_yes.jpg")
```