# SIMATS ENGINEERING
## ASSESSMENT TOOL 3 — DESCRIPTIVE WRITTEN TEST
**COURSE NAME:** ARTIFICIAL INTELLIGENCE  
**COURSE CODE:** CSA-1709 / CSA17  
**DONE BY:** Rithin Sai A (1972260016)  
**COURSE OUTCOME COVERED:** CO1: Apply AI basics such as intelligent agents and uninformed search methods to solve problems effectively. (BL3)  
**Assessment Tool Weightage:** 30% | **Duration:** 45 Minutes | **Total Marks:** 20  
**Annexure A:** Descriptive Written Test  

---

### Code of Conduct:
*I A. Rithin Sai (1972260016) certify that this submission is my original work and that I have adhered to the guidelines specified for this assessment. I understand that any violation of academic integrity rules will result in disciplinary action.*  
**Signature of the student:** A. Rithin Sai  

---

## QUESTION 1: SMART HOME AUTOMATION SYSTEM — INTELLIGENT AGENTS

### Problem Statement
A smart home automation system is being designed to manage lighting, temperature, and security based on user behavior and environmental conditions. The system must respond to real-time inputs such as motion detection, temperature changes, and time of day while also learning user preferences over time. In this context:
1. Explain the different types of intelligent agents (simple reflex, model-based, goal-based, and utility-based agents).
2. Analyze how each type would function within this system.
3. Justify which type of agent or hybrid approach would be most effective for ensuring comfort, energy efficiency, and security.

---

### Detailed Solution & Analysis

A **Smart Home Automation System** uses intelligent agents to control lighting, climate (HVAC), and security systems based on user behavior and dynamic environmental conditions. It interacts with the physical environment via:
- **Sensors:** Passive Infrared (PIR) motion detectors, ambient luminosity sensors, digital temperature/humidity sensors, magnetic door/window contact sensors, and surveillance cameras.
- **Actuators:** Smart lighting relays/dimmers, motorized HVAC thermostats and dampers, electronic door deadbolts, motorized window blinds, and alarm sirens/push notifications.

#### 1. Simple Reflex Agent
- **Operating Principle:** Operates strictly on the current percept, ignoring percept history, using pre-programmed condition-action rules:
  $$\text{condition} \to \text{action}$$
- **Function in Smart Home:**
  - *Lighting:* If a PIR sensor detects motion in a corridor and ambient light is $< 50\text{ lux}$, turn on the corridor lights. If no motion is detected for 5 minutes, turn the lights off.
  - *Safety:* If a smoke detector senses particulates above threshold, immediately trigger the fire alarm and cut gas supply.
- **Limitations:** Cannot handle partial observability, sensor noise, or contextual nuances (e.g., cannot distinguish between an empty room and a resident reading quietly on a sofa).

#### 2. Model-Based Reflex Agent
- **Operating Principle:** Maintains an internal state (a model of how the world evolves and how actions alter it) to handle unobservable aspects of the environment.
- **Function in Smart Home:**
  - *Occupancy & Thermal Tracking:* Tracks which rooms are occupied, current heat retention rates, whether exterior windows/doors are ajar, and HVAC status.
  - *Contextual Reasoning:* If a room temperature reading suddenly drops while heating is active, the agent infers that a window has been opened rather than erroneously driving the furnace to maximum output.

#### 3. Goal-Based Agent
- **Operating Principle:** Evaluates future states and formulates action plans to achieve explicit desirable goals.
- **Function in Smart Home:**
  - *Target States:* Goals include *"Maintain bedroom temperature at 22°C between 10:00 PM and 6:00 AM"*, *"Secure all exterior deadbolts by 11:00 PM"*, or *"Pre-cool living area before user arrives home at 6:30 PM"*.
  - *Flexibility:* Goals can be updated dynamically through smartphone apps or voice commands without rewriting underlying condition-action rules.

#### 4. Utility-Based Agent
- **Operating Principle:** Uses an explicit utility function $U(s)$ mapping states to real numbers, quantifying the degree of satisfaction when trading off conflicting objectives:
  $$\max \sum w_i U_i(s)$$
- **Function in Smart Home:**
  - *Comfort vs. Energy Cost:* Resolves the trade-off between occupant thermal comfort and electricity tariff expenses. During peak tariff hours (e.g., 2:00 PM – 6:00 PM), running air conditioning at maximum capacity maximizes comfort but causes severe energy costs. The utility-based agent balances both by setting the thermostat to 24°C, lowering solar blinds to reduce heat gain, and deferring laundry appliances.
  - *Security Prioritization:* If an anomalous perimeter breach is detected at night, the agent elevates security utility over energy conservation, activating high-intensity floodlights and alerting law enforcement.

#### 5. Learning Agent
- **Operating Principle:** Continuously observes user habits and feedback over time to adapt and optimize its behavior autonomously.
- **Function in Smart Home:**
  - *Routine Learning:* Automatically learns the resident's waking schedule, preferred sleeping temperatures across seasons, and lighting dimming preferences.
  - *Autonomous Refinement:* Eliminates repetitive manual programming by predicting needs before the user explicitly requests them.

---

### Comparative Evaluation of Agent Types

| Agent Type | Operational Mechanism | Smart Home Application | Key Strengths & Trade-offs |
|:---|:---|:---|:---|
| **Simple Reflex** | Condition-action rules on current percept | Motion-triggered lights; smoke alarms | Rapid real-time execution; brittle in partially observable spaces. |
| **Model-Based** | Internal state model tracking world dynamics | Occupancy awareness; open-window compensation | Context-aware; requires accurate state transition model. |
| **Goal-Based** | Search and planning toward target states | Pre-scheduled cooling; night security lockdown | Highly flexible goals; does not inherently balance competing trade-offs. |
| **Utility-Based** | Multi-attribute utility optimization | Balancing comfort vs electricity bills | Optimal trade-off resolution; complex utility modeling. |
| **Learning Agent** | Feedback learning adapting behavior over time | Personal habit learning (temperature/schedule) | Autonomous personalization; requires learning time and data stability. |
| **Hybrid Agent** | Hierarchical integration of reflex, model, utility & learning | Full smart home autonomous management | Combines real-time reflex speed with context, optimization, and adaptivity. |

---

### Justification of the Most Effective Approach: Hybrid Intelligent Agent
No single classical agent architecture satisfies all operational requirements of a smart home:
1. **Reflex Layer:** Provides sub-second reaction times for critical safety events (fire, intrusion, instant lighting).
2. **Model-Based Layer:** Maintains persistent state awareness across rooms despite intermittent sensor readings.
3. **Utility-Based Layer:** Systematically resolves trade-offs between electric utility costs and thermal comfort.
4. **Learning Layer:** Adapts internal models and threshold parameters to user habits over time.

**Conclusion:** A **Hybrid Intelligent Agent** layering immediate reflex behaviors over an internal model, guided by multi-objective utility optimization and continuous machine learning, is the most robust and effective architecture for delivering comfort, energy efficiency, and security.

---

## QUESTION 2: ROBOT FINDING AN EXIT IN AN UNKNOWN MAZE USING UCS AND IDS

### Problem Statement
A robot is placed in an unknown maze and must find a path to the exit without prior knowledge of the layout.
1. Explain how uninformed search strategies like Uniform Cost Search (UCS) and Iterative Deepening Search (IDS) can help solve this problem.
2. Discuss the advantages and disadvantages of these algorithms in terms of time and space complexity.
3. Relate the problem to different types of intelligent agents and explain how agent design affects decision-making.
4. Suggest which combination of agent type and search strategy would be most effective and justify your choice.

---

### Detailed Solution & Analysis

In an unknown maze, the robot lacks an environmental blueprint and exit coordinates, making heuristic estimation (like Manhattan distance to goal) impossible. The robot senses adjacent cells online (detecting walls and open passages) and must employ **uninformed (blind) search strategies**.

#### 1. Uniform Cost Search (UCS)
- **Mechanism:** Expands the unvisited frontier node with the lowest cumulative path cost $g(n)$ from the start node:
  $$g(n) = \sum \text{step\_cost}$$
  UCS maintains candidate paths inside a Priority Queue (min-heap).
- **Behavior in Maze:**
  - If all grid movements have equal step cost ($c = 1$), UCS expands nodes in concentric rings identical to Breadth-First Search (BFS).
  - If step costs vary (e.g., traversing rubble costs 3, inclined ramps cost 2, flat floor costs 1), UCS guarantees finding the cheapest total path.
- **Completeness & Optimality:** Complete and optimal if every step cost is strictly positive: $\text{step\_cost} \ge \epsilon > 0$.
- **Complexity:**
  - *Time Complexity:* $\mathcal{O}(b^{1 + \lfloor C^*/\epsilon \rfloor})$, where $b$ is the branching factor and $C^*$ is optimal path cost.
  - *Space Complexity:* $\mathcal{O}(b^{1 + \lfloor C^*/\epsilon \rfloor})$ — **Exponential memory** required because every generated frontier path must be stored in memory simultaneously.

#### 2. Iterative Deepening Search (IDS)
- **Mechanism:** Combines the minimal linear space requirements of Depth-First Search (DFS) with the completeness and optimality of Breadth-First Search (BFS). It repeatedly executes Depth-Limited Search (DLS), incrementally expanding the cutoff depth:
  $$\text{limit} = 0, 1, 2, \dots, d$$
  until the exit is reached at depth $d$.
- **Overhead of Node Regeneration:** Shallow nodes are regenerated across iterations, but due to exponential branching ($b$), the vast majority of nodes reside at the bottom level. The regeneration overhead is approximately:
  $$\frac{b}{b-1}$$
  For a grid maze with $b \approx 3$, the overhead is only $\sim 50\%$, an acceptable trade-off for eliminating exponential memory storage.
- **Completeness & Optimality:** Complete for finite branching factor $b$; optimal when all step costs are equal (uniform step costs).
- **Complexity:**
  - *Time Complexity:* $\mathcal{O}(b^d)$, asymptotically identical to BFS.
  - *Space Complexity:* $\mathcal{O}(b \cdot d)$ — **Strictly linear memory** proportional to path depth.

---

### Complexity Comparison

| Algorithm | Time Complexity | Space Complexity | Completeness | Optimality | Memory Practicality |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Uniform Cost Search (UCS)** | $\mathcal{O}(b^{1 + \lfloor C^*/\epsilon \rfloor})$ | $\mathcal{O}(b^{1 + \lfloor C^*/\epsilon \rfloor})$ | Yes (if step cost $\ge \epsilon > 0$) | Optimal for any non-negative cost | Poor on embedded systems; causes Out-Of-Memory (OOM) |
| **Iterative Deepening Search (IDS)** | $\mathcal{O}(b^d)$ | $\mathcal{O}(b \cdot d)$ | Yes (for finite $b$) | Optimal for uniform step cost ($c=1$) | Excellent; minimal RAM usage |

---

### Relationship to Intelligent Agent Types & Decision Making
1. **Simple Reflex Agent:** Cannot explore a maze systematically; without memory or map state, it gets trapped in local cycles and dead ends.
2. **Model-Based Agent:** Essential for physical maze traversal. Maintains an internal occupancy grid mapping explored cells, discovered walls, and visited frontiers, preventing the physical robot from repeatedly crashing or circling endlessly.
3. **Goal-Based Agent:** Maintains an explicit goal test (`current_pos == exit_pos`) and plans actions systematically to reach the goal.

---

### Recommendation & Justification of Most Effective Combination

#### Case A: Standard Grid Maze with Uniform Movement Cost (Step Cost = 1)
- **Recommended Combination:** **Model-Based Goal-Based Agent using Iterative Deepening Search (IDS)**.
- **Justification:** Embedded mobile robots (microcontrollers, Raspberry Pi, Arduino) have severely limited onboard RAM. UCS rapidly exhausts available memory by maintaining exponential queues ($\mathcal{O}(b^d)$). In contrast, IDS guarantees finding the shallowest, shortest path to the exit while consuming strictly linear space ($\mathcal{O}(b \cdot d)$), leaving ample memory for sensor processing and mapping.

#### Case B: Heterogeneous Maze with Non-Uniform Movement Costs (Terrain / Battery Variation)
- **Recommended Combination:** **Model-Based Goal-Based Agent using Uniform Cost Search (UCS)** with online replanning.
- **Justification:** When movements through mud, incline, or narrow corridors carry different energy/time penalties, IDS cannot guarantee an optimal path because it assumes uniform edge weights. UCS is strictly necessary to compute the minimum-cost exit trajectory.

---

## CONCLUSION
1. In **Question 1**, the analysis of intelligent agent architectures confirms that a **Hybrid Agent**—integrating reactive speed, model-based world tracking, utility-based optimization, and learning adaptivity—is the only architecture that simultaneously guarantees comfort, energy conservation, and robust security in a smart home.
2. In **Question 2**, comparing uninformed search strategies demonstrates that **Iterative Deepening Search (IDS)** is the superior choice for memory-constrained embedded robots navigating uniform-cost mazes due to its linear memory $\mathcal{O}(bd)$ and optimal path guarantees, whereas **Uniform Cost Search (UCS)** is the required algorithm when terrain and battery expenditures introduce non-uniform step costs.
