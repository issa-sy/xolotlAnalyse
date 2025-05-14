import h5py

# Ouvrir le fichier
f = h5py.File('xolotlStop.h5', 'r')

# Spécifie le chemin vers le groupe
group_path = 'concentrationsGroup/concentration_0_0_266'

# Vérifie que le groupe existe
if group_path in f:
    group = f[group_path]
    print(f"\nContenu de '{group_path}' :")
    
    # Attributs du groupe
    print("\nAttributs :")
    for key, value in group.attrs.items():
        print(f"- {key} : {value}")
    
    # Jeux de données (datasets) du groupe
    print("\nJeux de données :")
    for name in group:
        dset = group[name]
        print(f"- {name} : shape = {dset.shape}, dtype = {dset.dtype}")
        
        # Pour afficher les 5 premières lignes
        try:
            data = dset[:5]
            print("  Exemple de données :", data)
        except:
            print("  Impossible de lire les données.")
else:
    print(f"Le groupe '{group_path}' n'existe pas dans le fichier.")
