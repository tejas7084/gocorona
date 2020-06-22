from django.shortcuts import render
####################################################
import time
import pandas as pd
from plotly.io._renderers import config
import plotly
import plotly.express as px
import pandas as pd
px.set_mapbox_access_token('pk.eyJ1IjoicnV0dmlrMTEwIiwiYSI6ImNrYjFxdzFlejBhNTQycnBqdnIwdzM3Z3MifQ.s2C2zDlwgvFwqxRNqdSKXg')
import  requests
from bs4 import BeautifulSoup as soup
import csv
import numpy as np
from plotly.offline import plot
#################india data scrapping code start ####################

my_url='https://www.mygov.in/covid-19'

data=requests.get(my_url).text
soup_page=soup(data,'html.parser')
state_container=soup_page.find('div',class_='state_record').findAll('tr')
state_container.remove(state_container[0])
statewise_list=[]
csv_file = open('coronaapp/corona info.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['State name', 'Confirmed', 'Active', 'Recovered', 'Deaths', 'Lat', 'Long'])
for i,row in enumerate(state_container):
        list1 = state_container[i].text.split('\n')
        a, *list_of_info, b = list1
        statewise_list.append(list_of_info)



for lists in statewise_list:
        state_name=lists[0]
        Confirmed=lists[1]
        Active=lists[2]
        Recovered=lists[3]
        Deaths=lists[4]

        csv_writer.writerow([state_name,Confirmed,Active,Recovered,Deaths])

csv_file.close()


########india data scrapping code finish##############

#########code for plotting india covid-19 scatter map start###################
def place_value(number):
    return ("{:,}".format(number))

india = pd.read_csv("coronaapp/corona info.csv")
lat_long = pd.read_excel("coronaapp/india.xls")
Lats=lat_long['Lat']
Longs=lat_long['Long']
table_state=india['State name']


table_confirmed=india['Confirmed']
table_confirmed2=[]
for number in table_confirmed:

        table_confirmed2.append("{:,}".format(number))


table_active=india['Active']
table_active2=[]
for number in table_active:

        table_active2.append("{:,}".format(number))


table_recovered=india['Recovered']
table_recovered2=[]
for number in table_recovered:

        table_recovered2.append("{:,}".format(number))


table_deaths=india['Deaths']
table_deaths2=[]
for number in table_deaths:

        table_deaths2.append("{:,}".format(number))


import plotly.express as px


px.set_mapbox_access_token('pk.eyJ1IjoicnV0dmlrMTEwIiwiYSI6ImNrYjFxdzFlejBhNTQycnBqdnIwdzM3Z3MifQ.s2C2zDlwgvFwqxRNqdSKXg')

fig = px.scatter_mapbox(
    india, lat=Lats, lon=Longs,
    size='Confirmed',size_max=100,hover_name="State name",
    template="plotly_dark",
    hover_data={'Lat':False,'Long':False,

                'Active_cases':india['Active'],
                'Recovered_cases':india['Recovered'],
                'Deathss':india['Deaths']
                 },

    color_discrete_sequence=['#20B7EF'], zoom=3.5, height=600
            )

##Adding buttons









fig.update_layout(
    title_text = '2016 Presidential Election',
    geo_scope='asia', # limite map scope to USA
    hoverlabel=dict(


    )

)
fig.update_layout(mapbox_style="dark")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#########finish of plotting map code for india covid-19 ##############

############start of indias line chart of covid cases from jan2020##############
import pandas as pd
import csv
import plotly.express as px


data=pd.read_csv('coronaapp/india total covid cases from start.csv')
Date=pd.to_datetime(data['Date'])
TC=data['Total confirmed cases of COVID-19 (cases)']
data1 = dict(
    Date=Date,
    Total_cases=TC)
fig1 = (px.line(data1,x='Date',y='Total_cases',
template="plotly_dark",height=550,


            #hover_name=False,
               line_shape='spline',
            hover_data=dict(


            ))
         )
'''.update_traces(mode='lines+markers')'''
fig1.update_layout(
#plot_bgcolor='black'
)
fig1.update_xaxes(
showticklabels=True,
    title=None,

)
fig1.update_yaxes(
showticklabels=True,
    title=None,

)
fig1.update_layout(mapbox_style="seaborn")
fig1.update_traces(line_color='#007bff')
fig1.update_layout(margin={"r":10,"t":0,"l":0,"b":0})

#############finish of indias line chart of covid cases############
###########start of indias daily number of covid cases########
data=pd.read_csv('coronaapp/indias daily number of confirmed covid cases.csv')
Date=pd.to_datetime(data['Date'])
TC=data['Daily confirmed cases (cases)']
data1 = dict(
    Date=Date,
    Total_cases=TC)
fig2 = (px.line(data1,x='Date',y='Total_cases',template="plotly_dark",
height=250,


            #hover_name=False,
               line_shape='spline',
            hover_data=dict(


            ))
         )
'''.update_traces(mode='lines+markers')'''
fig2.update_traces(line_color='#1CDFDF')
fig2.update_layout(

)
fig2.update_xaxes(
showticklabels=True,
    title=None,

)
fig2.update_yaxes(
showticklabels=True,
    title=None,

)
fig2.update_layout(margin={"r":10,"t":0,"l":0,"b":0})

#############finish of indias daily number of covid cases line chart################

##############start of indias daily number of covid deaths line  chart#################
data=pd.read_csv('coronaapp/indias daily number of covid deaths.csv')
Date=pd.to_datetime(data['Date'])
TC=data['Daily confirmed deaths (deaths)']
data1 = dict(
    Date=Date,
    Total_cases=TC)
fig3 = (px.line(data1,x='Date',y='Total_cases',template="plotly_dark",
                height=250,



            #hover_name=False,
               line_shape='spline',
            hover_data=dict(


            ))
         )
'''.update_traces(mode='lines+markers')'''
fig3.update_traces(line_color='#F53849')
fig3.update_layout(

)
fig3.update_xaxes(
showticklabels=True,
    title=None,

)
fig3.update_yaxes(
showticklabels=True,
    title=None,

)
fig3.update_layout(margin={"r":10,"t":0,"l":0,"b":0})
###############finish of indias daily number of covid deaths line chart########################

def dashboard(request):
        global fig,table,india_active_cases,india_total_cases
        india = pd.read_csv("coronaapp/corona info.csv")
        lat_long = pd.read_excel("coronaapp/india.xls")
        Lats = lat_long['Lat']
        Longs = lat_long['Long']
        table_state = india['State name']
        table_confirmed = india['Confirmed']
        table_active = india['Active']
        table_recovered = india['Recovered']
        table_deaths = india['Deaths']
        table = zip(table_state, table_confirmed2, table_active2, table_recovered2, table_deaths2)
        print(india_deaths)
        plt_div=plot(fig,output_type='div',include_plotlyjs=False)
        line_chart = plot(fig1, output_type='div', include_plotlyjs=False)
        daily_cases_chart = plot(fig2, output_type='div', include_plotlyjs=False)
        daily_deaths_chart = plot(fig3, output_type='div', include_plotlyjs=False)
        context={'total_deaths_cases':india_deaths,'total_recovered_cases':india_recoveries,'total_confirmed_cases':india_total_cases,'total_active_cases':india_active_cases,'deaths':table_deaths,'recovered':table_recovered,'active':table_active,'confirmed':table_confirmed,'state':table_state,'table':table,'plot':plt_div,'line_chart':line_chart,'daily_cases_chart':daily_cases_chart,'daily_deaths_chart':daily_deaths_chart}

        return render(request,'coronaapp/dashboard.html',context)


##################start of world map############
my_url='https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid19-container'

data=requests.get(my_url).text
soup_page=soup(data,'html.parser')
country_table=soup_page.find('div',class_='mw-parser-output').find('tbody').findAll('tr')
csv_file=open('coronaapp/Mapdatas.csv','w',newline='')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Country','Cases','Deaths','Recovery'])
row_list=[]

for row in country_table[2:230]:

    row_list.append(row.text.split('\n'))
row_list.sort()
for row in row_list:

    for element in row:

        if element!=str:
            row.remove(element)
row_list.remove(row_list[214])
row_list.remove(row_list[93])
row_list.remove(row_list[63])
row_list.remove(row_list[42])
row_list.remove(row_list[47])
row_list.remove(row_list[56])




for row in row_list[:]:
    for element in row[1:4]:
        lists_element=list(element)
        if ',' in lists_element:
            while ',' in lists_element:
                lists_element.remove(',')
                num=''.join(lists_element)
            try:
                row[row.index(element)] = int(num)
            except  Exception as e:
                try:
                    row[row.index(element)]=0
                except ValueError:
                    row[row.index(element)]=0
        else:
            try:
                row[row.index(element)] = int(element)

            except  Exception as e:
                try:
                    row[row.index(element)]=0
                except ValueError:
                    row[row.index(element)]=0




for row in row_list:

        country_name=row[0]
        tc=row[1]
        Deaths=row[2]
        recovered=row[3]
        csv_writer.writerow([country_name,tc,Deaths,recovered])

csv_file.close()
case_data = pd.read_csv("coronaapp/Mapdatas.csv",encoding='latin-1')
ll= pd.read_csv("coronaapp/ll.csv",encoding='latin-1')
Lats=ll['Lat']
Longs=ll['Long']
country=case_data['Country']


Cases=case_data['Cases']
Cases2=[]
for number in Cases:

        Cases2.append("{:,}".format(number))


Deaths_per_country=case_data['Deaths']
Deaths_per_country2=[]
for number in Deaths_per_country:

        Deaths_per_country2.append("{:,}".format(number))


Recoveries=case_data['Recovery']
Recoveries2=[]
for number in Recoveries:

        Recoveries2.append("{:,}".format(number))


country_table=zip(country,Cases,Deaths_per_country,Recoveries)
india_total_cases=place_value(Cases[94])
india_active_cases=place_value(Cases[94]-Deaths_per_country[94]-Recoveries[94])
india_recoveries=place_value(Recoveries[94])
india_deaths=place_value(Deaths_per_country[94])

import plotly.express as px


px.set_mapbox_access_token('pk.eyJ1IjoicnV0dmlrMTEwIiwiYSI6ImNrYjFxdzFlejBhNTQycnBqdnIwdzM3Z3MifQ.s2C2zDlwgvFwqxRNqdSKXg')

fig4 = px.scatter_mapbox(


    case_data, lat=Lats, lon=Longs,


    size='Cases',size_max=100,hover_name="Country",
    hover_data={



                'Recovered_cases':case_data['Recovery'],
                'Deaths num':case_data['Deaths']
                 },



                color_discrete_sequence=['#20B7EF'], zoom=1, height=600,

#blugrn', 'bluyl', 'brbg','''


            )

##Adding buttons









fig4.update_layout(

    showlegend=True,
    hidesources=True,
    title_text = '2016 Presidential Election',
    geo_scope='world', # limite map scope to USA
    hoverlabel=dict(


    ),


)
fig4.update_layout(mapbox_style="dark")
fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#################finish of world map##########################
def globe(request):
    case_data = pd.read_csv("coronaapp/Mapdatas.csv", encoding='latin-1')
    ll = pd.read_csv("coronaapp/ll.csv", encoding='latin-1')
    Lats = ll['Lat']
    Longs = ll['Long']
    country = case_data['Country']
    Cases = case_data['Cases']
    Deaths_per_country = case_data['Deaths']
    Recoveries = case_data['Recovery']
    country_table = zip(country, Cases2, Deaths_per_country2, Recoveries2)


    plt_div = plot(fig4, output_type='div', include_plotlyjs=False)
    context={'table':country_table,'plot':plt_div}
    return render(request,'coronaapp/globe.html',context)

################end of view for globe page##########


##########start of view of facts page###############
def about_us(request):
    context={}
    return render(request,'coronaapp/aboutus.html',context)



def facts_page(request):
    return render(request, 'coronaapp/factspage.html')
