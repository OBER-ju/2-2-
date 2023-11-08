import matplotlib.pyplot as plt
f, ax = plt.subplot(1, 2, figsize=(10, 5))
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(
    explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.
pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
ax[0].set_title('Survived (Male)')
ax[1].set_title('Survived (Female)')
plt.show()

sns.countplot('pclass', hue='survived', data=titanic)
plt.title('Pclass vs Survived')
plt.show()
