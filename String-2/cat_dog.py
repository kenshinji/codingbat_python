def cat_dog(str):
   cat_n = 0
   dog_n = 0
   i = 0
   while i < len(str) - 2:
       if str[i:i+3] == "cat":
           cat_n += 1
       elif str[i:i+3] == "dog":
           dog_n += 1
        i += 1
    return dog_n == cat_n
