class date:
     def__init__(self,a,b,c):
         self.d=a
    self.m=b
    self.y=c
     def day(self):
        print("day=",self.d)
    def month(self):
        print("month=",self.m)
    def year(self): 
        print("yaer=",self.y)
    def monthName(self):
        month=["unknown","jan","feb","mar","apri","may","jun","jul","aug","sep","oct","nov","dec"]
        print("monthName:",month[self.m])
    def isLeapyear(self):
        if(self.y%400==0)and(self.y%100==0):
            print("It is a leap year")
    if(self.y%4==0)and(self.y%100!=0):
           print("It is a leap year")
    else:
           print("It is  not a leap year")
d1.date(3,8,2000)
d1.day()
d1.month()
d1.year()
d1.monthName()
d1.isLeapyear()
            
