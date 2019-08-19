from urllib.request import urlretrieve


with open('cow_imageLink.txt') as f:
    for i, line in enumerate(f):
        line = line.strip()
        # print(line)

        if len(line) > 0:
            link, name = line.split('\t')
            # print(link + ',' + name )
            urlretrieve(link, filename="train_images/" + name + ".jpg")
            print(link)

