def ilanginsimbol(var):
    var = var.replace(":"," ").replace("/"," ").replace("&"," ")
    var = var.replace("\""," ").replace("\\"," ").replace("("," ") #123.320->123.320, 123.->123
    var = var.strip() #" blabla"->"blabla", " blabla"->[ ,"blabla]

    if not(var.isalnum()): #issymbol =/=, jika bukan alfabet atau angka
        if var.startswith(("1","2","3","4","5","6","7","8","9","0")): #jika dimulai 123. atau 123, atau 123.123
            if var[-1] == ".": #jika karakter terakhirnya "." maka titiknya diganti spasi
                var=var.replace(".", " ") #jika karakter terakhirnya "," maka koma diganti spasi
            elif var[-1] == ",":
                var=var.replace(","," ") #a. atau a.23 langsung ganti titik dan koma jadi spasi
        else:
            var = var.replace(","," ").replace(","," ")

    var = var.strip()
    var2 = var.split() #rumah,rumah->[rumah,rumah]
    return var2