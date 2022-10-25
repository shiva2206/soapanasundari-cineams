import pandas as pd
import PySimpleGUI as sg
def  dataframe_condition(dataframe,column,value): #user defined function for creating a dataframe which satisfies a single condition(entire column) specified
    condition=dataframe[column]==value
    dataframe1=dataframe[condition]
    return (dataframe1)
def unique_value(dataframe,column):
    lst=[] 
    for var in dataframe[column]:
        if var not in lst:
            lst=lst+[var]
        elif var in lst:
            lst=lst
    return(lst)
tlist=[]
movie_refreshment=pd.read_csv('movie refreshments type.csv')
print(len(movie_refreshment))
unique_types=unique_value(movie_refreshment,'type')
text_layout=[]
image_layout=[]
button_layout=[]
for i in range(len(unique_types)):
    text_layout.append(sg.T(unique_types[i]))
    image_layout.append(sg.Image(unique_types[i]))
    button_layout.append(sg.B('ORDER NOW',key='t1b'+str(i)))
layot1=[text_layout,
                image_layout,
                 button_layout]
windw1=sg.Window('Order Refreshments',layot1)
variable1=1
while variable1==1:
    event,values=windw1.read()
    for i in range(len(unique_types)):
        key='t1b'+str(i)
        if event==sg.WIN_CLOSED or event=='BACK':
                variable1=0
                windw1.close()
        elif event==key:
            itemdf=movie_refreshment[movie_refreshment['type']==unique_types[int(key[-1])]].reset_index(drop=True)
            print(itemdf)
            serialno=[]
            refreshment=[]
            cost=[]
            add=[]
            for var2 in range(len(itemdf['refreshment'])):
                print((itemdf['refreshment'][var2]))
                refreshment=refreshment+[[]]
                refreshment[var2].append(sg.T(itemdf['refreshment'][var2]))
                cost=cost+[[]]
                cost[var2].append(sg.T(itemdf['cost'][var2]))
                add=add+[[]]
                add[var2].append(sg.B('ADD',key='w2b'+str(var2)))
            layot2=[refreshment,cost,add]
            windw2=sg.Window(unique_types[int(key[-1])],add)
            variable2=1
            while variable2==1:
                event,values=windw2.read()
                if event==sg.WIN_CLOSED:
                    variable2=0
                    windw2.close()
                    
                    


