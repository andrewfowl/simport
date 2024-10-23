# simport.py
import sys
import os
import importlib.util

def simport(import_statement):
    """
    Dynamically import a module using a relative path and import statement.
    
    :param import_statement: A string containing the import statement in the format
                             "from ../../folder/module.py import function_name"
    :return: Imported module or function.
    """
    
    # Split the import statement into components
    import_parts = import_statement.strip().split()
    
    if len(import_parts) < 4 or import_parts[0] != "from" or import_parts[2] != "import":
        raise ValueError("Invalid import statement format. Use: 'from ../../folder/module.py import functionName'")
    
    # Extract the relative path and the target function/class name
    relative_path = import_parts[1]
    imported_name = import_parts[3]
    
    # Get absolute path of the module
    base_path = os.path.abspath(os.path.dirname(__file__))
    module_path = os.path.abspath(os.path.join(base_path, relative_path))
    
    if not module_path.endswith('.py'):
        raise ValueError("The import path should point to a '.py' file")
    
    # Dynamically load the module
    module_name = os.path.basename(module_path)[:-3]  # Get the module name without .py extension
    
    # Load the module from the given path
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Return the requested object (function, class, etc.) from the module
    if hasattr(module, imported_name):
        return getattr(module, imported_name)
    else:
        raise ImportError(f"Module '{module_name}' does not have '{imported_name}'")

