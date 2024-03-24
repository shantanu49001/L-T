import pulp

prob = pulp.LpProblem("Warehouse_Transportation_Problem", pulp.LpMinimize)

trucks = ['I1', 'I2', 'O1', 'O2']
products = ['P1', 'P2']
docks = ['D1', 'D2']
storage_locations = ['S1', 'S2']

fvp = {
    ('I1', 'P1'): 10, ('I1', 'P2'): 15,
    ('I2', 'P1'): 20, ('I2', 'P2'): 25,
    ('O1', 'P1'): 5, ('O1', 'P2'): 10,
    ('O2', 'P1'): 15, ('O2', 'P2'): 20
}

PUp = {'P1': 100, 'P2': 100}
PLp = {'P1': 100, 'P2': 100}

Qsk = {('S1', 'D1'): 50, ('S1', 'D2'): 50, ('S2', 'D1'): 50, ('S2', 'D2'): 50}

Wkk_prime = {('D1', 'D2'): 0, ('D2', 'D1'): 0}

TS = 1
TE = 2
M = 1000000
lj = 5

av = {v: pulp.LpVariable(f"av_{v}", lowBound=0, cat='Continuous') for v in trucks}
dv = {v: pulp.LpVariable(f"dv_{v}", lowBound=0, cat='Continuous') for v in trucks}
Xijps = {(i, j, p, s): pulp.LpVariable(f"X_{i}_{j}_{p}_{s}", lowBound=0, cat='Continuous') 
         for i in trucks for j in trucks for p in products for s in storage_locations}
Vijs = {(i, j, s): pulp.LpVariable(f"V_{i}_{j}_{s}", cat='Binary') 
        for i in trucks for j in trucks for s in storage_locations}
Pijk = {(i, j, k): pulp.LpVariable(f"P_{i}_{j}_{k}", cat='Binary') 
        for i in trucks for j in trucks for k in docks}
qijk = {(i, j, k): pulp.LpVariable(f"q_{i}_{j}_{k}", cat='Binary') 
        for i in trucks for j in trucks for k in docks}
yik = {(i, k): pulp.LpVariable(f"y_{i}_{k}", cat='Binary') 
       for i in trucks for k in docks}
Zik = {(j, k): pulp.LpVariable(f"Z_{j}_{k}", cat='Binary') 
       for j in trucks for k in docks}

prob += dv['O2'] - av['I1'], "Total_Time"

# Adding constraint T ≥ dj for all outbound trucks
for j in [truck for truck in trucks if truck.startswith('O')]:
    prob += pulp.lpSum(dv[j] - av['I1']) >= 0, f"Departure_Time_of_{j}"

# Adding constraint ΣΣxijps = fip for all i€ Inbound trucks; for all p € products
for i in [truck for truck in trucks if truck.startswith('I')]:
    for p in products:
        prob += pulp.lpSum(Xijps[i, j, p, s] for j in trucks for s in storage_locations) == fvp[i, p], f"Constraint_Product_{p}_Truck_{i}"

# Adding constraint ΣΣxijps = fip for all j € Outbound trucks; for all p € products
for j in [truck for truck in trucks if truck.startswith('O')]:
    for p in products:
        prob += pulp.lpSum(Xijps[i, j, p, s] for i in trucks for s in storage_locations) == fvp[j, p], f"Constraint_Product_{p}_Truck_{j}"

# Adding constraint Xijps ≤ M * Vijs for all i∈ Inbound trucks; for all j∈ Outbound trucks; for all p ∈ Products; for all s ∈ Storage_locations
for i in [truck for truck in trucks if truck.startswith('I')]:
    for j in [truck for truck in trucks if truck.startswith('O')]:
        for p in products:
            for s in storage_locations:
                prob += Xijps[i, j, p, s] <= M * Vijs[i, j, s], f"Constraint_Binary_{i}_{j}_{p}_{s}"

# Adding constraint Σxijps >= vijs for all i € Inbound trucks, for all s € storage_locations, for all j € outbound trucks
for i in [truck for truck in trucks if truck.startswith('I')]:
    for s in storage_locations:
        for j in [truck for truck in trucks if truck.startswith('O')]:
            prob += pulp.lpSum(Xijps[i, j, p, s] for p in products) >= Vijs[i, j, s], f"Constraint_Binary_{i}_{j}_{s}"

# Adding constraint ΣΣxijps <= Qsk for all j€ Outbound trucks; for all s € Storage_locations, for all k € Docks
for j in [truck for truck in trucks if truck.startswith('O')]:
    for s in storage_locations:
        for k in docks:
            prob += pulp.lpSum(Xijps[i, j, p, s] for i in trucks for p in products) <= Qsk[s, k], f"Constraint_Storage_{s}_Dock_{k}_Truck_{j}"

# Adding constraint ΣΣxijps <= Qsk for all i€ Inbound trucks; for all s € Storage_locations
for i in [truck for truck in trucks if truck.startswith('I')]:
    for s in storage_locations:
        prob += pulp.lpSum(Xijps[i, j, p, s] for j in trucks for p in products) <= Qsk[s, k], f"Constraint_Inbound_Storage_{s}_{i}"

# # Adding constraint di >= ai + Σfip * Pup, for all i€ Inbound trucks, for all p € Products
# for i in [truck for truck in trucks if truck.startswith('I')]:
#     prob += dv[i] >= av[i] + pulp.lpSum(fvp[i, p] * PUp[p] for p in products), f"Constraint_Arrival_Product_{p}_Truck_{i}"

# # Adding constraint dj >= aj + Σfjp * PLp, for all j€ outbound trucks, for all p € Products
# for j in [truck for truck in trucks if truck.startswith('O')]:
#     prob += dv[j] >= av[j] + pulp.lpSum(fvp[j, p] * PLp[p] for p in products), f"Constraint_Arrival_Product_{p}_Truck_{j}"

# # Adding constraint dj <= lj for all outbound trucks
# for j in [truck for truck in trucks if truck.startswith('O')]:
#     prob += dv[j] <= lj, f"Departure_Bound_of_{j}"

# Adding constraint a_j >= d_i + TE - M * (1 - ΣPijk) for all i, j belonging to inbound trucks; i ≠ j
for i in [truck for truck in trucks if truck.startswith('I')]:
    for j in [truck for truck in trucks if truck.startswith('I')]:
        if i != j:
            prob += av[j] >= dv[i] + TE - M * (1 - pulp.lpSum(Pijk[i, j, k] for k in docks)), f"Constraint_Inbound_{i}_{j}"


# Adding constraint a_j >= d_i + TE - M * (1 - Σqijk) for all i, j belonging to outbound trucks; i ≠ j
for i in [truck for truck in trucks if truck.startswith('O')]:
    for j in [truck for truck in trucks if truck.startswith('O')]:
        if i != j:
            prob += av[j] >= dv[i] + TE - M * (1 - pulp.lpSum(qijk[i, j, k] for k in docks)), f"Constraint_Outbound_{i}_{j}"


# Adding constraint a_j >= a_i + TE - M * (2 - yik - zjk) for all i belonging to Inbound trucks,
# for all j belonging to Ougdt !tbound trucks, for all k belonging to docks
for i in [truck for truck in trucks if truck.startswith('I')]:
    for j in [truck for truck in trucks if truck.startswith('O')]:
        for k in docks:
            prob += av[j] >= av[i] + TE - M * (2 - yik[i, k] - Zik[j, k]), f"Constraint_Arrival_{i}_{j}_{k}"


# Adding constraint a_j + M*(3 - vij1 - yik - zjk) >= d_i + ΣXijp1 * Wkk' 
# for all i belonging to Inbound trucks, for all j belonging to Outbound trucks,
# for all k, k' belonging to docks, for all p from 1 to |P|
for i in [truck for truck in trucks if truck.startswith('I')]:
    for j in [truck for truck in trucks if truck.startswith('O')]:
        for k in docks:
            for k_prime in docks:
                if k != k_prime:  # Ensure k and k_prime are different
                    prob += av[j] + M * (3 - Vijs[i, j, 'S1'] - yik[i, k] - Zik[j, k_prime]) >= dv[i] + pulp.lpSum(Xijps[i, j, 'P1', 'S1'] * Wkk_prime[k, k_prime] for p in products), f"Constraint_Arrival_Dock_{k}_{k_prime}_{i}_{j}"


# Adding constraint a_j + M*(1 - vij2) >= d_i + ΣXijp2 * TS
# for all i belonging to Inbound trucks, for all j belonging to Outbound trucks, for all p from 1 to |P|
for i in [truck for truck in trucks if truck.startswith('I')]:
    for j in [truck for truck in trucks if truck.startswith('O')]:
        prob += av[j] + M * (1 - Vijs[i, j, 'S2']) >= dv[i] + pulp.lpSum(Xijps[i, j, 'P2', 'S2'] * TS for p in products), f"Constraint_Arrival_Outbound_{i}_{j}"


# Adding constraint Σyik = 1 for all i belonging to Inbound trucks
for i in [truck for truck in trucks if truck.startswith('I')]:
    prob += pulp.lpSum(yik[i, k] for k in docks) == 1, f"Constraint_Dock_Assignment_{i}"


# # Adding constraint ΣZjk = 1 for all j belonging to Outbound trucks
for j in [truck for truck in trucks if truck.startswith('O')]:
    prob += pulp.lpSum(Zik[j, k] for k in docks) == 1, f"Constraint_Outbound_Dock_Assignment_{j}"


# Adding constraint Pijk + Pjik <= 1 for all i, j belonging to Inbound trucks where i != j and for all k belonging to Docks
for i in [truck for truck in trucks if truck.startswith('I')]:
    for j in [truck for truck in trucks if truck.startswith('I')]:
        if i != j:
            for k in docks:
                prob += Pijk[i, j, k] + Pijk[j, i, k] <= 1, f"Constraint_Dock_Assignment_{i}_{j}_{k}"

# Adding constraint qijk + qjik <= 1 for all i, j belonging to Outbound trucks where i != j and for all k belonging to Docks
for i in [truck for truck in trucks if truck.startswith('O')]:
    for j in [truck for truck in trucks if truck.startswith('O')]:
        if i != j:
            for k in docks:
                prob += qijk[i, j, k] + qijk[j, i, k] <= 1, f"Constraint_Dock_Assignment_{i}_{j}_{k}"


# Adding constraint Pijk + Pjik >= yik + yjk - 1 for all i, j belonging to Inbound trucks where i > j and for all k belonging to Docks
for i in [truck for truck in trucks if truck.startswith('I')]:
    for j in [truck for truck in trucks if truck.startswith('I')]:
        if i != j:
            if trucks.index(i) > trucks.index(j):
                for k in docks:
                    prob += Pijk[i, j, k] + Pijk[j, i, k] >= yik[i, k] + yik[j, k] - 1, f"Constraint_Dock_Assignment_GT_{i}_{j}_{k}"


# Adding constraint qijk + qjik >= Zik + Zjk -1 for all i, j belonging to Outbound trucks; i > j for all k belonging to Docks
for i in [truck for truck in trucks if truck.startswith('O')]:
    for j in [truck for truck in trucks if truck.startswith('O')]:
        if i != j:
            if trucks.index(i) > trucks.index(j):
                for k in docks:
                    prob += qijk[i, j, k] + qijk[j, i, k] >= Zik[i, k] + Zik[j, k] - 1, f"Constraint_Outbound_Dock_Assignment_GT_{i}_{j}_{k}"

T = pulp.LpVariable("T", lowBound=0, cat='Continuous')
c = pulp.LpVariable("c", lowBound=0, cat='Continuous')
F = pulp.LpVariable("F", lowBound=0, cat='Continuous')
d = pulp.LpVariable("d", lowBound=0, cat='Continuous')
L = pulp.LpVariable("L", lowBound=0, cat='Continuous')

x = pulp.LpVariable("x", lowBound=0, cat='Integer')

v = pulp.LpVariable("v", cat='Binary')
p = pulp.LpVariable("p", cat='Binary')
q = pulp.LpVariable("q", cat='Binary')
y = pulp.LpVariable("y", cat='Binary')
z = pulp.LpVariable("z", cat='Binary')

prob.solve()

if pulp.LpStatus[prob.status] == "Optimal":
    print("Feasible Solution Found!")
   
    for v in trucks:
        print(f"Arrival Time of Truck {v}: {av[v].value()}")
else:
    print("No Feasible Solution Found!")
