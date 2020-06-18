#importing numpy
import pandas as pd

#reading csv file
sal = pd.read_csv("Documents/Programming/PYTHON/DSML/DSMLCourse/04-Pandas-Exercises/Salaries.csv")

#printing csv header
print(sal.head())

#getting .info()
sal.info()
 
############ Output 
#           <class 'pandas.core.frame.DataFrame'>
#            RangeIndex: 148654 entries, 0 to 148653
#            Data columns (total 13 columns):
#            #   Column            Non-Null Count   Dtype
#            ---  ------            --------------   -----
#            0   Id                148654 non-null  int64
#            1   EmployeeName      148654 non-null  object
#            2   JobTitle          148654 non-null  object
#            3   BasePay           148045 non-null  float64
#            4   OvertimePay       148650 non-null  float64
#            5   OtherPay          148650 non-null  float64
#            6   Benefits          112491 non-null  float64
#            7   TotalPay          148654 non-null  float64
#            8   TotalPayBenefits  148654 non-null  float64
#            9   Year              148654 non-null  int64
#            10  Notes             0 non-null       float64
#            11  Agency            148654 non-null  object
#            12  Status            0 non-null       float64
#            dtypes: float64(8), int64(2), object(3)
#            memory usage: 14.7+ MB


# What is the average BasePay ?
print("\nWhat is the average BasePay?\nA: ", sal['BasePay'].mean())

# What is the highest amount of OvertimePay in the dataset ?
print("\nWhat is the highest amount of OvertimePay in the dataset?\nA: ",sal['OvertimePay'].max())

# What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise 
# you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll).

print("\nWhat is the job title of JOSEPH DRISCOLL?\nA: ",sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["JobTitle"].values[0])

#What is the name of highest paid person (including benefits)?
print("\nWhat is the name of highest paid person (including benefits)?\nA: ", sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName'].values[0])

#What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?
print("\nWhat is the name of lowest paid person (including benefits)?\nA: ",sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]['EmployeeName'].values[0])

#What was the average (mean) BasePay of all employees per year? (2011-2014) ?
print("\nAverage base pay:\n\n",sal.groupby('Year')['BasePay'].mean())

#How many unique job titles are there?
print("Unique job titles: ",sal['JobTitle'].nunique())

#What are the top 5 most common jobs?
print("\nTop5 most common jobs: \n\n",sal['JobTitle'].value_counts().head(5))

#True evaluete 1 and False evaluate 0, so
#sum a series of boolean values should be enough
s = sal[sal['Year'] == 2013]['JobTitle'].value_counts()==1
print("\nHow many Job Titles were represented by only one person in 2013?\nA: ", sum(s))

#How many people have the word Chief in their job title?
def has_chief(job):
    if 'chief' in job.lower():
        return True
    else:
        return False
print("\nHow many people have the word Chief in their job title?\nA: ",sum(sal['JobTitle'].apply(lambda x:has_chief(x))))

#Bonus: Is there a correlation between length of the Job Title string and Salary?

sal['Job_Len'] = sal['JobTitle'].apply(len)
print("\nNo, correlation:\n", sal[['Job_Len','TotalPayBenefits']].corr())