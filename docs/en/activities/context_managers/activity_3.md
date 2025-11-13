# Third activity

Write a context manager to temporary change the working directory. Exiting the context, the working 
directory must be the same as before entering the context.

This is an example shows how to use the context manager:
```python
print(os.getcwd())

with changedir('/temp'):
    print(os.getcwd())

print(os.getcwd())
```
This code should display the current working directory, the directory `/temp` then once again the 
first directory.

**Warning**: on the code above, `'/temp'` is an example. Use an existing directory on your system. 
Of course, you can consider creating the directory tree if it does not exist but should you delete 
it on exit ? This is not asked for the activity.  

You can change the working directory with 
[`os.chdir(path)`](https://docs.python.org/3/library/os.html#os.chdir).