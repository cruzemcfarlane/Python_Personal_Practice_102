month_days = [('January',[31]),('February',[28,29]),('March',[31]), ('April',[30]),('May',[31]),('June',[30]),('July',[31]),('August',[31]),
('September',[30]),('October',[31]),('November',[30]),('December',[31]) ]

day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def days_in_month(d):
    for x in range(0,len(month_days)):
        if month_days[x][0]==d:
            return month_days[x][1]

def day_of_week(d,m,y):
    if m==1 or m==2:
        m+=12
        y-=1
        day = (((13*m+3) / 5 + d + y + (y / 4) - (y / 100) + (y / 400)) %7)
        return day_names[day]
    else:
        day = (((13*m+3) / 5 + d + y + (y / 4) - (y / 100) + (y / 400)) %7)
        return day_names[day]

def unlucky(y):
    return [(d,m,y) for d in range(1,14) for m in range(1,13) if (day_of_week(d,m,y)=="Friday" and d==13)]

def mostUnlucky():
    for i in range(0,2011):
        if len(unlucky(i))>2:
            print unlucky(i)
