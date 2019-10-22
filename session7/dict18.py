restarant =[
{"name": "Huy", "role": "waiter", "hours": 12, "salary per hour": 0.8},
{"name": "Tung", "role": "cook", "hours": 24 , "salary per hour": 1.5},
{"name": "M.Duc", "role": "manager", "hours": 20, "salary per hour": 2}
]
p1 = {
    "name": "don", 
    "role": "waiter", 
    "hours": 12,
    "salary per hour": 0.9,
}
p2 = {
    "name": "H.duc",
    "role": "waiter",
    "hours": 14,
    "salary per hour": 0.7
}
restarant.append(p1)
restarant.append(p2)
restarant.pop(4)
print(restarant)
