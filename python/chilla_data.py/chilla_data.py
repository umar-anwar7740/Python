# import pandas as pd
# #Import data from file
# data=pd.read_csv("data.csv.csv")
# print(data.csv.csv)
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks",color_codes=True)
# p=sns.countplot(x="feedback",data=data)
# p.set_title("With baba aamar basic plot for titanic")
# plt.show()
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
kashti=sns.load_dataset("titanic")
kashti
sns.boxplot(x="survived",
            y="age",showmeans=True,
            meanprops={"marker":"+",
                      "markersize":"12",
                      "markeredgecolor":"red"},
            data=kashti)
#show labels
plt.xlabel("How many survived")
plt.ylabel("Age"),
plt.title("Titanic Data")
plt.show()