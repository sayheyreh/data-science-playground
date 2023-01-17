import pandas as pd
import matplotlib.pyplot as plt
from seaborn import boxplot,scatterplot,lmplot

df = pd.read_excel("data.xlsx")

males = df[df['gender']=='M']['total']
females =  df[df['gender']=='F']['total']


# boxplot(y=df['gender'],x=df['total'],palette="Blues")
# plt.title("Total scores with genders")
# # plt.show()

# scatterplot(df,y=df['audience'],x=df['judge'],)
# lmplot(data=df,y='audience',x='judge')
# plt.title("Audience vs Judge Score")
# plt.show()

# samp1=pd.DataFrame()
# samp2=pd.DataFrame()
# samp1['score'] = df['audience']
# samp1['gender'] = df['gender']
# samp1['type'] = 'audience'

# samp2['score']=df['judge']
# samp2['gender']=df['gender']
# samp2['type']='judge'


# s = pd.concat([samp1,samp2])
# s.drop(s[(s['gender'] == 'M+M')].index,inplace=True)
# s.drop(s[(s['gender'] == 'M+F')].index,inplace=True)
# s.drop(s[(s['gender'] == 'F+F')].index,inplace=True)

# boxplot(data=s,y=s['score'],x=s['type'], hue=s['gender'],palette="Blues")
# plt.title("Comparitively Judge vs Audience scores gender-wise")
# plt.show()

# boxplot(data=df, y=df['total'], x=df[''])
# plt.show()