# Analyzing Vietnamese Graduation Score: Project Overview 
* Exploited Python to curl and clean data of 74000 + candidates, including full names, DOB, and scores for 11 exams
* Utilized rigorously NumPy and Pandas to create 5+ DataFrames for plotting
* Utilized Matplotlib, Seaborn, and Pandas built-in visualization tools flexibly draw 10+ charts for testing null hypothesis
* Created a database in pgAdmin and extracted output using SQL queries to assess the coding part's accuracy and efficiency and detect errors in the dataset

## Code and Resources Used 
**Python Version:** 3.10  
**Packages:** pandas, numpy, matplotlib, seaborn, wordcloud
**Reference:** Dung Lai Lap Trinh - https://www.youtube.com/watch?v=hkF_oIm3lU4&t=2068s

## Web Scraping
Tweaked the web scraper scrape 74000+ candidates information from http://diemthi.hcm.edu.vn/Home/Show. With following, we got a HTML code including those information: 
*	Student ID
*	Full name
*	Date of birth
*	Math score
*	Literature score 
*	Social science score
*	Natural science score 
*	History score
*	Geography score
*	Civics score
*	Biology score
*	Chemistry score
*	Physics score
*	English 

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for visualization. I made the following changes from the raw HTML code:

*	Wrote header to csv 
*	Found all IDs that do not exist in the range by try-except 
*	Removed \r and \t, tags, leading whitespaces, empty lines from the HTML code
*	Selected only relevant data from cleaned HTML code 
*	Converted all unreadable characters to readable ones using encoding ="utf8" 
*	Added scores to suitable columns 
*	Exported file as csv for further analytics 

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/ahnngo/analyzing_vietnamese_graduation_score_2020/blob/main/Charts/The%20numbers%20of%20student%20participating%20in%20each%20exam.png)
![alt text](https://github.com/ahnngo/analyzing_vietnamese_graduation_score_2020/blob/main/Charts/Percentage%20of%20exam%20combination%20taken%20by%20students.png)
![alt text](https://github.com/ahnngo/analyzing_vietnamese_graduation_score_2020/blob/main/Charts/Mandatory%20Meanscore.png)
![alt text](https://github.com/ahnngo/analyzing_vietnamese_graduation_score_2020/blob/main/Charts/Most%20Popular%20First%20Name.png)

