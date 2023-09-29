sales_per_hour = input("This Month's SPH Goal :")
hours_worked = input("How many hours have you worked :")
current_sales = input("Total Sales ex. 55136.95 :")

try:
    sph = float(sales_per_hour)
    hrswk = float(hours_worked)
    cs = float(current_sales)
except:
    print("Use numbers only")
    quit()

goal = sph * hrswk
mb = (sph * 180) * 1.50

b0 = 0.0, "Sorry, You did not earn a bonus"
b1 = 100.0
b2 = 200.0
b3 = 300.0

t1bm = 0
# def computebonus(sph, hrswk, cs, goal, bonus) :
# cb = computebonus(sph, hrswk, cs, goal, bonus)

def this_month(cs) :
    if 0 <= cs <= goal * .99:
        result = "your goal was", goal, "You didn't hit goal, you wrote", cs, b0

    elif goal <= cs <= goal * 1.24:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b1, "dollars!"

    elif goal * 1.25 <= cs <= goal * 1.49:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b2, "dollars!"

    elif 1.49 * goal <= cs:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b3, "dollars!"
    return result

q = this_month(cs)
print(q)

def this_montht2(cs) :
    if 0 <= cs <= goal * .99:
        result = "your goal was", goal, "You didn't hit goal, you wrote", cs, b0

    elif goal <= cs <= goal * 1.24:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b1 * 2, "dollars!"

    elif goal * 1.25 <= cs <= goal * 1.49:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b2 * 2, "dollars!"

    elif 1.49 * goal <= cs:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b3 * 2, "dollars!"
    return result
w = this_montht2(cs)

def this_montht3(cs) :
    if 0 <= cs <= goal * .99:
        result = "your goal was", goal, "You didn't hit goal, you wrote", cs, b0

    elif goal <= cs <= goal * 1.24:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b1 * 3, "dollars!"

    elif goal * 1.25 <= cs <= goal * 1.49:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b2 * 3, "dollars!"

    elif 1.49 * goal <= cs:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b3 * 3, "dollars!"
    return result
e = this_montht3(cs)

def this_montht4(cs) :
    if 0 <= cs <= goal * .99:
        result = "your goal was", goal, "You didn't hit goal, you wrote", cs, b0

    elif goal <= cs <= goal * 1.24:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b1 * 4, "dollars!"

    elif goal * 1.25 <= cs <= goal * 1.49:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b2 * 4, "dollars!"

    elif 1.49 * goal <= cs:
        result = "your goal was", goal, "max bonus is", mb, "You wrote", cs, "Your bonus is", b3 * 4, "dollars!"
    return result
r = this_montht4(cs)

print("Lets find out if you earned even more money!!")
b_inp = input("Department Tier? 1, 2, or 3? ")
try :
    bi = int(b_inp)
except :
    float(b_inp)
    str(b_inp)
    print("Tier 1, 2, 3, or 4 only! ")


if bi == 1 :
    print(q)
elif bi == 2 :
    print(w)
elif bi == 3 :
    print(e)
elif bi == 4 :
    print(r)