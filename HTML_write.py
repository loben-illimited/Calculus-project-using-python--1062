import markdown2
import os
from bs4 import BeautifulSoup
import base64
import re
from pathlib import Path
import json

class HTML_write:
    def __init__(self, title, css = "custom_css.html", js = "custom_js.html", add_readme = False):
        self.title = title
        #css
        self.css = ""
        with open(css, "r", encoding="utf-8") as i:
            self.css += i.read()
        #js
        self.js = "" 
        with open(js, "r", encoding="utf-8") as i:
            self.js += i.read()

        #construct head
        self.head = self.__construct_head()

        #store result
        self.table = []

        self.construct_html(self.title, add_readme)
    
    def __construct_head(self):
        head = '''
            <!doctype html>
            <html>
                <head>
                    <meta charset = "utf-8">
                    <meta name="author" content="Lo Ben">
                    <title>'''+self.title+'''</title>
                    '''
        head += str(self.css)+str(self.js)
        head += '''
                </head>
                <body>
            '''
        return head
    
    def README(self):
        readme = '''
                <div class = "README">
        ''' + str(markdown2.markdown_path("README.md")).replace("<em>", "").replace("</em>", "") +'''
                </div>
        '''
        a = open("readme.html", "w", encoding="utf-8")
        a.write(readme)
        return readme
    
    def __img2base64_in_Path(self):
        '''
        covert img to base64
        '''
        img_tag_list = []

        path = "temp/"
        for filename in os.listdir(path):
            if re.search(".png", filename) != None:
                ext_filename = re.findall('\..*$', filename)[0].strip(".")
                payload = "data:image/"+ext_filename+";base64,"
                print(filename + "已加入")

                image = open(path + filename, 'rb')
                image_read = image.read()
                image_64_encode = base64.b64encode(image_read)
                image_64_encode = payload + str(image_64_encode).lstrip("b'").rstrip("'")
                #img_tag = '<img src = "'+image_64_encode+'" alt = "'+filename+'"/>' #construct img tag
                img_tag_list.append([image_64_encode, filename])
        self.img_tag_list = img_tag_list
    
    def __construct_tail(self):
        html_head = "</body></html>"
        return html_head

    def __img_tag2html(self):
        self.__img2base64_in_Path()
        img_html_code = ""
        
        '''
        for i in self.img_tag_list:
            img_html_code += '<div class = "figure"><h3 class = "figure_title">'+i[1]+'</h3> <img src = "'+i[0]+'"></div>'
        '''
        for i in range(len(self.img_tag_list)):
            img_html_code += '<div class = "figure"><h3 class = "figure_title">'+self.img_tag_list[i][1]+'</h3>'
            img_html_code += self.table[i]
            img_html_code += '<img src = "'+self.img_tag_list[i][0]+'"></div><hr>'
        return img_html_code
    
    def __result(self):
        code = '<div class = "result">'
        code += self.__img_tag2html()
        code += '</div>'
        return code

    def construct_html(self, filename = None, add_readme = False):
        html_code = ""
        html_code += self.__construct_head() #add head
        if add_readme:
            html_code += self.README() #add readme
        self.construct_hole_table() #construct result table
        html_code += self.__result() #add result img
        html_code += self.__construct_tail()

        output_html_file = open(filename, "w", encoding="utf-8")
        output_html_file.write(html_code)

    def construct_hole_table(self):
        _temp_list = []
        path = "temp/"
        for filename in os.listdir(path):
            if re.search(".json", filename) != None:
                self.__process_a_table(self.__load_json(filename))

    
    def __process_a_table(self, list):
        table = "<table class = 'rwd-table'>"
        table += "<tr><th>年份</th><th>Malthus模型預測</th><th>真實人口</th><th>預測與實際人口相差</th></tr>"
        year_list = [i for i in list[0]]
        malthus_data_list = [list[0][i] for i in list[0]]
        real_population_list = [list[1][i] for i in list[1]]
        sd = list[2]
        for i in range(len(year_list)):
            table += "<tr>"
            table += "<td>"+str(year_list[i])+"</td>"
            table += "<td>"+str(malthus_data_list[i])+"</td>"
            table += "<td>"+str(real_population_list[i])+"</td>"
            if real_population_list[i]-malthus_data_list[i] >= 0:
                table += "<td class = 'positive'>"+str(real_population_list[i]-malthus_data_list[i])+"</td>"
            else:
                table += "<td class = 'negative'>"+str(real_population_list[i]-malthus_data_list[i])+"</td>"
            table += "</tr>"
        table += "</table>"
        self.table += [table]
        self.sn = "<span class= 'sd'>"+str(sd)+"</span>"
        
        #test
        return table

        #open("test_table.html", "w").write(table)
        #print(table)
    
    def __popluation_data_(self):
        path = "temp/"
        self.__data_list = []
        for filename in os.listdir(path):
            if re.search(".json", filename) != None:
                self.__data_list += [self.__load_json(filename)]
        
        print(self.__data_list)

    def __load_json(self, filename):
        path = "temp/"
        json_data_list = None
        with open(path+filename, "r", encoding="utf-8") as i:
            json_data_list = json.loads(i.read())
        return json_data_list

def main():
    a = HTML_write("test")
    a.construct_html("html_test.html", True)
    a.construct_hole_table()
    #test
    '''
    with open("temp/Afghanistan.json", "r", encoding="utf-8") as i:
            json_data_list = json.loads(i.read())
    print(json_data_list, type(json_data_list))
    print("-"*99)
    a.process_a_table(json_data_list)
    '''


if __name__ == "__main__":
    main()