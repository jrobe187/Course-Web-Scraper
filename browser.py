from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup, SoupStrainer
from selenium.webdriver.support import expected_conditions as EC
import re
import time



driver = webdriver.Chrome()


ids = []
names = []
iterator = 0
descriptions = []
matches = []
courses = []
last_page_id = ['WGST 3803', 'WGST 3820', 'WGST 4050', 'WGST 4051', 'WGST 4120', 'WGST 4130', 'WGST 4131', 'WGST 4132', 
  	  'WGST 4140', 'WGST 4143', 'WGST 4150', 'WGST 4151', 'WGST 4152', 'WGST 4153', 'WGST 4160', 'WGST 4165',  
  	  'WGST 4170', 'WGST 4190', 'WGST 4191', 'WGST 4228', 'WGST 4260', 'WGST 4401', 'WGST 4601','WRDS 1103', 'WRDS 1104', 'WRDS 2101', 'WRDS 3102', 'WRDS 3140'  
  	  'WRDS 3211', 'WRDS 3215', 'WRDS 3220', 'WRDS 4011', 'WRDS 4021', 'WRDS 4201'  
  	  'WRDS 4210', 'WRDS 4225', 'WRDS 4330', 'WRDS 4400', 'WRDS 4402', 'WRDS 4900']
last_page_name = ['Independent Study', 'Feminist Philosophy',"Topics in Women’s Studies",
  	     "Topics in Women’s Studies", "Women’s Studies International", 'Girl Studies in America', 'Culture, Pregnancy, and Birth',
  	     'Reproductive Justice Movement', 'African American Feminism', 'Black Masculinity, Health, and Society',
  	     'Gender, Science, and Technology', 'Women, Biology, and Health', 'Ecological Feminism',
  	     'Virginity: Power, Politics, and Pleasure', 'Race, Sexuality, and the Body', 'Sociology of Women', 'Queer Theory',
  	     'Indigenous Feminisms', 'Women’s Health Issues', 'French Women Writers in Translation',
  	     'Women: Middle Age and Beyond', 'Internship in Women’s Studies','Senior Colloquium',
         'Writing and Inquiry in Academic Contexts I and II', 'Writing and Inquiry in Academic Contexts I and II with Studio',
  	     'Advanced Writing: Research and Critical Analysis', 'The Effective Sentence: A Writing Course for All Majors',
  	     'Arguing With Images', 'Online Writing: Ethics, Appropriation, and Social Media', 'Information Literacy and Digital Composing', 'Current Theories and Applications of Writing',
  	     'Topics in Writing Technologies', 'Topics in Writing and Reading', 'Composing Across Borders: Transnational Digital Composition',
  	     'Contemporary Rhetorical Theory', 'Writing Research Methods', 'Reading, Writing, and Archiving: Charlotte',
  	     'Writing, Rhetoric, and Digital Studies Internship Practicum', 'Research, Theory, and Practice of Tutoring Writing', 'Senior Research Capstone'] 
course = {'name': None , 'id':  None, 'subject': None}
subjects = ['Accounting', 'Aerospace Studies', 'Africana Studies', 'American Studies', 'Anthropology',
            'Arabic', 'Architecture', 'Art: Academic and Departmental', 'Art: Basic Foundation Studios',
            'Art: Ceramics', 'Art: Drawing', 'Art: Education', 'Art: Fibers', 'Art: Graphic Design', 'Art: History',
            'Art: Illustration', 'Art: Digital Media', 'Art: Painting', 'Art: Print Media', 'Art: Photography',
            'Art: Sculpture', 'Arts + Architecture', 'Arts + Architecture Honors Program', 'Bioinformatics and Genomics',
            'Biology', 'Business', 'Business Analytics', 'Business Law', 'Capitalism Studies', 'Chemistry', 'Child and Family Development',
            'Chinese', 'Civil and Environmental Engineering', 'Civil Engineering Technology', 
            'Communication Studies', 'Computer Science', 'Computing and Informatics', 'Construction Management', 'Criminal Justice and Criminology',
            'Dance', 'Data Science', 'Earth Sciences', 'Economics', 'Education', 'Education - Learning, Design, and Technology',
            'Educational Research, Measurement, and Evaluation', 'Electrical and Computer Engineering',
            'Electrical Engineering Technology', 'Elementary Education', 'Energy and Electromechanical Systems',
            'Engineering', 'Engineering Technology', 'English', 'Entrepreneurship', 'Exercise Science', 'Farsi',
            'Film Studies', 'Finance', 'Fire and Safety Engineering Technology', 'First-Year Writing', 'Foreign Language Education', 
            'Francophone Studies', 'French', 'Geography', 'Geology', 'Gerontology', 'German', 'Greek',
            'Health and Human Services', 'Health/Medical Humanities', 'Health Systems Management', 'History',
            'Holocaust, Genocide, and Human Rights', 'Honors College', 'Humanities, Technology, and Science', 
            'Industrial Engineering Technology', 'Interdisciplinary Studies', 'International Business', 
            'International Studies', 'Italian', 'Japanese', 'Journalism', 'Kinesiology',
            'Languages and Culture Studies', 'Latin', 'Latin American Studies', 'Legal Studies', 'Liberal Arts & Sciences',
            'Liberal Studies/General Education', 'Management', 'Management Information Systems', 'Manufacturing Engineering Technology',
            'Mathematics', 'Mathematics Education', 'Mechanical Engineering', 'Mechanical Engineering Technology', 'Middle Grades Education',
            'Modern Greek', 'Meteorology', 'Marketing', 'Middle, Secondary, and K-12 Education', 'Military Science',
            'Music', 'Music Education', 'Music Performance', 'Neurodiagnostics and Sleep Science',
            'Nursing', 'Nursing: RN-to-BSN', 'Operations and Supply Chain Management', 'Operations Research', 'Philosophy',
            'Physics', 'Political Science', 'Portuguese', 'Professional Studies', 'Psychology', 'Public Health Sciences',
            'Reading, Language, and Literacy', 'Religious Studies', 'Respiratory Therapy', 'Russian', 'Secondary Education',
            'Social Work', 'Sociology', 'Software and Information Systems', 'Southern Studies', 'Spanish', 'Special Education',
            'Special and Elementary Education', 'Statistics', 'Swahili', 'Systems Engineering', 'Teaching English as a Second Language',
            'Theatre', 'Translating and Translation Studies', 'University College', 'Urban Studies', 'Urban Youth and Communities', 'Women’s and Gender Studies',
            'Writing, Rhetoric, and Digital Studies']




class browser:

    
    def __init__(self) -> None:
        pass

    def launchbrowser(self):
        

        # navigate to website
        driver.get("https://catalog.charlotte.edu/content.php?catoid=32&catoid=32&navoid=3395&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=1#acalog_template_course_filter")
        driver.maximize_window()
    


    def Scrape(self):
        
        new_string = ''
        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        
        
        
        #Converts page to string
        for i in page_source.find_all('a'):
            if str(i).find('-') != -1:
                new_string = new_string + str(i.get('title')) + " "
            
            
        #Puts all class Ids and Names in list   
        course_pattern = re.compile(r'(\w+\s\d+)\s-\s(.+?)\sopens', re.DOTALL)
        matches = course_pattern.findall(new_string)

        
        for match in matches:
            course = {}
            

            ids.append(match[0])
            names.append(match[1])

            course['name'] = match[1]
            course['id'] = match[0]
           
            
            
            


            courses.append(course)
        

        print(courses)

        

    def next(self, page: int):

       # time.sleep(1)
       # next = driver.find_element(By.LINK_TEXT, page)
        #time.sleep(2)
       # next.click()

        button = driver.find_element(By.LINK_TEXT, f'{page}')

        button.click()


    def subject(self):
        global iterator

        

        courses[0]['subject'] = 'Accounting'

        for i in range(1,len(courses)):
            if(ids[i][:4] == ids[i-1][:4]):
                courses[i]['subject'] = subjects[iterator]
            else:
                iterator = iterator + 1
                courses[i]['subject'] = subjects[iterator]

        
                

        
            print(courses[i])

    def corrections(self):
        for i in range(len(last_page_id)):
            ids.append(last_page_id[i])
            names.append(last_page_name[i])

        for i in range(len(courses)):
            temp = courses[i]['id'][:4]

            if(temp[0] == 'A'):
                if(temp == 'ACCT'):
                    courses[i]['subject'] = 'Accounting'

                elif(temp == 'AERO'):
                    courses[i]['subject'] = 'Aerospace Studies'

                elif(temp == 'AFRS'):
                    courses[i]['subject'] = 'Africana Studies'

                elif(temp == 'AMST'):
                    courses[i]['subject'] = 'American Studies'

                elif(temp == 'ANTH'):
                    courses[i]['subject'] = 'Anthropology'

                elif(temp == 'ARBC'):
                    courses[i]['subject'] = 'Africana Studies'

                elif(temp == 'ARCH'):
                    courses[i]['subject'] = 'Architecture'

                elif(temp == 'ARTA'):
                    courses[i]['subject'] = 'Art: Academic and Departmental'

                elif(temp == 'ARTB'):
                    courses[i]['subject'] = 'Art: Basic Foundation Studios'

                elif(temp == 'ARTC'):
                    courses[i]['subject'] = 'Art: Ceramics'
                
                elif(temp == 'ARTD'):
                    courses[i]['subject'] = 'Art: Drawing'

                elif(temp == 'ARTE'):
                    courses[i]['subject'] = 'Art: Eductation'

                elif(temp == 'ARTF'):
                    courses[i]['subject'] = 'Art: Fibers'

                elif(temp == 'ARTG'):
                    courses[i]['subject'] = 'Art: Graphic Design'

                elif(temp == 'ARTH'):
                    courses[i]['subject'] = 'Art: History'

                elif(temp == 'ARTL'):
                    courses[i]['subject'] = 'Art: Illustration'

                elif(temp == 'ARTM'):
                    courses[i]['subject'] = 'Art: Digital Media'

                elif(temp == 'ARTP'):
                    courses[i]['subject'] = 'Art: Painting'

                elif(temp == 'ARTR'):
                    courses[i]['subject'] = 'Art: Print Media'
                
                elif(temp == 'ARTT'):
                    courses[i]['subject'] = 'Art: Photography' 

                elif(temp == 'ARTZ'):
                    courses[i]['subject'] = 'Art: Sculpture'

                elif(temp == 'AAHP'):
                    courses[i]['subject'] = 'Arts + Architecture Honors Program'

                
            
            if(temp[0] == 'B'):
                if(temp == 'BINF'):
                    courses[i]['subject'] = 'Bioinformatics'

                elif(temp == 'BSN'):
                    courses[i]['subject'] = 'Business'

                elif(temp == 'BUSA'):
                    courses[i]['subject'] = 'Business Analytics'

                elif(temp == 'BLAW'):
                    courses[i]['subject'] = 'Business Law'

                




            if(temp[0] == 'C'):
                if(temp == 'COAA'):
                    courses[i]['subject'] = 'Arts + Architecture'

                elif(temp == 'CAPI'):
                    courses[i]['subject'] = 'Capitalism Studies'

                elif(temp == 'CHEM'):
                    courses[i]['subject'] = 'Chemistry'

                elif(temp == 'CHFD'):
                    courses[i]['subject'] = 'Child and Family Development'

                elif(temp == 'CHNS'):
                    courses[i]['subject'] = 'Chinese'

                elif(temp == 'CEGR'):
                    courses[i]['subject'] = 'Civil and Environmental Engineering'

                elif(temp == 'COMM'):
                    courses[i]['subject'] = 'Communication Studies'

                elif(temp == 'CMET'):
                    courses[i]['subject'] = 'Construction Management'

                elif(temp == 'CJUS'):
                    courses[i]['subject'] = 'Criminal Justice and Criminology'
                    
                elif(temp == 'CLAS'):
                    courses[i]['subject'] = 'Liberal Arts & Sciences'


                elif(temp == 'CUCY'):
                    courses[i]['subject'] = 'Urban Youth and Communities'
                
            
                
                

            if(temp[0] == 'D'):
                if(temp == 'DANC'):
                    courses[i]['subject'] = 'Dance'
                
                elif(temp == 'DTSC'):
                    courses[i]['subject'] = 'Data Science'

            if(temp[0] == 'E'):
                if(temp == 'ETCE'):
                    courses[i]['subject'] = 'Civil Engineering Technology'

                elif(temp == 'ESCI'):
                    courses[i]['subject'] = 'Earth Sciences'

                elif(temp == 'ECON'):
                    courses[i]['subject'] = 'Economics'

                elif(temp == 'EDUC'):
                    courses[i]['subject'] = 'Education'

                elif(temp == 'ELDT'):
                    courses[i]['subject'] = 'Education - Learning, Design, and Technology'

                elif(temp == 'ECGR'):
                    courses[i]['subject'] = 'Electrical and Computer Engineering'

                elif(temp == 'ELET' or temp == 'ETEE'):
                    courses[i]['subject'] = 'Electrical Engineering Technology'

                elif(temp == 'ELED'):
                    courses[i]['subject'] = 'Elementary Education'

                elif(temp == 'ENER'):
                    courses[i]['subject'] = 'Energy and Electromechanical Systems'

                elif(temp == 'ENGR'):
                    courses[i]['subject'] = 'Engineering'

                elif(temp == 'ETGR'):
                    courses[i]['subject'] = 'Engineering Technology'

                elif(temp == 'ENGL'):
                    courses[i]['subject'] = 'English'

                elif(temp == 'ENTR'):
                    courses[i]['subject'] = 'Entrepreneurship'

                elif(temp == 'EXER'):
                    courses[i]['subject'] = 'Exercise Science'

                elif(temp == 'ETFS'):
                    courses[i]['subject'] = 'Fire and Safety Engineering Technology'

                elif(temp == 'ETIN'):
                    courses[i]['subject'] = 'Industrial Engineering Technology'

                elif(temp == 'ETMF'):
                    courses[i]['subject'] = 'Manufacturing Engineering Technology'

                elif(temp == 'ETME'):
                    courses[i]['subject'] = 'Mechanical Engineering Technology'


            if(temp[0] == 'F'):
                if(temp == 'FARS'):
                    courses[i]['subject'] = 'Farsi'

                elif(temp == 'FILM'):
                    courses[i]['subject'] = 'Film Studies'

                elif(temp == 'FINN'):
                    courses[i]['subject'] = 'Finance'

                elif(temp == 'FLED'):
                    courses[i]['subject'] = 'Foreign Lanuage Education'

                elif(temp == 'FRAN'):
                    courses[i]['subject'] = 'Francophone Studies'

                elif(temp == 'FREN'):
                    courses[i]['subject'] = 'French'
                

            if(temp[0] == 'G'):
                if(temp == 'GEOG'):
                    courses[i]['subject'] = 'Geography'

                elif(temp == 'GEOL'):
                    courses[i]['subject'] = 'French'

                elif(temp == 'GRNT'):
                    courses[i]['subject'] = 'Gerontology'

                elif(temp == 'GERM'):
                    courses[i]['subject'] = 'German'

                elif(temp == 'GREK'):
                    courses[i]['subject'] = 'Greek'

            if(temp[0] == 'H'):
                if(temp == 'HAHS'):
                    courses[i]['subject'] = 'Health and Human Services'

                elif(temp == 'HHUM'):
                    courses[i]['subject'] = 'Health/Medical Humanities'
                
                elif(temp == 'HSMT'):
                    courses[i]['subject'] = 'Health Systems Management'

                elif(temp == 'HIST'):
                    courses[i]['subject'] = 'History'

                elif(temp == 'HGHR'):
                    courses[i]['subject'] = 'Holocaust, Genocide, and Human Rights'

                elif(temp == 'HONR'):
                    courses[i]['subject'] = 'Honors College'

                elif(temp == 'HTAS'):
                    courses[i]['subject'] = 'Humanities, Technology, and Science'

                elif(temp == 'HLTH'):
                    courses[i]['subject'] = 'Public Health Sciences'

            if(temp[0] == 'I'):
                if(temp == 'ITCS'):
                    name = courses[i]['name']
                    if('Senior' in name or 'Undergraduate' in name):
                        courses[i]['subject'] = 'Computer Science'

                    else:
                        courses[i]['subject'] = 'Computing and Informatics'

                elif(temp == 'IDST'):
                    courses[i]['subject'] = 'Interdisciplinary Studies'

                elif(temp == 'IBUS'):
                    courses[i]['subject'] = 'International Business'

                elif(temp == 'INTL'):
                    courses[i]['subject'] = 'International Studies'

                elif(temp == 'ITLN'):
                    courses[i]['subject'] = 'Italian'

                elif(temp == 'INFO'):
                    courses[i]['subject'] = 'Management Information Systems'

                elif(temp == 'ITIS'):
                    courses[i]['subject'] = 'Software and Information Systems'

            if(temp[0] == 'J'):
                if(temp == 'JAPN'):
                    courses[i]['subject'] = 'Japanese'

                elif(temp == 'JOUR'):
                    courses[i]['subject'] = 'Journalism'


            if(temp[0] == 'K'):
                if(temp == 'KNES'):
                    courses[i]['subject'] = 'Kinesiology'


            if(temp[0] == 'L'):
                if(temp == 'LACS'):
                    courses[i]['subject'] = 'Languages and Culture Studies'

                elif(temp == 'LATN'):
                    courses[i]['subject'] = 'Latin'

                elif(temp == 'LTAM'):
                    courses[i]['subject'] = 'Latin American Studies'

                elif(temp == 'LEGL'):
                    courses[i]['subject'] = 'Legal Studies'

                elif(temp == 'LBST'):
                    courses[i]['subject'] = 'Liberal Studies/General Education'

                

            if(temp[0] == 'M'):
                if(temp == 'MGMT'):
                    courses[i]['subject'] = 'Management'

                elif(temp == 'MATH'):
                    courses[i]['subject'] = 'Mathematics'

                elif(temp == 'MAED'):
                    courses[i]['subject'] = 'Mathematics Education'

                elif(temp == 'MEGR'):
                    courses[i]['subject'] = 'Mechanical Engineering'

                elif(temp == 'MDLG'):
                    courses[i]['subject'] = 'Middle Grades Education'

                elif(temp == 'MDGK'):
                    courses[i]['subject'] = 'Modern Greek'

                elif(temp == 'METR'):
                    courses[i]['subject'] = 'Meteorology'

                elif(temp == 'MKTG'):
                    courses[i]['subject'] = 'Marketing'

                elif(temp == 'METR'):
                    courses[i]['subject'] = 'Meteorology'

                elif(temp == 'MDSK'):
                    courses[i]['subject'] = 'Middle, Secondary, and K-12 Education'

                elif(temp == 'MSCI'):
                    courses[i]['subject'] = 'Military Science'

                elif(temp == 'MUSC'):
                    courses[i]['subject'] = 'Music'

                elif(temp == 'MUED'):
                    courses[i]['subject'] = 'Music Education'

                elif(temp == 'MUPF'):
                    courses[i]['subject'] = 'Music Performance'

                
            if(temp[0] == 'N'):
                if(temp == 'NDSS'):
                    courses[i]['subject'] = 'Neurodiagnostics and Sleep Science'

                elif(temp == 'NURS'):
                    courses[i]['subject'] = 'Nursing'

                elif(temp == 'NURN'):
                    courses[i]['subject'] = 'Nursing: RN-to-BSN'


            if(temp[0] == 'O'):
                if(temp == 'OPER'):
                   courses[i]['subject'] = 'Operations and Supply Chain Management'

                elif(temp == 'OPRS'):
                    courses[i]['subject'] = 'Operations Research'


            if(temp[0] == 'P'):
                if(temp == 'PHIL'):
                    courses[i]['subject'] = 'Philosophy'

                elif(temp == 'PHYS'):
                    courses[i]['subject'] = 'Physics'

                elif(temp == 'POLS'):
                    courses[i]['subject'] = 'Political Science'

                elif(temp == 'PORT'):
                    courses[i]['subject'] = 'Portugese'

                elif(temp == 'PROS'):
                    courses[i]['subject'] = 'Professional Studies'

                elif(temp == 'PSYC'):
                    courses[i]['subject'] = 'Psychology'

                
                 
                

                
            

            if(temp[0] == 'R'):
                if(temp == 'RSCH'):
                    courses[i]['subject'] = 'Educational Research, Measurement, and Evaluation'

                elif(temp == 'READ'):
                    courses[i]['subject'] = 'Reading, Language, and Literacy'
                
                elif(temp == 'RELS'):
                    courses[i]['subject'] = 'Religious Studies'

                elif(temp == 'RESP'):
                    courses[i]['subject'] = 'Respiratory Therapy'

                elif(temp == 'RUSS'):
                    courses[i]['subject'] = 'Russian'

            if(temp[0] == 'S'):
                if(temp == 'SECD'):
                    courses[i]['subject'] = 'Secondary Education'

                elif(temp == 'SOWK'):
                    courses[i]['subject'] = 'Social Work'

                elif(temp == 'SOCY'):
                    courses[i]['subject'] = 'Sociology'

                elif(temp == 'SOST'):
                    courses[i]['subject'] = 'Southern Studies'

                elif(temp == 'SPAN'):
                    courses[i]['subject'] = 'Spanish'

                elif(temp == 'SPED'):
                    courses[i]['subject'] = 'Special Education'

                elif(temp == 'SPEL'):
                    courses[i]['subject'] = 'Special and Elementary Education'

                elif(temp == 'STAT'):
                    courses[i]['subject'] = 'Statistics'

                elif(temp == 'SWAH'):
                    courses[i]['subject'] = 'Swahili'

                elif(temp == 'SEGR'):
                    courses[i]['subject'] = 'Systems Engineering'

            
            if(temp[0] == 'T'):
                if(temp == 'TESL'):
                    courses[i]['subject'] = 'Teaching English as a Second Language'

                elif(temp == 'THEA'):
                    courses[i]['subject'] = 'Theater'

                elif(temp == 'TRAN'):
                    courses[i]['subject'] = 'Translating and Translation Studies'

            if(temp[0] == 'U'):
                if(temp == 'UWRT'):
                    courses[i]['subject'] = 'First-Year Writing'

                elif(temp == 'UCOL'):
                    courses[i]['subject'] = 'University College'

                elif(temp == 'URBS'):
                    courses[i]['subject'] = 'Urban Studies'

            if(temp[0] == 'W'):
                if(temp == 'WGST'):
                    courses[i]['subject'] = "Women's and Gender Studies"

                elif(temp == 'WRDS'):
                    courses[i]['subject'] = 'Writing, Rhetoric, and Digital Studies'

                



        print(courses)
                

            
        
    
    def description(self):

        #class links start at index 89 and end at 188
        #full page has 233 links

       
        #for element in range(89, len(links) - 42):
        links = driver.find_elements(By.XPATH, '//a')

        for element in range(0, len(links)):
            time.sleep(.5)
            links[element].click()
            print(links[element].text)



        elements = driver.find_elements(By.XPATH, '//div[2]')
        for i in range(len(elements)):
            print(elements[i].text)

    


    
                

        
            
