# simport

`simport` is a Python package that allows you to dynamically import modules using relative paths.

## Installation

```bash
pip install simport

Usage
You can use simport to dynamically import any Python module or function by specifying a relative path.

```python
import simport

# Import functionName from a module located at a relative path
function_name = simport.simport("from ../../folder/module.py import functionName")

# Use the imported function
function_name()