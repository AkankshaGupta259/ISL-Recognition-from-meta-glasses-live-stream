import json

path = r'c:\Users\Asus\Projects\MetaApp\Scripts\impementation.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if cell['cell_type'] == 'code':
        source = cell['source']
        if any('import io, queue' in line for line in source):
            # Modify this cell
            for i, line in enumerate(source):
                if 'import io, queue' in line:
                    source.insert(i+1, 'from IPython.display import Image as IPImage\n')
                    break
            for i, line in enumerate(source):
                if 'end=""' in line:
                    source[i] = line.replace('end=""', 'end="", flush=True')

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print('Notebook patched successfully.')
