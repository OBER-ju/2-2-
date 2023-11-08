import seaborn as sns
import panfas as sns
titanic = sns.load_dataset("titanic")
titanic.to_csv('C:/Users/kmj/My_Python/7장_data/titanic.csv', index=False)

titanic.isnull().sum()

titanic['age'] = titanic['age'].fillna(titanic['age'].media())
titanic['embarked'].value_couns()

titanic['embarked'] = titanic['embarked'].fillna('S')
titanic['embark_town'].value_counts()

titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
titanic['deck'].value_counts()

titanic['deck'] = titanic['deck'].value_counts('C')
titanic.isnull().sum()

titanic.info()
titanic.survived.volue_counts()
