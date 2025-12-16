import pandas as pd
import matplotlib.pyplot as plt


df_spillover_JP = pd.read_csv('../Data/crimespilloverJP_notsorted.csv')
df_spillover_Mattapan = pd.read_csv('../Data/crimespilloverMattapan_notsorted.csv')
df_spillover_SouthBos = pd.read_csv('../Data/crimespilloverSouthBoston_notsorted.csv')
df_spillover_SouthEnd= pd.read_csv('../Data/crimespilloverSouthEnd_notsorted.csv')
df_spillover_Dorchester = pd.read_csv('../Data/crimespilloverDorchester_notsorted.csv')

data_spillover_fromRox = [df_spillover_JP['Spillover Roxbury to JP'],df_spillover_Mattapan['Spillover Roxbury to Mattapan'],df_spillover_SouthBos['Spillover Roxbury to South Boston'],df_spillover_SouthEnd['Spillover Roxbury to South End'],df_spillover_Dorchester['Spillover Roxbury to Dorchester'] ]

fig, ax = plt.subplots(figsize=(18,8))
ax.violinplot(data_spillover_fromRox, showmeans=True, showmedians=False)
ax.set_xticks([1,2,3,4,5])
plt.xticks(rotation=10)
ax.set_xticklabels(['Spillover Roxbury to JP', 'Spillover Roxbury to Mattapan','Spillover Roxbury to South Boston', 'Spillover Roxbury to South End', 'Spillover Roxbury to Dorchester' ], fontsize=22)
plt.ylabel("Spillover Probabilities ", fontsize=30)
plt.xlabel("Spillover from Roxbury", fontsize=30)
plt.title('Violin Plot of Spillover Probabilities for Roxbury to Neighboring Districts', fontsize=30)
fig.tight_layout()
fig.savefig('violin_from.eps', bbox_inches='tight', pad_inches=0.05)
plt.show()

data_spillover_toRox = [df_spillover_JP['Spillover JP to Roxbury'],df_spillover_Mattapan['Spillover Mattapan to Roxbury'],df_spillover_SouthBos['Spillover South Boston to Roxbury'],df_spillover_SouthEnd['Spillover South End to Roxbury'],df_spillover_Dorchester['Spillover Dorchester to Roxbury'] ]
fig, ax = plt.subplots(figsize=(18,8))
parts = ax.violinplot(data_spillover_toRox, showmeans=True, showmedians=False)
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('#D43F3A')
    pc.set_alpha(1)
ax.set_xticks([1,2,3,4,5])
plt.xticks(rotation=10)
ax.set_xticklabels(['Spillover JP to Roxbury', 'Spillover Mattapan to Roxbury','Spillover South Boston to Roxbury', 'Spillover South End to Roxbury', 'Spillover Dorchester to Roxbury'], fontsize=22)
plt.ylabel("Spillover Probabilities ", fontsize=30)
plt.xlabel("Spillover to Roxbury", fontsize=30)
plt.title('Violin Plot of Spillover Probabilities for Roxbury from Neighboring Districts', fontsize=30)
fig.tight_layout()
fig.savefig('violin_to.eps', bbox_inches='tight', pad_inches=0.05)
plt.show()
