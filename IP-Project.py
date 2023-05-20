import pandas as pd
import numpy as np
import sqlalchemy
import matplotlib.pyplot as pl
import getpass
import stdiomask

csv_file="F:\github projects\CSV-File.csv"

#purpose: To clear output screen
def clear():
    for x in range(10):
        print()

#purpose: To print end line after each program gets completed
def end():
    print('\n\n Press Enter to continue...')
    wait=input()

#purpose: To read CSV file and create DataFrame df
def read_csv_file():
    df=pd.read_csv(csv_file)
    print()
    print(df)
    print('\n\n Press Enter to continue...')

#purpose: To generate Data Analysis menu
def data_analysis():
    df=pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nDATA ANALYSIS MENU ')
        print('_'*115)
        print()
        print('1. Display Whole DataFrame\n')
        print('2. Display Columns\n')
        print('3. Show Top Rows\n')
        print('4. Show Bottom Rows\n')
        print('5. Show Specific Column\n')
        print('6. Display Datatype of each column\n')
        print('7. Display Transpose of Dataset\n')
        print('8. Add a New Record\n')
        print('9. Add a New Column\n')
        print('10. Delete a Column\n')
        print('11. Delete a Record\n')
        print('12. Display Records whose Loan is Approved\n')
        print('13. Display Records Proprty Area wise\n')
        print('14. Display Records Qualificatin wise\n')
        print('15. Show Data Summary\n')
        print('16. Exit (Back to Main Menu)\n')
        print('_'*115)
        print()
        ch=int(input('Enter your choice: '))
        if ch==1:
            print(df)
            end()
        elif ch==2:
            print(df.columns)
            end()
        elif ch==3:
            n = int(input('Enter number of rows you want to see :'))
            print(df.head(n))
            end()
        elif ch==4:
            n = int(input('Enter number of rows you want to see :'))
            print(df.tail(n))
            end()
        elif ch==5:
            print(df.columns)
            colname = input('Enter Column Name that You want to print : ')
            print(df[colname])
            end()
        elif ch==6:
            print(df.dtypes)
            end()
        elif ch==7:
            print(df.T)
            end()
        elif ch==8:
            a = input('Enter Loan ID :')
            b = input('Enter Gender(Male/Female) :')
            c = input('Enter Married Status (Yes/No) :')
            d = float(input('Enter Dependents :'))
            e = input('Enter Education Status(Graduate/Not Graduate)  :')
            f = input('Self Employed(Yes/No) :')
            g = float(input('Enter Applicant Income :'))
            h = float(input('Enter Coapplicant Income :'))
            i = float(input('Enter Loan Amount :'))
            j = float(input('Enter Loan Amount Terms :'))
            k = float(input('Enter Credit History :'))
            l = input('Enter Property Area(Rural/Semiurban/Urban) :')
            m = input('Enter Loan Status(Y/N) :')
            df.loc[len(df)]=[a,b,c,d,e,f,g,h,i,j,k,l,m] 
            print(df)
            end()
        elif ch==9:
            colname = input('Enter new column name :')
            colvalue = input('Enter default column value :')
            df[colname]=colvalue
            print(df)
            end()
        elif ch==10:
            print(df.columns)
            colname =input('Enter Column Name to delete :')
            del df[colname]
            print(df)
            end()
        elif ch==11:
            print('Choose row index from 0 to ',len(df)-1)
            indexno=int(input('Enter the Index Number that You want to delete :'))
            df=df.drop(indexno) 
            print(df)
            end()
        elif ch==12:
            print("Here are the records with approved Loan\n")
            df1=df[df.Loan_Status=='Y']
            print(df1)
            end()
        elif ch==13:
            pa=input('Enter Property Area(Out of Urban/Semiurban/Rural):')
            if pa=='Urban':
                print("Loan details where Property comes under Urban Area\n")
                df1=df[df.Property_Area=='Urban']
                print(df1)
                end()
            elif pa=='Semiurban':
                print("Loan details where Property comes under Semiurban Area\n")
                df1=df[df.Property_Area=='Semiurban']
                print(df1)
                end()
            elif pa=='Rural':
                print("Loan details where Property comes under Rural Area\n")
                df1=df[df.Property_Area=='Rural']
                print(df1)
                end()
            else:
                print("Invalid Choice :-(")
                end()
        elif ch==14:
            eq=input('Enter Education Status you want to see(Graduate/Not Graduate)')
            if eq=='Graduate':
                print('Loan details of Graduate Applicants\n')
                df1=df[df.Education=='Graduate']
                print(df1)
                end()
            elif eq=='Not Graduate':
                print('Loan details of Ungraduate Applicants\n')
                df1=df[df.Education=='Not Graduate']
                print(df1)
                end()
            else:
                print("Invalid Choice :-(")
                end()
        elif ch==15:
            print(df.describe())
            end()
        elif ch==16:
            print('\n\n Press Enter to continue...')
            break
        else:
            print('Error: Invalid choice try again...')

#purpose: To generate Graph menu
def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n GRAPH MENU ')
        print('_'*115)
        print()
        print('1. Display line graph showing loan amount of applicants\n')
        print('2. Display Graph Loan Status wise\n')
        print('3. Display Graph Property Area wise\n')
        print('4. Display Graph Qualification wise\n')
        print('5. Whole Data LINE Graph\n')
        print('6. Whole Data BAR Graph\n')
        print('7. Exit (Back to MAIN MENU)\n')
        print('_'*115)
        print()
        ch=int(input('Enter your choice: ' ))
        if ch==1:
            x=df['Loan_ID']
            y=df['LoanAmount']
            pl.xticks(rotation='vertical')
            pl.xlabel('---Loan ID---')
            pl.ylabel('---Loan Amount---')
            pl.title('PLOT SHOWING LOAN AMOUNT')
            pl.grid(True)
            pl.plot(x,y,'green',linewidth=3,marker='o',markeredgecolor='red',linestyle='-.')
            fig=input('Want to save the Figure(yes/no): ')
            if fig=='yes':
                pl.savefig("D:\\Figure_1.png")
                print('\nCheck the Figure on D: Drive...')
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            elif fig=='no':
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            else:
                print('\nError: Invalid choice try again...')
                end()
            pl.show()
        elif ch==2:
            x=df['Loan_Status']
            pl.hist(x,edgecolor='black',color='orange')
            n=np.arange(2)
            pl.xticks(n,['Approved','Not Approved'])
            pl.yticks(range(0,40,5))
            pl.xlabel('---Loan Status---')
            pl.ylabel('---Number of Loan Applicants---')
            pl.title('Graph Loan Status wise')
            pl.grid(True)
            fig=input('Want to save the Figure(yes/no): ')
            if fig=='yes':
                pl.savefig("D:\\Figure_2.png")
                print('\nCheck the Figure on D: Drive...')
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            elif fig=='no':
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            else:
                print('\nError: Invalid choice try again...')
                end()
            pl.show()
        elif ch==3:
            x=df['Property_Area']
            pl.hist(x,edgecolor='black',color='red')
            pl.yticks(range(0,40,5))
            pl.xlabel('---Property Area---')
            pl.ylabel('---Number of Loan Applicants---')
            pl.title('Graph Property Area wise')
            pl.grid(True)
            fig=input('Want to save the Figure(yes/no): ')
            if fig=='yes':
                pl.savefig("D:\\Figure_3.png")
                print('\nCheck the Figure on D: Drive...')
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            elif fig=='no':
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            else:
                print('\nError: Invalid choice try again...')
                end() 
            pl.show()
        elif ch==4:
            x=df['Education']
            pl.hist(x,edgecolor='black',color='green')
            pl.yticks(range(0,40,5))
            pl.xlabel('---Education Qualification---')
            pl.ylabel('---Number of Loan Applicants---')
            pl.title('Graph Qualification wise')
            pl.grid(True)
            fig=input('Want to save the Figure(yes/no): ')
            if fig=='yes':
                pl.savefig("D:\\Figure_4.png")
                print('\nCheck the Figure on D: Drive...')
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            elif fig=='no':
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            else:
                print('\nError: Invalid choice try again...')
                end()
            pl.show()
        elif ch==5:
            df.plot(kind='line')
            pl.xticks(range(0,len(df)))
            pl.xlabel('---Loan Applicants---')
            pl.title('Whole Data LINE Graph')
            pl.grid(True)
            fig=input('Want to save the Figure(yes/no): ')
            if fig=='yes':
                pl.savefig("D:\\Figure_5.png")
                print('\nCheck the Figure on D: Drive...')
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            elif fig=='no':
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            else:
                print('\nError: Invalid choice try again...')
                end()
            pl.show()
        elif ch==6:
            df.plot(kind='bar',stacked=True,edgecolor='black')
            pl.xlabel('---Loan Applicants---')
            pl.title('Whole Data BAR Graph')
            pl.grid(True)
            fig=input('Want to save the Figure(yes/no): ')
            if fig=='yes':
                pl.savefig("D:\\Figure_6.png")
                print('\nCheck the Figure on D: Drive...')
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            elif fig=='no':
                print("\nLet's have a look on the Graph")
                print('Press Enter')
                wait=input()
            else:
                print('\nError: Invalid choice try again...')
                end()
            pl.show()
        elif ch==7:
            print('\n\n Press Enter to continue...')
            break
        else:
            print('Error: Invalid choice try again...')

#purpose: To generate export menu
def export():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nEXPORT MENU ')
        print('_'*115)
        print()
        print('1. CSV File\n')
        print('2. MYSQL Table\n')
        print('3. Exit (Back to MAIN MENU)')
        print('_'*115)
        print()
        ch=int(input('Enter your Choice: '))
        if ch==1:
            df.to_csv('D:\\Loan_DataBase.csv')
            print('\nCheck your new file "Loan_DataBase.csv" on D: Drive...')
            end()
        elif ch==2:
            engine=sqlalchemy.create_engine('mysql+pymysql://root:shekhawat190@localhost:3306/IP_PROJECT')
            df.to_sql(name='loans',con=engine,index=False,if_exists='replace')
            print('\n Please check IP_PROJECT database for loans table...')
            end()
        elif ch==3:
            print('\n\n Press Enter to continue...')
            break
        else:
            print('Error: Invalid choice try again...')

#purpose: To generate Main Menu
def main_menu():
    while True:
        clear()
        print('---WELCOME', name,'TO THE MAIN MENU OF LOAN DATABASE SYSTEM---\n')
        print()
        print('\/\/\/MAIN MENU\/\/\/ ')
        print('_'*115)
        print()
        print('1. Read CSV File\n')
        print('2. Data Analysis Menu\n')
        print('3. Graph Menu\n')
        print('4. Export Data\n')
        print('5. Exit')
        print('_'*115)
        print()
        choice=int(input('\n Enter your choice: '))
        if choice==1:
            read_csv_file()
            wait=input()
        elif choice==2:
            data_analysis()
            wait=input()
        elif choice==3:
            graph()
            wait=input()
        elif choice==4:
            export()
            wait=input()
        elif choice==5:
            print('\n\n\t\t---THANK YOU---\n')
            break
        else:
            print('Error: Invalid choice try again...')

#Intro section
print('WELCOME TO THE PROJECT')
print('          ->Let us verify before taking you in...\n')
count=3
while count>0:
    count=count-1
    name=input('NAME: ')
    password=stdiomask.getpass(prompt='PASSWORD: ',mask='*')
    if password=='27Kuldeep':
        main_menu()
    else:
        print('Incorrect Password!')
        print('You have',count,'valid attempts left now\n')
print()
print("Sorry,", name,"You can't use the project, Ask for the password")
wait=input()




