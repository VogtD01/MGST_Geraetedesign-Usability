import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Risiken und zugehörige Daten (inkl. neuem Risiko)
risiken = [
    "Fehlbedienung durch UI",
    "Datenmissbrauch",
    "Hautreizungen",
    "Verwirrung durch Symbolsprache"
]
eintrittswkeit = [30, 10, 20, 5]  # Eintrittswahrscheinlichkeit in %
schadensausmass = [2, 4, 3, 1]    # Schadensausmaß: 1 = gering, 4 = sehr hoch

# Farben je nach Risiko
farben = []
for x, y in zip(eintrittswkeit, schadensausmass):
    if x < 15 and y <= 2:  # Niedriges Risiko
        farben.append('lime')
    elif x >= 30 and y >= 3:  # Hohes Risiko
        farben.append('red')
    else:
        farben.append('orange')  # Mittleres Risiko (orange statt gelb für bessere Sichtbarkeit)

# Plot vorbereiten
fig, ax = plt.subplots(figsize=(10, 6))

# Hintergrundbereiche
green_area = Polygon([[0, 0], [30, 0], [0, 4.5]], color='lime', alpha=0.5)
yellow_area = Polygon([[30, 0], [40, 2], [25, 4.5], [0, 4.5]], color='yellow', alpha=0.5)
red_area = Polygon([[25, 4.5], [40, 4.5], [40, 2]], color='red', alpha=0.5)
yellow_triangle = Polygon([[30, 0], [40, 0], [40, 2]], color='yellow', alpha=0.5)

# Bereiche hinzufügen
ax.add_patch(green_area)
ax.add_patch(yellow_area)
ax.add_patch(red_area)
ax.add_patch(yellow_triangle)

# Risiken als Punkte einzeichnen
ax.scatter(eintrittswkeit, schadensausmass, c=farben, s=200)

# Beschriftung der Punkte
for i, risiko in enumerate(risiken):
    ax.text(eintrittswkeit[i] + 0.5, schadensausmass[i], risiko, fontsize=9)

# Achsentitel und Layout
ax.set_xlabel("Eintrittswahrscheinlichkeit [%]")
ax.set_ylabel("Schadensausmaß")
ax.set_title("Risikobewertung Implantat-Scanner-3000")
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(["gering", "mittel", "hoch", "sehr hoch"])
ax.set_xlim(0, 40)
ax.set_ylim(0, 4.5)
ax.grid(True)
plt.tight_layout()

# Diagramm anzeigen
plt.show()
