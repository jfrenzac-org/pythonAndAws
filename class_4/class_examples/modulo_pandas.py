# pip -- Manager de paquetes - Se usa para instalar los módulos

# pip install <nombre_del_modulo>

import pandas as pd
from faker import Faker
import random 
fake = Faker()
data=[]
for i in range(1000):
    person={
        'name':fake.first_name(),
        'lastname':fake.last_name(),
        'age':random.randint(18, 80),
        'weight':round(random.uniform(50.0, 120.0), 1),
    }
    data.append(person)
df=pd.DataFrame(data)
df.to_csv('data.csv', index=False)
