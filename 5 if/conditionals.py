pasta="boloneze"
print(" pasta boloneze should give true")
print(pasta=="boloneze","\n")

print("pasta carbonera should give false")
print(pasta=="carbonera","\n")

madoka="mAGi"
print("normlly madoka magi should give false")
print(madoka=="magi","\n")
print("but if you use lower()...")
print(madoka.lower()=="magi","\n")

print("lets tset both conditions using AND")
print(pasta=="boloneze" and madoka=="magi","\n")
print("lets test both conditions useing OR")
print(pasta=="boloneze" or madoka=="magi","\n")

gems=["ruby","saphire","emerald"]
print(gems,"\n lets test if ruby is in gems list")
gem="ruby"
print("ruby" in gems,"\n")
print("lets test if topaz is not in gems list")
gem="topaz"
print(gem not in gems)
