from ast import For
from pickle import TRUE
print('HI!!!! user please set your login id or password......')
a=input('enter your username as login id:')
b=int(input('enter your password'))
print('you can access provide of two more people:')
c=input('Type yes or no')
l=[]
if c=='yes':
  for i in range(0,2):
    x=input(f'enter your {i+1} username as login id:')
    l.append(x)
    print(l)
  else:
    print('ok fine!! now process of authentication:')
else:
  for i in range(0,2):
    l.append('-')
print('!!!NOW authentication start!!!')

info={'name':[],'roll_no':[],'attendance':[],'date':[]}

def work():
  print('what do you want to do??')
  while True:
    print('1.For student information..' '2.For the marking attendence..'  '3.For view attendence file:'   '4.For generate file for attendence....' )
    
    y=int(input('type your choice!!!!'))
    match y:
      case 1:
        print('if you want to add a new student.. then type yes otherwise no!!')
        k=input()
        if k=='yes':
          global info
          print('How many students do you want to enter??')
          val=int(input())
          for i in range(val):
            info['name'].append(input('enter a name '))
            info['roll_no'].append(int(input('enter a int value for roll_no:')))
            print(info['name'])
            print(info['roll_no'])
        else:
          print(info)
        print('if you want to view a student record.. then type yes otherwise no!!')
        q=input()
        if q=='yes':
          print(info)
        print('if you want to update a student record.. then type yes otherwise no!!')
        h=input()
        if h=='yes':
          i=int(input('you want to update which student name:'))
          info['name'][i-1]=input('enter updated name:')
          i=int(input('you want to update which student roll_no:'))
          info['roll_no'][i-1]=int(input('enter updated roll_no:'))
          i=int(input('you want to update which student attendance:'))
          info['attendance'][i-1]=input('enter updated attendence')
          i=int(input('you want to update which student date:'))
          info['date'][i-1]=input('enter updated date in formate dd:mm:yy')
          print(info)
        print('if you want to delete a student record.. then type yes otherwise no!!')
        h=input()
        if h=='yes':
          i=int(input('you want to delete which student record:'))
          del info['name'][i-1]
          del info['roll_no'][i-1]
          del info['attendence'][i-1]
          del info['date'][i-1]
          print(info)
      case 2:
        # print('FOR marking Attendance!!!')
        print('if you want to mark attendance of a student.. then type yes otherwise no!!')
        h=input()
        if h=='yes':
          print('Attendance marking of the student who was added...then type yes otherwise no!!')
          h=input()
          if h=='yes':
            # global info
            print(' how many new students..')
            val=int(input())
            for i in range(val):
              info['attendance'].append(input('mark attendence... type p for present and a for apsent:'))
              info['date'].append(input('enter date in formate dd:mm:yy'))
            print(info)
          else:
            i=int(input('enter a student number:'))
            info['attendance'][i-1]=input('mark attendence')
            info['date'][i-1]=input('enter date in formate dd:mm:yy')
            print(info)
        else:
            print(info['attendance'])
            print(info['date'])
      case 4:
        # print('FOR generate file !!')
        present_attendance=[]
        for index,x in enumerate(info['attendance']):
          if x=='p':
            # print('present list')
            present_attendance.append(info['name'][index]+'\n')
        # present_attendance=list(filter(lambda x:x=='p',info['attendance']))
            f=open('myfile.txt','w')
            f.writelines(present_attendance)
            f.close()
      case 3:
        # print('For g')
        f=open('myfile.txt','r')
        text=f.readlines()
        print(text,end='  ')

        f.close()
      case _:
        break


# this part is a authentication

count=0
while True:
  count+=1
  p=input('please enter your login id....')
  q=int(input('enter password:'))
  if a==p and b==q :
    print('<<authentication successful>>')
    work()
    break
  if l[0]==p and b==q:
    print('<<authentication successful>>')
    work()
    break
  if l[1]==p and b==q:
    print('<<authentication successful>>')
    work()
    break
  else:
    print('sorry!! try again')
  if count==3:
    print('<<YOU CAN NOT ACCESS THIS SYSTEM>>')
    break