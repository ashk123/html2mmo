import Hcore
import xml.etree.ElementTree as ET
import random

def getRandomNumber():
    return random.randint(50, 1000)

def getRandomString(mult) :
    #print("This is from getRandomString function:", mult)
    words = mult.replace("#[", "").replace("]", "").split(",")
    return words[random.randint(0, len(words) - 1)]

def main() :
    print("HTML 2 MMO games - simple old HTML MMO-RPG maker")
    print()
    #ofile = ET.parse('test.xml')
    ofile = ET.parse('story.xml')
    Vars = {}
    root = ofile.getroot()
    body_str = ""
    buttons = {}
    obj = Hcore.Hcore("the best MMO", "THE TEST HTML MMO-RPG")
    for i in range(0, len(root)) :
        #print(root[i].attrib)
        if root[i].tag == "page" :
            for i2 in range(0, len(root[i])) :
                if root[i][i2].tag == "body" :
                    main_text = root[i][i2].text
                    if "#smile" in main_text :
                        #print("I found a smile")
                        main_text = main_text.replace("#smile", "😉")
                    if "#rand" in main_text:
                        randstrorg = str(getRandomNumber())
                        main_text = main_text.replace("#rand", randstrorg)
                    while "#[" in main_text:
                        #print("I Found a better solution")
                        char_index = main_text.find("#[")
                        utils = ""
                        for chars in range(char_index, len(main_text)) :
                            if (main_text[chars] == "]") :
                                utils += "]"
                                break
                            utils += main_text[chars]
                        # print("This is the text:", org)
                        main_text = main_text.replace(utils, getRandomString(utils))
                    #if "$rand" in main_text:
                    #    if "health" in Vars:
                    #        main_text = main_text.replace("$rand", Vars["health"])
                    #    else:
                    #        randstrorg = str(getRandomNumber())
                    #        main_text = main_text.replace("$rand", randstrorg)
                    #        Vars["health"] = randstrorg # save the health variable
                    body_str += main_text

                    #$print(root[i][i2].text)
                elif root[i][i2].tag == "btn" :
                    buttons[root[i][i2].text] = root[i][i2].attrib['page'] + ".html"
            obj.makePage(root[i].attrib['name'], body_str, buttons);
            body_str = ""
            buttons = {}

if __name__ == "__main__" :
    main()
