#  Pipeline ETL – Location de trottinettes (Python + KPI)

##  Objectif
Créer un mini pipeline ETL pour nettoyer des données de trajets de trottinettes et produire des indicateurs (KPI) utiles pour l’analyse.

## 🔧 Technologies
- Python (Pandas)
- Dataset CSV (exemple)
- Concepts SQL (jointures, agrégations, intégrité)

##  Données
Le fichier `data/trottinettes.csv` contient des trajets avec :
- date/heure de début et fin
- distance (km)
- niveau de batterie au départ
- zone (quartier)

##  Étapes ETL
1. Chargement des données CSV
2. Conversion des dates
3. Création de la durée de trajet (minutes)
4. Nettoyage : suppression des valeurs invalides
5. Calcul des KPI :
   - nombre de trajets
   - distance moyenne
   - durée moyenne
   - batterie moyenne au départ
   - zone la plus active
6. Détection d’anomalies :
   - trajets trop longs (> 60 min)
   - trajets trop courts (< 2 min)
   - batterie faible (< 15%)

##  Exécution
Installer les dépendances :
```bash
pip install -r requirements.txt
