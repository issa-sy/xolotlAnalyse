import h5py

f = h5py.File('xolotlStop.h5', 'r')
print("Top-level keys:", list(f.keys()))

if 'concentrationsGroup' in f:
    print("\nContenu de 'concentrationsGroup' :")
    for name in f['concentrationsGroup']:
        print("-", name)
else:
    print("'concentrationsGroup' n'existe pas dans le fichier.")
if 'networkGroup' in f:
    print("\nContenu de 'networkGroup' :")
    for name in f['networkGroup']:
        print("-", name)
else:
    print("'networkGroup' n'existe pas dans le fichier.")


