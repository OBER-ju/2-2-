import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
sns.displot(red_win_quality, kde=True, color="red", label='red wind')
sns.displot(while_wind_quality, kde=True, label='while wind')
plt.title("Quality of Wind Type")
plt.legend()
plt.show()
