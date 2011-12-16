
def get_item(select):
	data=open("items.txt","r").readlines()
	tolist=0
	item=[]
	for row in data:
		if row[0]=="#":
			tolist=0
			key = row.split("#")
			if select[0]==key[1] and select[1]==key[2]:
				tolist=1
		if tolist==1 and row[0]!="#":
			l=[]
			for i in range(4):
				l.append(row[i].replace("0"," "))
			item.append(l)
	return item
