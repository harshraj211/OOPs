````markdown
# OOP Basics in Python — Class and Object

## Code

```python
class Car:
    def __init__(self, brand_name, brand_speed):
        self.brand_name = brand_name
        self.brand_speed = brand_speed


my_car = Car("Toyota", "100km/h")

print(my_car.brand_speed)
print(my_car.brand_name)


my_new_car = Car("Tata", "150km/h")

print(my_new_car.brand_name)
print(my_new_car.brand_speed)
````

---

## 1. What is a Class?

A **class** is like a blueprint or template.

For example:

```python
class Car:
```

Here, `Car` is a class.

The class describes what information a car object should contain.

In our example, every car will have:

* `brand_name`
* `brand_speed`

Think of it like:

Car Blueprint

```
brand_name
brand_speed
```

From this blueprint, we can create many different cars.

---

## 2. What is an Object?

An **object** is an actual instance created from a class.

Example:

```python
my_car = Car("Toyota", "100km/h")
```

Here:

* `Car` → class
* `my_car` → object
* `"Toyota"` → brand name
* `"100km/h"` → brand speed

So conceptually:

```text
Car Class
   |
   |
   ---> my_car
          brand_name = "Toyota"
          brand_speed = "100km/h"
```

Another object:

```python
my_new_car = Car("Tata", "150km/h")
```

Now:

```text
Car Class
   |
   |----> my_car
   |        brand_name = Toyota
   |        brand_speed = 100km/h
   |
   |----> my_new_car
            brand_name = Tata
            brand_speed = 150km/h
```

Both objects are created from the same `Car` class, but they store different data.

---

# 3. What is `__init__()`?

```python
def __init__(self, brand_name, brand_speed):
```

`__init__()` is a special method in Python.

It is called automatically whenever we create a new object.

For example:

```python
my_car = Car("Toyota", "100km/h")
```

Python automatically calls:

```python
__init__(my_car, "Toyota", "100km/h")
```

You normally do not call `__init__()` manually.

Its main job is to initialize the data of an object.

---

# 4. What is `self`?

`self` refers to the **current object**.

Consider:

```python
self.brand_name = brand_name
```

When we create:

```python
my_car = Car("Toyota", "100km/h")
```

`self` refers to:

```python
my_car
```

So this:

```python
self.brand_name = brand_name
```

can be mentally understood as:

```python
my_car.brand_name = "Toyota"
```

And:

```python
self.brand_speed = brand_speed
```

becomes:

```python
my_car.brand_speed = "100km/h"
```

For the second object:

```python
my_new_car = Car("Tata", "150km/h")
```

`self` now refers to:

```python
my_new_car
```

Therefore:

```python
self.brand_name = brand_name
```

becomes:

```python
my_new_car.brand_name = "Tata"
```

---

# 5. Parameters vs Object Attributes

This line is very important:

```python
self.brand_name = brand_name
```

There are actually two different things here.

### `brand_name`

This is a parameter received by the function.

```python
def __init__(self, brand_name, brand_speed):
```

### `self.brand_name`

This is an attribute belonging to the object.

So:

```python
self.brand_name = brand_name
```

means:

> Take the value received in `brand_name` and store it inside the current object as `brand_name`.

Example:

```python
Car("Toyota", "100km/h")
```

Here:

```text
brand_name = "Toyota"
brand_speed = "100km/h"
```

Then:

```python
self.brand_name = brand_name
```

stores:

```text
my_car.brand_name = "Toyota"
```

---

# 6. Creating the First Object

```python
my_car = Car("Toyota", "100km/h")
```

Step by step:

```text
Car("Toyota", "100km/h")
        |
        v
__init__(self, brand_name, brand_speed)
        |
        | brand_name = "Toyota"
        | brand_speed = "100km/h"
        |
        v
my_car
```

The object now contains:

```text
my_car
 ├── brand_name = "Toyota"
 └── brand_speed = "100km/h"
```

---

# 7. Accessing Object Attributes

We access an object's data using the dot `.` operator.

Example:

```python
print(my_car.brand_speed)
```

Output:

```text
100km/h
```

And:

```python
print(my_car.brand_name)
```

Output:

```text
Toyota
```

The dot operator means:

```text
object.attribute
```

Example:

```python
my_car.brand_name
```

means:

> Give me the `brand_name` stored inside `my_car`.

---

# 8. Creating Another Object

```python
my_new_car = Car("Tata", "150km/h")
```

Now another completely separate object is created.

```text
my_new_car
 ├── brand_name = "Tata"
 └── brand_speed = "150km/h"
```

The first object's data is not changed.

So we now have:

```text
my_car
 ├── brand_name = Toyota
 └── brand_speed = 100km/h


my_new_car
 ├── brand_name = Tata
 └── brand_speed = 150km/h
```

---

# 9. Output of the Program

The program produces:

```text
100km/h
Toyota
Tata
150km/h
```

Because the print statements execute in this order:

```python
print(my_car.brand_speed)
print(my_car.brand_name)

print(my_new_car.brand_name)
print(my_new_car.brand_speed)
```

---

# 10. Main OOP Concepts Learned Here

From this small program we learned:

### Class

Blueprint for creating objects.

```python
class Car:
```

### Object

An instance of a class.

```python
my_car = Car("Toyota", "100km/h")
```

### Constructor

Special method automatically executed when an object is created.

```python
def __init__(self, brand_name, brand_speed):
```

### `self`

Refers to the current object.

```python
self.brand_name
```

### Attribute

A variable stored inside an object.

```python
self.brand_name
self.brand_speed
```

### Dot Operator

Used to access attributes or methods of an object.

```python
my_car.brand_name
```

---

# Important Mental Model

Think of:

```python
class Car:
```

as a **factory design**.

Then:

```python
my_car = Car("Toyota", "100km/h")
```

means:

```text
Use Car blueprint
       ↓
Create new object
       ↓
Store Toyota and 100km/h inside it
       ↓
Save reference in my_car
```

And:

```python
my_new_car = Car("Tata", "150km/h")
```

creates another independent object.

---

# One-Line Summary

A **class defines what an object should have**, while an **object is the actual thing created from that class with its own data**.


