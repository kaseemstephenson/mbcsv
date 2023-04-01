fileContent = ""
linee = ""
file1 = open('temptemp.csv',"w")
sku = "SOP"
host = "https://merchboothphotos.herokuapp.com/"
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



        if ",30" in line:
            if ",12.00000001" in line:
                 line = line.replace(",30",",18.36")
            if ",12" in line:
                 line = line.replace(",30",",18.36")
            if ",10" in line:
                 line = line.replace(",30",",16.3")
            if ",15" in line:
                 line = line.replace(",30",",21.45")


        if ",55" in line:
            if ",32.0000001" in line:
                 line = line.replace(",55",",43.96")

            if ",30" in line:
                 line = line.replace(",55",",41.9")

            if ",32" in line:
                 line = line.replace(",55",",43.96")

            if ",35" in line:
                 line = line.replace(",55",",47.05")
        if ",25" in line:
            if ",13.000001" in line:
                 line = line.replace(",25",",18.39")

            if ",11" in line:
                 line = line.replace(",25",",16.33")

            if ",13" in line:
                 line = line.replace(",25",",18.39")

            if ",16" in line:
                 line = line.replace(",25",",21.48")

        if ",45" in line:
            if ",23" in line:
                 line = line.replace(",45",",32.69")

            if ",25.0000001" in line:
                 line = line.replace(",45",",34.75")

            if ",25" in line:
                 line = line.replace(",45",",34.75")

            if ",28" in line:
                 line = line.replace(",45",",37.84")

        if ",35" in line:
            if ",16.00000001" in line:
                 line = line.replace(",35",",21.42")
            if ",14" in line:
                 line = line.replace(",35",",23.48")
            if ",16" in line:
                 line = line.replace(",35",",23.48")
            if ",19" in line:
                 line = line.replace(",35",",26.57")










        file1.write(line)
        linee = linee + line + "\n"
        print(linee)
file1.close()