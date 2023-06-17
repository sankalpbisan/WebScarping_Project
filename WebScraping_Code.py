from bs4 import BeautifulSoup
import requests
import csv

print("LINKED-IN WEBSITE SCRAPING PROGRAM".center(50))

try:
    while(1):
        site = input("\nPaste Linked-In webpage URl here : ")
        if "https://www.linkedin.com/jobs/" in site:
            print('')
            break
        else:
            print("\nPlease paste proper URL !\n{Note : You might have entered wrong URl, Goto linkedin.com then go for a Job Search, copy and paste that URL here.}\n")
   
    print("Stand by !\nScraping..........\n")
   
    url = requests.get(site)
    hcontent = url.content
    soup = BeautifulSoup(hcontent,"html.parser")
    
    jtitle = soup.find_all('h3', class_='base-search-card__title')
    comp_name = soup.find_all('h4', class_='base-search-card__subtitle')
    location = soup.find_all('span', class_='job-search-card__location')
    salary = soup.find_all('span', class_='job-search-card__salary-info')
    post_date = soup.find_all('time', class_='job-search-card__listdate')
    status = soup.find_all('div', class_='job-search-card__benefits')
    goto = soup.find_all('a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')

    i = 0
    j = len(jtitle)

    while(i<j):
        print("Job Title : "+jtitle[i].text.strip())
        print("Company Name : "+comp_name[i].text.strip())
        print("Location : "+location[i].text.strip())
        try:
            print("Salary : "+salary[i].text.replace(' ',''))
        except:
            print("Salary : Not Mentioned !")
        try:
            print("Job Listed : "+post_date[i].text.strip())
        except:
            print("Job Listed : Not Mentioned !")
        try:
            print("Currently (Status) : "+status[i].text.strip())
        except:
            print("Currently (Status) : Not Mentioned !")
        link = goto[i].get('href')
        print("Apply Here : "+link)
        desc = requests.get(link) #description
        desc_content = desc.content #description content
        soupx = BeautifulSoup(desc_content,"html.parser")
        descriptn = soupx.find('div', class_='show-more-less-html__markup') #description done
        try:
            print("Description : "+descriptn.text.strip())
        except:
            print("Description : Not Found !")
        print("-------------------------------------------------------------------------------------------\n")
        i = i+1
   
    print("Scraping is completed successfully.\n")
    def savetotxt():
        i = 0
        filename = input("What would you like to be your file name : ")
        print("Please Wait !\nProcessing...")
        fp = open(filename+".txt","a")
        while(i<j):
            fp.write("Job Title : "+jtitle[i].text.strip()+"\n")
            fp.write("Company Name : "+comp_name[i].text.strip()+"\n")
            fp.write("Location : "+location[i].text.strip()+"\n")
            try:
                fp.write("Salary : "+salary[i].text.replace(' ','')+"\n")
            except:
                fp.write("Salary : Not Mentioned !"+"\n")
            try:
                fp.write("Job Listed : "+post_date[i].text.strip()+"\n")
            except:
                fp.write("Job Listed : Not Mentioned !"+"\n")
            try:
                fp.write("Currently (Status) : "+status[i].text.strip()+"\n")
            except:
                fp.write("Currently (Status) : Not Mentioned !"+"\n")
            link = goto[i].get('href')
            fp.write("Apply Here : "+link+"\n")
            desc = requests.get(link)
            desc_content = desc.content
            soupx = BeautifulSoup(desc_content,"html.parser")
            descriptn = soupx.find('div', class_='show-more-less-html__markup')
            try:
                fp.write("Description : "+descriptn.text.strip()+"\n")
            except:
                fp.write("Description : Not Found !"+"\n")
            fp.write("-----------------------------------------------------------------------------------------------\n\n")
            i = i+1
        fp.close()
        print("File saved successfuly by name "+filename+".txt")
        print("\nScrape Again after few days, to check new job openings.....")


    data = []
    def savetocsv():
        i = 0
        filename = input("What would you like to be your file name : ")
        print("Please Wait !\nProcessing...")
        with open(filename+".csv",'w',encoding="utf-8") as fp:
            writer=csv.writer(fp)
            writer.writerow(["Job Title","Company Name","Location","Salary","Job Listed","Currently (Status)","Apply Here"])
            while(i<j):
                data.append(jtitle[i].text.strip())
                data.append(comp_name[i].text.strip())
                data.append(location[i].text.strip())
                try:
                    s = salary[i].text.replace('\n','')
                    sal = s.replace(' ','')
                    salar = sal.replace('₹','')
                    data.append(salar)
                except:
                    data.append("Not Mentioned !")
                try:
                    data.append(post_date[i].text.strip())
                except:
                    data.append("Not Mentioned !")
                try:
                    data.append(status[i].text.strip())
                except:
                    data.append("Not Mentioned !")
                link = goto[i].get('href')
                data.append(link)
                writer.writerow(data)
                data.clear()
                i = i+1
        print("File saved successfuly by name "+filename+".csv")
        print("\nScrape Again after few days, to check new job openings.....")  


    
    while True:
        print("Do you want to save this data in a file ?")
        a = int(input("Press 0 to discard or Press 1 to save test file or Press 2 to save csv file : "))
        if a==0 or a==1 or a==2:
            break
        else:
            print("Enter correct value !")
    if a==1:
        savetotxt()
    elif a==2:
        savetocsv()
    else:
        print("No problem, you can come and save file whenever you want.")
        print("\nScrape Again after few days, to check new job openings.....")

except:
    print("\nError Occurred !\nYour Internet may not be connected at the moment or having issue while connecting.\nMake sure your Internet works properly before running application again.")

