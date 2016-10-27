import csv
import os
import errno
from HTMLParser import HTMLParser

filepath = "path/to/folder"
filename = "file.csv"
    
filepath = os.path.join(filepath, filename)
directory = os.path.dirname(filepath)



# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
        
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = {'PMID': 'No PMID', 'Title': 'No Data', 'Abstract': 'No Abstract', 'MeSH': 'MESH'}
        self.abstag = None
        self.tag = None
        self.temp = []
        self.ttag = None
        self.ptag = None
        self.mstag = None
            
    def handle_starttag(self, tag, attrs):
        self.tag = tag       
        if (self.tag == 'abstract'):
            self.abstag = tag
        elif (self.tag == 'articletitle'):
            self.ttag = tag
        elif (self.tag == 'pmid'):
            self.ptag = 'pmid'
        elif (self.tag == 'meshheadinglist'):
            self.mstag = 'mesh'
            
            
    def handle_endtag(self, tag):
        if tag == 'abstract':
            self.abstag = None
            self.temp = []
        elif tag == 'articletitle':
            self.ttag = None
            self.temp = []
        elif tag == 'pmid':
            self.ptag = None
            self.temp = []
        elif tag == 'meshheadinglist':
            self.mstag = None
            self.temp = []
            self.cleandata()
            self.writecsv()
        
                        
    def handle_data(self, data):
        if (self.ttag == 'articletitle'): #or ((self.ttag == 'atl') & ((self.tag == 'it') or (self.tag == 'sup') or (self.tag == 'inf') or (self.tag == 'scp'))):
            self.temp.append(data)
            ' '.join(self.temp).strip()
                    
            self.data["Title"] = self.temp
             
        
            
        if (self.abstag == 'abstract') or ((self.abstag == 'abstract') & ((self.tag == 'abstracttext'))):
           
            self.temp.append(data)
            ' '.join(self.temp).strip()
            self.data["Abstract"] = self.temp
        
        if (self.ptag == 'pmid'):
            self.temp.append(data)
            " ".join(self.temp).strip()
            self.data["PMID"] = self.temp
        
        if ((self.mstag == 'mesh') & ((self.tag == 'qualifier' or self.tag == 'descriptorname'))):
            
            self.temp.append(data)
            " ".join(self.temp).strip()
            self.data["MeSH"] = self.temp
            #self.clear()
            
            
                
    def writecsv(self):
            
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise
   
        with open(filepath, 'ab+') as csvfile:
        
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    
            writer.writerow([parser.data['PMID'], parser.data['Title'], parser.data['Abstract'], parser.data['MeSH']])
        csvfile.close()
        
    
    def cleandata(self):
        esc_sequence = ''.join([chr(char) for char in range(1, 32)]) + ','


        str_temp_abs = parser.data['Abstract']
        parser.data['Abstract'] = " ".join(map(str, str_temp_abs)).translate(None, esc_sequence).strip()
        
        str_temp_title = parser.data['Title']
        parser.data['Title'] = " ".join(map(str, str_temp_title)).translate(None, esc_sequence).strip()

        str_temp_pmid = parser.data['PMID']
        parser.data['PMID'] = "".join(map(str, str_temp_pmid)).strip()

        str_temp_mesh = parser.data['MeSH']
        parser.data['MeSH'] = " ".join(map(str, str_temp_mesh)).translate(None, esc_sequence).strip()
        
        
        
            
                    
           
##################################################################
def writecsv():
        
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise
   
    with open(filepath, 'ab+') as csvfile:
        
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    
        writer.writerow([parser.data['PMID'], parser.data['Title'], parser.data['Abstract'], parser.data['MeSH']])
    csvfile.close()
########################################################################

    
def cleandata():
    esc_sequence = ''.join([chr(char) for char in range(1, 32)]) + ','


    str_temp_abs = parser.data['Abstract']
    parser.data['Abstract'] = " ".join(map(str, str_temp_abs)).translate(None, esc_sequence).strip()
        
    str_temp_title = parser.data['Title']
    parser.data['Title'] = " ".join(map(str, str_temp_title)).translate(None, esc_sequence).strip()
    str_temp_pmid = parser.data['PMID']
    parser.data['PMID'] = "".join(map(str, str_temp_pmid)).strip()

    str_temp_mesh = parser.data['MeSH']
    parser.data['MeSH'] = "".join(map(str, str_temp_mesh)).translate(None, esc_sequence).strip()

#########################################################################
# instantiate the parser and fed it some HTML
with open(filepath, 'wb+') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    
    writer.writerow(['PMID', 'Title', 'Abstract', 'MeSH'])
    csvfile.close()



con = open("path/to/2004_TREC_XML_MEDLINE_")

       
content = con.read()
parser = MyHTMLParser()
parser.feed(content)

cleandata()
writecsv()        
        
        

       
parser.close()
con.close()