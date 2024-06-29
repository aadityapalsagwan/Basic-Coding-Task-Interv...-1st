String = "aditya"
index = -1
fnc = ""
 
if len(String) == 0 :
  print("EMTPY STRING");
 
for i in String:
    if String.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == len(String)-1 :
    print("All characters are repeating ")
else:
    print("First non-repeating character is", fnc)
