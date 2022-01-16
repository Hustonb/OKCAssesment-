import csv, math
shotsfile=open('shots_data.csv')
data=shotsfile.readlines()
rows=data[1:]
length=len(rows)

#preallocate here
totalshots=0
twoptshots=0
twoptmakes=0
cornerthrees=0
cornermakes=0
otherthrees=0
otherthreemakes=0
#do the shot distribution for team A first:
for i in range(length):
     temprow=rows[i-1]
     temprow = temprow.split(",")
     if temprow[0] == 'Team A':
        totalshots=totalshots+1
        #determine the type of shot, start by allocating x and y
        x=float(temprow[1])
        y=float(temprow[2])
        #decision structure to determine type of shot:
        if abs(x)>22 and y<=7.8:
            #print("Corner three")
            cornerthrees=cornerthrees+1
            if temprow[3] == '1\n':
                cornermakes=cornermakes+1
        elif math.sqrt((x*x)+(y*y)) > 23.75:
            otherthrees=otherthrees+1
            #print('NC3')
            if temprow[3] == '1\n':
                otherthreemakes=otherthreemakes+1
        else:
            twoptshots=twoptshots+1
            #print('2 pointer')
            if temprow[3] == '1\n':
                twoptmakes=twoptmakes+1

print('The following shot distribution and efg values are for team A:')
print('\n')
#now calculate the shot distributions:
print("Shot distribution in the order: 2, NC3, C3")
twoptpercent=(twoptshots/totalshots)*100
print(twoptpercent)

NC3percent=(otherthrees/totalshots)*100
print(NC3percent)

C3percent=(cornerthrees/totalshots)*100
print(C3percent)

#Now find the efg from each zone:
print('\n')
print("efg% by zone in the order: 2, NC3, C3")
twoptefg=(twoptmakes/twoptshots)*100
print(twoptefg)

NC3efg=((otherthreemakes+(.5*otherthreemakes))/otherthrees)*100
print(NC3efg)

C3efg=((cornermakes+(.5*cornermakes))/cornerthrees)*100
print(C3efg)
print('\n')

#now do the shot dist for B:
totalshots=0
twoptshots=0
twoptmakes=0
cornerthrees=0
cornermakes=0
otherthrees=0
otherthreemakes=0

for i in range(length):
     temprow=rows[i-1]
     temprow = temprow.split(",")
     if temprow[0] == 'Team B':
        totalshots=totalshots+1
        #determine the type of shot, start by allocating x and y
        x=float(temprow[1])
        y=float(temprow[2])
        #decision structure to determine type of shot:
        if abs(x)>22 and y<=7.8:
            #print("Corner three")
            cornerthrees=cornerthrees+1
            if temprow[3] == '1\n':
                cornermakes=cornermakes+1
        elif math.sqrt((x*x)+(y*y)) > 23.75:
            otherthrees=otherthrees+1
            #print('NC3')
            if temprow[3] == '1\n':
                otherthreemakes=otherthreemakes+1
        else:
            twoptshots=twoptshots+1
            #print('2 pointer')
            if temprow[3] == '1\n':
                twoptmakes=twoptmakes+1

print('The following shot distribution and efg values are for team B:')
print('\n')
#now calculate the shot distributions:
print("Shot distribution in the order: 2, NC3, C3")
twoptpercent=(twoptshots/totalshots)*100
print(twoptpercent)

NC3percent=(otherthrees/totalshots)*100
print(NC3percent)

C3percent=(cornerthrees/totalshots)*100
print(C3percent)

#Now find the efg from each zone:
print('\n')
print("efg% by zone in the order: 2, NC3, C3")
twoptefg=(twoptmakes/twoptshots)*100
print(twoptefg)

NC3efg=((otherthreemakes+(.5*otherthreemakes))/otherthrees)*100
print(NC3efg)

C3efg=((cornermakes+(.5*cornermakes))/cornerthrees)*100
print(C3efg)

shotsfile.close()