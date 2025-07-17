filenames = ["1.dhollu.txt","2.punjabi.txt", "3.lassi.txt"]
content = ["aloo","kaju","chaklka"]
for filename,z in zip(filenames,content):
    x = open(f"../files/{filename},'w'")
    x.write(filename,z)
