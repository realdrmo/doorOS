import os

import ast
import astor

SCENES_DIR_PATH = "src/scenes"

def cache_modules():
    lock_file = "dooros-lock.py"
    scenes_dir = os.listdir(SCENES_DIR_PATH)

    with open(lock_file, "w") as f:
        classes = []
        imports = set()

        for scene in scenes_dir:
            path = os.path.join("src", "scenes", scene)
            
            with open(path, "r") as fs:
                source_code = fs.read()

            for node in ast.parse(source_code).body:
                if isinstance(node, ast.ClassDef) and node.name.lower() == scene[:-3]:
                    classes.append(astor.to_source(node))

                elif isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                    imports.add(astor.to_source(node))
            
        for n, imp in enumerate(imports):

            if n == len(imports) - 1:
                f.write(imp + "\n\n")
            else:
                f.write(imp + "\n")
            
        for x in range(len(classes)):

            f.write(classes[x] + "\n\n")


cache_modules()

