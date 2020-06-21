import pandas as pd
ecom = pd.read_csv("Documents/Programming/PYTHON/DSML/DSMLCourse/04-Pandas-Exercises/Ecommerce Purchases")
print(ecom.head())
print(ecom.info())
ecom_min = ecom_min = ecom['Purchase Price'].min()
ecom_max = ecom['Purchase Price'].max()

print('Average purchase price: ',ecom['Purchase Price'].mean())
print(f'Lowest purchase price is {ecom_min} and the highest is {ecom_max}')

print("How many people have 'en' as language?: ",ecom[ecom['Language']=='en'].count())
print("How many people have the job title of 'Lawyer'?: ", ecom[ecom['Job']=='Lawyer'].count())

ecom_am = sum(ecom[ecom['AM or PM']=='AM']['Email'].value_counts())
ecom_pm = sum(ecom[ecom['AM or PM']=='PM']['Email'].value_counts())

print(f"How many people made the purchase during the AM? A: {ecom_am} \nHow many people made the purchase during PM? A: {ecom_pm}")

print("\n5 most common jobs?\n",ecom['Job'].value_counts().head(5))

print("Purchase price that came from Lot 90 WT:\n",ecom[ecom['Lot'] == '90 WT']['Purchase Price'].values[0])

print("What is the email of the person with the following Credit Card Number: 4926535242672853 ? \nA: ", ecom[ecom['Credit Card'] == 4926535242672853]['Email'].values[0])

#How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
ecom_condition = ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count().values[0]
print("How many people have American Express as their Credit Card Provider and made a purchase above $95 ?\nA: ",ecom_condition)

#Hard: How many people have a credit card that expires in 2025?
def has_25(date):
    if '/25' in date:
        return True
    else:
        return False
print("How many people have a credit card that expires in 2025?\nA: ",sum(ecom['CC Exp Date'].apply(lambda x:has_25(x))))

#What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)

prov = ecom['Email'].apply(lambda x:x.split('@')[1]).value_counts().head(5)
print("Most providers:\n",prov)