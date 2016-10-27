import csv


con = "path/to/2004_TREC_ASCII_MEDLINE_2"

outcon = "path/to/trec_ASCII_2.csv"

text = {"PMID": "PMID", "Title": "Title", "Abstract": "Abstract", "MeSH": "MeSH", "PT": "Pub Type"}

esc_sequence = ''.join([chr(char) for char in range(1, 32)])+ '/' + '*' + ',' 

with open(outcon, 'wb+') as csvfile:
    writer = csv.writer(csvfile, quoting = csv.QUOTE_MINIMAL)
    writer.writerow(['PMID', 'Title', 'Abstract', 'MeSH', 'Pub_Type'])
    

with open(con, 'r')as f:
    for line in f:
        if(line.startswith("PMID")):
            text["PMID"] = line.replace('PMID-', '')
        
        elif (line.startswith("TI")):
            text["Title"] = line.replace("TI", '').replace('-','')
            line = f.next()
            if (not(line.startswith("PG"))):
                text["Title"] += ''  + line.replace("TI", '').replace('-','')
        
        elif (line.startswith("AB")):
            text["Abstract"] = line.replace("AB", '').replace('-','')
            line = f.next()
            while(not(line.startswith("AD"))):
                text["Abstract"] += '' + line.replace("AB", '').replace('-','')
                line = f.next()
        elif (line.startswith("PT")):
            text["PT"] = line.replace("PT", '').replace("-", '')
        
        elif (line.startswith("MH")):
            text["MeSH"] = line.replace("MH", '').replace('-','')
            while(not(line.startswith("SO"))):
                text["MeSH"] += '' + line.replace("MH", '').replace('-','')
                line = f.next()
                
            text["PMID"] = "".join(map(str, text["PMID"])).strip()
            text["Title"] = "".join(map(str, text["Title"])).translate(None, esc_sequence).strip()
            text["Abstract"] = "".join(map(str, text["Abstract"])).translate(None, esc_sequence).strip()
            text["MeSH"] = "".join(map(str, text["MeSH"])).translate(None, esc_sequence).strip()
            text["PT"] = "".join(map(str, text["PT"])).strip()
            
            with open(outcon, 'ab+') as w:
                writer = csv.writer(w, quoting = csv.QUOTE_MINIMAL)
                writer.writerow([text["PMID"], text["Title"], text["Abstract"], text["MeSH"], text["PT"]])
        
            text = {"PMID": "PMID", "Title": "Title", "Abstract": "Abstract", "MeSH": "MeSH", "PT": "Pub Type"}
            
            
       
           
            
            
        
        

