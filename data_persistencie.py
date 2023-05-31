import pandas as pd
import json
import matplotlib.pyplot as plt

#el objetivo principal de estas estadisticas es para poder asegurar mas la privacidad de los usuarios, con los datos principales que tenemos, los usuarios y contraseñas

data = json.load(open(r'csv\users_manifest.json'))

df = pd.DataFrame.from_dict(data, orient='index', columns=['password'])



#estadisticas generales de las contraseñas
password_counts = df['password'].value_counts()
most_common_password = password_counts.idxmax()
print("Contraseña más comun:", most_common_password)

df = pd.DataFrame.from_dict(data, orient='index', columns=['password'])
password_counts = df['password'].value_counts()

# de contraseñas repetidas
plt.bar(password_counts.index, password_counts.values)
plt.xlabel('Contraseñas')
plt.ylabel('Conteos')
plt.title('Conteos de contraseñas')


#contraseñas unicas
unique_passwords = df['password'].unique()
print("contraseñas mas unicas ", unique_passwords)


#porcentaje de contraseña mas comunes
password_percentage = password_counts[most_common_password] / len(df) * 100
print("Porcentaje de contraseña mas comun", password_percentage)


#estadisticas generales de longitud de contraseñas
password_lengths = df['password'].str.len()
min_length = password_lengths.min()
max_length = password_lengths.max()
average_length = password_lengths.mean()
print("contraseñas mas pequeña:", min_length)
print("contraseñas mas larga:", max_length)
print("Tamaño medio:", average_length)

plt.xticks(rotation=45)

#estadisticas generales de contraseñas fuertes
common_passwords = df['password']  #miraremos entre nuestras propias contraseñas
strong_passwords = df[(df['password'].str.len() >= 8) & (~df['password'].isin(common_passwords))]
strong_password_percentage = len(strong_passwords) / len(df) * 100
print("Percentage of strong passwords:", strong_password_percentage)

plt.show()



#estadisticas mas complejas de contraseñas

#bastante autoexplicativo
common_passwords = df['password']  #miraremos entre nuestras propias contraseñas
strong_passwords = df[(df['password'].str.len() >= 8) & (~df['password'].isin(common_passwords))]
strong_password_percentage = len(strong_passwords) / len(df) * 100
print("Porcentaje de seguridad de contraseñas", strong_password_percentage)


