import requests as req
import json

handle=input("Enter handle : ")
count=input("Enter the number of submissions : ")


r1=req.get("https://codeforces.com/api/user.status?handle="+handle+"&from=1&count="+count)

data=json.loads(r1.text)


cnt=0
sum=0
if(data["status"]!="OK"):
    print("Something went wrong")
    exit()

count=int(len(data["result"]))

for i in range(count):
    #print(data["result"][i]["problem"]["rating"])
    if(data["result"][i]["verdict"]=="OK"):
        print(cnt+1," name : ",data["result"][i]["problem"]["name"])
        try:
            sum+=int(data["result"][i]["problem"]["rating"])
        except KeyError:
            cnt=cnt-1
        cnt=cnt+1
print("Total no. of submissions : ",count)
print("Sum :",sum)
print("Average ratings of solved problems : ",(sum/cnt))
print("No. of problems solved : ",cnt)
