import json

def create():

    def writejson(data,filename="datastore1.json"):
        with open (filename,"w") as f:
            json.dump(data,f,indent=3)

    with open("datastore1.json") as jfile:
        data = json.load(jfile)
        temp=data["employee_details"]
        per = {}
        vem=input("enter employee name ")
        for i in range(len(temp)):
            if vem in temp[i]:
                print("already exists")
                break
        else:
            p = {}
            p["name"]=vem
            p["age"]=input("ENTER AGE")
            p["empid"]=input("ENTER EMPLOYEE ID")
            p["location"]=input("enter the location")
            per[vem] = p
            temp.append(per)
    writejson(data)

def read():
    f=open("datastore1.json","r")
    temp=json.load(f)

    flag=temp['employee_details']

    name_for_read=input("enter the name of employee").strip()
    for i in flag:
        if name_for_read in i.keys():
            print(i[name_for_read])
            break
    else:
        print("no such employee")


def delete():
    f = open("datastore1.json", "r")
    temp = json.load(f)

    flag = temp['employee_details']

    name_for_read = input("enter the name of employee").strip()
    for i in flag:
        b=i[name_for_read]
        if b in i.keys():
            del(b)

            print("employee details successfully deleted")
            break
    else:
        print("no such employee")
    with open("datastore1.json","w")as kfile:
        kfile.write(json.dumps(flag,indent=3))





while(True ):
    def switch(k):
        if k == "c" or k == "C":
            create()
        elif k == "r" or k == "R":
            read()
        elif k == "d" or k == "D":
            delete()
        else:
            print("NO SUCH OPERATION")



    cont = input("to start or continue the process give input as 1 to quit give 0")

    if cont=="1":
        pass
    else:
        quit()
    print("EMPLOYEE DETAILS "
              "c- TO CREATE NEW EMPLOYEE DETAILS"
              "r- TO READ ABOUT EMPLOYEE DETAILS"
              "d- TO DELETE EMPLOYEE DETAILS ")
    k = input().strip()
    switch(k)



