# CRTP (Curiously Recurring Template Pattern)

In short, CRTP (Curiously Recurring Template Pattern) is when a class A has a base class which is a template specialization for the class A itself. E.g.

```c++
	template <class T> 
	class X{...};
	class A : public X<A> {...};
```
It is curiously recurring, isn't it? :)

Now, what does this give you? This actually gives the X template the ability to be a base class for its specializations.

For example, you could make a generic singleton class (simplified version) like this
```c++
#include <iostream>

template <class T>
class Singleton
{
public:
     static T* GetInstance() {
         if ( p == nullptr ) p = new T();
         return p;
     }
protected:
     Singleton() = default;

     Singleton(Singleton const &) = delete;
     Singleton &operator=(const Singleton &) = delete;

private:
     static T *p;
};
template <class T>
T *Singleton<T>::p= nullptr;
```

Now, in order to make an arbitrary class A a singleton you should do this

```c++
class A : public Singleton<A> 
{ 
friend Singleton;
private:
    A() = default;
};
A *a0= A::GetInstance();
```

However, CRTP is not necessary in this case, see as follow:

```c++
class C 
{ 
friend Singleton<C>; 
private: C() = default;
};
C *c1= Singleton<C>::GetInstance();
```

So you see? The singleton template assumes that its specialization for any type `X` will be inherited from `singleton<X>` and thus will have all its (public, protected) members accessible, including the GetInstance! There are other useful uses of CRTP. For example, if you want to count all instances that currently exist for your class, but want to encapsulate this logic in a separate template (the idea for a concrete class is quite simple - have a static variable, increment in ctors, decrement in dtors). Try to do it as an exercise!

Yet another useful example, for Boost (I am not sure how they have implemented it, but CRTP will do too). Imagine you want to provide only operator < for your classes but automatically operator == for them!

you could do it like this:

```c++
template<class Derived>
class Equality
{
};

template <class Derived>
bool operator == (Equality<Derived> const& op1, Equality<Derived> const & op2)
{
    Derived const& d1 = static_cast<Derived const&>(op1);//you assume this works     
    //because you know that the dynamic type will actually be your template parameter.
    //wonderful, isn't it?
    Derived const& d2 = static_cast<Derived const&>(op2); 
    return !(d1 < d2) && !(d2 < d1);//assuming derived has operator <
}
```

or implement within the template scope without casting

```c++
template<class T>
class Equality
{
    friend bool operator == (const T& op1, const T& op2)
    { 
        return !(op1 < op2) && !(op2 < op1); 
    }
};
```

Now you can use it like this

```c++
struct Apple:public Equality<Apple> 
{
    int size;
};

bool operator < (Apple const & a1, Apple const& a2)
{
    return a1.size < a2.size;
}
```

Now, you haven't provided explicitly operator `==` for Apple? But you have it! You can write

```c++
int main()
{
    Apple a1;
    Apple a2; 

    a1.size = 10;
    a2.size = 10;
    if(a1 == a2) //the compiler won't complain! 
    {
    }
}
```

This could seem that you would write less if you just wrote operator `==` for Apple, but imagine that the Equality template would provide not only `==` but `>`, `>=`, `<=` etc. And you could use these definitions for multiple classes, reusing the code!

Here is another example:
https://godbolt.org/z/fEhsGq6q3

```c++
#include <array>
#include <cstdint>

int square(int num) {
    return num * num;
}


//CRTP
template <class T> 
struct Figure
{
    int area()
    {
        return static_cast<T*>(this)->area_implementation();
    }

    static void static_func()
    {
        T::static_sub_func();
    }
};

struct Circle : Figure<Circle>
{
    uint32_t radius;
    
    Circle(uint32_t new_radius = 5) : radius(new_radius){};

    int area_implementation(){
        return 2 * 3 * square(this->radius);
    }
    static void static_sub_func();
};

struct Rectangle : Figure<Rectangle>
{
    uint32_t c, l;
    
    Rectangle(uint32_t new_c=5, uint32_t new_l=5) : c(new_c), l(new_l){};

    int area_implementation(){
        return c * l;
    }
    static void static_sub_func();
};

template<typename derived>
int callArea(Figure<derived> &fig){
    return fig.area();
}


// Virtual
struct FigureVirtual
{
    virtual int area();
};

struct CircleVirtual : FigureVirtual
{
    uint32_t radius;
    
    CircleVirtual(uint32_t new_radius = 5) : radius(new_radius){};

    int area(){
        return 2 * 3 * square(this->radius);
    }
};

struct RectangleVirtual : FigureVirtual
{
    uint32_t c, l;
    
    RectangleVirtual(uint32_t new_c=5, uint32_t new_l=5) : c(new_c), l(new_l){};

    int area(){
        return c * l;
    }
    static void static_sub_func();
};

int main(){
    Circle circ_crtp(5);
    Rectangle rec_ctrp(5, 2);

    CircleVirtual circ(5);
    RectangleVirtual rec(5, 2);

    std::array<FigureVirtual*, 2> figures{&circ, &rec};
    return figures[0]->area() + figures[1]->area();
    //return callArea(circ_crtp) + callArea(rec_ctrp);
}
```