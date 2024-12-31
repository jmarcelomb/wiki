# **The Rule of Three**
If your class directly manages some kind of resource (such as a new'ed pointer), then you almost certainly need to hand-write three special member functions:
- A destructor to free the resource
- A copy constructor to copy the resource
- A copy assignment operator to free the left-hand resource and copy the right-hand one
- Use the copy-and-swap idiom to implement assignment.

# **The Rule of Zero**
If your class does not directly manage any resource, but merely uses library components such as vector and string, then you should strive to write **no** special member functions. 

**Default them all**

- Let the compiler implicitly generate a default destructor
- Let the compiler implicitly generate the copy constructor
- Let the compiler implicitly generate the copy assignment operator
- (But your own swap might improve performance)