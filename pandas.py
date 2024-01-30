import pandas as pd
import matplotlib.pyplot as plt

# Beispiel Daten erstellen
data = {'Jahr': [2010, 2011, 2012, 2013, 2014],
        'Umsatz': [10000, 15000, 18000, 20000, 22000]}

# DataFrame erstellen
df = pd.DataFrame(data)

# Line-Chart erstellen
plt.plot(df['Jahr'], df['Umsatz'], marker='o', linestyle='-')

# Achsenbeschriftungen hinzufügen
plt.xlabel('Jahr')
plt.ylabel('Umsatz')

# Titel hinzufügen
plt.title('Umsatzentwicklung über die Jahre')

# Diagramm anzeigen
plt.grid(True)
plt.show()
