import pymongo
#mongodb client
db=pymongo.MongoClient("mongodb://localhost:27017/")
studdb=db.school
studcol=studdb.student

c=1
while(c==1):
    print("select the option")
    print("1:insert data")
    print("2:display data")
    print("3:update data")
    print("4:delete data")
    i=int(input("Enter here :--> "))    
    #insert data
    if(i==1):
        r=int(input("Enter roll no"))
        n=input("Enter name")
        a=int(input("Enter age"))
        mydata={"roll":r,"name":n,"age":a}
        studcol.insert_one(mydata)
        print("One Reccord inserted")
    #display data
    elif(i==2):
        print("select the display option")
        print("1: from roll no----2:from name----3:from age 4:to display all reccords")
        op=int(input("Enter here --> "))
        if(op==1):
            rn=int(input("Enter roll no."))
            x=studcol.find_one({"roll":rn})
            print(x)
        elif(op==2):
            nm=input("Enter the name")
            x=studcol.find_one({"name":nm})
            print(x)
        elif(op==3):
            ag=int(input("Enter the age"))
            x=studcol.find_one({"age":ag})
            print(x)
        elif(op==4):
            x=studcol.find()
            for r in x:
                print(r)
    #delete data
    elif(i==4):
        print("select the delete option")
        print("1: from roll no----2:from name----3:from age")
        op=int(input("Enter here :--> "))
        if(op==1):
            rn=int(input("Enter roll no."))
            x=studcol.delete_one({"roll":rn})
            print("one reccord deleted")
        elif(op==2):
            nm=input("Enter the name")
            x=studcol.delete_one({"name":nm})
            print("one reccord deleted")
        elif(op==3):
            ag=int(input("Enter the age"))
            x=studcol.delete_one({"age":ag})
            print("one reccord deleted")
    #update data
    elif(i==3):
        print("select the update option")
        print("1: from roll no----2:from name----3:from age")
        op=int(input("Enter here :--> "))
        if(op==1):
            print("which data is to be update--")
            print("1:roll number")
            print("2:name")
            print("3:age")
            uc=int(input())
            if(uc==1):
                rn=int(input("Enter roll no."))
                nrn=int(input("Enter new roll no"))
                x=studcol.update_one({"roll":rn},{"$set":{"roll":nrn}})
                print("one reccord updated")
            elif(uc==2):
                rn=int(input("Enter roll no."))
                nrn=input("Enter new name")
                x=studcol.update_one({"roll":rn},{"$set":{"name":nrn}})
                print("one reccord updated")
            elif(uc==3):
                rn=int(input("Enter roll no."))
                nrn=int(input("Enter new age"))
                x=studcol.update_one({"roll":rn},{"$set":{"age":nrn}})
                print("one reccord updated")    
        elif(op==2):
            print("which data is to be update--")
            print("1:roll number")
            print("2:name")
            print("3:age")
            uc=int(input())
            if(uc==1):
                rn=input("Enter name")
                nrn=int(input("Enter new roll no"))
                x=studcol.update_one({"name":rn},{"$set":{"roll":nrn}})
                print("one reccord updated")
            elif(uc==2):
                rn=input("Enter name")
                nrn=input("Enter new name")
                x=studcol.update_one({"name":rn},{"$set":{"name":nrn}})
                print("one reccord updated")
            elif(uc==3):
                rn=input("Enter name")
                nrn=int(input("Enter new age"))
                x=studcol.update_one({"name":rn},{"$set":{"age":nrn}})
                print("one reccord updated")
        elif(op==3):
            print("which data is to be update--")
            print("1:roll number")
            print("2:name")
            print("3:age")
            uc=int(input())
            if(uc==1):
                rn=int(input("Enter age"))
                nrn=int(input("Enter new roll no"))
                x=studcol.update_one({"age":rn},{"$set":{"roll":nrn}})
                print("one reccord updated")
            elif(uc==2):
                rn=int(input("Enter age"))
                nrn=input("Enter new name")
                x=studcol.update_one({"age":rn},{"$set":{"name":nrn}})
                print("one reccord updated")
            elif(uc==3):
                rn=int(input("Enter age"))
                nrn=int(input("Enter new age"))
                x=studcol.update_one({"age":rn},{"$set":{"age":nrn}})
                print("one reccord updated")
        
    print("for continue press y")
    print("for exit press n")
    z=input("Enter here :--> ")
    if(z=='y'):
        c=1
    else:
        c=0
        
