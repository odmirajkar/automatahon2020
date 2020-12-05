
data="The program has 4 Keynotes, 2 Panel discussions, 7 Hands on Labs, 26 Interactive session, 14 Lightning sessions"
data=data.replace(',','')
data_values=data.split(" ")
print(data_values)
value_dict={}
for ind,data in enumerate(data_values):
    print(ind,data)
    if "Lightning" == data:
        value_dict['Lightning Talks'] = data_values[ind-1]
    elif "Interactive" in data:
        value_dict['Interactive Sessions'] = data_values[ind-1]
    elif "Hands"  == data:
        value_dict['Labs/Workshop'] = data_values[ind-1]
    elif "Panel"  ==data:
        value_dict['Panel'] = data_values[ind - 1]     
    elif "Keynotes" == data:
        value_dict['Kaynotes']= data_values[ind-1]
    print(value_dict)    