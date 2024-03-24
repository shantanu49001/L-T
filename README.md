# L&T CreaTech Project - Peaky Balwinders

## Team Members:
1. Shantanu Tiwari - ECE, 3rd Year
2. Pritesh Lohot - CSE, 3rd Year
3. Aayush Singh - ECE, 3rd Year

## Campus Name:
Indian Institute of Information Technology Guwahati (IIITG)

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
This code solves a warehouse transportation problem using optimization techniques.

#### Setting Up the Problem:
Define the problem using the Python Pulp library to minimize time between the arrival of the first inbound truck and the departure of the last outbound truck.

#### Defining Variables & Constraints:
Define variables representing truck arrival/departure times and product movement, adding constraints to ensure adherence to specific rules.

#### Defining Objective Function:
Define an objective function to minimize the time between truck arrival and departure.

#### Solving the Problem:
Optimization problem is solved using the solve() method.

#### Checking the Solution:
If an optimal solution is found, arrival times of each truck are printed; otherwise, it indicates no feasible solution.

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

## Conclusion:
These solutions leverage AI-driven approaches and optimization techniques to streamline material sourcing, warehouse transportation, and supply chain management, ultimately enhancing efficiency and cost-effectiveness in construction projects.
