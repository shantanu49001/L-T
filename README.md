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

### 2. Warehouse Transportation Problem:
This model solves a warehouse transportation problem using optimization techniques.

#### Setting Up the Problem:
Defined the problem using the Python Pulp library to minimize the time between the arrival of the first inbound truck and the departure of the last outbound truck.

#### Defining Variables & Constraints:
Define variables representing truck arrival/departure times and product movement, adding constraints to ensure adherence to specific rules.

#### Defining Objective Function:
Define an objective function to minimize the time between truck arrival and departure.

#### Solving the Problem:
The optimization problem is solved using the solve() method.

#### Checking the Solution:
If an optimal solution is found, the arrival times of each truck are printed; otherwise, it indicates no feasible solution.

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
- Using algorithms like Ant Colony Optimization (ACO) can help find near-optimal solutions to such combinatorial optimization problems by iteratively exploring and exploiting search space, leveraging pheromone trails to guide the search towards promising regions, and incorporating heuristic information to guide decision-making.
- By applying ACO or similar optimization algorithms to this dataset, we can expect to find routes that minimize the total distance traveled by the vehicles, optimize resource utilization, and ensure timely delivery to customers within their specified time windows.

## Implementation

To solve the VRPTW problem efficiently, we can implement algorithms like Ant Colony Optimization (ACO). ACO is a metaheuristic optimization algorithm inspired by the foraging behavior of ants. It iteratively constructs solution paths by simulating the pheromone-based communication among ants. This allows the algorithm to converge towards optimal or near-optimal solutions.

### Example Application

We can use the provided dataset as input for the ACO algorithm. The algorithm will iteratively explore and exploit the solution space, finding optimal or near-optimal routes for the vehicles to deliver goods to customers within their time windows while minimizing total travel distance and respecting vehicle capacities.

### Result Visualization

We can visualize the solution obtained from the ACO algorithm using various plotting libraries in Python. Below is an example GIF showing the convergence of the ACO algorithm and the final routes obtained for the vehicles.

![ACO Algorithm Convergence](https://github.com/shantanu49001/L-T/blob/main/c101-example.gif)
