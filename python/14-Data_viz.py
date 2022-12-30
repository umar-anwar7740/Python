#steps involved in data visualization
#Step 1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt
#Step-2 set a theme
sns.set_theme(style="ticks",color_codes=True)
#import data set as you can also import your own data
kashti=sns.load_dataset("titanic")
print(kashti.sex)
#plot step1 basic graph with 1 variable 
# p=sns.countplot(x="sex",data=kashti)
# plt.show()
#plot step2 with 2 variable
p=sns.countplot(x="sex",hue="survived",data=kashti)
p.set_title("With baba aamar basic plot for titanic")
plt.show()