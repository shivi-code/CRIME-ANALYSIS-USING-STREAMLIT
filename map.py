import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium
import base64

data_url=('C:\\Users\\dell\\crimeproject\\crime.csv')
data=pd.read_csv(data_url)

st.markdown("<h1 style='text-align:left; color:Black;'><u><b>Crime Insights Of Delhi</b></u></h1>",unsafe_allow_html=True)
st.markdown("<h4 style='text-align:left; color:Brown;'>This application exploits Data analytics techniques to give useful insights to people so that they can be safe and have information about unknown areas they have to visit...</h4>",unsafe_allow_html=True)
st.sidebar.title("Select Area and type of visualisation you want")
#st.sidebar.title("<h4 style='text-align:left; color:#696969;'>Select Area and type of visualisation you want</h4>",unsafe_allow_html=True)

select = st.sidebar.selectbox('Area', ['NONE','EAST', 'GRP(RLY)', 'IGI AIRPORT', 'NEW DELHI', 'NORTH',
       'NORTH EAST', 'NORTH WEST', 'SOUTH', 'SOUTH WEST', 'CENTRAL',
       'hazrat nizamuddin railway station', 'WEST', 'OUTER', 'CAW',
       'SOUTH EAST', 'Chandni chowk metro station'])
st.sidebar.write('You selected: ',select)
vis=st.sidebar.selectbox('Select Type of visualization you want',['NONE','Linear Representation','Bar Graph','Pie Chart','Map Visualization'])
st.sidebar.write('You chose: ',vis)

# background-color:#FFCDC8;
 # background-color:LEMONCHIFFON;
 # background-color:KHAKI;
  # background-color:DARKKHAKI;  GOOD

  # background-color:WHEAT;

#st.markdown("""
#<style>
#body{

 #       background-color:;

#</style>
#""", unsafe_allow_html=True)

def get_base64_of_bin_file(bin_file):
    with open(bin_file,'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
        background-image: url("data:/png;base64,%s");
        background-size: cover;
        }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img,unsafe_allow_html=True)
    return
set_png_as_page_bg('dk.png')











side_bg = "ss.jpg"
side_bg_ext = "jpg"
st.markdown(
    f"""
<style>
.sidebar .sidebar-content {{
   background: url(data:{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()}) 
    
    }}
background-size:cover;
    
</style>

    
""",unsafe_allow_html=True)



group=data.groupby('DISTRICT',as_index=False)
def search_group(selected,group_):
    if select=='NONE':
        return
    for g, item in group_:
        temp=group.get_group(g)
        if g==selected:
            return temp

def line_plot(temp_):
    plot1 = plt.figure(1)
    plt.plot(temp_["YEAR"],temp_["MURDER"],label="MURDER",color="r")
    plt.scatter(temp_["YEAR"],temp_["MURDER"])
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    st.write("The graph below shows a LINEAR REPRESENTATION OF VARIOUS CRIMES IN THE AREA: ",select)
    st.pyplot()
    plot2 = plt.figure(2)
    plt.plot(temp_["YEAR"],temp_["ATTEMPT TO MURDER"],label="ATTEMPT TO MURDER",color="blue")
    plt.scatter(temp_["YEAR"],temp_["ATTEMPT TO MURDER"])
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    st.pyplot()
    plot3 = plt.figure(3)
    plt.plot(temp_["YEAR"],temp_["RAPE"],label="RAPE",color="magenta")
    plt.scatter(temp_["YEAR"],temp_["RAPE"])
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    st.pyplot()
    plot4 = plt.figure(4)
    plt.plot(temp_["YEAR"],temp_["KIDNAPPING & ABDUCTION"],label="KIDNAPPING & ABDUCTION",color="green")
    plt.scatter(temp_["YEAR"],temp_["KIDNAPPING & ABDUCTION"])
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    st.pyplot()
    plot5 = plt.figure(5)
    plt.plot(temp_["YEAR"],temp_["DACOITY"],label="DACOITY",color="orange")
    plt.scatter(temp_["YEAR"],temp_["DACOITY"])
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    st.pyplot()
    plot6 = plt.figure(6)
    plt.plot(temp_["YEAR"],temp_["ROBBERY"],label="ROBBERY",color="pink")
    plt.scatter(temp_["YEAR"],temp_["ROBBERY"])
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    st.pyplot()
    plot7 = plt.figure(7)
    plt.plot(temp_["YEAR"],temp_["ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY"],label="assault on women",color="purple")
    plt.scatter(temp_["YEAR"],temp_["ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY"])
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    st.pyplot()
    plot8 = plt.figure(8)
    plt.plot(temp_["YEAR"],temp_["ARSON"],label="ARSON",color="black")
    plt.scatter(temp_["YEAR"],temp_["ARSON"])
    #plt.title(g)
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    #plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

def bar_plot(temp_):
    temp= temp_.set_index('YEAR')
    #plt.bar(temp["YEAR"],temp["MURDER"],label="MURDER")
    tem=temp
    tem.drop(["latitude","long"],axis=1,inplace=True)
    tem.plot(kind='bar', stacked=True, rot=0, figsize=(10,6), legend=False, zorder=3)
    plt.grid(zorder=0)
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    st.write("The graph below shows a BAR PLOT REPRESENTATION OF VARIOUS CRIMES IN THE AREA: ",select)
    st.pyplot()

def pie_chart(temp_):
    t=temp_[["MURDER","ATTEMPT TO MURDER","RAPE","KIDNAPPING & ABDUCTION","DACOITY","ROBBERY","ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY","ARSON"]].aggregate(np.mean)
    t.plot(kind='pie', subplots=True, figsize=(8, 8))
    plt.ylabel("")
    st.write("The graph below shows a PIE CHART REPRESENTATION of various crimes in the area: ",select.upper()," based on average crime(category) per year ")
    st.pyplot()





obj=search_group(select,group)

if obj is not None:
    obj.reset_index(drop=True,inplace=True)
if vis=='Linear Representation':
    line_plot(obj)
elif vis== 'Bar Graph':
    bar_plot(obj)
elif vis=='Pie Chart':
    pie_chart(obj)
elif vis == 'Map Visualization':
    temp=obj[["MURDER","ATTEMPT TO MURDER","RAPE","KIDNAPPING & ABDUCTION","DACOITY","ROBBERY","ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY","ARSON"]].aggregate(np.mean)
    for i in range(len(obj["YEAR"])):
        loc=[]
        loc.append(obj.loc[i,"latitude"])
        loc.append(obj.loc[i,"long"])
    m = folium.Map(location=loc, zoom_start=16)
    value="{0:.2f}".format(np.mean(temp))

    if np.mean(temp)>2 and np.mean(temp)<50:
        folium.Marker(location=loc,popup='MODERATELY UNSAFE ZONE'+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='blue',icon='none')).add_to(m)
    elif np.mean(temp)>0 and np.mean(temp)<2:
        folium.Marker(location=loc,popup='SAFE'+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='green',icon='none')).add_to(m)
    else:
        folium.Marker(location=loc,popup='DANGEROUS ZONE'+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='red',icon='none')).add_to(m)
    folium_static(m)
    



#https://colab.research.google.com/drive/1h1UZlhtGf74iO3keDilKmNEbvRrUemd4#scrollTo=c7CGcqriIfj2
#CORRECT FILE TO USE
