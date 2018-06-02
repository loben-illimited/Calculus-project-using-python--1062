import markdown2
import os
from bs4 import BeautifulSoup
import base64
import re
from pathlib import Path

class HTML_write:
    def __init__(self, title, css = "custom_css.html", js = "custom_js.html"):
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
        
        for i in self.img_tag_list:
            img_html_code += '<div class = "figure"><h3 class = "figure_title">'+i[1]+'</h3> <img src = "'+i[0]+'"></div>'
        
        #file = open("test_img.html", "w")
        #file.write(img_html_code)
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
        html_code += self.__result() #add result img
        html_code += self.__construct_tail()

        output_html_file = open(filename, "w", encoding="utf-8")
        output_html_file.write(html_code)

    def __construct_table(self):
        pass
    
    def __process_table(self):
        pass

def main():
    a = HTML_write("test")
    #a.README()
    #a.img_tag2html()
    a.construct_html("html_test.html", True)

if __name__ == "__main__":
    main()