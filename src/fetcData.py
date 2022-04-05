import os
import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def fetch_description_data():
    try:
        parsed_data=[]
        try:
            unparsed__dis_data=os.listdir('..//data/description')
        except:
            raise Exception("please make sure the descripton folder is not empty")
        for i in unparsed__dis_data:
            novel={'title':str(),'auth':str(),'dis':str(),}
            #this part to be changed after disccusion
            novel['title']=i[0:i.find('-')]
            novel['auth']=i[i.find('-'):i.find('(')]
            novel['dis']=getText(f"..//data/description/{i}")
            parsed_data.append(novel)
        return parsed_data
    except:
        raise Exception('check ur data')




