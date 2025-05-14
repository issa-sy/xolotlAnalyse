import h5py

# Ouvrir le fichier HDF5 en lecture
with h5py.File('xolotlStop.h5', 'r') as f:
    # Vérifie que 'networkGroup' existe
    if 'networkGroup' in f:
        network_group = f['networkGroup']

        # ID du cluster à lire
        cluster_id = '997'  # 0-999
        # Vérifie si le cluster existe
        if cluster_id in network_group:
            cluster = network_group[cluster_id]
            print(f"Contenu de networkGroup/{cluster_id} :")

            # Affiche les attributs
            for attr in cluster.attrs:
                print(f"- {attr} : {cluster.attrs[attr]}")
        else:
            print(f"Cluster '{cluster_id}' n'existe pas dans networkGroup.")
    else:
        print("'networkGroup' n'existe pas dans le fichier.")
