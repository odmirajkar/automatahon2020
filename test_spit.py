
data="The program has 4 Keynotes, 2 Panel discussions, 7 Hands on Labs, 26 Interactive session, 14 Lightning sessions"
data=data.replace(',','')
data_values=data.split(" ")
print(data_values)
value_dict={}
for ind,data in enumerate(data_values):
    print(ind,data)
    if "Lightning" == data:
        value_dict['Lightning Talks'] = data[ind-1]
    elif "Interactive" in data:
        value_dict['Interactive Sessions'] = data[ind-1]
    elif "Hands" in data:
        value_dict['Labs/Workshop'] = data[ind-1]
    elif "Panel" in data:
        value_dict['Panel'] = data[ind - 1]     
    elif "Keynotes" == data:
        value_dict['Kaynotes']=data[ind -1]
    print(value_dict)    