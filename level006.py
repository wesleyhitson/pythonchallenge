import zipfile

zip_f = zipfile.ZipFile("channel.zip")
print(zip_f.read("readme.txt"))

start_file = 90052

names = zip_f.namelist()
comments = []

while str(start_file) + ".txt" in names:
    contents = zip_f.read(str(start_file) + ".txt")
    print(contents)
    comments.append(zip_f.getinfo(str(start_file) + ".txt").comment)
    start_file = contents.split(' ')[-1]

print("".join(comments))

# gets hockey, which leads to oxygen
