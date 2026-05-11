# Crash Avoidance

# Low Speed Collisions

Protocol 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/3d4d672ec231db2f32e80f7d6566c715ac3e2602f662fe09e6817476a59a5e39.jpg)


# PREFACE

During the test preparation, vehicle manufacturers are encouraged to liaise with the laboratory and to check that they are satisfied with the way cars are set up for testing. Where a manufacturer feels that a particular item should be altered, they should ask the laboratory staff to make any necessary changes. Manufacturers are forbidden from making changes to any parameter that will influence the test, such as dummy positioning, vehicle setting, laboratory environment etc. 

It is the responsibility of the test laboratory to ensure that any requested changes satisfy the requirements of Euro NCAP. Where a disagreement exists between the laboratory and manufacturer, the Euro NCAP secretariat should be informed immediately to pass final judgment. Where the laboratory staff suspect that a manufacturer has interfered with any of the set up, the manufacturer's representative should be warned that they are not allowed to do so themselves. They should also be informed that if another incident occurs, they will be asked to leave the test site. 

Whe e the e is ecu ence of the p oblem, the m nuf ctu e ’s ep esent tive will be told to le ve the test site and the Secretary General should be immediately informed. Any such incident may be reported by the Secretary General to the manufacturer and the person concerned may not be allowed to attend further Euro NCAP tests. 

DISCLAIMER: Euro NCAP has taken all reasonable care to ensure that the information published in this protocol is accurate and reflects the technical decisions taken by the organisation. In the unlikely event that this protocol contains a typographical error or any other inaccuracy, Euro NCAP reserves the right to make corrections and determine the assessment and subsequent result of the affected requirement(s). 

# CONTENTS

# DEFINITIONS 2

# 1 MEASURING REQUIREMENTS 6

Reference system 6 

Scenario Parameters 7 

VUT 9 

Targets 1 0 

Measurements and variables 1 2 

2 TEST CONDITIONS 1 5 

Test track 1 5 

Lane Markings 1 5 

Weather Conditions 1 6 

VUT Preparation 1 7 

3 TEST PROCEDURE 1 9 

Car & PTW Scenarios 1 9 

Pedestrian & Cyclist Scenarios 2 7 

4 TEST EXECUTION 3 7 

Performance predictions 3 7 

Verification tests 3 7 

Test Conduct 3 7 

5 ASSESSMENT 4 0 

General requirements 4 0 

Criteria 4 0 

Scoring 4 2 

# APPENDIX A OBSTRUCTION DIMENSIONS 43

# DEFINITIONS

Throughout this protocol the following terms are used: 

Start from Stop (SfS) – a test condition in which the VUT starts moving off from standstill. 

Peak Braking Coefficient (PBC) – the measure of tyre to road surface friction based on the maximum deceleration of a rolling tyre, measured using the American Society for Testing and Materials (ASTM) E1136-10 (2010) standard reference test tyre, in accordance with ASTM Method E 1337-90 (reapproved 1996), at a speed of 64.4 km/h, without water delivery. Alternatively, the method as specified in UNECE R13-H. 

Autonomous Emergency Braking (AEB) – braking that is applied automatically by the vehicle in response to the detection of a likely collision to reduce the vehicle speed and potentially avoid the collision. 

Accelerator Control for Pedal Error (ACPE) – defined in UN R175 as a system that detects misapplication of the accelerator control by the driver and is able to control unintended acceleration. 

Creeping – means the state of motion with the powertrain engaged and operating at idle, and no acceleration or brake demand, up to the Maximum Creeping Speed. 

Maximum Creeping Speed – means the maximum steady state speed which the vehicle achieves on a horizontal surface with the powertrain engaged and operating at idle, and no acceleration or brake demand. 

Door Opening Warning (DOW) – an audio-visual warning that is provided automatically by the vehicle in response to the detection of a likely dooring collision with a passing bicyclist. 

Vehicle width – the widest point of the vehicle ignoring the rear-view mirrors, side marker lamps, tyre pressure indicators, direction indicator lamps, position lamps, flexible mud-guards and the deflected part of the tyre side-walls immediately above the point of contact with the ground. 

Car-to-Pedestrian – a collision between a vehicle and an adult or child pedestrian in its path, when no braking and/or steering action is applied. 

Car-to-Bicyclist – a collision between a vehicle and an adult bicyclist in its path, when no braking and/or steering is applied. 

Car-to-Motorcyclist – a collision between a vehicle and a Motorcyclist in its path, when no braking and/or steering is applied. 

Vehicle under test (VUT) – means the vehicle tested according to this protocol with a pre-crash collision mitigation or avoidance system on board. 

Euro NCAP Pedestrian Target (EPTa) – means the articulated adult pedestrian target used in this protocol as specified in ISO 19206-2:2018 

Euro NCAP Child Target (EPTc) – means the articulated child pedestrian target used in this protocol as specified in ISO 19206-2:2018 

Euro NCAP Bicyclist Target (EBTa) – means the adult bicyclist and bike target used in this protocol as specified in ISO 19206-4:2020 

Euro NCAP 

Version 1.1 — October 2025 

Euro NCAP Motorcyclist Target (EMT) – means the Motorcyclist target used in this protocol as specified in ISO 19206-5. 

Global Vehicle Target (GVT) – means the vehicle target used in this protocol as defined in ISO 19206-3:2021 

Time To Collision (TTC) – means the remaining time before the VUT strikes the test target, assuming that the VUT and test target would continue to travel with the speed it is travelling. 

TAEB – means the time where the AEB system activates. Activation time is determined by identifying the last data point where the filtered acceleration signal is below $- 1 \ m / s ^ { 2 }$ , and then going back to the point in time where the acceleration first crossed $- 0 . 3 \mathsf { m } / \mathsf { s } ^ { 2 }$ 

Vimpact – means the speed at which the profiled line around the front or rear end of the VUT coincides with the virtual box around the test targets (platform not included in the virtual box) EPTa, EPTc, EBTa and EMT as shown in the right part of the figures below. 

Vrel_test – means the relative speed between the VUT and the test target (GVT, EPT, EBT or EMT) by subtracting the longitudinal velocity of the test target from that of the VUT at the start of test. 

Vrel_impact – means the relative speed at which the VUT hits the test target (GVT, EPT, EBT or EMT) by subtracting the longitudinal velocity of the test target from $\mathsf { V } _ { \mathrm { i m p a c t } }$ at the time of collision. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/bb05db9cb2bb2bc93c835abe42ecf29cf72d474d836744c9c1000df5612f5b54.jpg)



Figure 0-1 Front end profile vs EPT, EMT, and EBT targets, and rear end profile vs EPT target.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/e54e571698470480f7e4b02110f9f2e665454130115dc9f6781a6a747181e157.jpg)



Figure 0-2 Front end profile and GVT


# Test Scenarios

Car-to-Bicyclist Dooring Adult (CBDA) – collision between the vehicle’s doo (o n occup nt exiting a vehicle equipped with a sliding door) and a bicyclist traveling alongside the parked vehicle. 

Car-to-Bicyclist Nearside Adult Obstructed (CBNAO) – a collision in which a vehicle travels forwards towards a bicyclist crossing its path cycling from the nearside from behind an obstruction and the frontal structure of the vehicle strikes the bicyclist when no braking action is applied. 

Car-to-Motorcyclist Turn Across Path (CMFtap) – a collision in which a vehicle turns across the path of an oncoming motorcyclist travelling at a constant speed, and the frontal structure of the vehicle strikes the front of the motorcycle. 

Car-to-Motorcyclist Crossing Straight Crossing Path (CMCscp) – a collision in which a vehicle travels forwards along a straight path across a junction, towards a motorcyclist crossing the junction on a perpendicular path. The outermost frontal structure of the vehicle under test strikes the front of the motorcycle. 

Car-to-Car Front Turn-Across-Path (CCFtap) – a collision in which a vehicle turns across the path of an oncoming vehicle travelling at constant speed, and the frontal structure of the vehicle strikes the front structure of the other. 

Car-to-Car Crossing Straight Crossing Path (CCCscp) – a collision in which a vehicle travels forwards along a straight path across a junction, towards a vehicle crossing the junction on a perpendicular path. The frontal structure of the vehicle under test strikes the side of the other vehicle. 

Car-to-Pedestrian Manoeuvring Reverse Child moving (CPMRCm) – a collision in which a vehicle travels rearwards towards a child pedestrian crossing its path walking from the nearside. The e st uctu e of the vehicle st ikes the pedest i n t $50 \%$ of the vehicle’s width when no braking action is applied. 

Car-to-Pedestrian Manoeuvring Reverse Child stationary (CPMRCs) – a collision in which a vehicle travels rearwards towards a child pedestrian standing still. The rear structure of the 

Euro NCAP 

Version 1.1 — October 2025 

vehicle st ikes the pedest i n t 25, 50 o $7 5 \%$ of the vehicle’s width when no b king ction is applied. 

Car-to-Pedestrian Manoeuvring Front Child (CPMFC) – a collision in which a vehicle creeps forwards towards a child pedestrian standing still, followed by a sudden and rapid accelerator pedal application. The front structure of the vehicle strikes the pedestrian at 25, 50 or $7 5 \%$ of the vehicle’s width when no torque suppression is applied. The scenario aims to address the effectiveness of ACPE. 

# 1 MEASURING REQUIREMENTS

# Reference system

# 1.1.1 Local Coordinate System

Use the convention specified in ISO 8855:2011, with the origin at the most forward point on the centreline of the VUT for dynamic data measurements as shown in Figure 1-1. This reference system should be used for both left- and right-hand drive vehicles. In Figure 1-1 nearside and farside are shown for a left-hand drive vehicle. For a right-hand drive vehicle, nearside and far-side are swapped. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/e096ea9186e4fc05767164b0929c63386f85704da2899a72eb2745a226eb3ea7.jpg)



Figure 1-1 Coordinate system and notation


# 1.1.2 Global Coordinate System

The origin of the Global Coordinate System $\scriptstyle \sum = 0$ , $\scriptstyle \mathtt { Y } = 0$ ) shall be located by default at the theoretical expected collision point between the VUT and the Target. 

In pedestrian and bicyclist crossing scenarios, this point is defined as the intersection between the projected paths of the VUT and Target reference points (e.g., CPNCO). 

In head-on or rear-end scenarios, this point is defined as the position where the reference points of the VUT and Target are expected to coincide at impact (e.g., CCRs). 

For scenarios involving a marked intersection (e.g., CCCscp, CCFtap, CPTA), the origin shall be set at the geometric centre of the intersection. 

In all cases, the x-axis shall be aligned with the nominal direction of travel of the VUT, and the y-axis pe pendicul to it, with positive y defined to the left of the VUT’s di ection of t vel. 

# Scenario Parameters

# 1.2.1 Test paths for turning scenarios

For CCFtap SfS and CMFtap SfS, the following parameters should be used to create the test path, which is the 10km/h to Farside case from the Frontal Collisions protocol: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/245520d0f2690d78ddfb185db2ba84821e73b217f5144cbb512af7465e496412.jpg)


<table><tr><td rowspan="3">Test Speed</td><td colspan="3">Part 1 (Clothoid)</td><td colspan="3">Part 2 (constant radius)</td><td colspan="3">Part 3 (Clothoid)</td></tr><tr><td>Start Radius R1 [m]</td><td>End Radius R2 [m]</td><td>Angle α [deg]</td><td>Start Radius R1 [m]</td><td>End Radius R2 [m]</td><td>Angle β [deg]</td><td>Start Radius R2 [m]</td><td>End Radius R1 [m]</td><td>Angle α [deg]</td></tr><tr><td>Start Radius R1 [m]</td><td>End Radius R2 [m]</td><td>Angle α [deg]</td><td>Start Radius R1 [m]</td><td>End Radius R2 [m]</td><td>Angle β [deg]</td><td>Start Radius R2 [m]</td><td>End Radius R1 [m]</td><td>Angle α [deg]</td></tr><tr><td>10 km/h to Farside</td><td>1500</td><td>9.00</td><td>20.62</td><td>9.00</td><td>9.00</td><td>48.75</td><td>9.00</td><td>1500</td><td>20.62</td></tr></table>

# 1.2.2 Impact Location

Impact location is defined as where the reference point of the target coincides with the $\%$ -age of the VUT width. For reference, $0 \%$ is defined is the projection of the outer right edge of the vehicle, and $100 \%$ is defined is the projection of the outer left edge of the vehicle (according to the definition of the vehicle width). 

For CMCscp SfS scenario only, which involves a side impact, the impact location is defined as where the reference point of the target coincides with the $\%$ -age of the VUT length. For reference, $100 \%$ is defined is the projection of the most forward point of the vehicle, and $0 \%$ is defined is the projection of the most rearward point of the vehicle (according to the definition of the vehicle length). 

For CBDA, the impact location is defined as where the reference point of the target coincides with the most e w d point of the d ive ’s doo of the vehicle. 

# 1.2.2.1 Car-to-Car Crossing

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/25ce5e783822ceda23bef62f03e3fefe08307653a0f1ba3835b27fb723488478.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/69a0707aff2d831c66c621068ef997dbfd9092da7a765a71dae4649292a838fa.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/f25f2a15325dd61b973b861add3fc43a6001d13010deadfa83fecadb191f4e68.jpg)


# 1.2.2.2 Car-to-Car Turn Across Path

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/3cad008ab88c7bcd7c83d3f16bdba288534f2eb4a7e373083786a7213ea562fc.jpg)


# 1.2.2.3 Car-to-PTW Crossing

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/6c1a20be11a1fcb4224ce7ac6aeb9c22ff5f3659c51d2d0a4558d4989519bac8.jpg)



$90 \%$ side impact location (nearside)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/f29de0b8fd6f930f0068ae5b8c612aba4799c5185daa10f860b3ee1a2fd4fc8d.jpg)



$90 \%$ side impact location (farside)


# 1.2.2.4 Car-to- Bicyclist Dooring

The impact location for the CBDA scenario is at the VUT’s most rearward point of closed driver door, and applicable for front door and rear door assessment 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/4a4f436cd60d760b0cdb4003444df1f4a9499ff7e226c4a8fcf10ce2abc6ac06.jpg)


# 1.3 VUT

# 1 . 3 .1 V UT P rof i le

A virtual profiled line is defined around both the front end and the rear end of the VUT, as well as around the right and left side of the VUT. The front and rear profiles are defined by straight line segments connecting seven points that are equally distributed over the vehicle width minus 50mm on each side. The side profiles are defined by straight line segments connecting seven points that are equally distributed between the outermost rear and front profiles, on each side. The theoretical x,y coordinates for each of these points are provided by the OEMs and verified by the test laboratory. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/7b3af2899a42338684d4d70cade5cf8224988c965acb83232d80dc14b97bc2b4.jpg)



Figure 1-2 Virtual profiled line around the front end, rear end of the VUT


# Targets

Only equipment listed in the current version of TB G003-1 and TB G003-2 may be used for testing. The current version can be found on the Euro NCAP website. 

# 1.4.1 Virtual Boxes

For each test target, a virtual box defined will be used to determine the impact speed. The dimensions of these virtual boxes are shown in the figures below, along with impact reference points related to each test target. 

Impact location descriptions in section 1.2.2 and scenario descriptions in section 3 illustrate which of the reference points is to be utilised for each specific scenario. 

# 1.4.1.1 EPTa and EPTc

The dimensions of this virtual box are shown in the figure below, with reference points on the hip and a virtual point where the centreline of the dummy crosses the virtual box. 

Euro NCAP 

Version 1.1 — October 2025 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/d7e28207b6085c98b38fe7957470894eebf493080c67bc1dc63e51de9fc5b38f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/a1b62e3e0aaf9c646b87b99a67162d528958f770755f5fa68ef996006fe81923.jpg)



Figure 1.2.1: Virtual box dimensions around EPTa and EPTc


# 1.4.1.2 EBT

The dimensions of this virtual box are shown in the figure below, with reference points on the crank shaft (applicable to crossing scenarios), most forward point on the front wheel (applicable to turning scenarios) and most rearward point on the rear wheel (applicable to longitudinal scenarios). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/48b2987aae3bddc3f28e568eebd78d953099cb32a8c0fa5908fe5cd11f048eeb.jpg)



Figure 1.2.2: Virtual box dimensions around EBT


# 1.4.1.3 EMT

The dimensions of this virtual box are shown in the figure below with reference points on the most forward point on the front wheel (applicable to longitudinal-front, turning and crossing scenarios) and most rearward point on the rear wheel (applicable to longitudinal-rear scenarios). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/b7c6b9df35b18eccaa25326c8b0fdb9def32da29893c9bfe292bb3e002defe4c.jpg)



Figure 1.2.3: Virtual box dimensions around EMT


# 1.4.1.4 GVT

The virtual box of the GVT is shown in the figure below, with reference points on: the most forward point on the front profile (1 in the centre and 1 in the intersection of the front profile and each of the side profiles), the most rearward point on the rear profile (in the centre), and at $7 5 \%$ along the length of each side of the GVT. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/cc3fb1f8b9963529a19723c774f755cf9b04b134b1b1c556301485e6ee90d096.jpg)



Figure 1.2.4: Virtual box illustration around the GVT


# Measurements and variables

Sample and record all dynamic data at a frequency of at least 100Hz. Synchronise using the DGPS time stamp the GVT data with that of the VUT. 

# 1.5.1 Variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>T</td><td>Time</td></tr><tr><td>T0</td><td>Time of test start T0 = TTC 4s, unless stated otherwise</td></tr><tr><td></td><td>- Turning/Crossing scenarios: T0 = 0.5s after target acceleration phase</td></tr><tr><td>TAEB</td><td>Time where AEB activates</td></tr><tr><td>Timpact</td><td>Time where the VUT impacts the target</td></tr><tr><td>Tsteer</td><td>Time where the VUT enters in curve segment</td></tr><tr><td>TTarget_deceleration_start</td><td>Time where the target starts decelerating</td></tr><tr><td>TVisual-warning</td><td>Time where the Dooring visual warning is triggered</td></tr><tr><td>Twarning</td><td>Time where the Dooring acoustic warning is triggered</td></tr><tr><td>Tdoor_operation</td><td>Time where VUT driver door opening interface is operated</td></tr><tr><td>Tdoor</td><td>Time where the door opens</td></tr><tr><td>TACC</td><td>Time where accelerator pedal input is applied</td></tr><tr><td>TStart</td><td>Time where the VUT starts moving</td></tr><tr><td>TEnd</td><td>Time of test end (see 4.3.2)</td></tr><tr><td>TAvg</td><td>Time average value of TEnd from all the executed trials</td></tr><tr><td>Vimpact</td><td>Speed when the VUT impacts the target</td></tr><tr><td>Vrel_impact</td><td>Relative speed when the VUT impacts the target</td></tr><tr><td>XVUT, YVUT</td><td>Position of the VUT during the entire test</td></tr><tr><td>VVUT</td><td>Speed of the VUT during the entire test</td></tr><tr><td>AVUT</td><td>Acceleration of the VUT during the entire test</td></tr><tr><td>ψVUT</td><td>Yaw velocity of the VUT during the entire test</td></tr><tr><td>ΩVUT</td><td>Steering wheel velocity of the VUT during the entire test</td></tr><tr><td>Xtarget, Ytarget</td><td>Position of the target during the entire test</td></tr><tr><td>Vtarget</td><td>Speed of the target during the entire test</td></tr><tr><td>Atarget</td><td>Acceleration of the target during the entire test</td></tr><tr><td>ψtarget</td><td>Yaw velocity of the target during the entire test</td></tr></table>

# 1.5.2 Measurements

Equip the VUT and GVT with data measurement and acquisition equipment to sample and record data with an accuracy of at least: 

VUT and target speed to 0.1km/h 

VUT and target lateral and longitudinal position to 0.03m 

- VUT heading angle to $0 . 1 ^ { \circ }$ 

VUT and target yaw rate to $0 . 1 \%$ 

VUT and target longitudinal acceleration to $0 . 1 \mathsf { m } / \mathsf { s } ^ { 2 }$ 

VUT steering wheel velocity to $1 . 0 ~ \%$ 

To determine Xtarget at Tvisual_warning, Twarning, Topen and Tdoor_operation in CBDA scenario for assessment, use of video recording (including reference markings for $\mathsf { X } _ { \mathsf { t a r g e t } } )$ is permitted. 

# 1 . 5 . 3 D a t a F i l t e r i n g

Filter the measured data as follows: 

- Position and speed are not filtered and are used in their raw state. 

Acceleration, yaw rate, steering wheel velocity and force are filtered with a 12-pole phase less Butterworth filter with a cut off frequency of 10Hz. 

# 2 TEST CONDITIONS

# Test track

Conduct tests on a dry (no visible moisture on the surface), uniform, solid paved surface with a maximum longitudinal slope of $\pm 1 \%$ and a maximum lateral slope of $\pm 3 \%$ . The test surface shall have a minimal peak braking coefficient (PBC) of 0.9. 

The test track surface must be paved and may not contain irregularities (e.g. large dips or cracks, manhole covers or reflective studs) that may give rise to abnormal sensor measurements within a lateral distance of $5 . 0 \mathsf { m }$ to either side of the test path, and with a longitudinal distance of 20m ahead of the VUT when the test ends. 

Unless otherwise specified: 

Conduct testing such that, between ${ \sf T } _ { 0 }$ and the test end, there are no other vehicles, infrastructure (except lighting columns during the low ambient lighting condition tests), obstructions, other objects or persons which may give rise to abnormal sensor measurements within the visual axis of the VUT and test target, and $_ { 2 0 \mathsf { m } }$ ahead of the VUT at test end. 

The general view ahead and to either side of the test area shall not comprise of any highly reflective surfaces or contain any silhouettes similar in shape to the test target. 

# 2.2 Lane Markings

The presence of lane markings is allowed for AEB tests. However, testing may only be conducted in an area where typical road markings depicting a driving lane may not be parallel to the test path within $3 . 0 \mathsf { m }$ either side. Lines or markings may cross the test path but may not be present in the area where AEB activation and/or braking after FCW is expected. 

Some scenarios described in this document require the use of a junction, where this is the case the scenario description will illustrate the scenario on a junction as in Figure 4.2. The main approach lane where the VUT path starts, (horizontal lanes in Figure 4.2) will have a width of 3.5m. The side lane (vertical lanes in Figure 4.2) will have a width of 3.25 to 3.5m. The lane markings on these lanes need to conform to one of the lane markings as defined in UNECE Regulation 130: 

1. Dashed line starting at the same point where the radius transitions into a straight line with a width between 0.10 and 0.15m 

2. Solid line with a width between 0.10 and 0.25m 

3. Junction without any central markings 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/04e60a8c7d635986ea6f2d7adf458493f6add7f818e4cb0f92a39684eafeccb5.jpg)



Figure 4.2: Layout of junction and the connecting lanes



(Dimensions reference centre of lane markings)


# 2.3 Weather Conditions

Unless otherwise specified: 

Conduct tests in dry conditions with ambient temperature above $5 \textdegree C$ and below $4 0 ^ { \circ } \mathsf { C }$ . 

No precipitation shall be falling and horizontal visibility at ground level shall be greater than 1km. Wind speeds shall be below $1 0 \mathsf { m } / \mathsf { s }$ to minimise GVT and VUT disturbance. 

Natural ambient illumination must be homogenous in the test area and in excess of 2000 lux for daylight testing with no strong shadows cast across the test area other than those caused by the VUT or GVT. Ensure testing is not performed driving towards, or away from the sun when there is direct sunlight. 

Measure and record the following parameters preferably at the commencement of every single test or at least every 30 minutes: 

a) Ambient temperature in $^ \circ \mathsf { C }$ ; 

b) Track Temperature in $^ \circ \mathsf { C }$ 

c) Wind speed and direction in $\mathsf { m } / \mathsf { s }$ 

d) Ambient illumination in Lux. 

# 2.4 VUT Preparation

# 2.4.1 AEB and FCW System Settings

Set any driver configurable elements of the AEB and/or FCW system (e.g. the timing of the collision warning or the braking application if present) to the middle setting or midpoint and then next latest setting similar to the examples shown in Figure 4.4. 

When the vehicle is equipped with a Driver State Monitoring (DSM) which alters the AEB and/or F W sensitivity cco ding to the d ive ’s st te (e.g. dist cted / ttentive), this system sh ll be deactivated before the testing commences. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/367a36ad6cdd8ce4828a5345396da084f4072e8e50b1920bc4bd59ffca5ff620.jpg)



Figure 4.4: AEB and/or FCW system setting for testing


# 2.4.2 Deployable Pedestrian/VRU Protection Systems

When the vehicle is equipped with a deployable pedestrian/VRU protection system, this system shall be deactivated before the testing commences. 

# 2.4.3 Tyres

Perform the testing with new original fitment tyres of the make, model, size, speed and load rating as specified by the vehicle manufacturer. It is permitted to change the tyres which are supplied by the manufacturer or acquired at an official dealer representing the manufacturer if those tyres are identical make, model, size, speed and load rating to the original fitment. Inflate the tyres to the vehicle m nuf ctu e ’s ecommended cold ty e infl tion p essu e(s). Use infl tion p essu es corresponding to least loading normal condition. 

Run-in tyres according to the tyre conditioning procedure specified in 2.4.3. After running-in maintain the run-in tyres in the same position on the vehicle for the duration of the testing. 

# 2.4.4 Wheel Alignment Measurement and Unladen Kerb Mass

The vehicle should be subject to a vehicle (in-line) geometry check to record the wheel alignment set by the OEM. This should be done with the vehicle in kerb weight. 

Fill up the t nk with fuel to t le st $90 \%$ of the t nk’s c p city of fuel. 

Check the oil level and top up to its maximum level if necessary. Similarly, top up the levels of all other fluids to their maximum levels if necessary. 

Ensure that the vehicle has its spare wheel on board, if fitted, along with any tools supplied with the vehicle. Nothing else should be in the car. 

Ensu e th t ll ty es e infl ted cco ding to the m nuf ctu e ’s inst uctions fo the pp op i te loading condition. 

Euro NCAP 

Version 1.1 — October 2025 

Measure the front and rear axle masses and determine the total mass of the vehicle. The total m ss is the ‘unl den ke b m ss’ of the vehicle. Reco d this m ss in the test det ils. 

Calculate the required ballast mass, by subtracting the mass of the test driver and test equipment from the required $2 0 0 ~ \mathsf { k g }$ interior load. 

# 2.4.5 Vehicle Preparation

Fit the on-board test equipment and instrumentation in the vehicle. Also fit any associated cables, cabling boxes and power sources and place weights with a mass of the ballast mass. Any items added should be securely attached to the car. 

With the driver in the vehicle, weigh the front and rear axle loads of the vehicle and compare these lo ds with the “unl den ke b m ss” 

The total vehicle mass shall be within $\pm 1 \%$ of the sum of the unladen kerb mass, plus 200kg. The front/rear axle load distribution needs to be within $5 \%$ of the front/rear axle load distribution of the original unladen kerb mass plus full fuel load. If the vehicle differs from the requirements given in this paragraph, items may be removed or added to the vehicle which has no influence on its performance. Any items added to increase the vehicle mass should be securely attached to the car. 

Care needs to be taken when adding or removing weight in order to approximate the original vehicle inertial properties as close as possible. Record the final axle loads in the test details. Reco d the xle weights of the VUT in the ‘ s tested’ condition. 

# 3 TEST PROCEDURE

# Car & PTW Scenarios

<table><tr><td>CAR &amp; PTW</td><td>TOTAL 10</td></tr><tr><td>Turning</td><td>4</td></tr><tr><td>Car-to-Car Turn Across Path</td><td>1</td></tr><tr><td>Car-to-Motorcycle Turn Across Path</td><td>3</td></tr><tr><td>Crossing</td><td>6</td></tr><tr><td>Car-to-Car Crossing</td><td>3</td></tr><tr><td>Car-to-Motorcycle Crossing</td><td>3</td></tr></table>

# 3.1.1 Car-to-Car Crossing

<table><tr><td>CCCscp</td><td colspan="5">GVT speed</td></tr><tr><td rowspan="2">Sfs</td><td>20 km/h</td><td>30 km/h</td><td>40 km/h</td><td>50 km/h</td><td>60 km/h</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>

The VUT is initially at standstill with an initial longitudinal distance to the impact point of $_ { 2 . 9 \mathsf { m } }$ . Assume a straight-line path equivalent to the centre line of the driving lane, approaching and continuing straight ahead across a junction. 

For the GVT, assume a straight-line path equivalent to the centre line of the driving lane, perpendicular to that of the VUT, travelling across the junction from the farside direction, 

The scenario setup is illustrated in Figure 3-1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/65212748868f0cdc69207a67d3864523fb808f1a9a31da2f422e24e4f81e096f.jpg)



Figure 3-1 CCCscp SfS scenario setup


Apply brake pedal to ensure that VUT is stationary until ${ \sf T } _ { 0 }$ condition is reached, and then conduct the Accelerator Pedal profile as described in Technical Bulletin CA 102. 

The GVT shall be accelerated to the selected speed at a rate ${ > } 1 \mathsf { m } / \mathsf { s } ^ { 2 }$ during the acceleration phase. This is followed by a 0.5 s stabilization phase, after which steady state conditions shall be met before the lower of 3.5s TTC. 

The paths will be synchronised so that the front of the VUT collides with the reference point of the GVT at an impact location of $5 0 \% \pm 2 5 \%$ (assuming no system reaction). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/07da72e79a0c0a79dcb1a93a7edae05cb113772271ccdabdf3006b7258d6ceed.jpg)



Figure 3-2 CCCscp SfS Impact location definition (GVT approaching from farside, impacting at $50 \%$ of VUT width)


# 3.1.2 Car-to-Motorcyclist Crossing

<table><tr><td>CMCscp</td><td colspan="7">EMT speed</td></tr><tr><td rowspan="2">SfS</td><td>20 km/h</td><td>30 km/h</td><td>40 km/h</td><td>50 km/h</td><td>60 km/h</td><td>70 km/h</td><td>80km/h</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The VUT is initially at standstill with an randomly selected longitudinal distance to the impact point of $_ { 2 . 9 \mathsf { m } }$ . Assume a straight-line path equivalent to the centre line of the driving lane, approaching and continuing straight ahead across a junction. 

For the EMT, assume a straight-line path equivalent to the centre line of the driving lane, perpendicular to that of the VUT, travelling across the junction from the farside direction. 

The scenario setup is illustrated in Figure 3-3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/07244da504b55c0ba2fe4732877fd2726800177d3fcb0ba4178a7d643d156504.jpg)



Figure 3-3 CMCscp SfS scenario setup


Apply brake pedal to ensure that VUT is stationary until ${ \sf T } _ { 0 }$ condition is reached, and then conduct the Accelerator Pedal profile as described in Technical Bulletin CA 102. 

The EMT shall be accelerated to the selected speed at a rate ${ \tt > } 1 { \sf m } / { \tt s } ^ { 2 }$ during the acceleration phase. This is followed by a 0.5 s stabilization phase, after which steady state conditions shall be met before the lower of 3.5s TTC. 

The paths will be synchronised so that the VUT collides with the reference point of the EMT at an impact location of $90 \%$ of the VUT length, with a tolerance of $\pm 1 0 \%$ (assuming no system reaction). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/751365182bf78534090af49771929746ee53da56193dd97923236536fc17e9b1.jpg)



Figure 3-4 CMCscp SfS Impact location definition (EMT approaching from farside, impacting at $90 \%$ of VUT length)


Car-to-car Turn Across Path 

# 3.1.3 Car-to-car Turn Across Path

<table><tr><td>CCFtap</td><td colspan="3">GVT speed</td></tr><tr><td rowspan="2">SfS</td><td>30 km/h</td><td>45 km/h</td><td>60 km/h</td></tr><tr><td></td><td></td><td></td></tr></table>

The initial position of the VUT shall be defined so that it first follows the 10km/h test case path and then stops when the front farside corner of the VUT bounding box coincides with inner side of of the (virtual) central lane marking of the intersection, with a tolerance of 0.10m to the inner edge of the (virtual) central lane marking. The direction indicator is applied at 1.0s before TSteer. 

The GVT will follow a straight-line p th in the l ne dj cent to the VUT’s initi l position, in the opposite direction to the VUT. The straight-line path of the VUT and GVT will be 1.75m from the centre of the centre dashed lane marking of the VUT lane. 

The scenario setup is illustrated in Figure 3-5. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/7d19452ecd6f8c41b17f887a09293efad98ad507b0afde3838aa39e977272f72.jpg)



Figure 3-5 CCFtap SfS scenario setup


Apply brake pedal to ensure that VUT is stationary until ${ \sf T } _ { 0 }$ condition is reached, and then conduct the Accelerator Pedal profile as described in Technical Bulletin CA 102. 

The paths of the VUT and GVT will be synchronised so that the VUT coincides with the reference point of the GVT at an impact location of $5 0 \% \pm 2 5 \%$ (assuming no system reaction), as illustrated in Figure 3-6. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/31585e929426df3b6b18fca07862ac7c499c265696fd12ce8faf7de00b2b2f54.jpg)



Figure 3-6 CCFtap SfS Impact point definition $5 0 \%$ of VUT width)


# 3.1.4 Car-to-Motorcyclist Turn Across Path

<table><tr><td>CMFtap</td><td colspan="4">EMT speed</td></tr><tr><td rowspan="2">SfS</td><td>30 km/h</td><td>45 km/h</td><td>60 km/h</td><td>80 km/h</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

The initial position of the VUT shall be defined so that it first follows the 10km/h test case path and then stops when the front farside corner of the VUT bounding box coincides with inner side of of the (virtual) central lane marking of the intersection, with a tolerance of 0.10m to the inner edge of the (virtual) central lane marking. The direction indicator is applied at 1.0s before TSteer. 

The EMT will follow a straight-line p th in the l ne dj cent to the VUT’s initi l position, in the opposite direction to the VUT. The straight-line path of the VUT and EMT will be 1.75m from the centre of the centre dashed lane marking of the VUT lane, as illustrated in Figure 3-7. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/d718e90201e2f13aabb7129b15db1125d36f286a1725c5deabee107ae033f71c.jpg)



Figure 3-7 CMFtap SfS scenario setup


Apply brake pedal to ensure that VUT is stationary until ${ \sf T } _ { 0 }$ condition is reached, and then conduct the Accelerator Pedal profile as described in Technical Bulletin CA 102. 

The paths of the VUT and EMT will be synchronised so that the VUT coincides with the reference point of the EMT at an impact location of $5 0 \% \pm 2 5 \%$ (assuming no system reaction), as illustrated in Figure 3-8. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/9d51209459042fc916bf97ee413f1da9261aab69925b3ebcc52eadcab2d5a2a4.jpg)



Figure 3-8 CMFtap SfS Impact point definition $5 0 \%$ of VUT width)


# 3.2 Pedestrian & Cyclist Scenarios

<table><tr><td>Pedestrian &amp; Cyclist</td><td>TOTAL 10</td></tr><tr><td>Crossing</td><td>3</td></tr><tr><td>Car-to-Bicyclist Crossing</td><td>3</td></tr><tr><td>Manoeuvring</td><td>5</td></tr><tr><td>Car-to-Pedestrian Manoeuvring Reverse</td><td>3</td></tr><tr><td>Car-to-Pedestrian Manoeuvring Forward</td><td>2</td></tr><tr><td>Dooring</td><td>2</td></tr><tr><td>Car-to-Bicyclist Dooring</td><td>2</td></tr></table>

# 3.2.1 Car-to-Bicyclist Crossing

# 3.2.1.1 CBNAO

<table><tr><td>CBNAO</td><td colspan="3">EBT speed</td></tr><tr><td>d</td><td>10 km/h</td><td>15 km/h</td><td>20 km/h</td></tr><tr><td>1.50 m</td><td></td><td></td><td></td></tr><tr><td>2.50 m</td><td></td><td></td><td></td></tr></table>

The VUT is initially positioned 1m beside the full obstruction from the nearside of the vehicle, and t dist nce ‘d’ f om the f ont of the vehicle until the p th long the EBT efe ence point. The distance between the obstruction and the EBT reference point is fixed to $\mathsf { 2 . 5 0 m }$ . 

The scenario setup is illustrated in Figure 3-9 CBNAO SfS scenario setupThe EBT shall accelerate to the selected speed within the acceleration distance G. Parameter H represents the steady state distance of the EBT, which shall be met at ${ \mathsf { T } } { \mathsf { T } } C { = } 4 { \mathsf { s } } $ . 

Apply brake pedal to ensure that VUT is stationary until ${ \sf T } _ { 0 }$ condition is reached, and then conduct the Accelerator Pedal profile as described in Technical Bulletin CA 102. 

The paths of the VUT and EMT will be synchronised so that the VUT coincides with the reference point of the EBT at an impact location of $5 0 \% \pm 2 5 \%$ (assuming no system reaction), as illustrated in Figure 3-9 CBNAO SfS scenario setup 

The obstruction to be used for this scenario would be at a discretion of the test laboratory and shall be made from a material that blocks VUT sensors, from ground level up to the VUT sensors height. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/ea49de94753140da5e153c08055963e797c17644f1d649434a55688dfd55bd74.jpg)



Figure 3-9 CBNAO SfS scenario setup


# 3.2.2 Car-to-Pedestrian Manoeuvring

<table><tr><td>Car-to-Pedestrian Manoeuvring Reverse</td><td>TOTAL 3</td></tr><tr><td>CPMRCm</td><td>1.5</td></tr><tr><td>CPMRCs</td><td>1.5</td></tr></table>

# 3.2.2.1 CPMRCm

<table><tr><td>CPMRCm</td><td colspan="2">EPTc speed</td></tr><tr><td>Rear gap</td><td>5 km/h</td><td>8 km/h</td></tr><tr><td>1.00 m</td><td></td><td></td></tr><tr><td>1.50 m</td><td></td><td></td></tr><tr><td>2.00 m</td><td></td><td></td></tr></table>

The VUT is initially positioned at the selected Rear gap, measured as the distance from the rearmost side of the VUT and the reference point of the EPTc. The EPTc is initially positioned 10.00m away from the centre of the VUT trajectory. 

The scenario setup is illustrated in Figure 3-10. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/57b8f2f555139148d5d1bec06cb1979fbfb0c91afef576332bbfb3ea1b391bf3.jpg)



Figure 3-10 CPMRCm scenario setup


Euro NCAP 

Version 1.1 — October 2025 

Conduct an Accelerator Pedal manoeuvre as outlined in Technical Bulletin CA 102, to start reversing the VUT so that the impact occurs at $50 \%$ of the vehicle width and with a tolerance of $\pm 2 5 \%$ (assuming no system reaction), as illustrated in Figure 3-10 CPMRCm scenario setup. 

# 3.2.2.2 CPMRCs

<table><tr><td rowspan="2">CPMRCs</td><td colspan="3">EPTc position</td></tr><tr><td>25%</td><td>50%</td><td>75%</td></tr><tr><td>4 km/h</td><td></td><td></td><td></td></tr><tr><td>8 km/h</td><td></td><td></td><td></td></tr></table>

The EPTc is initially positioned at the selected impact location, facing a randomly selected direction (left or right), and at a distance of 2s TTC from the VUT, measured from Tsteady. The EPTc should be used in its resting position with the articulation being switched off (i.e. not the static dummy posture as defined in ISO 19206-2). 

The scenario setup is illustrated in Figure 3-11. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/638440f5d04001e115b5362ec8df73ab0ea9d6422095953c9a3ee2ea7df10222.jpg)



Figure 3-11 CPMRCs scenario setup


The VUT shall accelerate to the selected speed within the minimum distance from its initial position until VUT speed can be reached. The pedestrian is located at three different impact locations: 25, 50 and $7 5 \%$ of the vehicle width. 

The selected speed shall be kept steady until the end of the test. 

# 3.2.2.3 CPMFC

<table><tr><td>CPMFC</td><td>25%</td><td>50%</td><td>75%</td></tr><tr><td>d1</td><td></td><td></td><td></td></tr><tr><td>d2</td><td></td><td></td><td></td></tr></table>

The (stationary) EPTc is initially positioned at the selected impact location, facing a randomly selected direction (left or right), and at a distance of $1 . 5 + [ 0 . 5 ] \mathrm { m }$ to the TACC position. 

The VUT will start creeping from standstill $( \mathsf { T } _ { 0 } )$ and travel the selected distance d $[ { \mathsf { d } } _ { 1 }$ or d2) until the point in time where accelerator pedal input is applied (TACC). The starting point $( \mathsf { T } _ { 0 } )$ shall be selected such that AEB would not intervene before TACC. ${ \mathsf { d } } _ { 1 }$ or ${ \sf d } _ { 2 }$ are defined as follows: 

${ \mathsf { d } } _ { 1 }$ : Distance travelled from standstill until the VUT reaches a speed as close as possible as maximum creeping speed so that the boundary conditions are met, until TACC 

${ \sf d } _ { 2 }$ : Distance travelled from standstill after creeping for [1]s 

The scenario setup is illustrated in Figure 3-12. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/0842bb588a81f4d9e0dac6b01f67b0003c4751371ec869d73d7db479e17ab4a5.jpg)



Figure 3-12 CPMFC scenario setup


The accelerator pedal input profile shall meet all the following conditions at TACC: 

Resulting in continuous acceleration, 

Having a velocity of at least $400 \% / \mathsf { s }$ over a travel distance of at least $70 \%$ of the total travel distance of the accelerator control, 

Reaching a maximum position of the accelerator control of at least $90 \%$ with that velocity 

The following boundary conditions shall be ensured during the test: 

The VUT shall be set in creep mode 

TACC shall occur at $1 . 5 + [ 0 . 5 ] \mathsf { n }$ from the EPTc 

There shall be no AEB intervention before TACC 

For vehicles without creeping mode, apply the accelerator pedal input profile with the VUT in standstill condition, and with the EPTc target at the selected distance d (in this case, $\mathsf { d } _ { 1 } { = } 1 . 0 \mathsf { m }$ and $\mathsf { d } _ { 2 } = 1 . 5 \mathsf { m }$ ). 

# 3.2.3 Car-to-Bicyclist Dooring

<table><tr><td>CBDA</td><td colspan="3">EBT speed</td></tr><tr><td>Rear gap</td><td>10 km/h</td><td>15 km/h</td><td>20 km/h</td></tr><tr><td>0.50 m</td><td></td><td></td><td></td></tr><tr><td>1.00 m</td><td></td><td></td><td></td></tr><tr><td>1.50 m</td><td></td><td></td><td></td></tr><tr><td>2.00 m</td><td></td><td></td><td></td></tr></table>

For the CBDA scenario, a bicycle is traveling in a straight line at 10, 15 and 20 km/h beside the parked vehicle. The Rear gap (distance between VUT and obstruction car) is varied from 0.5 to 2.00m. 

The widest outside structure (without mirrors) of VUT and obstruction car are aligned one meter from the path of the VRU while the central-axis of the cars are in parallel to VUT path. The obstruction vehicle to be used is the smaller obstruction vehicle as defined in APPENDIX A. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/12393b90-cece-4f24-8e96-8d01cc12f118/d8fb93eb4101c115fa164020b11e3be2f20b163c47b473503c3482723ba89790.jpg)



Figure 3-13 CBDA scenario setup


In the first run, the EBT passes the parking car without operation on the door opening interface to assess the information given to the driver, where applicable. 

In the second run (applicable for a warning system Topen and for a retention system Tdoor operation), the VUT driver door opening interface shall be operated at ‘Doo ope tion dist nce’, defined from the bicyclist front reference point and the most rearward point of the driver’s door: 

<table><tr><td>EBT Speed (km/h)</td><td>Door operation distance (m)</td></tr><tr><td>10</td><td>5.5 + [0.4]</td></tr><tr><td>15</td><td>8 + [0.5]</td></tr><tr><td>20</td><td>11 + [0.7]</td></tr></table>

Door opening (manually operated): 

Pull door handle or activate other door opening interface (e.g. push a button) in a manner that would open the door to exit the car in a normal non-hazard situation, while pushing the door open. Emergency exit functions are permitted where triggered by an additional action (e.g. second pull). 

For CBDA, all tests shall be performed with the VUT in parking position within 180 seconds after propulsion system turned off with the driver in unbelted state. 

# 4 TEST EXECUTION

# Performance predictions

The Vehicle Manufacturer shall provide the Euro NCAP with colour data detailing the predicted performance of the system for all test scenarios. The predicted performance will be used as a reference to identify discrepancies between the predicted results and the test results. 

# Verification tests

The verification tests shall be conducted by the test laboratory in a selection of grid cells as indicated below (from the grid cells where the Vehicle Manufacturer predicted performance, excluding red grid cells): 

Car & PTW Scenarios: test lowest and highest target speed, and 1 random target speed in between. In case of impact, test adjacent cases and keep testing in $+ 1 0 \mathsf { k m / h }$ increments of target speed until prediction is met. 

CPMRCm: Test 1.00 and $_ { 2 . 0 0 \mathsf { m } }$ gaps for all EPTc speeds. In case of impact, test 1.50m gap. 

CPMRCs, CPMFC: Test all cases for the 25 and $7 5 \%$ impact location. In case of impact, test the $50 \%$ case. 

BNAO: Test the highest nd lowest t get speed, in ll ‘d’ c ses. In c se of imp ct, test the mid target speed (if applicable). 

• CBDA: Test the largest and shortest gap in combination with the highest and lowest target speed. In case of the prediction not being met, test adjacent grid cells in all directions until prediction is met. 

Grid cells where a verification test is applied will be updated with the colour corresponding to the outcome of the test. 

In case of absence of Vehicle Manufacturer predictions, test all cases, in consultation with the Euro NCAP Secretariat – in which case, the result of each Verification Test will dictate the colour of each grid cell. 

# Test Conduct

# 4.3.1 VUT Pre-test conditioning

# 4.3.1.1 General

A new car is used as delivered to the test laboratory. 

If requested by the vehicle manufacturer, drive a maximum of 100km on a mixture of urban and u l o ds with othe t ffic nd o dside fu nitu e to ‘c lib te’ the senso system. Avoid h sh acceleration and braking. 

# 4.3.1.2 Brakes

ondition the vehicle’s b kes in the following m nne , if it h s not been done befo e o in c se the lab has not performed a 100km of driving: 

Perform twenty stops from a speed of 56km/h with an average deceleration of approximately 0.5 to 0.6g. 

Euro NCAP 

Version 1.1 — October 2025 

Immediately following the series of 56km/h stops, perform three additional stops from a speed of 72km/h, e ch time pplying sufficient fo ce to the ped l to ope te the vehicle’s antilock braking system (ABS) for the majority of each stop. 

Immediately following the series of 72km/h stops, drive the vehicle at a speed of approximately 72km/h for five minutes to cool the brakes. 

# 4.3.1.3 Tyres

ondition the vehicle’s ty es in the following m nne to emove the mould sheen, if this h s not been done before for another test or in case the lab has not performed a 100km of driving: 

Drive around a circle of $_ { 3 0 \mathsf { m } }$ in diameter at a speed sufficient to generate a lateral acceleration of approximately 0.5 to 0.6g for three clockwise laps followed by three anticlockwise laps. 

Immediately following the circular driving, drive four passes at 56km/h, performing ten cycles of a sinusoidal steering input in each pass at a frequency of 1Hz and amplitude sufficient to generate a peak lateral acceleration of approximately 0.5 to 0.6g. 

Make the steering wheel amplitude of the final cycle of the final pass double that of the previous inputs. 

In case of instability in the sinusoidal driving, reduce the amplitude of the steering input to an appropriately safe level and continue the four passes. 

# 4.3.1.4 System Check

Before any testing begins, perform a maximum of ten runs at the lowest test speed the system is supposed to work, to ensure proper functioning of the system. 

# 4.3.2 Low Speed Collisions tests

Accelerate the VUT and target to the respective test speeds where needed. 

The test shall start at ${ \sf T } _ { 0 }$ and is valid when all boundary conditions are met between ${ \sf T } _ { 0 }$ and: 

- TACC for CPMFC scenario 

- T d o o r _ o p e r a t i o n for CBDA scenario 

TAEB for all other scenarios 

<table><tr><td></td><td>VUT</td><td>GVT</td><td>EPT</td><td>EBT</td><td>EMT</td></tr><tr><td>Speed</td><td>-</td><td>±1.0 km/h</td><td>±0.2 km/h</td><td>±0.5 km/h</td><td>±1.0 km/h</td></tr><tr><td>Lateral deviation</td><td>0 ± 0.05 m
(0 ± 0.1 m for CPTA and CBTA)</td><td>0 ± 0.10 m</td><td colspan="2">0 ± 0.05 m for crossing scenarios (incl. junction)
0 ± 0.15 m for longitudinal scenarios</td><td>0 ± [0.15] m</td></tr><tr><td>Lateral velocity</td><td></td><td>-</td><td>0 ± 0.15 m/s</td><td>0 ± 0.15 m/s</td><td>-</td></tr><tr><td>Yaw velocity (upto TSTEER)</td><td>0 ± 1.0 °/s</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Steering wheel velocity (upto TSTEER)</td><td>0 ± 15.0 °/s</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

The end of a test for all Low Speed Collisions scenarios except CBDA is considered when one of the following occurs: 

- $\mathsf { V } _ { \mathsf { V U T } } = 0 \mathsf { k m / h }$ (crossing) or $\mathsf { V } _ { \mathsf { V U T } } = \mathsf { V } _ { \mathsf { t a r g e t } }$ (longitudinal) 

Contact between VUT and target 

The target has left the VUT path or VUT has left the target path 

To avoid contact in the junction scenarios, the test laboratory may include an automated braking action by the robot in case the AEB system fails to intervene (sufficiently). This braking action is applied automatically when: 

The VUT reaches the latest position at which maximum braking applied to the vehicle will prevent the VUT entering the path of the Motorcyclist and no intervention from the AEB system is detected. 

L te l sep tion between the VUT nd EMT e ches $\leq 0 . 3 \mathsf { m }$ du ing / fte AEB intervention. 

It is t the test l bo to y’s disc etion to select nd use one of the options bove to ensu e s fe testing environment. If the Vehicle Manufacturer feels the avoidance action is negatively affecting the performance of their vehicle, they should consult with the test laboratory and Euro NCAP secretariat. 

# 5 ASSESSMENT

Each scenario in this assessment consists of a matrix with combinations of different parameters (e.g., impact location, target speed). Each combination in a matrix is referred to as grid cell. 

# General requirements

To be eligible for scoring points in this assessment, the following requirements shall be met: 

All systems involved in all scenarios in this assessment shall be default ON at the start of every journey and deactivation of the system shall not be possible with a momentary single push on a button. 

For Manoeuvring Reverse, the system may not release the brakes after an intervention, unless the threat (EPT) has left the vehicle path or in case of an override action by the driver. When the VUT is fitted as standard with a rear-view camera, the brakes may be release after 1.5s or longer after the AEB intervention. 

# 5.2 Criteria

The following criteria and associated KPIs is used across scenarios to evaluate the performance of the system 

<table><tr><td rowspan="2">Criteria</td><td rowspan="2">KPI</td><td colspan="2">Scenarios</td></tr><tr><td>Car &amp; PTW</td><td>Pedestrian &amp; Cyclist</td></tr><tr><td>Avoidance</td><td>Vimpact</td><td>ALL</td><td>CPMRCm, CPMRCs, CBNAO</td></tr><tr><td>Mitigation</td><td>Drivetrain torque suppression</td><td>-</td><td>CPMFC</td></tr><tr><td>Dooring</td><td>TTC</td><td>-</td><td>CBDA</td></tr></table>

# 5.2.1 Avoidance

For all avoidance-only scenarios, the following criteria applies: 

<table><tr><td>Vimpact [km/h]</td><td>Colour band</td></tr><tr><td>0</td><td>Green</td></tr><tr><td>&gt;0</td><td>Red</td></tr></table>

# 5 . 2 . 2 M i t i g a t i o n

For Car-to-Pedestrian Manoeuvring Forward scenario, the assessment criteria is based on crash mitigation enabled by a reduction of the effective demand of the accelerator control to zero upon accelerator pedal input. The following scaling is applied to each grid cell: 

<table><tr><td>Drivetrain torque suppression</td><td>Colour band</td></tr><tr><td>YES</td><td>Green</td></tr><tr><td>NO</td><td>Red</td></tr></table>

Euro NCAP 

Version 1.1 — October 2025 

In the case a collision is not prevented, manufacturer shall demonstrate that the power/torque demand of VUT has been reduced to the equivalent of the driver removing any input onto the accelerator pedal before collision. 

# 5.2.3 Dooring

For Car-to-Bicyclist Dooring scenario, the assessment criteria is based on the timely vehicle response upon a door opening attempt before a bicyclist is passing by. The following scaling is applied to each grid cell depending on whether the vehicle response is Information, Warning or Retention: 

<table><tr><td>Vehicle response</td><td>Criteria</td><td>Doors</td><td>Colour Band</td></tr><tr><td rowspan="2">Information</td><td>TTC ≥ 2.30s</td><td rowspan="2">Driver&#x27;s only</td><td>Brown</td></tr><tr><td>TTC &lt; 2.30s</td><td>Red</td></tr><tr><td rowspan="3">Warning</td><td rowspan="2">TTC ≥ 1.70s</td><td>Driver&#x27;s only</td><td>Orange</td></tr><tr><td>All</td><td>Yellow</td></tr><tr><td>TTC &lt; 1.70s</td><td>Driver&#x27;s only OR All</td><td>Red</td></tr><tr><td rowspan="4">Retention</td><td>Start @ TTC ≥ 1.70s</td><td>Driver&#x27;s only</td><td>Yellow</td></tr><tr><td>AND End @TTC ≤ -0.40s</td><td>All</td><td>Green</td></tr><tr><td>Start @ TTC &lt; 1.70s</td><td>Driver&#x27;s only</td><td rowspan="2">Red</td></tr><tr><td>OR End @TTC &gt; -0.40s</td><td>OR All</td></tr></table>

# Where:

Information shall be visually provided in the field of view of the d ive ’s side window. 

Warning shall have a visual component (e.g., flashing) in the field of view of the d ive ’s side window, and an audible or haptic component. 

Warning or retention functionality shall be issued on eithe the d ive ’s doo nd/o all doors on the side where the threat is present. Reference point for all tests is the rear of the front door. Visual warning on the rear doors is not required. 

Doors that cannot endanger VRUs passing by the VUT (e.g. sliding doors that open to a small extend), Retention may be replaced by Warning and the scaling for Retention shall be used. This warning can be suppressed 10 seconds after Tdoor 

operation. 

# Scoring

For score calculation in each of the scenarios, first each grid cell is given a sub-score according to the Vehicle Manufacturer colour prediction: 

<table><tr><td>Predicted Colour</td><td>Sub-score per grid cell</td></tr><tr><td>Green</td><td>1.00</td></tr><tr><td>Yellow</td><td>0.75</td></tr><tr><td>Orange</td><td>0.50</td></tr><tr><td>Brown</td><td>0.25</td></tr><tr><td>Red</td><td>0.00</td></tr></table>

Secondly, the resulting score is calculated by normalizing all the scenario sub-scores to the total score of that scenario (rounded to hundredth): 

$$
S c e n a r i o S c o r e = \frac {\sum S c e n a r i o S u b s c o r e s \times T o t a l S c e n a r i o S c o r e}{N u m b e r o f G r i d C e l l s}
$$

# APPENDIX A OBSTRUCTION DIMENSIONS

# A.1 Smaller obstruction vehicle

The smaller obstruction vehicle shall be: 

Of the category Small Family Car 

Of a dark colour 

Within the following geometrical dimensions: 

<table><tr><td></td><td>Vehicle length</td><td>Vehicle width (without mirrors)</td><td>Vehicle height</td><td>Bonnet length (till A pillar)</td><td>Bonnet Leading Edge height</td></tr><tr><td>Minimum</td><td>4100 mm</td><td>1700 mm</td><td>1300 mm</td><td>1000 mm</td><td>650 mm</td></tr><tr><td>Maximum</td><td>4400 mm</td><td>1900 mm</td><td>1500 mm</td><td>1500 mm</td><td>850 mm</td></tr></table>

# A.2 Larger obstruction vehicle

The larger obstruction vehicle shall be: 

Of the category Small SUV 

Of a dark colour 

Within the following geometrical dimensions: 

<table><tr><td></td><td>Vehicle length</td><td>Vehicle width
(without mirrors)</td><td>Vehicle height</td></tr><tr><td>Minimum</td><td>4300 mm</td><td>1750 mm</td><td>1500 mm</td></tr><tr><td>Maximum</td><td>4700 mm</td><td>1900 mm</td><td>1800 mm</td></tr></table>