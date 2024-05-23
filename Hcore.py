import os

class Hcore :
    def __init__(self, game_name, banner) :
        self.GameName = game_name
        self.Pages = []
        self.banner = banner
        self.old_page = "."
        self.cstyle = ""
    def SetStyle(self) :
        if os.path.exists("./style.css") :
            self.cstyle = open("./style.css").read()
            print("Read the style file");
    def writeFile(self, body, page_name) :
        if os.path.exists("./Game/") == False :
            os.system("mkdir Game");
            
        with open("Game/"+page_name + ".html", "w") as ofile :
            ofile.write(body)
            ofile.close()
        return 0
    def makePage(self, page_name, page_body, page_buttons) :
        #self.SetStyle() # read the style file
        org = ""
        org += "<html>"
        org += "<head>"
        org += "<style>"
        org += self.cstyle
        org += "</style>"
        # head contents
        org += "<title> " + page_name + "</title>" 
        org += "</head>"
        # start body
        org += "<body>"
        org += "<h2>" + self.banner + "</h2><hr>"
        page_body = "\n".join(page_body.split("\n")[1::]).replace("\n", "<br>") if page_body.split("\n")[0] == "" else page_body.replace("\n", "<br>")
        org += "<h3>" + page_body.replace('\t', "") + "</h3>"
        for key, value in page_buttons.items() :
            org += "<a href='" + value + "'>" + key + "</a><br>"
        org += "</body>"

        org += "</html>"

        if (Hcore.writeFile(self, org, page_name) == 0) :
            print("Page", page_name, "created");
            self.old_page = page_name
            return 0
        else :
            return 1
