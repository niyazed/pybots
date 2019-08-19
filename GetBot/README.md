Download image from link and rename it.

```
from urllib.request import urlretrieve

link = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
name = 'google'
urlretrieve(link, filename="IMAGES_FOLDER/" + name + ".png")
```
