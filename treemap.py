#import relevant packages 
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt        
import squarify 

#read csv file 
df = pd.read_csv("rankOrder.csv")

#remove commas 
df["Deaths"] = df["Deaths"].str.replace(",","").astype(float)

#sort values in ascending order 
df = df.sort_values(by="Deaths", ascending= False)

#rename column 
df.columns = df.columns.str.replace('Cause of death','Cause')

#drop unnecessary rows and columns, specifically unnamed ones
df= df.drop(index= [12], columns= ['Unnamed: 0', 'Unnamed: 4', 'Unnamed: 3'])

#specify color 
cmap = matplotlib.cm.coolwarm

#specify minimum and maximum values 
mini = min(df["Deaths"])
maxi = max(df["Deaths"])
norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in df["Deaths"]]

#plot using squarify 
squarify.plot(sizes=df["Deaths"], label=df["Cause"], alpha = 1.0, color = colors)

#remove axes on graph 
plt.axis('off')

#adjust font sizes 
plt.rc('font', size= 6)         
plt.rc('axes', labelsize= 6)     


#insert graph title 
plt.title("Causes of Death in 2016", fontsize= 12)

#show graph 
plt.show()

