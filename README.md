# L&T CreaTech Project - Peaky Balwinders
<p align="center">
  <img src="https://github.com/shantanu49001/L-T/blob/main/logo.png" alt="L&T CreaTech Logo">
</p>


## Team Members:
1. Shantanu Tiwari - ECE, 3rd Year
2. Pritesh Lohot - CSE, 3rd Year
3. Aayush Singh - ECE, 3rd Year

## Campus Name:
Indian Institute of Information Technology Guwahati (IIIT-G)

## Construction Material Sourcing and Supply Chain Optimization

### 1. (A) Material Sourcing:
#### A1. Challenges in Material Quality Assurance:
Businesses often face challenges in ensuring the required quality of construction materials like steel, cement, tiles, pipes, and valves. Parameters such as texture, color, and water content are crucial but difficult to verify consistently.

#### A2. AI-driven Solution:
To address this, we've implemented an AI-driven solution using OpenCV for image processing. The algorithm compares uploaded images of materials with reference images, calculating a match percentage to verify quality.

#### A3. Extended Functionality:
The algorithm can also measure dimensions, enhancing assurance of both visual quality and dimensional accuracy of supplied materials.

#### B1. Material Repository & Order Placement:
Our platform hosts a repository of materials categorized by type and region. Suppliers upload images of actual products during order placement.

#### B2. Image Processing Algorithm:
Leveraging OpenCV, the algorithm enhances uploaded images and compares features using various matching algorithms to assess product quality.

#### B3. User Feedback:
Users receive quality percentage feedback, empowering them to make informed procurement decisions based on quality standards.

### B4. Results:
<p align="center">
  <img src="https://github.com/shantanu49001/L-T/blob/main/Platform-1.png" alt="L&T CreaTech Logo">
  <br/>
  <img src="https://github.com/shantanu49001/L-T/blob/main/Platform-2.png" alt="L&T CreaTech Logo">
  <br/>
  <img src="https://github.com/shantanu49001/L-T/blob/main/Platform-3.png" alt="L&T CreaTech Logo">
  <br/>
  <img src="https://github.com/shantanu49001/L-T/blob/main/Screenshot%20(57).png" alt="L&T CreaTech Logo">
  <br/>
</p>


### 2. Warehouse Transportation Problem

This repository contains a Python implementation to solve a warehouse transportation problem using optimization techniques. The problem is formulated as a mixed-integer linear programming (MILP) model aiming to minimize the time between the arrival of the first inbound truck and the departure of the last outbound truck, also known as makespan.

## Problem Description

In a warehouse setting, the problem involves scheduling inbound and outbound trucks at dock locations while transferring products efficiently. The goal is to minimize the overall time spent in the transportation process, leading to several advantages such as:

- *Storage Elimination*: By adopting a cross-docking strategy, the need for storage and order picking operations is eliminated. Products are transferred directly from inbound trucks to outbound trucks, reducing the storage space required in the warehouse.

- *Handling Cost Efficiency*: Storage and order picking are usually the costliest processes in traditional distribution centers. By implementing cross-docking, companies can reduce inventory maintenance costs and labor expenses associated with handling products multiple times.

## Mathematical Model

The mathematical model is implemented using the Python Pulp library and includes the following components:

- *Variables & Constraints*: Define variables representing truck arrival/departure times and product movement, adding constraints to ensure adherence to specific rules.

- *Objective Function*: Define an objective function to minimize the time between truck arrival and departure.

## Input Parameters

The model takes the following input parameters:

- trucks: List of all trucks involved in transportation, categorized as inbound ('I') or outbound ('O').
- products: List of all products being transported.
- docks: List of all dock locations where trucks can load and unload products.
- storage_locations: List of storage locations at docks where products can be stored temporarily.
- fvp: Transfer times between trucks and products.
- PUp: Upper bounds of product quantities.
- PLp: Lower bounds of product quantities.
- Qsk: Maximum capacities of storage locations at docks.
- Wkk_prime: Transfer times between docks.
- TS: Transfer time between storage locations and outbound trucks.
- TE: Transfer time between trucks.
- M: A very large constant used for formulating constraints.
- lj: Departure time limit for outbound trucks.

## Output

The output indicates the results of solving the optimization problem:

- *Feasible Solution Found*: Indicates whether the optimization solver found a feasible solution.
- *Arrival Time of Trucks*: Displays the arrival time for each truck in the problem.

## Sample Example

### Sample Input:

```python
trucks = ['I1', 'I2', 'O1', 'O2']
products = ['P1', 'P2']
docks = ['D1', 'D2']
storage_locations = ['S1', 'S2']
fvp = {
    ('I1', 'P1'): 20, ('I1', 'P2'): 35,
    ('I2', 'P1'): 20, ('I2', 'P2'): 15,
    ('O1', 'P1'): 5, ('O1', 'P2'): 10,
    ('O2', 'P1'): 15, ('O2', 'P2'): 20
}
PUp = {'P1': 100, 'P2': 100}
PLp = {'P1': 100, 'P2': 100}
Qsk = {('S1', 'D1'): 50, ('S1', 'D2'): 50, ('S2', 'D1'): 50, ('S2', 'D2'): 50}
Wkk_prime = {('D1', 'D2'): 0, ('D2', 'D1'): 0}
```

TS = 1
TE = 2
M = 1000000
lj = 5

<p align="center">
  <img src="https://github.com/shantanu49001/L-T/blob/main/WAREHOUSE.jpeg" alt="L&T CreaTech Logo">
</p>




### 3. Ant Colony Optimization (ACO) for Supply Chain Optimization:
Using the provided datasets, the ACO algorithm optimizes supply chain routes, supplier selection, and inventory management.

#### Problem Statement:
Prepare an AI-based model for cost-effective material sourcing, supplier selection, and inventory management along with geotagging from ordering to supply.

#### Algorithm Execution:
The ACO algorithm iteratively finds optimal routes for material delivery considering factors such as transportation costs, supplier reliability, and inventory levels.

#### Advantages:
- Efficiently optimizes supply chain routes considering various constraints.
- Selects reliable suppliers based on predefined criteria and historical performance.
- Recommends optimal inventory management policies for cost-effective inventory levels.

  # Vehicle Routing Problem with Time Windows (VRPTW) Dataset Analysis

## Vehicle Information:

- Number of Vehicles: 25
- Capacity per Vehicle: 200 units

## Customer Information:

- Each customer is represented by a row in the dataset.
- Each row includes:
  - Customer Number (CUST NO.)
  - X and Y coordinates of the customer location (XCOORD., YCOORD.)
  - Demand: The amount of goods demanded by the customer
  - Ready Time: The earliest time at which the customer can be served
  - Due Date: The latest time by which the customer must be served
  - Service Time: The time required to serve the customer

## Output and Efficiency:

- The output of an efficient solution to this problem should be a set of routes for each vehicle, where each route starts and ends at the depot (customer 0), and visits each customer exactly once within their respective time windows while respecting vehicle capacities.
- The goal is to minimize the total distance traveled by the vehicles while ensuring timely delivery and efficient resource utilization.
- An efficient solution would optimize the assignment of customers to vehicles and the sequence in which customers are visited to minimize the overall cost, which includes transportation costs, vehicle operating costs, and potential penalties for late deliveries.
- Using algorithm Ant Colony Optimization (ACO) can help find near-optimal solutions to such combinatorial optimization problems by iteratively exploring and exploiting search space, leveraging pheromone trails to guide the search towards promising regions, and incorporating heuristic information to guide decision-making.
- By applying ACO optimization algorithm to this dataset, we can expect to find routes that minimize the total distance traveled by the vehicles, optimize resource utilization, and ensure timely delivery to customers within their specified time windows.

### Example Application

We can use the provided dataset as input for the ACO algorithm. The algorithm will iteratively explore and exploit the solution space, finding optimal or near-optimal routes for the vehicles to deliver goods to customers within their time windows while minimizing total travel distance and respecting vehicle capacities.

### Result Visualization

We can visualize the solution obtained from the ACO algorithm using various plotting libraries in Python. Below is an example GIF showing the convergence of the ACO algorithm and the final routes obtained for the vehicles.

![ACO Algorithm Convergence](https://github.com/shantanu49001/L-T/blob/main/c101-example.gif)

This is the result of sample dataset c101 of the Vehicle routing problem with Time Windows 

[Hindawi](https://www.hindawi.com/journals/ddns/2018/1295485/) - For detailed explanation of algorithm refer here! :))

# Delivery Encryption and Geotagging with JSON Web Tokens

## Overview

Our web application ensures secure and traceable deliveries by leveraging Delivery Encryption and Geotagging using JSON Web Tokens (JWTs). This document outlines the process and functionality of our system.

## Delivery Encryption and Geotagging

Our web application utilizes geotagging and JSON Web Tokens (JWTs) to ensure secure and traceable deliveries.

### Generation and Management of Tokens

Upon order placement, the web application collects parameters such as seller name, customer name, current geo-location, and previous geo-location for each item to generate a token.

- Unique Signature Generation: These parameters are utilized to create a unique signature for each commodity using JSON Web Tokens (JWTs).
- Verification and Updating at Distribution Centers:
  - At every distribution center, the previous JWT associated with the commodity is verified based on customer and seller details and location data at the center available via its token.
  - Once verified, the JWT is updated with the current geo-location information and signed.
  - The updated token, along with the new location data, is pushed to the user model database for record-keeping.
- Final Destination Verification and Expiry:
  - Upon reaching the final destination, the last JWT is verified against the original order details.
  - If all details match, the token is marked as inactive and expires using the built-in features of JWTs.
  - Expired tokens are saved in the customer database model as a reference for order history and future analytical data.

<p align="center">
  <img src="https://github.com/shantanu49001/L-T/blob/main/jwt.png" alt="L&T CreaTech Logo">
   
 

</p>
 <img src="https://github.com/shantanu49001/L-T/blob/main/jwt2.png" alt="L&T CreaTech Logo">
## Implementation Details

### 1. Generation of Consignment Token

- Header: `{supp_id, cust_id}`
- Secret: `{prev_loc, curr_loc}`

### 2. Token Verification and Update at Distribution Centers

- At each center, the token details are verified, and the token is updated with the current center's information.

## Usage

Instructions for using the system/API.
