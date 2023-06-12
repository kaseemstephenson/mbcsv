fileContent = ""
linee = ""
file1 = open('temptemp.csv',"w")
sku = "TALB"
host = "https://merchboothphotos3.herokuapp.com/"
replaceCounter = 0
designCounter = 1
imgSrc = host+sku+"-"+str(designCounter)+'-0'
with open('temp.csv') as topo_file:
    for line in topo_file:
        #print (line) 
        if designCounter == 5:
            break
        if replaceCounter == 6:
            designCounter+=1
            replaceCounter = 0
            imgSrc = host+sku+"-"+str(designCounter)+'-0'
        if "REPLACE" in line:
            replaceCounter += 1
            imgSrc  = imgSrc +str(replaceCounter)+".png"
            line = line.replace("REPLACE",imgSrc)
            imgSrc = host+sku+"-"+str(designCounter)+'-0'


        file1.write(line)
        linee = linee + line + "\n"
        print(linee)
file1.close()