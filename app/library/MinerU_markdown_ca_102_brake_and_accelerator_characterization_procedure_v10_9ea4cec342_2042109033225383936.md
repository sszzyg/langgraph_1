# Brake and accelerator characterization procedure

Crash Avoidance 

# Technical Bulletin CA 102

Implementation January 2026 

# PREFACE

DISCLAIMER: Euro NCAP has taken all reasonable care to ensure that the information published in this protocol is accurate and reflects the technical decisions taken by the organisation. In the unlikely event that this protocol contains a typographical error or any other inaccuracy, Euro NCAP reserves the right to make corrections and determine the assessment and subsequent result of the affected requirement(s). 

# CONTENTS

# INTRODUCTION 3

# 1 BRAKE CHARACTERIZATION PROCEDURE 4

Definitions 4 

Measurements 4 

Brake Characterization Procedure 4 

# 2 ACCELERATOR CHARACTERIZATION PROCEDURE 7

Definitions 7 

Measurements 7 

Procedure for Crossing and Turn across path scenarios 7 

Procedure for Manoeuvring Reverse scenarios 9 

# INTRODUCTION

This document outlines the brake and characterization procedures that must be followed by the Test Laboratory at the time of conducting tests for Euro NCAP Crash Avoidance – Frontal Collisions and Low Speed Collisions protocols. 

# 1 BRAKE CHARACTERIZATION PROCEDURE

The braking input characterisation test determines the brake pedal displacement and force necessary to achieve a vehicle deceleration typical of that produced by a typical real-world driver in emergency situations. 

# Defi ni tio ns

TBRAKE - The point in time where the brake pedal displacement exceeds 5mm. 

T-6m/s2 - The point in time is defined as the first data point where filtered, zeroed and corrected longitudinal acceleration data is less than $- 6 m / \mathsf { s } ^ { 2 }$ . 

T-2m/s2, T-4m/s2 - similar to T-6m/s2. 

# Measurements

Measurements and filters to be applied as described in the Crash Avoidance protocols. 

# Brake Characterization Procedure

First perform the brake and tyre conditioning tests as described in 7.1.2 and 7.1.3. The brake input characterisation tests shall be undertaken within 10 minutes after conditioning the brakes and tyres. 

# 1.3.1 Brake Displacement Characterisation Tests

• Push the brake pedal through the full extent of travel and release. 

Accelerate the VUT to a speed in excess of 85km/h. Vehicles with an automatic transmission will be driven in D. For vehicles with a manual transmission select the highest gear where the RPM will be at least 1500 at the 85km/h. 

Release the accelerator and allow the vehicle to coast. At a speed of $8 0 \pm 1 . 0 \mathrm { k m / h }$ initiate a ramp braking input with a pedal application rate of $2 0 { \pm } 5 \mathsf { m m } / \mathsf { s }$ and apply the brake until a longitudinal acceleration of $- 7 \mathsf { \ m } / \mathsf { s } ^ { 2 }$ is achieved. For manual transmission vehicles, press the clutch as soon as the RPM drops below 1500. The test ends when a longitudinal acceleration of $- 7 m / \mathsf { S } ^ { 2 }$ is achieved. 

Measure the pedal displacement and applied force normal to the direction of travel of the initial stroke of the brake pedal, or as close as possible to normal as can be repeatedly achieved. 

1.3.1.1 Perform three consecutive test runs. A minimum time of 90 seconds and a maximum time of 10 minutes shall be allowed between consecutive tests. If the maximum time of 10 minutes is exceeded, perform three brake stops from 72 km/h at approximately 0.3g. 

Using second order curve fit and the least squares method between $\mathsf { T } { \cdot } 2 \mathsf { m } / \mathsf { s } ^ { 2 }$ , $\mathsf { T } { \cdot } 6 \mathsf { m } / \mathsf { s } ^ { 2 }$ , calculate the pedal travel value corresponding to a longitudinal acceleration of $- 4 \ m / \mathsf { s } ^ { 2 }$ $\scriptstyle ( = \mathsf { D } 4$ , unit is m). Use data of at least three valid test runs for the curve fitting. 

• This brake pedal displacement is referred to as D4 in the next chapters. 

Using second order curve fit and the least squares method between $\mathsf { T } { \cdot } 2 \mathsf { m } / \mathsf { s } ^ { 2 }$ , $\mathsf { T } { \cdot } 6 \mathsf { m } / \mathsf { s } ^ { 2 }$ , calculate the pedal force value corresponding to a longitudinal acceleration of $- 4 \ m / \mathsf { s } ^ { 2 }$ $( = \mathsf { F 4 }$ , unit is N). Use data of at least three valid test runs for the curve fitting. 

• This brake pedal force is referred to as F4 in the next chapters. 

# 1.3.2 Brake Force Confirmation and Iteration Procedure

Accelerate the VUT to a speed of $8 0 + 1 \ k m / \mu$ . Vehicles with an automatic transmission will be driven in D. For vehicles with a manual transmission select the highest gear where the RPM will be at least 1500 at the 80km/h. 

Apply the brake force profile as specified in 1.3.3, triggering the input manually rather than in response to the FCW. Determine the mean acceleration achieved during the window from TBRAKE $+ 1 \mathsf { s }$ TBRAKE $+ 3 5$ . If a mean acceleration outside the range of $\mathsf { - 4 } \mathsf { \Pi } _ { - 0 . 5 } \mathsf { m } / \mathsf { s } ^ { 2 }$ results, apply the following method to ratio the pedal force applied. 

F4new $=$ F4original * (-4/mean acceleration), i.e. if F4original results in a mean acceleration of - $5 \mathsf { m } / \mathsf { S } ^ { 2 }$ , F4new $=$ F4original * -4 / -5 

Repeat the brake force profile with this newly calculated F4, determine the mean acceleration achieved and repeat the method as necessary until a mean acceleration within the range of $- 4 - 0 . 5 \mathrm { m } / \mathsf { s } ^ { 2 }$ is achieved. 

1.3.2.1 Three valid pedal force characteristic tests (with the acceleration level being in the range as specified) are required. A minimum time of 90 seconds and a maximum time of 10 minutes shall be allowed between consecutive tests. If the maximum time of 10 minutes is exceeded, perform three brake stops from $7 2 \mathrm { k m / h }$ at approximately 0.3g. 

before restarting the brake pedal force characterisation tests. This brake pedal force is referred as F4 in the next chapters. 

# 1.3.3 Brake Application Profile

• Detect TFCW during the experiment in real-time. 

• Release the accelerator at TFCW + 1 s. 

Perform displacement control for the brake pedal, starting at $\mathsf { T F C W } + 1 . 2$ s with a gradient of the lesser of $5 \times { \mathsf { D 4 } }$ or 400mm/s (meaning the gradient to reach pedal position D4 within 200ms, but capped to a maximum application rate of 400mm/s). 

Monitor brake force during displacement control and use second-order filtering with a cut-off frequency between 20 and $1 0 0 \mathsf { H z }$ (online) as appropriate. 

• Switch to force control, maintaining the force level, with a desired value of F4 when i. the value D4 as defined in 1.3.1.1 is exceeded for the first time, 

ii. the force F4 as defined in 1.3.1.1 is exceeded for the first time, whichever is reached first. 

The point in time where position control is switched to force control is noted as Tswitch. 

Maintain the force within boundaries of $F 4 \pm 2 5 \%$ F4. A stable force level should be achieved within a period of 200ms maximum after the start of force control. Additional disturbances of the force over ± 25% F4 due to further AEB interventions are allowed, as long as they have a duration of less than 200ms. 

The average value of the force between TFCW + 1.4s and the end of the test should be in the range of $\mathsf { F } 4 \pm 1 0 \mathsf { N }$ . 

# 2 ACCELERATOR CHARACTERIZATION PROCEDURE

The accelerator pedal characterization test determines the accelerator pedal displacement and accelerator pedal application velocity necessary to achieve a typical vehicle drive-away acceleration in junction, turning and manoeuvring situations. In addition, the corresponding synchronization timing between VUT and GVT is determined with the obtained speed profile. 

# Defi ni tio ns

• TStart, Time when VUT filtered acceleration reaches [0.1] m/s2 TStart 

• TEnd, time where VUT meets the impact point location TEnd 

• TAvg, average time value of ${ \sf T } _ { \sf E n d }$ from all the executed trials TAvg 

# Measurements

Measurements and filters to be applied as described in the Crash Avoidance protocols. 

# Procedure for Crossing and Turn across path scenarios

Via an iterative approach the accelerator pedal position has to be examined to achieve the following: 

The longitudinal acceleration shall not exceed 1 m/s² before TStart + 0.5 seconds. 

The longitudinal acceleration shall not exceed $1 . 7 5 \ : \mathsf { m } / \mathsf { s } ^ { 2 }$ at any point and shall exceed $1 \mathsf { m } / \mathsf { s } ^ { 2 }$ from TStart + 1.25 until TEnd. 

Execute the start action as trial (without the GVT) at least three times. TEnd of all runs should be inside of an Interval of [0.1 s]. The results from the trials are used to determine the accelerator pedal position and ${ \sf T } _ { \sf A v g }$ which constitute the parameters for the test. 

Thereby, TAvg is used to trigger the start action of the VUT to ensure correct synchronization to the target. With the known time that the VUT needs to reach the impact location, it can be triggered by the approaching target and its known time to reach the impact point location. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/0085bbd1-12ac-4da4-910d-d649128169f4/b43165235700244236868dd5d519ffe1e2852612e805fe74671e10ba2d1f1296.jpg)


In the event that the above method does not satisfy the test requirements, or that the intended vehicle to be tested (i.e. vehicle with base safety pack) is only offered with a manual transmission and has Start-from-Stop capabilities, the OEM shall contact Euro NCAP to discuss an alternative approach. 


Procedure for Manoeuvring Reverse scenarios


<table><tr><td>Category</td><td>Automatic</td><td>Automatic with Auto Hold</td><td>EV with Auto Hold</td><td>Manual</td></tr><tr><td>Gearbox Type</td><td>Automatic</td><td>Automatic</td><td>Automatic (EV)</td><td>Manual</td></tr><tr><td>Auto Hold Functionality</td><td>None</td><td>Auto Hold</td><td>Auto Hold</td><td>With or without Auto Hold</td></tr><tr><td>Creep Functionality</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Creep Description</td><td>The vehicle begins creeping immediately after releasing the brake.</td><td>The vehicle creeps after an initial activation of the accelerator robot (AR). It continues creeping after releasing AR.</td><td>Requires constant pedal input to move (one-pedal driving mode).</td><td>Reverse speed control is managed using the clutch.</td></tr><tr><td>Steering Control</td><td>Follows a straight-line path</td><td>Follows a straight-line path</td><td>Follows a straight-line path</td><td>To be determined</td></tr><tr><td>Brake Control</td><td>Holds with 150N force, then releases the brake.</td><td>Holds with 150N force, then releases the brake after 200ms.</td><td>Holds with 150N force, then releases the brake after 200ms.</td><td>To be determined</td></tr><tr><td>Accelerator Control</td><td>No action required.</td><td>- Short activation of the accelerator robot (AR). 
- AR is held for 350ms before release. 
- Calibration run: AR hold level at 10 kph, apply rate ≈ 100%/s.</td><td>- Accelerator robot is applied and held. 
- Calibration run: AR hold level at 10 kph, apply rate ≈ 50%/s.</td><td>To be determined</td></tr></table>