from bs4 import BeautifulSoup
import requests
import pandas as pd



data =[]
countries = ['germany','ireland','malta','france','lithuania','latvia','uk','hungary']

for country in countries:
    proceed = True
    current_page = 1
    while(proceed):
        

        url = "https://studyabroad.careers360.com/"+str(country)+"/universities-in-"+str(country)+"-unvlst?page="+str(current_page)

        page = requests.get(url)

        soup = BeautifulSoup(page.content,"html.parser")
        
        if soup.title.text == "404 Error Page - Sorry, Page Not Found | Careers360":
            proceed = False
            
        else:
            s = soup.find_all('div', class_='tuple_content_block')
            
            for content in s:
                item = {}
                item['Country']=country
                item['University Name'] = content.find('h3', class_='study_abroad_college_name').text
                item['Type Of University'] = "".join(content.find('span', class_='duration_tag').text.split())
                item['Location'] = content.find('span',attrs={'class': None}).text
                
                data.append(item)
                # data.append(item['college_name'].replace(",",""))
    
                
        current_page += 1
        print(current_page,country)
    print(country,"completed")
    # proceed=False
df = pd.DataFrame(data)
df.to_excel("universities.xlsx")
print("Completed")


################################################################################################################

from bs4 import BeautifulSoup
import requests
import pandas as pd

universities = ["technical university of munich","rwth aachen university aachen","aalen university of applied sciences aalen","anhalt university of applied sciences kothen","bauhaus university weimar","bavarian university of applied sciences munich","berlin international university of applied sciences berlin","berlin school of economics and law berlin","berlin university of the arts berlin","bielefeld university bielefeld","bingen technical university of applied sciences bingen","brandenburg medical school theodor fontane neuruppin","brandenburg university of technology cottbus","bremen university of applied sciences bremen","bremerhaven university of applied sciences bremerhaven","cbs international business school cologne","code university of applied sciences berlin","carl benz school of engineering karlsruhe","carl von ossietzky university of oldenburg","catholic university of eichstatt ingolstadt","charite university medicine berlin","chemnitz university of technology chemnitz","clausthal university of technology clausthal-zellerfeld","coburg university of applied sciences and arts coburg","constructor university Bremen","darmstadt university of applied sciences darmstadt","deggendorf institute of technology deggendorf","dresden international university dresden","dresden university of technology and economics dresden","ebs university of economics and law wiesbaden","escp business school berlin campus","eu business school munich","eastern bavarian technical university of regensburg","eberhard karls university of tubingen","eberswalde university for sustainable development eberswalde","esslingen university of applied sciences esslingen","european school of management and technology berlin","european university viadrina frankfurt","fh aachen-university of applied sciences aachen","fh munster","fom university of economics and management essen","fachhochschule dortmund-university of applied sciences and arts dortmund","frankfurt school of finance and management frankfurt","frankfurt university of applied sciences frankfurt","free university of berlin","fresenius university idstein","friedrich alexander university erlangen","friedrich schiller university jena","fulda university of applied sciences fulda","furtwangen university furtwangen","georg august university of gottingen","gisma university of applied sciences potsdam","goethe university frankfurt","leibniz university","hhl leipzig graduate school of management leipzig","hof university of applied sciences hof","hafencity university hamburg","hamburg university of applied sciences hamburg","hamburg university of technology hamburg","hamm-lippstadt university of applied sciences hamm","hannover medical school hannover","harz university of applied sciences wernigerode","heidelberg university of education heidelberg","heidelberg university heidelberg","heilbronn university of applied sciences heilbronn","heinrich heine university dusseldorf","helmut schmidt university hamburg","hochschule dusseldorf university of applied sciences dusseldorf","hochschule wismar university of applied sciences technology business and design wismar","humboldt university of berlin","iu international university of applied sciences erfurt","ingolstadt technical university ingolstadt","international school of management dortmund campus","johannes gutenberg university mainz","justus liebig university giessen","kaiserslautern university of applied sciences kaiserslautern","karlsruhe institute of technology karlsruhe","karlsruhe school of optics and photonics karlsruhe","karlsruhe university of applied sciences karlsruhe","kempten university of applied sciences kempten","kiel university of applied sciences kiel","kuhne logistics university hamburg","lancaster university leipzig","leipzig university leipzig","leuphana university luneburg","lubeck university of technology lubeck","ludwig maximilian university of munich","macromedia university of applied sciences berlin campus","macromedia university of applied sciences munich campus","magdeburg-stendal university of applied sciences magdeburg","mannheim business school mannheim","mannheim university of applied sciences mannheim","martin luther university halle-wittenberg","munich business school munich","munich university of applied sciences munich","new european college munich","nordhausen university of applied sciences nordhausen","nuremberg institute of technology nuremberg","nurtingen-geislingen university of economics and environment nurtingen","oth-technical university of applied sciences amberg","owl university of applied sciences and arts lemgo","offenburg university of applied sciences offenburg","osnabruck university osnabruck","otto beisheim school of management vallendar","otto von guericke university magdeburg","pfh private university of applied sciences gottingen","pforzheim university pforzheim","philipps university of marburg","ruhr university bochum","ravensburg-weingarten university of applied sciences weingarten","reutlingen university reutlingen","rhine-waal university of applied sciences kleve","rosenheim technical university of applied sciences rosenheim","srh berlin university of applied sciences berlin","srh berlin university of applied sciences hamburg campus","srh berlin university of applied sciences heidelberg campus","srh berlin university of applied sciences nordrhein-westfalen campus","htw saar","saarland university saarbrucken","schmalkalden university of applied sciences schmalkalden","south westphalia university of applied sciences iserlohn","steinbeis university berlin","stralsund university stralsund","stuttgart media university stuttgart","stuttgart university of technology stuttgart","th koln-university of applied sciences cologne","tu dortmund university dortmund","technical university of applied sciences augsburg","technical university of applied sciences wildau","technical university of applied sciences wurzburg-schweinfurt","technical university of berlin","technical university of braunschweig","technical university of dresden","technical university of ilmenau","technological university bergakademie freiberg","the christian albrechts university of kiel","the technical university of darmstadt","the university of cologne","the university of kaiserslautern landau","trier university of applied sciences trier","trier university trier","ukrainian free university munich","ulm university of applied sciences ulm","university targu mures medical campus hamburg","university of applied management studies mannheim","university of applied sciences erfurt","htw berlinx","university of applied sciences emden-leer","university of applied sciences jena","university of augsburg" ,"university of bamberg ","university of bayreuth","university of bonn","university of Bremen","university of duisburg duisburg campus","university of duisburg essen campus","university of erfurt","university of flensburg","university of freiburg","university of greifswald","university of hamburg","university of hildesheim","university of hohenheim stuttgart","university of kassel","university of koblenz","university of konstanz","university of lubeck","university of mannheim","university of munster","university of paderborn","university of passau","university of potsdam","university of regensburg","university of rostock","university of siegen","university of stuttgart","university of ulm","university of wuppertal","university of wurzburg","university of the bundeswehr munich","wedel university of applied sciences wedel","west saxon university of applied sciences zwickau","witten-herdecke university witten",'zeppelin university friedrichshafen']


data = []
university_num = 1
for university in universities:
    proceed = True
    current_page = 1
    university_link = "-".join(university.split())

    while(proceed == True):
        
        page = requests.get("https://studyabroad.careers360.com/germany/universities/"+str(university_link)+"-unpg/courses-listpg?page="+str(current_page)) 
        soup = BeautifulSoup(page.content,"html.parser")
        courses_list = soup.find_all('div',class_='college_tuple')
        
        if courses_list == []:
            proceed = False
        
        else:
            for courses in courses_list:
                item = {}
                item['University'] = university
                item['Course Name'] = courses.find('h4',class_='course_name').text
                course_info = courses.find_all('div',class_='col-md-4 col-6')
                course_details = []
                for info in course_info:
                    value = info.find('b').text
                    item[info.text.replace(value,'')]=value
                # print(item)
                data.append(item)

        current_page += 1
    print(university_num,university,"completed")
    university_num += 1
df = pd.DataFrame(data)
df.to_excel("Germany.xlsx")
print("completed")