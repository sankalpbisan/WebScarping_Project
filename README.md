Hey there !
I have completed my very first project based on web scraping.
To be more precise, I scraped Linkedin web site.
I have used python language for my project.
The modules used are :  bs4 (Beautifulsoup) and requests.

**Procedure:**
First I have studied the HTML code of a particular Linkedin webpage (i.e. particular job search result).
Then I stored the HTML object file into a variable by using request module.
This object file is parsed into a parse tree using html-parser so that the html content can be manipulated.
Next, I fetched specific data using the HTML tags and classes.
Used various functions like .text(), .strip() etc. to get result in normal text (string) form.
At last the fetch data is displayed and stored in either TEXT or CSV file. 
