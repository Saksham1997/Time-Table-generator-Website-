# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:27:23 2017

@author: sakshamsinghal
"""

from bs4 import BeautifulSoup
time="""
<table class="table table-responsive">
    <tr>
      <td>Time</td>
      <td>08:00-08:50</td>
      <td>08:50-09:40</td>
      <td>09:45-10:35</td>
	  <td>10:40-11:30</td>
	  <td>11:35-12:25</td>
	
    </tr>
    <tr>
      <td>Hour/Day Order</td>
      <td>M</td>
      <td>BD</td>
      <td>DW</td>
	  <td>W</td>
	  <td>M</td>
	
    </tr>

  <tbody>
    <tr>
      <td scope="row">Day1</td>
      <td>M</td>
      <td>BD</td>
      <td>W</td>
	  <td>DW</td>
	  <td>W</td>
	 
	  
    </tr>
    <tr>
      <td scope="row">Day2</td>
      <td>DW</td>
	  <td>BD</td>
	  <td>W</td>
	  <td>M</td>
	  <td>M</td>
	
    </tr>
    
	<tr>
      <td scope="row">Day3</td>
      <td>M</td>
	  <td>W</td>
	  <td>BD</td>
	  <td>DW</td>
	  <td>W</td>
	
    </tr>
	<tr>
      <td scope="row">Day4</td>
      <td>BD</td>
	  <td>BD</td>
	  <td>W</td>
	  <td>M</td>
	  <td>DW</td>
	
	
    </tr>
	<tr>
      <td scope="row">Day5</td>
      <td>M</td>
	  <td>W</td>
	  <td>BD</td>
	  <td>W</td>
	  <td>DW</td>
	 
    </tr>
  </tbody>
 </table>"""

teacher="""
<html>
<body>
<table >
<th>
<td>Name</td>
<td>Subject</td>
<td>Code</td>
</th>
<tr>
<td>Sunderesan</td>
<td>Maths</td>
<td>M</td>
</tr>
<tr>
<td>Sindhu</td>
<td>Big Data</td>
<td>BD</td>
</tr>
<tr>
<td>Margatham</td>
<td>Data Warehouse</td>
<td>DW</td>
</tr>
<tr>
<td>Metilda</td>
<td>Wst</td>
<td>W</td>
</tr>
</table>
</body>
</html>"""

#extract data from teacherlist site
teachers = []
tl = open('teacherlist.html','r')
souptest=tl.read()
souptest = BeautifulSoup(souptest,"lxml")
table = souptest.find('table')
#table_body = table.find('tbody')


rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    teachers.append([ele for ele in cols if ele])
print(teachers)

#extract data from time table
period = []
timet = open('tt.html','r')
soup_time=timet.read()
soup_time = BeautifulSoup(soup_time,"lxml")
table = soup_time.find('table')

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    period.append([ele for ele in cols if ele])
print(period)
temp=period

#loop to replace
for index, item in enumerate(temp):
    for no,a in enumerate(item):
        if(a=="M"):
            temp[index][no]="sunder"
        elif(a=="BD"):
            temp[index][no]="sindhu"
        elif(a=="DW"):
            temp[index][no]="margatham"
        elif(a=="W"):
            temp[index][no]="metilda"
print(temp)
#code to create html file
import webbrowser
f = open('timetablef.html','w')
message="""<html>
<body>
<table>
"""
f.write(message)

for a in temp:
    message="""<tr>"""
    f.write(message)
    for b in a:
        message="""<td>"""
        f.write(message)
        f.write(b)
        message="""</td>"""
        f.write(message)
    message="""</tr>"""
    f.write(message)

message="""</table>
</body>
</html>"""
f.write(message)
f.close()
webbrowser.open_new_tab('timetablef.html')
