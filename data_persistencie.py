import pandas as pd
import json
import matplotlib.pyplot as plt

data = json.load(open(r'csv\users_manifest.json'))

df = pd.DataFrame.from_dict(data, orient='index', columns=['password'])




password_counts = df['password'].value_counts()
most_common_password = password_counts.idxmax()
print("Contraseña más común:", most_common_password)

df = pd.DataFrame.from_dict(data, orient='index', columns=['password'])
password_counts = df['password'].value_counts()

# de contraseñas repetidas
plt.bar(password_counts.index, password_counts.values)
plt.xlabel('Password')
plt.ylabel('Count')
plt.title('Count of Passwords')


plt.xticks(rotation=45)


plt.show()