# Crash Avoidance

# Frontal Collisions

# Protocol

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/3d4d672ec231db2f32e80f7d6566c715ac3e2602f662fe09e6817476a59a5e39.jpg)


# PREFACE

During the test preparation, vehicle manufacturers are encouraged to liaise with the laboratory and to check that they are satisfied with the way cars are set up for testing. Where a manufacturer feels that a particular item should be altered, they should ask the laboratory staff to make any necessary changes. Manufacturers are forbidden from making changes to any parameter that will influence the test, such as dummy positioning, vehicle setting, laboratory environment etc. 

It is the responsibility of the test laboratory to ensure that any requested changes satisfy the requirements of Euro NCAP. Where a disagreement exists between the laboratory and manufacturer, the Euro NCAP secretariat should be informed immediately to pass final judgment. Where the laboratory staff suspect that a manufacturer has interfered with any of the set up, the manufacturer's representative should be warned that they are not allowed to do so themselves. They should also be informed that if another incident occurs, they will be asked to leave the test site. 

Whe e the e is ecu ence of the p oblem, the m nuf ctu e ’s ep esent tive will be told to le ve the test site and the Secretary General should be immediately informed. Any such incident may be reported by the Secretary General to the manufacturer and the person concerned may not be allowed to attend further Euro NCAP tests. 

DISCLAIMER: Euro NCAP has taken all reasonable care to ensure that the information published in this protocol is accurate and reflects the technical decisions taken by the organisation. In the unlikely event that this protocol contains a typographical error or any other inaccuracy, Euro NCAP reserves the right to make corrections and determine the assessment and subsequent result of the affected requirement(s). 

# CONTENTS

# DEFINITIONS 3

# 1 MEASURING REQUIREMENTS 8

Reference System 8 

Scenario Parameters 9 

VUT 1 7 

Targets 1 8 

Measurements and variables 2 1 

# 2 TEST CONDITIONS 2 3

Test track 2 3 

Weather Conditions 2 4 

Surroundings 2 4 

VUT Preparation 2 5 

# 3 TEST PROCEDURE 2 7

Car & PTW Scenarios 2 7 

Pedestrian & Cyclist Scenarios 4 1 

# 4 TEST EXECUTION 5 8

Performance Predictions 5 8 

Verification tests 5 9 

Test Conduct 6 1 

# 5 ASSESSMENT 6 4

General requirements 6 4 

Criteria 6 4 

Scoring 7 1 

Links to Driver State 7 4 

# APPENDIX A APPLICABILITY OF ROBUSTNESS LAYERS 76

# APPENDIX B OBSTRUCTION DIMENSIONS 80

# DEFINITIONS

Throughout this protocol the following terms are used: 

Peak Braking Coefficient (PBC) – the measure of tyre to road surface friction based on the maximum deceleration of a rolling tyre, measured using the American Society for Testing and Materials (ASTM) E1136-10 (2010) standard reference test tyre, in accordance with ASTM Method E 1337-90 (reapproved 1996), at a speed of 64.4 km/h, without water delivery. Alternatively, the method as specified in UNECE R13-H. 

Vehicle under test (VUT) – means the vehicle tested according to this protocol with a pre-crash collision mitigation or avoidance system on board. 

Global Vehicle Target (GVT) – means the vehicle target used in this protocol as defined in ISO 19206-3:2021 

Secondary Other Vehicle (SOV) – means the vehicle being overtaken by VUT in CCFhol scenario. This vehicle can either be a GVT or a real vehicle. 

Euro NCAP Pedestrian Target (EPTa) – means the articulated adult pedestrian target used in this protocol as specified in ISO 19206-2:2018 

Euro NCAP Bicyclist Target (EBTa) – means the adult bicyclist and bike target used in this protocol as specified in ISO 19206-4:2020 

Euro NCAP Child Target (EPTc) – means the articulated child pedestrian target used in this protocol as specified in ISO 19206-2:2018 

Euro NCAP Motorcyclist Target (EMT) – means the Motorcyclist target used in this protocol as specified in ISO 19206-5. 

Real Motorcycle – Means a motorcyclist target that can be used in the Blind-Spot Monitoring Tests of this protocol, as an alternative to the EMT. The Real Motorcycle shall be a type approved two-wheeled motorcycle, with a maximum speed of at least 80km/h by design, without front fairing or windshield. It shall closely resemble the EMT (as specified in section 2.1 of deliverable D2.1 of the MUSE project), thus staying within the mean dimensions of the most registered middleweight naked motorcycles in Europe (i.e. wheelbase >1405mm. and <1445mm.). 

Autonomous Emergency Braking (AEB) – braking that is applied automatically by the vehicle in response to the detection of a likely collision to reduce the vehicle speed and potentially avoid the collision. 

Forward Collision Warning (FCW) – an audio-visual warning that is provided automatically by the vehicle in response to the detection of a likely collision to alert the driver. 

Autonomous Emergency Steering (AES) – steering that is applied automatically by the vehicle in response to the detection of a likely collision to steer the vehicle and potentially avoid the collision. 

Emergency Steering Support (ESS) – a system that supports the driver steering input in response to the detection of a likely collision to alter the vehicle path and potentially avoid a collision. 

Vehicle width – the widest point of the vehicle ignoring the rear-view mirrors, side marker lamps, tyre pressure indicators, direction indicator lamps, position lamps, flexible mud-guards and the deflected part of the tyre side-walls immediately above the point of contact with the ground. 

Vehicle length – from the most rearward point to the most forward point on the centreline of the vehicle. 

Car-to-Pedestrian – a collision between a vehicle and an adult or child pedestrian in its path, when no braking and/or steering action is applied. 

Car-to-Bicyclist – a collision between a vehicle and an adult bicyclist in its path, when no braking and/or steering is applied. 

Car-to-Motorcyclist – a collision between a vehicle and a Motorcyclist in its path, when no braking and/or steering is applied. 

Standard range – refers to the most basic and controlled format a test scenario will be tested. Tests within the standard range are deemed the foundational level performance expectations for any given test scenario. 

Extended range – refers to test points in which minor levels of complexity are introduced to the standard range tests. Changes for this range are limited to variations in impact position and longitudinal velocity for the VUT and / or test target. 

Robustness layer – refers to the introduction of test complexity and variation, designed to ch llenge vehicle systems nd encou ge eli ble “ e l-wo ld” pe fo m nce. 

Time To Collision (TTC) – means the remaining time before the VUT strikes the test target, assuming that the VUT and test target would continue to travel with the speed it is travelling. 

TAEB – means the time where the AEB system activates. Activation time is determined by identifying the last data point where the filtered acceleration signal is below $- 3 \ m / \mathsf { s } ^ { 2 }$ , and then going back to the point in time where the acceleration first crossed $- 1 m / \mathsf { s } ^ { 2 }$ 

TFCW – means the time where the audible warning of the FCW starts. The starting point is determined by audible recognition. 

TDiver_steer – means the time where the control handover from the steering robot to the test driver starts. From that point, the test driver shall hold the steering wheel in a neutral position resembling naturalistic driving and avoiding overly harsh/aggressive inputs. 

TDriver_throttle – means the time where the control handover from the accelerator robot to the test driver starts. From that point, the test driver shall manually control de target vehicle speed with the accelerator pedal, resembling naturalistic driving and avoiding overly harsh/aggressive inputs. 

Vimpact – means the speed at which the profiled line around the front, rear end, or side of the VUT coincides with the virtual box around the test targets (platform not included in the virtual box) EPTa, EPTc, EBTa and EMT as shown in the right part of the figures below, as illustrated in Figure 0-1 and Figure 0-2. 

Vrel_test – means the relative speed between the VUT and the test target (GVT, EPT, EBT or EMT) by subtracting the longitudinal velocity of the test target from that of the VUT at the start of test. 

Vrel_impact – means the relative speed at which the VUT hits the test target (GVT, EPT, EBT or EMT) by subtracting the longitudinal velocity of the test target from $\mathsf { V } _ { \mathrm { i m p a c t } }$ at the time of collision. 

Euro NCAP 

Version 1.1 — October 2025 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/c9b8fb3c7cdd93dc5adb8eb33c1808ccf5ae3dc75a0619b495a74a3a0fd32d10.jpg)



Figure 0-1 :Front end profile vs EPT, EMT, and EBT targets, and rear end profile vs EPT target.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/d0d5f840072c4fd58a6503bd295ecfb038a825bfd0994effe8ad5258c4f1ba41.jpg)



Figure 0-2 Front end profile and GVT


# Test Scenarios

Car-to-Pedestrian Farside Adult (CPFA) – a collision in which a vehicle travels forwards towards an adult pedestrian crossing its path running from the farside and the frontal structure of the vehicle strikes the pedestrian when no braking action is applied. 

Car-to-Pedestrian Nearside Adult (CPNA) – a collision in which a vehicle travels forwards towards an adult pedestrian crossing its path walking from the nearside and the frontal structure of the vehicle strikes the pedestrian when no braking action is applied. 

Car-to-Pedestrian Nearside Child Obstructed (CPNCO) – a collision in which a vehicle travels forwards towards a child pedestrian crossing its path running from behind and obstruction from the nearside and the frontal structure of the vehicle strikes the pedestrian when no braking action is applied. 

Car-to-Pedestrian Longitudinal Adult (CPLA) – a collision in which a vehicle travels forwards towards an adult pedestrian walking in the same direction in front of the vehicle where the vehicle strikes the pedestrian when no braking action is applied or an evasive steering action is initiated after an FCW. 

Car-to-Pedestrian Turning Adult (CPTA) – a collision in which a vehicle turns towards an adult pedestrian crossing its path, walking across a junction (in either the same and opposite direction as the VUT, before the VUT made the turn) and the frontal structure of the vehicle strikes the pedestrian when no braking action is applied. 

Car-to-Bicyclist Nearside Adult (CBNA) – a collision in which a vehicle travels forwards towards a bicyclist crossing its path cycling from the nearside and the frontal structure of the vehicle strikes the bicyclist when no braking action is applied. 

Car-to-Bicyclist Nearside Adult Obstructed (CBNAO) – a collision in which a vehicle travels forwards towards a bicyclist crossing its path cycling from the nearside from behind an obstruction and the frontal structure of the vehicle strikes the bicyclist when no braking action is applied. 

Car-to-Bicyclist Farside Adult (CBFA) – a collision in which a vehicle travels forwards towards a bicyclist crossing its path cycling from the farside and the frontal structure of the vehicle strikes the bicyclist when no braking action is applied. 

Car-to-Bicyclist Longitudinal Adult (CBLA) – a collision in which a vehicle travels forwards towards a bicyclist cycling in the same direction in front of the vehicle where the vehicle would strike the cyclist when no braking action is applied or an evasive steering action is initiated after an FCW. 

Car-to-Bicyclist Turning Adult (CBTA) – a collision in which a vehicle turns towards a bicyclist crossing its path, cycling in the opposite direction across a junction and the frontal structure of the vehicle strikes the cyclist when no braking action is applied. 

Car-to-Motorcyclist Rear Stationary (CMRs) – a collision in which a vehicle travels forwards towards a motorcyclist and the front structure of the vehicle strikes the rear of the motorcycle. 

Car-to-Motorcyclist Rear Braking (CMRb) – a collision in which a vehicle travels forwards towards a motorcyclist that is travelling at constant speed and then decelerates, and the frontal structure of the vehicle strikes the rear of the motorcycle. 

Car-to-Motorcyclist Front Turn Across Path (CMFtap) – a collision in which a vehicle turns across the path of an oncoming motorcyclist travelling at a constant speed, and the frontal structure of the vehicle strikes the front of the motorcycle. 

Car-to-Motorcyclist Crossing Straight Crossing Path (CMCscp) – a collision in which a vehicle travels forwards along a straight path across a junction, towards a motorcyclist crossing the junction on a perpendicular path. The frontal structure of the vehicle under test strikes the front of the motorcycle. 

Car-to-Car Rear Stationary (CCRs) – a collision in which a vehicle travels forwards towards another stationary vehicle and the frontal structure of the vehicle strikes the rear structure of the other. 

Car-to-Car Rear Moving (CCRm) – a collision in which a vehicle travels forwards towards another vehicle that is travelling at constant speed and the frontal structure of the vehicle strikes the rear structure of the other. 

Car-to-Car Rear Braking (CCRb) – a collision in which a vehicle travels forwards towards another vehicle that is travelling at constant speed and then decelerates, and the frontal structure of the vehicle strikes the rear structure of the other. 

Car-to-Car Front Turn-Across-Path (CCFtap) – a collision in which a vehicle turns across the path of an oncoming vehicle travelling at constant speed, and the frontal structure of the vehicle strikes the front structure of the other. 

Car-to-Car Crossing Straight Crossing Path (CCCscp) – a collision in which a vehicle travels forwards along a straight path across a junction, towards a vehicle crossing the junction on a perpendicular path. The frontal structure of the vehicle under test strikes the side of the other vehicle. 

Car-to-Car Front Head-On Straight (CCFhos) – a collision where a vehicle is travelling along a straight path within its defined lane and strikes another vehicle travelling in the opposite direction, which has drifted into the same lane as the original vehicle. The frontal structure of the vehicle strikes the frontal structure of the other. 

Car-to-Car Front Head-On Lane change (CCFhol) – a collision where a vehicle is travelling along a straight path within its defined lane and strikes another vehicle travelling in the opposite direction which has intentionally moved into the lane of the original vehicle to attempt an overtake. The frontal structure of the vehicle strikes the frontal structure of the other. 

# 1 MEASURING REQUIREMENTS

# Reference System

# 1.1.1 Local Coordinate System

Use the convention specified in ISO 8855:2011, with the origin at the most forward point on the centreline of the VUT for dynamic data measurements as shown in Figure 1-1. This reference system should be used for both left- and right-hand drive vehicles. In Figure 1-1 nearside and farside are shown for a left-hand drive vehicle. For a right-hand drive vehicle, nearside and far-side are swapped. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/0a175bb01e88a6c5a94f6a7d609455515a72fab818c8999117a9ac1e68f9a70e.jpg)



Figure 1-1 Coordinate system and notation


# 1.1.2 Global Coordinate System

The origin of the Global Coordinate System $\scriptstyle \mathtt { X } = 0$ , $\scriptstyle \mathtt { Y } = 0$ ) shall be located: 

In longitudinal scenarios, at the position where the projected path of the impact location of the VUT coincides with the Target reference point. 

In crossing scenarios, at the intersection between the projected paths of the VUT and Target reference points. 

In turning scenarios, at the geometric centre of the marked intersection. 

# Scenario Parameters

# 1.2.1 VUT Longitudinal Path Error

# 1 . 2 . 1 . 1 C a r - t o - C a r

The VUT longitudinal path error is determined as the difference between the desired position and the ctu l position of the f ont of the VUT when me su ed t single defined “st ble” position of the front of the GVT during the test. 

$$
V U T \text {l o n g i t u d i n a l} = X _ {V U T, \text {d e s i r e d}} - X _ {V U T, \text {a c t u a l}} (@ X _ {G V T})
$$

For CCFtap, when the origin of the reference system is at the intended collision point, the values shown in the table below shall be used to determine the VUT longitudinal path error. 

<table><tr><td>VUT speed</td><td>Target speed</td><td>XVUT, desired</td><td>XGVT</td></tr><tr><td rowspan="3">10 km/h</td><td>30 km/h</td><td></td><td>29.17 m</td></tr><tr><td>45 km/h</td><td>-9.57 m</td><td>43.75 m</td></tr><tr><td>60 km/h</td><td></td><td>58.33 m</td></tr><tr><td rowspan="3">15 km/h</td><td>30 km/h</td><td></td><td>29.17 m</td></tr><tr><td>45 km/h</td><td>-14.53 m</td><td>43.75 m</td></tr><tr><td>60 km/h</td><td></td><td>58.33 m</td></tr><tr><td rowspan="3">20 km/h</td><td>30 km/h</td><td></td><td>29.17 m</td></tr><tr><td>45 km/h</td><td>-19.47 m</td><td>43.75 m</td></tr><tr><td>60 km/h</td><td></td><td>58.33 m</td></tr><tr><td rowspan="3">25 km/h</td><td>30 km/h</td><td></td><td>29.17 m</td></tr><tr><td>45 km/h</td><td>-24.33 m</td><td>43.75 m</td></tr><tr><td>60 km/h</td><td></td><td>58.33 m</td></tr></table>

# 1 . 2 . 1 . 2 C a r - t o - M o t o r c y c l i s t

For CMFtap scenario, the VUT longitudinal path error is determined as the difference between the desired position and the actual position of the front of the VUT when measured at a single defined “st ble” position of the f ont of the EMT du ing the test. 

$$
V U T \text {l o n g i t u d i n a l p a t h e r r o r} = X _ {V U T, \text {d e s i r e d}} - X _ {V U T, \text {a c t u a l}} (@ X _ {E M T})
$$

When the origin of the reference system is at the intended collision point, the values shown in the table below shall be used to determine the VUT longitudinal path error. 

<table><tr><td>VUT speed</td><td>Target speed</td><td>XVUT, desired</td><td>XEMT</td></tr><tr><td rowspan="2">10 km/h</td><td>30 km/h</td><td rowspan="2">-10.66 m</td><td>33.33 m</td></tr><tr><td>45 km/h</td><td>50.00 m</td></tr><tr><td></td><td>60 km/h</td><td></td><td>66.66 m</td></tr><tr><td rowspan="3">15 km/h</td><td>30 km/h</td><td rowspan="3">-16.39 m</td><td>33.33 m</td></tr><tr><td>45 km/h</td><td>50.00 m</td></tr><tr><td>60 km/h</td><td>66.66 m</td></tr><tr><td rowspan="3">20 km/h</td><td>30 km/h</td><td rowspan="3">-22.02 m</td><td>33.33 m</td></tr><tr><td>45 km/h</td><td>50.00 m</td></tr><tr><td>60 km/h</td><td>66.66 m</td></tr><tr><td rowspan="3">25 km/h</td><td>30 km/h</td><td rowspan="3">-27.60 m</td><td>33.33 m</td></tr><tr><td>45 km/h</td><td>50.00 m</td></tr><tr><td>60 km/h</td><td>66.66 m</td></tr></table>

# 1.2.2 VUT Lateral Path Error

The lateral offset (YVUT-error) is determined as the lateral distance between the centre of the front axle of the VUT when measured in parallel to the intended path as shown in Figure 1-2 VUT Lateral Path Error. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/ae7e06f7be02fdf710d6dc22625b44a4dbc1588f8c96547c26362484490e0e79.jpg)



Figure 1-2 VUT Lateral Path Error


# 1.2.3 SCP Time Error

The SCP (Straight Crossing Path) Time Error is determined as the difference between the actual time of the VUT to the intended collision point (CP) and the actual time of the target, GVT or EMT, to the intended collision point (CP). This is applicable to CCCscp and CMCscp scenarios. 

$$
V U T T i m e E r r o r [ s ] = \frac {X _ {C P} - X _ {V U T , a c t u a l}}{V _ {V U T , a c t u a l}} - \frac {Y _ {C P} - Y _ {T a r g e t , a c t u a l}}{V _ {T a r g e t , a c t u a l}}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/fee45141e01baa4da94e343cb79b95923adeb27a871b0ae1deca91c2e7d38825.jpg)


# 1.2.4 Test paths for turning scenarios

For CPTA, CBTA, CCFtap and CMFtap, the following parameters should be used to create the test paths. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/b6e242cbe199b3c542f6ebe1be943eaff3fbfff17f8c514ef2aa708aeffb01f7.jpg)


<table><tr><td rowspan="2">Test Speed</td><td colspan="3">Part 1 (Clothoid)</td><td colspan="3">Part 2 (constant radius)</td><td colspan="3">Part 3 (Clothoid)</td></tr><tr><td>Start Radius R1 [m]</td><td>End Radius R2 [m]</td><td>Angle α [deg]</td><td>Start Radius R1 [m]</td><td>End Radius R2 [m]</td><td>Angle β [deg]</td><td>Start Radius R2 [m]</td><td>End Radius R1 [m]</td><td>Angle α [deg]</td></tr><tr><td>10 km/h to Farside</td><td>1500</td><td>9.00</td><td>20.62</td><td>9.00</td><td>9.00</td><td>48.75</td><td>9.00</td><td>1500</td><td>20.62</td></tr><tr><td>15 km/h to Farside</td><td>1500</td><td>11.75</td><td>20.93</td><td>11.75</td><td>11.75</td><td>48.14</td><td>11.75</td><td>1500</td><td>20.93</td></tr><tr><td>20 and 25 km/h to Farside</td><td>1500</td><td>14.75</td><td>21.79</td><td>14.75</td><td>14.75</td><td>46.42</td><td>14.75</td><td>1500</td><td>21.79</td></tr><tr><td>10 km/h to Nearside</td><td>1500</td><td>8.00</td><td>22.85</td><td>8.00</td><td>8.00</td><td>44.30</td><td>8.00</td><td>1500</td><td>22.85</td></tr></table>

# 1.2.5 Impact location

Impact location is defined as where the reference point of the target coincides with the $\%$ -age of the VUT width. For reference, $0 \%$ is defined is the projection of the outer right edge of the vehicle, and $100 \%$ is defined is the projection of the outer left edge of the vehicle (according to the definition of the vehicle width). 

For scenarios involving a side impact (CMCscp, CBTAfs, CBTAns) the impact location is defined as where the reference point of the target coincides with the $\%$ -age of the VUT length. For reference, $100 \%$ is defined is the projection of the most forward point of the vehicle, and $0 \%$ is defined is the projection of the most rearward point of the vehicle (according to the definition of the vehicle length). 


1.2.5.1 Car-to-Car Rear


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/3e75c6552b31394e16013b97b3bb51b0ac9434830eaa25a1a44f6f6a35dd1655.jpg)


# 1.2.5.2 Car-to-car Rear $^ +$ Heading

Rotation by target reference point, dependent on combination of VUT impact location and rotation direction, collision may occur with corner edge before impact location and target reference point contact: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/44161e08bf9f898a274cd2bd9d973598a8ea0e6aa1a3b7b045815c43bcc652ed.jpg)



1.2.5.3 Car-to-Car Front


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/47d9f6a035fbeec3b3016443c28182ec9b9a563a551cf93367247efed177fd2a.jpg)



1.2.5.4 Car-to-Car Crossing


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/dd8e30aac153c95693b8fb8bc1ac14b84f5c343f019b13b55e17514f71b5e540.jpg)



1.2.5.5 Car-to-Car Turn Across Path


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/53919226b7a41aaf7d1ff6e7f9a3bf3ec9db63bffc16bbfd2cc5ec5e5f3ff6b9.jpg)



1.2.5.6 Car-to-PTW Rear


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/a3859219419605347a9705e18c6a710c8c49c659e7afafb468ed934fe227b0a4.jpg)


# 1.2.5.7 Car-to-PTW Crossing

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/3e3f486b59d674aa57a4a1c5291fdfc09bb2a4680264e36d15a8f41363f8ac3b.jpg)



$90 \%$ side impact location (nearside)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/3d26ababb0472110a61433a49b2e32c7181dcfafbdb1a1295f1e9fe640af9969.jpg)



$90 \%$ side impact location (farside)


# 1.2.5.8 Car-to-PTW Turn Across Path

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/14e2c2b43bb3149a17341b15cd5495a92e1ae3fd8a501284cfb08c694f1d14c0.jpg)



Impact location


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/fd2f331d34fc62d74fc4c708b02d7654200d1fdd4dca5373007ca4e453358eed.jpg)



75%


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/ee58974c853823365395fdddcdf01d8ba5c534f30df0c56e58c71375e0e0910a.jpg)



50%



25%


# 1.2.5.9 Car-to-PedestrianTurning

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/7ebc07cece2beadd249f67ae6110e65a9bfc5396931eaff948a06efe05c0f09d.jpg)



50% impact location


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/c089f8baaaeaf4e00b40c16c093877923fea328ccc4d225507b157ab9b94cba8.jpg)



$5 0 \%$ impact location


# 1.2.5.10 Car- to- Bicyclist Turning

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/58453a52cbdf4426c7d6a30953ba7ac2aa3094f0c547b59c8a176adccf8fc122.jpg)



50% impact location


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/2b19be87f6919f6596e7a1173c904971160c84749a493be104d7ce9576924c6b.jpg)



50% impact location


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/35e6936c03aeadd1e13290ed72b0f10ef287b9acbafec44683a2b4d064608d7e.jpg)



75% side impact location (farside)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/650e4a5539e0f671629a78c39f4d742fad0faeddb08e98dc3940aa7f195fc028.jpg)



$7 5 \%$ side impact location (nearside)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/f1d153ac21a96918aeac22891fe164c665d18aa7f2ba074b23848c5d597d6c8e.jpg)



Impact location (farside)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/a6fdb4fd95a00a974d1f2b64534806fbec4a2d64c17328a6c696ea344c71cd1d.jpg)



Impact location (nearside)



0%


# VUT

# 1 . 3 .1 V UT P rof i le

A virtual profiled line is defined around both the front end and the rear end of the VUT, as well as around the right and left side of the VUT. The front and rear profiles are defined by straight line segments connecting seven points that are equally distributed over the vehicle width minus 50mm on each side. The side profiles are defined by straight line segments connecting seven points that are equally distributed between the outermost rear and front profiles, on each side. The theoretical x,y coordinates for each of these points are provided by the OEMs and verified by the test laboratory. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/5cd749917a2b6fcf30c1794690920cd43883dff350995f24cd69cd09996a854b.jpg)



Figure 1-3 Virtual profiled line around the front end, rear end of the VUT


# Targets

Only equipment listed in the current version of TB G003-1 and TB G003-2 may be used for testing. The current version can be found on the Euro NCAP website. 

# 1.4.1 Virtual Boxes

For each test target, a virtual box defined will be used to determine the impact speed. The dimensions of these virtual boxes are shown in the figures below, along with impact reference points related to each test target. 

Impact location descriptions in section 1.2.5 and scenario descriptions in section 3 illustrate which of the reference points is to be utilised for each specific scenario. 

# 1.4.1.1 EPTa and EPTc

The dimensions of this virtual box are shown in the figure below, with reference points on the hip (for turning scenarios) and at the back where the centreline of the dummy crosses the virtual box (for longitudinal scenarios). 

Euro NCAP 

Version 1.1 — October 2025 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/1c5bfdf35ff6583087ce52f92cca5ed53416781fef01211f8d9cbc5116cd9b00.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/513f49eef4dd66d66fb8b760381eb0bcb1e256c699aaf06e35d5e0738febd6d9.jpg)



Figure 1.2.1: Virtual box dimensions around EPTa and EPTc


# 1.4.1.2 EBT

The dimensions of this virtual box are shown in the figure below, with reference points on the crank shaft (applicable to crossing scenarios), most forward point on the front wheel (applicable to turning scenarios) and most rearward point on the rear wheel (applicable to longitudinal scenarios). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/f94a8dc914b63e095f236f1b540c6492041af1ae90de061dd5d89064a5e44d0a.jpg)



Figure 1.2.2: Virtual box dimensions around EBT


# 1.4.1.3 EMT

The dimensions of this virtual box are shown in the figure below with reference points on the most forward point on the front wheel (applicable to longitudinal-front, turning and crossing scenarios) and most rearward point on the rear wheel (applicable to longitudinal-rear scenarios). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/1464dd529ad8f60878fc3608533a8f1acc62edf8cded0a48d699b8bc274eee3b.jpg)



Figure 1.2.3: Virtual box dimensions around EMT


# 1.4.1.4 GVT

The virtual box of the GVT is shown in the figure below, with reference points on: the most forward point on the front profile (1 in the centre and 1 in the intersection of the front profile and each of the side profiles), the most rearward point on the rear profile (in the centre), and at $7 5 \%$ along the length of each side of the GVT. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/3852125321c4151f1ccb1a124c37f4c91ed899507df6faab383748935ea7477b.jpg)



Figure 1.2.4: Virtual box illustration around the GVT


# Measurements and variables

Sample and record all dynamic data at a frequency of at least 100Hz. Synchronise using the DGPS time stamp the target data with that of the VUT. 

# 1.5.1 Variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>T</td><td>Time</td></tr><tr><td>T0</td><td>Time of test start T0 = TTC 4s, unless stated otherwise</td></tr><tr><td></td><td>- Turning scenarios: T0 = Tsteer -1s</td></tr><tr><td></td><td>- braking scenarios: T0 = TTarget_deceleration_start -1s</td></tr><tr><td></td><td>- Crossing scenarios: T0 = 0.5s after target acceleration phase</td></tr><tr><td>TAEB</td><td>Time where AEB activates</td></tr><tr><td>TFCW</td><td>Time where FCW activates</td></tr><tr><td>Timpact</td><td>Time where the VUT impacts the target</td></tr><tr><td>Tsteer</td><td>Time where the VUT enters in curve segment</td></tr><tr><td>TTarget_deceleration_start</td><td>Time where the target starts decelerating</td></tr><tr><td>Tend</td><td>Time of test end (see 4.3.2 and 4.3.3)</td></tr><tr><td>Vimpact</td><td>Speed when the VUT impacts the target</td></tr><tr><td>Vrel_impact</td><td>Relative speed when the VUT impacts the target</td></tr><tr><td>XVUT, YVUT</td><td>Position of the VUT during the entire test</td></tr><tr><td>VVUT</td><td>Speed of the VUT during the entire test</td></tr><tr><td>AVUT</td><td>Acceleration of the VUT during the entire test</td></tr><tr><td>ψVUT</td><td>Yaw velocity of the VUT during the entire test</td></tr><tr><td>ΩVUT</td><td>Steering wheel velocity of the VUT during the entire test</td></tr><tr><td>Xtarget, Ytarget</td><td>Position of the target during the entire test</td></tr><tr><td>Vtarget</td><td>Speed of the target during the entire test</td></tr><tr><td>Atarget</td><td>Acceleration of the target during the entire test</td></tr><tr><td>ψtarget</td><td>Yaw velocity of the target during the entire test</td></tr></table>

# 1.5.2 Measurements

Equip the VUT and GVT with data measurement and acquisition equipment to sample and record data with an accuracy of at least: 

VUT and target speed to 0.1km/h 

- VUT and target lateral and longitudinal position to 0.03m 

VUT heading angle to $0 . 1 ^ { \circ }$ 

- VUT and target yaw rate to $0 . 1 \%$ 

VUT and target longitudinal acceleration to $0 . 1 \mathsf { m } / \mathsf { s } ^ { 2 }$ 

VUT steering wheel velocity to $1 . 0 ~ \%$ 

# 1 . 5 . 3 D a t a F i l t e r i n g

Filter the measured data as follows: 

- Position and speed are not filtered and are used in their raw state. 

Acceleration, yaw rate, steering wheel velocity and force are filtered with a 12-pole phase less Butterworth filter with a cut off frequency of $1 0 H z$ . 

# 2 TEST CONDITIONS

# Test track

Conduct tests on a dry (no visible moisture on the surface), uniform, solid paved surface with a maximum longitudinal slope of $\pm 1 \%$ and a maximum lateral slope of $\pm 3 \%$ . The test surface shall have a minimal peak braking coefficient (PBC) of 0.9. 

The test track surface must be paved and may not contain irregularities (e.g. large dips or cracks, manhole covers or reflective studs) that may give rise to abnormal sensor measurements within a lateral distance of $5 . 0 \mathsf { m }$ to either side of the test path, and with a longitudinal distance of 20m ahead of the VUT when the test ends. 

Unless otherwise specified, conduct testing such that, between ${ \sf T } _ { 0 }$ and the test end, there are no other vehicles, infrastructure (except lighting columns during the low ambient lighting condition tests), obstructions, other objects or persons which may give rise to abnormal sensor measurements within the visual axis of the VUT and test target, and $_ { 2 0 \mathsf { m } }$ ahead of the VUT at test end. 

The general view ahead and to either side of the test area shall not comprise of any highly reflective surfaces or contain any silhouettes similar in shape to the test target. 

# 2.1.1 Lane Markings

The presence of lane markings is allowed for CCR tests. However, testing may only be conducted in an area where typical road markings depicting a driving lane may not be parallel to the test path within 3.0m either side. Lines or markings may cross the test path but may not be present in the area where AEB activation and/or braking after FCW is expected. 

Some scenarios described in this document require the use of a junction, where this is the case the scenario description will illustrate the scenario on a junction as in Figure 4.2. The main approach lane where the VUT path starts, (horizontal lanes in Figure 4.2) will have a width of 3.5m. The side lane (vertical lanes in Figure 4.2) will have a width of 3.25 to 3.5m. The lane markings on these lanes need to conform to one of the lane markings as defined in UNECE Regulation 130: 

Dashed line starting at the same point where the radius transitions into a straight line with a width between 0.10 and 0.15m 

Solid line with a width between 0.10 and 0.25m 

Junction without any central markings 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/32957931ea7613daf35e501c011553139e245dec2ee56fc7a1ba8c219b4d78e1.jpg)



Figure 4.2: Layout of junction and the connecting lanes


# Weather Conditions

Conduct tests in dry conditions with ambient temperature above $5 \textdegree C$ and below $4 0 ^ { \circ } \mathsf { C }$ . 

No precipitation shall be falling and horizontal visibility at ground level shall be greater than 1km. Wind speeds shall be below $1 0 \mathsf { m } / \mathsf { s }$ to minimise Target and VUT disturbance. 

Natural ambient illumination must be homogenous in the test area and in excess of 2000 lux for daylight testing with no strong shadows cast across the test area other than those caused by the VUT or Target. Ensure testing is not performed driving towards, or away from the sun when there is direct sunlight. 

Measure and record the following parameters preferably at the commencement of every single test or at least every 30 minutes: 

Ambient temperature in $^ \circ \mathsf { C }$ 

Track Temperature in $^ \circ \mathsf { C }$ 

Wind speed and direction in m/s 

Ambient illumination in Lux 

# Surroundings

Conduct testing such that there are no other vehicles, highway infrastructure (except lighting columns during the low ambient lighting condition tests), obstructions, other objects or persons protruding above the test surface, that may give rise to abnormal sensor measurements during the full duration of the test starting at T0 and within a longitudinal distance 20m ahead of the VUT when the test ends, within: 

5m either side of the VUT test path, 

a circle around the GVT, and 

The visual axis between the geometric centre of the VUT and the circle surrounding the GVT. 

- For CCCscp only, the above applies from TTC $= 3 . 5 5$ (instead of T0). 

Euro NCAP 

Version 1.1 — October 2025 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/a317ec1df7c03b75243f33053374101671b6dbb6d02c18e82698a0e8a49aaea5.jpg)



Figure 2-1 Free space requirements – CCCscp Farside Test


Test areas where the VUT needs to pass under overhead signs, bridges, gantries or other significant structures are not permitted. 

The general view ahead and to either side of the test area shall comprise of a wholly plain man made or natural environment (e.g. further test surface, plain coloured fencing or hoardings, natural vegetation or sky etc.) and must not comprise any highly reflective surfaces or contain any vehicle-like silhouettes that may give rise to abnormal sensor measurements. 

# VUT Preparation

# 2.4.1 System Settings

Set any driver configurable elements of the AEB and/or FCW system (e.g. the timing of the collision warning or the braking application if present) to the middle setting or midpoint and then next latest setting similar to the examples shown in Figure 4.4. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/7f26966dc7548f4c8ba7f0dfd16f2cbaf093b91c035b10ed90d9c27f4774c377.jpg)



Figure 4.4: AEB and/or FCW system setting for testing


When the vehicle is equipped with a Driver State Monitoring (DSM) which alters the AEB and/or F W sensitivity cco ding to the d ive ’s st te as described in section 5.4, the Vehicle Manufacturer shall provide a list of the scenarios that are to be tested with Driver State Link. For all other scenarios the system shall be deactivated before the testing commences. 

When the vehicle is equipped with a deployable pedestrian/VRU protection system, this system shall be deactivated before the testing commences. 

Euro NCAP 

Version 1.1 — October 2025 

# 2.4.2 Tyres

Perform the testing with new original fitment tyres of the make, model, size, speed and load rating as specified by the vehicle manufacturer. It is permitted to change the tyres which are supplied by the manufacturer or acquired at an official dealer representing the manufacturer if those tyres are identical make, model, size, speed and load rating to the original fitment. Inflate the tyres to the vehicle manufacturer’s recommended cold tyre inflation pressure(s). Use inflation pressures corresponding to least loading normal condition. 

Run-in tyres according to the tyre conditioning procedure. After running-in maintain the run-in tyres in the same position on the vehicle for the duration of the testing. 

# 2.4.3 Wheel Alignment Measurement and Unladen Kerb Mass

The vehicle should be subject to a vehicle (in-line) geometry check to record the wheel alignment set by the OEM. This should be done with the vehicle in kerb weight. 

If applicable, fill up the t nk with fuel to t le st $90 \%$ of the t nk’s c p city of fuel. 

Check the oil level and top up to its maximum level if necessary. Similarly, top up the levels of all other fluids to their maximum levels if necessary. 

Ensure that the vehicle has its spare wheel on board, if fitted, along with any tools supplied with the vehicle. Nothing else should be in the car. 

Ensu e th t ll ty es e infl ted cco ding to the m nuf ctu e ’s inst uctions fo the pp op i te loading condition. 

Measure the front and rear axle masses and determine the total mass of the vehicle. The total m ss is the ‘unl den ke b m ss’ of the vehicle. Reco d this m ss in the test det ils. 

Calculate the required ballast mass, by subtracting the mass of the test driver and test equipment from the required $2 0 0 ~ \mathsf { k g }$ interior load. 

# 2.4.4 Vehicle Preparation

Fit the on-board test equipment and instrumentation in the vehicle. Also fit any associated cables, cabling boxes and power sources and place weights with a mass of the ballast mass. Any items added should be securely attached to the car. 

With the driver in the vehicle, weigh the front and rear axle loads of the vehicle and compare these lo ds with the “unl den ke b m ss” 

The total vehicle mass shall be within $\pm 1 \%$ of the sum of the unladen kerb mass, plus 200kg. The front/rear axle load distribution needs to be within $5 \%$ of the front/rear axle load distribution of the original unladen kerb mass plus full fuel load. If the vehicle differs from the requirements given in this paragraph, items may be removed or added to the vehicle which has no influence on its performance. Any items added to increase the vehicle mass should be securely attached to the car. 

Care needs to be taken when adding or removing weight in order to approximate the original vehicle inertial properties as close as possible. Record the final axle loads in the test details. Reco d the xle weights of the VUT in the ‘ s tested’ condition. 

# 3 TEST PROCEDURE

Each scenario in this assessment consists of a matrix combining vehicle longitudinal speeds, and ranges of impact locations or target longitudinal speeds. Each combination in a matrix is referred to as grid cell. The grid cells forming a matrix are grouped into two groups: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/a0471379d0ef5ad011d3a6c1ed019fe73908b1b313000d501f318aaad49928ea.jpg)


Standard Range 

Extended Range 

# Car & PTW Scenarios

<table><tr><td rowspan="2">Car &amp; PTW Scenarios</td><td colspan="4">Score</td></tr><tr><td>Standard</td><td>Extended</td><td>Robustness</td><td>Total</td></tr><tr><td>Longitudinal</td><td></td><td></td><td></td><td>15.0</td></tr><tr><td>Car-to-Car Rear</td><td>5.2</td><td>0.65</td><td>0.65</td><td></td></tr><tr><td>Car-to-Car Front</td><td>4.0</td><td>0.5</td><td>0.5</td><td></td></tr><tr><td>Car-to-Motorcyclist Rear</td><td>2.8</td><td>0.35</td><td>0.35</td><td></td></tr><tr><td>Turning</td><td></td><td></td><td></td><td>10.0</td></tr><tr><td>Car-to-Car Turn Across Path</td><td>4.0</td><td>0.5</td><td>0.5</td><td></td></tr><tr><td>Car-to-Motorcyclist Turn Across Path</td><td>4.0</td><td>0.5</td><td>0.5</td><td></td></tr><tr><td>Crossing</td><td></td><td></td><td></td><td>15.0</td></tr><tr><td>Car-to-Car Crossing</td><td>6</td><td>0.75</td><td>0.75</td><td></td></tr><tr><td>Car-to-Motorcyclist Crossing</td><td>6</td><td>0.75</td><td>0.75</td><td></td></tr></table>

# 3.1.1 Longitudinal

<table><tr><td rowspan="2">Longitudinal</td><td colspan="4">Score</td></tr><tr><td>Standard</td><td>Extended</td><td>Robustness</td><td>Total</td></tr><tr><td>Car-to-Car-Rear</td><td></td><td></td><td></td><td rowspan="4">6.5</td></tr><tr><td>CCRs</td><td>1.2</td><td>0.15</td><td>0.15</td></tr><tr><td>CCRm</td><td>2.4</td><td>0.3</td><td>0.3</td></tr><tr><td>CCRb</td><td>1.6</td><td>0.2</td><td>0.2</td></tr><tr><td>Car-to-Car-Front</td><td></td><td></td><td></td><td rowspan="3">5.0</td></tr><tr><td>CCFhos</td><td>2.0</td><td>0.25</td><td>0.25</td></tr><tr><td>CCFhol</td><td>2.0</td><td>0.25</td><td>0.25</td></tr><tr><td>Car-to-Motorcyclist Rear</td><td></td><td></td><td></td><td rowspan="3">3.5</td></tr><tr><td>CMRs</td><td>1.2</td><td>0.15</td><td>0.15</td></tr><tr><td>CMRb</td><td>1.6</td><td>0.2</td><td>0.2</td></tr></table>


3.1.1.1 Car-to-Car Rear


<table><tr><td rowspan="2">CCRs</td><td rowspan="2">GVT speed</td><td rowspan="2">Function</td><td colspan="7">Impact Location</td></tr><tr><td>125%</td><td>100%</td><td>75%</td><td>50%</td><td>25%</td><td>0%</td><td>-25%</td></tr><tr><td>10 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>0 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>0 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>0 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The Vehicle Manufacturer shall inform Euro NCAP whether the FCW cases are to be verified with FCW or AEB. Where the AEB system is able to match the colour prediction in the FCW cases, the points are automatically awarded for the corresponding FCW test. 

<table><tr><td rowspan="2">CCRm</td><td rowspan="2">GVT speed</td><td rowspan="2">Function</td><td colspan="7">Impact Location</td></tr><tr><td>125%</td><td>100%</td><td>75%</td><td>50%</td><td>25%</td><td>0%</td><td>-25%</td></tr><tr><td>30 km/h</td><td>20 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>20 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>20 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>20 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>20 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>20 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>30 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td>40 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>110 km/h</td><td>50 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>120 km/h</td><td>60 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>130 km/h</td><td>70 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">CCRb</td><td rowspan="2">GVT speed</td><td rowspan="2">Function</td><td colspan="7">Impact Location</td></tr><tr><td>125%</td><td>100%</td><td>75%</td><td>50%</td><td>25%</td><td>0%</td><td>-25%</td></tr><tr><td>30 km/h</td><td>30 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>40 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>50 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>60 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>70 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>80 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>90 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td>100 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>110 km/h</td><td>110 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>120 km/h</td><td>120 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>130 km/h</td><td>130 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Euro NCAP 

Version 1.1 — October 2025 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/c1f62814c481fe06aeddf38cb3b7967546cf9f656cd625acade32caea3836666.jpg)


For CCRb, the Time Headway $= 1 . 0 \ s$ , and the target acceleration $= - 4 \mathsf { m } / \mathsf { s } ^ { 2 }$ for both Standard Range and Extended Range. 

The desired deceleration of the GVT shall be reached within 1.0 second $( \mathsf { T } _ { 0 } + 2 . 0 \mathsf { s } )$ which after the GVT shall remain within $\pm \ : 0 . 5 \ : \mathsf { k m / h }$ of the reference speed profile, derived from the desired deceleration, until the vehicle speed equals 2km/h. 

# 3 . 1 . 1 . 2 C a r - t o - C a r F r o n t

<table><tr><td rowspan="2">CCFhos</td><td rowspan="2">GVT speed</td><td colspan="4">Impact Location</td></tr><tr><td>100%</td><td>75%</td><td>50%</td><td>25%</td></tr><tr><td>30 km/h</td><td>50 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>50 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>50 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>90 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td>100 km/h</td><td></td><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/df0a168205ddb0d7b3260501f0e8017b925a40559df28a214c8960c5acc07b66.jpg)



Figure 3-1 CCFhos


<table><tr><td rowspan="2">CCFhol</td><td rowspan="2">GVT &amp; SOV speed</td><td colspan="4">Impact Location</td></tr><tr><td>100%</td><td>75%</td><td>50%</td><td>25%</td></tr><tr><td>30 km/h</td><td>50 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>50 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>50 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>90 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td>100 km/h</td><td></td><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/46bdae7b7f6e4dc77fcec9d9e500f887d2aab8cb3719743ed835b09cd8e73161.jpg)



Figure 3-2 CCFhol


Detailed scenario parametrization in CCFhol for all VUT and Target speed combinations will be made available through OpenScenario files by Euro NCAP in GitHub. 

Below table indicates the parameters of test cases where the VUT and Target travel at the same speed, and with a $50 \%$ impact location (full overlap). When impact location is different than $50 \%$ , the initial lateral position of SOV and GVT shall be altered so that a 3.5m lane change offset (parameter O) results in the targeted impact location. 

<table><tr><td>GVT &amp; SOV speed</td><td>Lane change offset (O)</td><td>Curvature (1/m)</td><td>Lane change length (L)</td><td>Following Distance (F)</td><td>TTC at end of lane change</td><td>Max Lateral acceleration</td></tr><tr><td>50 km/h</td><td>3.5 m</td><td>0.0076</td><td>44 m</td><td>[13.9] m</td><td>[1.5] s</td><td>1.50 m/s2</td></tr><tr><td>70 km/h</td><td>3.5 m</td><td>0.0039</td><td>60 m</td><td>[19.4] m</td><td>[1.5] s</td><td>1.50 m/s2</td></tr><tr><td>90 km/h</td><td>3.5 m</td><td>0.0023</td><td>78 m</td><td>[25.0] m</td><td>[1.5] s</td><td>1.50 m/s2</td></tr><tr><td>100 km/h</td><td>3.5 m</td><td>0.0019</td><td>88 m</td><td>[27.8] m</td><td>[1.5] s</td><td>1.50 m/s2</td></tr></table>

Euro NCAP 

Version 1.1 — October 2025 


3.1.1.3 Car-to- Motorcyclist Rear


<table><tr><td rowspan="2">CMRs</td><td rowspan="2">EMT speed</td><td rowspan="2">Function</td><td colspan="5">Impact Location</td></tr><tr><td>90%</td><td>75%</td><td>50%</td><td>25%</td><td>10%</td></tr><tr><td>10 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>0 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>0 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>0 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>0 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/bc1d8ef857054d7c380aeddf52b7a34f6296dd4eb865a69e59bb4a6cf4a45458.jpg)



Figure 3-3 CMRs scenario, representing the $50 \%$ impact location


The Vehicle Manufacturer shall inform Euro NCAP whether the FCW cases are to be verified with FCW or AEB. Where the AEB system is able to match the colour prediction in the FCW cases, the points are automatically awarded for the corresponding FCW test. 

<table><tr><td rowspan="2">CMRb</td><td rowspan="2">EMT Speed</td><td rowspan="2">Function</td><td colspan="5">Impact Location</td></tr><tr><td>90%</td><td>75%</td><td>50%</td><td>25%</td><td>10%</td></tr><tr><td>30 km/h</td><td>30 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>40 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>50 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>60 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>70 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>80 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>90 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td>100 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>110 km/h</td><td>110 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>120 km/h</td><td>120 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>130 km/h</td><td>130 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/ccb348d8fe74bf1c6486f74168cce5b59dd888f7f1e8a81c1f525b7609fe87a4.jpg)



Figure 3-4 CMRb scenario, representing the $2 5 \%$ impact location


For CMRb, the Time Headway $= 1 . 0 \ s$ , and the target acceleration $= - 4 \mathsf { m } / \mathsf { s } ^ { 2 }$ for both Standard Range and Extended range. The desired deceleration of the EMT shall be reached within 1.0 second $( \mathsf { T } 0 + 2 . 0 \mathsf { s } )$ which after the EMT shall remain within $\pm \ : 0 . 5 \ : \mathsf { k m / h }$ of the reference speed profile, derived from the desired deceleration, until the vehicle speed equals 2km/h. 

# 3.1.2 Turning

<table><tr><td rowspan="2">Turning</td><td colspan="4">Score</td></tr><tr><td>Standard</td><td>Extended</td><td>Robustness</td><td>Total</td></tr><tr><td>Car-to-Car Front TAP</td><td>4.0</td><td>0.5</td><td>0.5</td><td>5.0</td></tr><tr><td>Car-to-Motorcyclist Front TAP</td><td>4.0</td><td>0.5</td><td>0.5</td><td>5.0</td></tr></table>

# 3.1.2.1 Car-to-Car Front Turn Across Path

<table><tr><td>CCFtap</td><td colspan="4">GVT speed</td></tr><tr><td></td><td>30 km/h</td><td>45 km/h</td><td>60 km/h</td><td>80 km/h</td></tr><tr><td>10 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>15 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>25 km/h</td><td></td><td></td><td></td><td></td></tr></table>

For the CCFtap scenario, for the VUT assume an initial straight-line path followed by a turn (clothoid, fixed radius and clothoid as specified in section 1.2.4), followed again by a straight line, hereby known as the test path. The direction indicator is applied at $1 . 0 \mathsf { s } \pm 0 . 5 \mathsf { s }$ before Tsteer. 

The GVT will follow a straight-line p th in the l ne dj cent to the VUT’s initi l position, in the opposite direction to the VUT. The straight-line path of the VUT and GVT will be 1.75m from the centre of the centre dashed lane marking of the VUT lane. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/916bad08267bcea443b6bcc65bf1898534fca566906fe09b45a38e56f55c0df8.jpg)



Figure 3-5 CCFtap scenario VUT and GVT paths


The paths of the VUT and target vehicle will be synchronised so that the front edges of the target meets the $50 \%$ impact location (assuming no system reaction) of the width of the VUT. The VUT longitudinal path error shall be within $\pm$ [1.0] m when determined in accordance with section 1.2.1.1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/b9d26282fb5b757da75f578a57f1360cbeadd288c4676c03cbbd3683cb5d4018.jpg)



Figure 3-6 CCFtap impact location definition


# 3.1.2.2 Car-to-Motorcyclist Front Turn Across Path

<table><tr><td>CMFtap</td><td colspan="4">EMT speed</td></tr><tr><td></td><td>30 km/h</td><td>45 km/h</td><td>60 km/h</td><td>80 km/h</td></tr><tr><td>10 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>15 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>25 km/h</td><td></td><td></td><td></td><td></td></tr></table>

Euro NCAP 

Version 1.1 — October 2025 

For the CMFtap scenario, for the VUT assume an initial straight-line path followed by a turn (clothoid, fixed radius and clothoid as specified in section 1.2.4), followed again by a straight line, hereby known as the test path. The direction indicator is applied at $1 . 0 \mathsf { s } \pm 0 . 5 \mathsf { s }$ before Tsteer. 

The EMT will follow a straight-line p th in the l ne dj cent to the VUT’s initi l position, in the opposite direction to the VUT. The straight-line path of the VUT and target will be 1.75m from the centre of the centre dashed lane marking of the VUT lane. 

The paths of the VUT and EMT will be synchronised so that the front wheel of the target meets the $50 \%$ impact location (assuming no system reaction) of the width of the VUT. The VUT longitudinal path error shall be within ± [1.0] m when determined in accordance with section 1.2.1.2. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/8c7f565930f15a88069ec60ab9f2257f06897fe8a84fbaec04521cd4c684fa04.jpg)



Figure 3-7 CMFtap scenario VUT and EMT paths


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/20cf432ba1b27df72c0c75e8193c5d0c0ba20c76e33cbd9f6fa4c61e6901c761.jpg)



Figure 3-8 CMFtap impact location definition


# 3.1.3 Crossing

<table><tr><td rowspan="2">Crossing</td><td colspan="4">Score</td></tr><tr><td>Standard</td><td>Extended</td><td>Robustness</td><td>Total</td></tr><tr><td>Car-to-Car</td><td>6</td><td>0.75</td><td>0.75</td><td>7.5</td></tr><tr><td>Car-to-Motorcyclist</td><td>6</td><td>0.75</td><td>0.75</td><td>7.5</td></tr></table>

# 3.1.3.1 Car-to-Car Crossing

<table><tr><td rowspan="2">CCCscp</td><td rowspan="2">Function</td><td colspan="7">GVT speed</td></tr><tr><td>20 km/h</td><td>30 km/h</td><td>40 km/h</td><td>50 km/h</td><td>60 km/h</td><td>70 km/h</td><td>80 km/h</td></tr><tr><td>20 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td>N/A</td><td>N/A</td></tr><tr><td>50 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td>N/A</td><td>N/A</td></tr><tr><td>60 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td>N/A</td><td>N/A</td></tr><tr><td>70 km/h</td><td>AEB</td><td></td><td></td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>80 km/h</td><td>AEB</td><td></td><td></td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr></table>

For the VUT assume a straight-line path equivalent to the centre line of the driving lane, approaching and continuing straight ahead across a junction. 

For the GVT assume a straight-line path equivalent to the centre line of the driving lane, perpendicular to that of the VUT, travelling across the junction from either the nearside or farside direction, randomly selected by the test laboratory. 

To achieve the correct GVT speed, the GVT must be accelerated at a rate ${ \tt > } 1 { \sf m } / { \tt s } ^ { 2 }$ during the acceleration phase. This is followed by a 0.5s stabilization phase, after which steady state conditions must be met as soon as the GVT has arrived in the field of vision of the VUT, corresponding to [3.5]s TTC. 

The paths will be synchronised to that (assuming no system reaction) the reference point of the GVT collides with $50 \%$ impact location of the VUT, for both Standard and Extended Range, as indicated in Figure 3-11. The boundary condition for synchronization is SCP Time Error of ±[0.1]s, as specified in section 1.2.3. 

The scenario is executed with obstruction for Standard Range, and without obstruction for Extended Range. 

The obstruction is formed by 3 vehicles parked in parallel at either side along the VUT trajectory (parked either at the farside when target approaches from the farside, or nearside when target approaches from the nearside). 

The group of 3 obstruction vehicles are parked 1m apart from each other, and at a lateral offset of 2m for nearside target approach and $5 . 5 \mathsf { m }$ for farside target approach (from the edge of the parked vehicles to the VUT trajectory), where: 

F ont obscu tion vehicle (closest to t get t jecto y) is of type “l ge obst uction vehicle” as per APPENDIX B 

Second obscu tion vehicle is of type “sm lle obst uction vehicle” s pe APPENDIX B 

- Third obscuration vehicle can be any type of passenger vehicle 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/5780407b24006898a809cf20244f07ec1dcd4ea8d92ee0e8c71e5bf51b6c9c79.jpg)



Figure 3-9 CCCscp, obstructed (only applicable to Standard Range)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/7f53ded40c5366c90fce17ab24c01f09a5f3eee69f1c0a7741d5b3f0733e7f61.jpg)



Figure 3-10 Figure 3 9 CCCscp, unobstructed (only applicable to Extended Range)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/e2cff54835271b76abb8d2c948b41b4a01104a7d348bbf0c3bab7536a487a3c8.jpg)



Figure 3-11 Impact location on CCCscp



3.1.3.2 Car-to-Motorcyclist Crossing


<table><tr><td rowspan="2">CMCscp</td><td rowspan="2">Function</td><td colspan="7">EMT speed</td></tr><tr><td>20 km/h</td><td>30 km/h</td><td>40 km/h</td><td>50 km/h</td><td>60 km/h</td><td>70 km/h</td><td>80 km/h</td></tr><tr><td>20 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td>N/A</td><td>N/A</td></tr><tr><td>50 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td>N/A</td><td>N/A</td></tr><tr><td>60 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td><td></td><td>N/A</td><td>N/A</td></tr><tr><td>70 km/h</td><td>AEB</td><td></td><td></td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>80 km/h</td><td>AEB</td><td></td><td></td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr></table>

For the VUT assume a straight-line path equivalent to the centre line of the driving lane, approaching and continuing straight ahead across a junction. 

For the EMT, assume a straight-line path equivalent to the centre line of the driving lane, perpendicular to that of the VUT, travelling across the junction from either the nearside or farside direction, randomly selected by the test laboratory 

To achieve the correct EMT speed, the EMT must be accelerated at a rate ${ > } 1 \mathsf { m } / \mathsf { s } ^ { 2 }$ during the acceleration phase. This is followed by a 0.5s stabilization phase, after which steady state conditions must be met as soon as the EMT has arrived in the field of vision of the VUT, corresponding to [3.5]s TTC. 

The paths will be synchronised to that (assuming no system reaction) the reference point of the EMT collides with $90 \%$ side impact location (EMT approaching from both nearside and farside), for both Standard and Extended Range, as indicated in Figure 3-14. The boundary condition for synchronization is SCP Time Error of ±[0.1]s, as specified in section 1.2.3. 

The scenario is executed with obstruction for Standard Range, and without obstruction for Extended Range. 

The obstruction is formed by 3 vehicles parked in parallel at either side along the VUT trajectory (parked either at the farside when target approaches from the farside, or nearside when target approaches from the nearside). 

The group of 3 obstruction vehicles are parked 1m apart from each other, and at a lateral offset of 2m for nearside target approach and 5.5m for farside target approach (from the edge of the parked vehicles to the VUT trajectory), where: 

F ont obscu tion vehicle (closest to t get t jecto y) is of type “l ge obst uction vehicle” as per APPENDIX B 

Second obscu tion vehicle is of type “sm lle obst uction vehicle” s pe APPENDIX B 

Third obscuration vehicle can be any type of passenger vehicle 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/a9ab321c4c0b9ce612aa7a2ce72b994ee5d481912e813f2f27bb02d710d76676.jpg)



Figure 3-12 CMCscp, obstructed (only applicable to Standard Range)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/1d1b2f6a1a122e2ec2296947f7a7b13734114ca81bcf3adb09b852560a20bebb.jpg)



Figure 3-13 CMCscp, unobstructed (only applicable to Extended Range)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/5272792516a8a83ccaa42659e376f568b8b01750ee359eadc22010a7648a040f.jpg)



Figure 3-14 CMCscp Impact location definition (EMT approaching from farside, impacting at $90 \%$ of VUT length)


# Pedestrian & Cyclist Scenarios

<table><tr><td rowspan="2">Pedestrian &amp; Cyclist</td><td colspan="4">Score</td></tr><tr><td>Standard</td><td>Extended</td><td>Robustness</td><td>Total</td></tr><tr><td>Longitudinal</td><td></td><td></td><td></td><td>5.0</td></tr><tr><td>Car-to-Pedestrian</td><td>2.0</td><td>0.25</td><td>0.25</td><td></td></tr><tr><td>Car-to-Bicyclist</td><td>2.0</td><td>0.25</td><td>0.25</td><td></td></tr><tr><td>Turning</td><td></td><td></td><td></td><td>5.0</td></tr><tr><td>Car-to-Pedestrian</td><td>2.0</td><td>0.25</td><td>0.25</td><td></td></tr><tr><td>Car-to-Bicyclist</td><td>2.0</td><td>0.25</td><td>0.25</td><td></td></tr><tr><td>Crossing</td><td></td><td></td><td></td><td>10.0</td></tr><tr><td>Car-to-Pedestrian</td><td>4.0</td><td>0.5</td><td>0.5</td><td></td></tr><tr><td>Car-to-Bicyclist</td><td>4.0</td><td>0.5</td><td>0.5</td><td></td></tr></table>

# 3.2.1 Longitudinal

<table><tr><td rowspan="2">Longitudinal</td><td colspan="4">Score</td></tr><tr><td>Standard</td><td>Extended</td><td>Robustness</td><td>Total</td></tr><tr><td>Car-to-Pedestrian</td><td>2.0</td><td>0.25</td><td>0.25</td><td rowspan="3">2.5</td></tr><tr><td>CPLAday</td><td>1.0</td><td>0.125</td><td rowspan="2">0.25</td></tr><tr><td>CPLAnight</td><td>1.0</td><td>0.125</td></tr><tr><td>Car-to-Bicyclist</td><td>2.0</td><td>0.25</td><td>0.25</td><td>2.5</td></tr></table>

# 3.2.1.1 Car-to-Pedestrian Longitudinal

<table><tr><td rowspan="2">CPLAday</td><td rowspan="2">EPT speed</td><td rowspan="2">Function</td><td rowspan="2">*/cc</td><td colspan="4">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td></tr><tr><td>10 km/h</td><td>5 km/h</td><td>AEB</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>5 km/h</td><td>AEB</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>5 km/h</td><td>AEB</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>5 km/h</td><td>AEB</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>5 km/h</td><td>AEB</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>5 km/h</td><td>AEB</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>5 km/h</td><td>FCW</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>5 km/h</td><td>FCW</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>5 km/h</td><td>FCW</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>5 km/h</td><td>FCW</td><td>*</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">CPLAnight</td><td rowspan="2">EPT speed</td><td rowspan="2">Function</td><td rowspan="2">*/C</td><td colspan="4">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td></tr><tr><td>10 km/h</td><td>5 km/h</td><td>AEB</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>5 km/h</td><td>AEB</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>5 km/h</td><td>AEB</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>5 km/h</td><td>AEB</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>5 km/h</td><td>AEB</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>5 km/h</td><td>AEB</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>5 km/h</td><td>FCW</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>5 km/h</td><td>FCW</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>5 km/h</td><td>FCW</td><td>C</td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>5 km/h</td><td>FCW</td><td>C</td><td></td><td></td><td></td><td></td></tr></table>

For nighttime tests in CPLA (marked with $\mathbb { \ C }$ ), illumination conditions shall apply as described in Technical Bulletin CA 101. Furthermore, nighttime tests shall be conducted with low beams, unless the vehicle is equipped with automated high beam as standard (in which case, tests shall be executed with high beams). 

If AEB can avoid the collision even when FCW criteria is not met, points are awarded. The OEM shall inform Euro NCAP in advance about the criteria to be applied. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/20dbd5157a196e6af926994345e995d60512c60f604ef913d3a8b8ba3cb182d1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/f0c186c73ec89f9399d04a6d7b5f2fa9de4808d1cf3bd49082b19a226154e48b.jpg)



Figure 3-15 CPLA scenario, Longitudinal walking Adult


# 3.2.1.2 Car-to-Bicyclist Longitudinal

<table><tr><td rowspan="2">CBLA</td><td rowspan="2">EBT speed</td><td rowspan="2">Function</td><td colspan="4">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td></tr><tr><td>20 km/h</td><td>15 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>15 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>15 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>15 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>15 km/h</td><td>AEB</td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>20 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>20 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>20 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>20 km/h</td><td>FCW</td><td></td><td></td><td></td><td></td></tr></table>

If AEB can avoid the collision even when FCW criteria is not met, points are awarded. The OEM shall inform Euro NCAP in advance about the criteria to be applied. 


AEB


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/0cea99c596a64a7f5eba4a2af10f88e8fe45bb43b073db40d9eed35198afc524.jpg)



FCW


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/2e7c5ba8247692f298e0b0f45116d95a5f74908a8fa53849d7e51310af16963f.jpg)



Figure 3-16 CBLA scenarios, Longitudinal Bicyclist (AEB left & FCW right)


Note: the reflected acceleration distances $\mathsf Q$ and R are meant to suit the limited usable length of a belt-driven carrier platform. If a self-propelled carrier platform is used for the execution of CBLA, the acceleration distances Q and R can be increased according to the acceleration capabilities of the platform carrier. 

Euro NCAP 

Version 1.1 — October 2025 

# 3.2.2 Turning

<table><tr><td rowspan="2">Turning</td><td colspan="4">Score</td></tr><tr><td>Standard</td><td>Extended</td><td>Robustness</td><td>Total</td></tr><tr><td>Car-to-Pedestrian</td><td>2.0</td><td>0.25</td><td>0.25</td><td rowspan="3">2.5</td></tr><tr><td>CPTAfs &amp; CPTAns</td><td>1.0</td><td>0.125</td><td>0.125</td></tr><tr><td>CPTAfo &amp; CPTAno</td><td>1.0</td><td>0.125</td><td>0.125</td></tr><tr><td>Car-to-Bicyclist</td><td>2.0</td><td>0.25</td><td>0.25</td><td rowspan="3">2.5</td></tr><tr><td>CBTAfs &amp; CBTAns</td><td>1.0</td><td>0.125</td><td>0.125</td></tr><tr><td>CBTAfo &amp; CBTAno</td><td>1.0</td><td>0.125</td><td>0.125</td></tr></table>

# 3.2.2.1 Car-to-Pedestrian Turning

The CPTA scenario consists of 2 clusters of 2 sub-scenarios each: 

Cluster 1: target travelling in the same direction 

o CPTAfs: Farside turn 

o CPTAns: Nearside turn 

Cluster 2: target travelling in the opposite direction 

o CPTAfo: Farside turn 

o CPTAno: Nearside turn 

The 25 km/h turn as part of the Extended Range is conducted in the 20 km/h path. 

<table><tr><td rowspan="2">CPTAfs&amp;ns</td><td rowspan="2">Turn</td><td rowspan="2">EPT Direction</td><td rowspan="2">EPT Speed</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>Farside</td><td>Same</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15 km/h</td><td>Farside</td><td>Same</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>Farside</td><td>Same</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>25 km/h</td><td>Farside</td><td>Same</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10 km/h</td><td>Nearside</td><td>Same</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">CPTAfo&amp;no</td><td rowspan="2">Turn</td><td rowspan="2">EPT Direction</td><td rowspan="2">EPT Speed</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>Farside</td><td>Opposite</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15 km/h</td><td>Farside</td><td>Opposite</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>Farside</td><td>Opposite</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>25 km/h</td><td>Farside</td><td>Opposite</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10 km/h</td><td>Nearside</td><td>Opposite</td><td>5 km/h</td><td></td><td></td><td></td><td></td><td></td></tr></table>

For the CPTA scenarios, for the VUT assume an initial straight-line path followed by a turn (clothoid, fixed radius and clothoid as specified in section 1.2.4), followed again by a straight line, hereby known as the test path. 

These tests are conducted without the use of the turn signals. 

The VUT will follow a straight-line path in the approach lane which will be 1.75m from the centre of the centre dashed lane marking of the VUT lane. 

The 4 different scenarios of CPTA are represented below: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/c0396beae4a760ee75f39a6972a4880d138c86f5f82f092427f7c4739522d994.jpg)



Axes



AA-Trajectory of pedestrian dummy H-point BB -Axis of centerline of Vehicle under Test



Distances



E - Dummy H-point, start to $50 \%$ impact



R- Dummy acceleration distance (walking)



Point



K - Impact position for $50 \%$ far-side scenario


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/f6b3d562ad67bb063ad621be592ab35aa9ffafe1bbffa1662d4ea5569a328d37.jpg)



Figure 3-17 CPTAfs scenario – VUT left turn, pedestrian crossing from farside


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/7237e4a73dc1bc775bc5d8d8d8c4fb861790d1d2c547aac5880e6af3b3474ff6.jpg)



Axes



AA - Trajectory of pedestrian dummy H-point



BB-Axis of centerline of Vehicle under Test



Distances



E - Dummy H-point, start to $50 \%$ impact



R- Dummy acceleration distance (walking)



Point



K- Impact position for $50 \%$ far-side scenario


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/82a9186904d45c0f92ffa9be63d136249349abb8149f603e78ce324028ad57f2.jpg)



Figure 3-18 CPTAfo scenario – VUT left turn, pedestrian crossing from nearside


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/dc49b7ae97f6b7b1339f85a640bf87520e31377cec68e86f2bb3c9b46b426a1b.jpg)



Axes



AA - Trajectory of pedestrian dummy H-point BB-Axis of centerline of Vehicle under Test



Distances



E - Dummy H-point, start to $50 \%$ impact R- Dummy acceleration distance (walking)



Point



K- Impact position for $50 \%$ near-side scenario RP - Reference Point (dummy hip-point)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/2328a5c941bd776276ca37ed8b7261b2d8a590b0a5f38e5f75faadff7b60b294.jpg)



Figure 3-19 CPTAno scenario – VUT right turn, pedestrian crossing from farside


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/897ac855c9810a8b51c7411687ff9fa744e45460c5515a07e334d45b230987b1.jpg)



Axes



AA- Trajectory of pedestrian dummy H-point



BB-Axis of centerline of Vehicle under Test


Distances 

E - Dummy H-point, start to $50 \%$ impact 

R - Dummy acceleration distance (walking) 

Point 

K - Impact position for $50 \%$ near-side scenario 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/2721b209e4703e1cc2ebfe87a4fab026634313fbe6d435ac6b09e0a675c408b9.jpg)



Figure 3-20 CPTAns scenario – VUT right turn, pedestrian crossing from nearside


# 3.2.2.2 Car-to- Bicyclist Turning

The CBTA scenario consists of 2 clusters of 2 sub-scenarios each: 

Cluster 1: target travelling in the same direction 

o CBTAfs: Farside turn, target travelling in the same direction 

o CBTAns: Nearside turn, target travelling in the same direction 

Cluster 2: target travelling in the opposite direction 

o CBTAfo: Farside turn, target travelling in the opposite direction 

o CBTAno: Nearside turn, target travelling in the opposite direction 

In all cases, the target speed is $1 5 \mathrm { k m / h }$ and the target reference point is on the front wheel. 

The $2 5 ~ \mathrm { k m / h }$ turn as part of the Extended Range is conducted in the 20 km/h path (where applicable). 

<table><tr><td rowspan="2">CBTAfs&amp;ns</td><td rowspan="2">Turn</td><td rowspan="2">EBT Direction</td><td rowspan="2">EBT Speed</td><td colspan="3">Impact Location</td></tr><tr><td>100%</td><td>75% (side)</td><td>0%</td></tr><tr><td>10 km/h</td><td>Farside</td><td>Same</td><td>15 km/h</td><td></td><td></td><td>N/A</td></tr><tr><td>15 km/h</td><td>Farside</td><td>Same</td><td>15 km/h</td><td></td><td></td><td>N/A</td></tr><tr><td>20 km/h</td><td>Farside</td><td>Same</td><td>15 km/h</td><td></td><td></td><td>N/A</td></tr><tr><td>25 km/h</td><td>Farside</td><td>Same</td><td>15 km/h</td><td></td><td></td><td>N/A</td></tr><tr><td>10 km/h</td><td>Nearside</td><td>Same</td><td>15 km/h</td><td>N/A</td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">CBTAfo&amp;no</td><td rowspan="2">Turn</td><td rowspan="2">EBT Direction</td><td rowspan="2">EBT Speed</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>Farside</td><td>Opposite</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15 km/h</td><td>Farside</td><td>Opposite</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>Farside</td><td>Opposite</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>25 km/h</td><td>Farside</td><td>Opposite</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10 km/h</td><td>Nearside</td><td>Opposite</td><td>15 km/h</td><td>N/A</td><td></td><td></td><td></td><td>N/A</td></tr></table>

For the CBTA scenarios, for the VUT assume an initial straight-line path followed by a turn (clothoid, fixed radius and clothoid as specified in section 1.2.4), followed again by a straight line, hereby known as the test path. The direction indicator is applied at $1 . 0 \mathsf { s } \pm 0 . 5 \mathsf { s }$ before Tsteer. 

The VUT will follow a straight-line p th in the l ne dj cent to the VUT’s initi l position, in the opposite direction to the VUT. The straight-line path of the VUT and GVT will be 1.75m from the centre of the centre dashed lane marking of the VUT lane. 

The VUT will follow a straight-line path in the approach lane which will be 1.75m from the centre of the centre dashed lane marking of the VUT lane. The EBT will follow a straight-line path which will be respectively 2.75m (CBTAfo) and $5 . 0 0 \mathsf { m }$ (CBTAfs, CBTAns, CBTAno) from the centre of the centre dashed lane marking of the VUT lane. Steady state speed of EBT starts at 4sec TTC. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/61109e1ce084fb934b45f1cf0a00e934ee344b8b96e843cdfbb724a23948b373.jpg)



Figure 3-21 CBTA scenario


Euro NCAP 

Version 1.1 — October 2025 

# 3.2.3 Crossing

<table><tr><td rowspan="2">Crossing</td><td colspan="4">Score</td></tr><tr><td>Standard</td><td>Extended</td><td>Robustness</td><td>Total</td></tr><tr><td>Car-to-Pedestrian</td><td>4.0</td><td>0.5</td><td>0.5</td><td rowspan="7">5.0</td></tr><tr><td>CPNAday</td><td>0.5</td><td>0.0625</td><td rowspan="2">0.125</td></tr><tr><td>CPNAnight</td><td>0.5</td><td>0.0625</td></tr><tr><td>CPFAday</td><td>0.5</td><td>0.0625</td><td rowspan="2">0.125</td></tr><tr><td>CPFAnight</td><td>0.5</td><td>0.0625</td></tr><tr><td>CPNCOday</td><td>1.0</td><td>0.125</td><td rowspan="2">0.25</td></tr><tr><td>CPNCOnight</td><td>1.0</td><td>0.125</td></tr><tr><td>Car-to-Bicyclist</td><td>4.0</td><td>0.5</td><td>0.5</td><td rowspan="4">5.0</td></tr><tr><td>CBNA</td><td>1.0</td><td>0.125</td><td>0.125</td></tr><tr><td>CBFA</td><td>1.0</td><td>0.125</td><td>0.125</td></tr><tr><td>CBNAO</td><td>2.0</td><td>0.25</td><td>0.25</td></tr></table>

# 3.2.3.1 Car-to-Pedestrian Crossing

<table><tr><td rowspan="2">CPNAday</td><td rowspan="2">EPT Speed</td><td rowspan="2">*/C</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">CPNA night</td><td rowspan="2">EPT Speed</td><td rowspan="2">*/C</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/a5c8d8fde8520c0f8b7b9feddef836ffd4a683dce846340b9bf4a02e0287428a.jpg)



Figure 3-22 CPNA-25 & CPNA-75 scenarios, Walking Adult from Nearside


<table><tr><td rowspan="2">CPFAday</td><td rowspan="2">EPT Speed</td><td rowspan="2">*/C</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>8 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>8 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>8 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>8 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>8 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>8 km/h</td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">CPFAnight</td><td rowspan="2">EPT Speed</td><td rowspan="2">*/C</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>8 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>8 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>8 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>8 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>8 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>8 km/h</td><td>C</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/1f10beeb0fbbbe022e3c25634aa625438846f8080b78a83dfac56bb8bb253fc9.jpg)



Figure 3-23 CPFA-50 scenario, Adult running from Farside


<table><tr><td rowspan="2">CPNCOday</td><td rowspan="2">EPTc Speed</td><td rowspan="2">*/cc</td><td colspan="3">Impact Location</td></tr><tr><td>25%</td><td>50%</td><td>75%</td></tr><tr><td>10 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>5 km/h</td><td>*</td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">CPNCOnight</td><td rowspan="2">EPTc Speed</td><td rowspan="2">*/C</td><td colspan="3">Impact Location</td></tr><tr><td>25%</td><td>50%</td><td>75%</td></tr><tr><td>10 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>5 km/h</td><td>C</td><td></td><td></td><td></td></tr></table>

In the CPNCO scenario, the smaller obstruction vehicle is positioned closest to the pedestrian path, and the larger obstruction vehicle is positioned behind the smaller obstruction vehicle (see dimensions of obstruction vehicles in APPENDIX B) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/df8a981c6ca6bf2517d91b1e13cf3688cb00fb1e684f83cf900bfb5603341a6d.jpg)



Figure 3-24 CPNCO-50 scenario, Running Child from Nearside from Obstruction.



3.2.3.2 Car-to-Bicyclist Crossing


<table><tr><td rowspan="2">CBNA</td><td rowspan="2">EBT Speed</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>15 km/h</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/301f9c0bb1f29e266e71590bed185cb53c4ae7f3a239c124a5587eb3f3e970a9.jpg)



Figure 3-25 CBNA scenario, Bicyclist from Nearside


Note: the gap between the obscuration vehicles should be [0.1 ~ 0.3] m. 

<table><tr><td rowspan="2">CBNAO</td><td rowspan="2">EBT Speed</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>10 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>10 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>10 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>10 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>10 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>10 km/h</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/874d71acf2fbc2615d80a31fbb2b0bff7046d95c37a56cfb3d92e063d94a124b.jpg)



Figure 3-26 CBNAO scenario, Bicyclist from Nearside (obstructed)


Note: the gap between the obscuration vehicles should be [0.1 ~ 0.3] m. 

<table><tr><td rowspan="2">CBFA</td><td rowspan="2">EBT Speed</td><td colspan="5">Impact Location</td></tr><tr><td>10%</td><td>25%</td><td>50%</td><td>75%</td><td>90%</td></tr><tr><td>10 km/h</td><td>20 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20 km/h</td><td>20 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30 km/h</td><td>20 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>40 km/h</td><td>20 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>50 km/h</td><td>20 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>20 km/h</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/3d4e0b55dd63ab0a9cbc84538ea91101c6f92ab961db472ebdbca571262080ee.jpg)



Figure 3-27 CBFA scenario, Bicyclist from Farside


Note: the gap between the obscuration vehicles should be $[ 0 . 1 \sim 0 . 3 ] \mathsf { m }$ . 

# 4 TEST EXECUTION

# Performance Predictions

The Vehicle Manufacturer shall provide the Euro NCAP with data detailing the predicted performance of the AEB/FCW system in each of the grid cells for all test scenarios and in accordance with the assessment criteria outlined in 5.2. 

The predicted performance will be used as a reference to verify performance using randomly selected verification tests. Performance predictions may be provided in either of the following formats: 

<table><tr><td colspan="2">Performance Predictions</td><td>Virtual Testing</td><td>Self-claim</td><td>Field Data</td><td>System overriding conditions</td></tr><tr><td colspan="2">Standard Range</td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td colspan="2">Extended Range</td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td rowspan="2">Robustness Layers</td><td>Decision &amp; Control</td><td>✓</td><td>✓</td><td></td><td>✓*</td></tr><tr><td>Perception</td><td></td><td></td><td>✓</td><td></td></tr></table>


* Applicable only for the ‘Driver input pre-crash’ robustness layer. 


The information shall be supplied by the manufacturer before any testing begins, preferably with delivery of the test vehicle(s). 

In case a Vehicle Manufacturer does not supply any prediction data, the test laboratory shall conduct a testing approach defined by the Euro NCAP Secretariat. 

# 4 . 1 .1 V i rt ua l T es ti ng

Virtual Testing refers to simulation-based performance predictions, in which case the provisions outlined in Euro NCAP VTA Protocol shall be followed. VTA performance predictions for Decision & Control Target Robustness Layers shall be provided 1) with the layer present and 2) without the layer present. 

# 4 . 1 . 2 S e l f - c l a i m

Self-claim refers to colour data provided by the Vehicle Manufacturer, where no further evidence is required. For the following cases where Self-claimed performance is declared, the Vehicle Manufacturer shall provide the Euro NCAP Secretariat with supporting evidence in the form of simulation and/or in-house track test data: 

CCRb with GVT speed >100 km/h 

CCFhos/hol with GVT speed ${ > } 7 0 \ \mathsf { k m / h }$ 

CMRb with EMT speed $\mathtt { > 8 0 }$ km/h 

CCFtap and CMFtap with target speed $\mathtt { > 6 0 }$ km/h 

CCCscp and CMCscp with target speed $\mathtt { > 6 0 }$ km/h 

# 4.1.3 Field Data

Where Field Data is required, the Vehicle Manufacturer shall demonstrate function availability (i.e., function is able to detect and classify objects) and/or specific performance under the presence of perception-related robustness layers, by means of insights gathered in real-world Euro NCAP 

driving conditions. This is to be reported according to the provisions outlined in Technical Bulletin CA 003. 

# 4.1.4 System overriding conditions

This info m tion is only equi ed f om the Vehicle M nuf ctu e fo the obustness l ye “D ive Input pre-c sh”, s p t of the necess y evidence to w d points. This info m tion sh ll contain, but not be limited to, conditions leading to the system override e.g., steering wheel angle/speed, acceleration pedal percentage/rate, driver state link, etc. 

# Verification tests

The verification tests are randomly selected grid cells, distributed in line with the Vehicle Manufacturer prediction (excluding red grid cells), and covering Standard Range, Extended Range and Robustness Layers. 

For each scenario, the following random selection of Verification Tests is made by Euro NCAP and executed by the test laboratory: 

# 4.2.1 Standard and Extended Range

For Standard Range, a random selection of 3 to 5 verification tests is done per scenario, as indicated in the table below. For Extended Range, a random selection of 2 verification tests is done per scenario. 

<table><tr><td rowspan="2">Car &amp; PTW</td><td rowspan="2">Scenario Type</td><td rowspan="2">Scenario</td><td colspan="2">Verification tests</td></tr><tr><td>Standard Range</td><td>Extended Range</td></tr><tr><td rowspan="7">Longitudinal</td><td rowspan="3">Car-to-Car Rear</td><td>CCRs</td><td>3</td><td>2</td></tr><tr><td>CCRm</td><td>3</td><td>2</td></tr><tr><td>CCRb</td><td>3</td><td>2</td></tr><tr><td rowspan="2">Car-to-Car Front</td><td>CCFhos</td><td>4</td><td>2</td></tr><tr><td>CCFhol</td><td>4</td><td>2</td></tr><tr><td rowspan="2">Car-to-Motorcyclist Rear</td><td>CMRs</td><td>3</td><td>2</td></tr><tr><td>CMRb</td><td>3</td><td>2</td></tr><tr><td rowspan="2">Turning</td><td>Car-to-Car TAP</td><td>CCFtap</td><td>3</td><td>2</td></tr><tr><td>Car-to-Motorcyclist TAP</td><td>CMFtap</td><td>3</td><td>2</td></tr><tr><td rowspan="2">Crossing</td><td>Car-to-Car</td><td>CCCscp</td><td>5</td><td>2</td></tr><tr><td>Car-to-Motorcyclist</td><td>CMCscp</td><td>5</td><td>2</td></tr><tr><td rowspan="2">Pedestrian &amp; Cyclist</td><td rowspan="2">Scenario Type</td><td rowspan="2">Scenario</td><td colspan="2">Verification tests</td></tr><tr><td>Standard Range</td><td>Extended Range</td></tr><tr><td rowspan="3">Longitudinal</td><td rowspan="2">Car-to-Pedestrian</td><td>CPLAday</td><td>3</td><td>2</td></tr><tr><td>CPLAnight</td><td>3</td><td>2</td></tr><tr><td>Car-to-Bicyclist</td><td>CBLA</td><td>3</td><td>2</td></tr><tr><td rowspan="4">Turning</td><td rowspan="2">Car-to-Pedestrian</td><td>CPTAfs &amp; CPTAns</td><td>3</td><td>2</td></tr><tr><td>CPTAfo &amp; CPTAno</td><td>3</td><td>2</td></tr><tr><td rowspan="2">Car-to-Bicyclist</td><td>CBTAfs &amp; CBTAns</td><td>3</td><td>2</td></tr><tr><td>CBTAfo &amp; CBTAno</td><td>3</td><td>2</td></tr><tr><td rowspan="9">Crossing</td><td rowspan="6">Car-to-Pedestrian</td><td>CPNA day</td><td>3</td><td>2</td></tr><tr><td>CPNAnight</td><td>3</td><td>2</td></tr><tr><td>CPFAday</td><td>3</td><td>2</td></tr><tr><td>CPFAnight</td><td>3</td><td>2</td></tr><tr><td>CPNCO day</td><td>3</td><td>2</td></tr><tr><td>CPNCOnight</td><td>3</td><td>2</td></tr><tr><td rowspan="3">Car-to-Bicyclist</td><td>CBNA</td><td>3</td><td>2</td></tr><tr><td>CBFA</td><td>3</td><td>2</td></tr><tr><td>CBNAO</td><td>3</td><td>2</td></tr></table>

# 4.2.2 Robustness Layers

For the Decision & Control Robustness Layers listed in section 5.2.1.1, one layer is randomly selected per scenario (see applicability in APPENDIX A). 

For the Standard Range only, the verification tests will be performed with the presence of one randomly selected Robustness Layer for which performance was predicted. All verification tests within that scenario will be performed with that selected layer, provided the outcome is equal or better than the initially predicted colour. 

If any verification test with the Robustness Layer results in a fail (i.e., a colour downgrade from the initial prediction), that layer will be considered failed for the scenario. The test will then be repeated without the layer present. Subsequent verification tests in the Standard Range of that scenario will be conducted without the layer. 

If a specific Robustness Layer fails in two scenarios involving the same collision partner (i.e., car, PTW, pedestrian, or bicyclist), it will be considered failed for all scenarios involving that collision partner. 

# 4.2.3 Additional test runs

For the verification tests without a robustness layer present that does not result in the predicted performance, two additional runs may be conducted (at the expense of the Vehicle Manufacturer). The two additional test runs shall pass to achieve a pass in that verification test. 

# 4.2.4 Impact speed tolerance

As test results can be variable between labs and in-house tests and/or simulations, a 2 km/h tolerance to the impact speeds of the verification test is applied. The tolerance is applied in both directions, meaning that when a tested point scores better than predicted, but within tolerance, the predicted result is applied. 

Euro NCAP 

Version 1.1 — October 2025 

The tolerance only applies to verify whether the predicted colour of the tested verification point is correct. When, including tolerance, the colour is not in line with the prediction, the true colour of the test point will be determined by comparing the actual measured impact speed with the colour bands in section 5.2, without applying a tolerance to the impact speed. 

As an example, the accepted impact speed ranges for the 60km/h CMRs test: 

<table><tr><td>Colour</td><td>Impact speed range (km/h)</td><td>Accepted Range (km/h)</td></tr><tr><td>Green</td><td>Vimpact = 0</td><td>Vimpact &lt; 2</td></tr><tr><td>Yellow</td><td>0 &lt; vimpact ≤ 10</td><td>0 &lt; vimpact ≤ 12</td></tr><tr><td>Orange</td><td>10 &lt; vimpact ≤ 20</td><td>8 &lt; vimpact ≤ 22</td></tr><tr><td>Brown</td><td>20 &lt; vimpact ≤ 30</td><td>18 &lt; vimpact ≤ 32</td></tr><tr><td>Red</td><td>30 &lt; vimpact</td><td></td></tr></table>

# Test Conduct

# 4.3.1 VUT Pre-test conditioning

If requested by the Vehicle Manufacturer, an initialisation run may be included before every test run. Bring the VUT to a halt and push the brake pedal through the full extent of travel and release. 

For vehicles with an automatic transmission select D. For vehicles with a manual transmission select the highest gear where the RPM will be at least 1500 at the test speed. 

Perform the first test a minimum of 90s and a maximum of 10 minutes after completing the tyre conditioning (if applicable), and subsequent tests after the same time period. If the time between consecutive tests exceeds 10 minutes perform three brake stops from 72 km/h at approximately 0.3g. 

Between tests, manoeuvre the VUT at a maximum speed of 50km/h and avoid riding the brake pedal and harsh acceleration, braking or turning unless strictly necessary to maintain a safe testing environment. 

Control the VUT with driver inputs or using alternative control systems that can modulate the vehicle controls as necessary to perform the tests within the boundary for the AEB tests. 

# 4.3.2 AEB tests

Accelerate the VUT and target to the respective test speeds where needed. The test shall start at ${ \sf T } _ { 0 }$ and is valid when all boundary conditions are met between ${ \sf T } _ { 0 }$ and TAEB, TFCW, or any other system intervention – whichever comes/occurs first: 

<table><tr><td></td><td>VUT</td><td>GVT</td><td>EPT</td><td>EBT</td><td>EMT</td></tr><tr><td>Speed</td><td>+ 1.0 km/h</td><td>± 1.0 km/h</td><td>± 0.2 km/h</td><td>± 0.5 km/h</td><td>± 1.0 km/h</td></tr><tr><td>Lateral deviation</td><td>0 ± 0.05 m(0 ± 0.10 m during the turn in turning scenarios)</td><td>0 ± 0.10 m</td><td colspan="2">0 ± 0.05 m for crossing scenarios (incl. junction)0 ± 0.15 m for longitudinal scenarios</td><td>0 ± [0.15] m</td></tr><tr><td>Lateral velocity</td><td></td><td></td><td>0 ± 0.15 m/s</td><td>0 ± 0.15 m/s</td><td></td></tr><tr><td>Relative distance</td><td></td><td>1.0 sec [+0.1sec] time gap</td><td></td><td></td><td>1.0 sec [+0.1sec] time gap</td></tr><tr><td>Yaw velocity(up to TSTEER)</td><td>0 ± 1.0 °/s</td><td></td><td></td><td></td><td></td></tr><tr><td>Steering wheel velocity(up to TSTEER)</td><td>0± 15.0 °/s</td><td></td><td></td><td></td><td></td></tr><tr><td>SCP Time Error(only for CCCscp &amp; CMCscp)</td><td>0 ± 0.1 s</td><td></td><td></td><td></td><td></td></tr></table>

The end of a test, where the AEB function is assessed and for CCRs FCW and CMRs FCW, is considered when one of the following occurs: 

- $\mathsf { V } _ { \mathsf { V U T } } = 0 \mathsf { k m / h }$ (crossing) or $\mathsf { V } _ { \mathsf { V U T } } = \mathsf { V } _ { \mathsf { t a r g e t } }$ (longitudinal) 

Contact between VUT and target 

- The target has left the VUT path or VUT has left the target path 

<table><tr><td></td><td>Longitudinal (Rear)</td><td>Turning</td><td>Crossing</td><td>Longitudinal (Front)</td></tr><tr><td>\(V_{\text{VUT}}=0 \text{km/h}\)</td><td>✓</td><td>✓*</td><td>✓</td><td>✓</td></tr><tr><td>\(V_{\text{VUT}}=\text{V}_{\text{Target}}\)</td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Contact between VUT and Target</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>The target has left the path of the VUT</td><td></td><td>✓</td><td>✓</td><td></td></tr></table>


* The VUT must not enter the path of the target to achieve the pass. 


To avoid contact in the junction scenarios involving a motorcyclist, the test laboratory may include an automated braking action by the robot in case the AEB system fails to intervene (sufficiently). This braking action is applied automatically when: 

Euro NCAP 

Version 1.1 — October 2025 

The VUT reaches the latest position at which maximum braking applied to the vehicle will prevent the VUT entering the path of the Motorcyclist and no intervention from the AEB system is detected. 

L te l sep tion between the VUT nd EMT e ches $\leq 0 . 3 \mathsf { m }$ du ing $/$ fte AEB intervention. 

It is t the test l bo to y’s disc etion to select nd use one of the options bove to ensu e s fe testing environment. If the Vehicle Manufacturer feels the avoidance action is negatively affecting the performance of their vehicle, they should consult with the test laboratory and Euro NCAP secretariat. 

For manual or automatic accelerator control, it needs to be assured that during automatic brake the accelerator pedal does not result in an override of the system. The accelerator pedal needs to be released when the initial test speed is reduced by 5 km/h. There shall be no operation of other driving controls during the test, e.g. clutch or brake pedal. 

# 4.3.3 FCW tests

The CCRs and CMRs FCW system tests should be performed using a braking robot reacting to the warning with a delay time of 1.2 seconds as per Technical Bulletin CA 102 to account for driver reaction time. 

Braking will be applied that results in a maximum brake level of $- 4 ~ \mathrm { m } / \mathsf { s } ^ { 2 } - 0 . 5 0 ~ \mathrm { m } / \mathsf { s } ^ { 2 }$ when applied in a non-threat situation. The particular brake profile to be applied (pedal application rate applied in 200ms (max. 400mm/s) and pedal force) shall be specified by the manufacturer. When the brake profile provided by the manufacturer results in a higher brake level than allowed, the iteration steps as described in Technical Bulletin CA 102 will be applied to scale the brake level to $- 4 ~ \mathrm { m } / \mathsf { s } ^ { 2 } - 0 . 5 0 ~ \mathrm { m } / \mathsf { s } ^ { 2 }$ . 

If no brake profile is provided, apply default brake profile as described in Technical Bulletin CA 102. 

Where the FCW function is assessed, the end of a test is considered when one of the following occurs: 

- VVUT = Vtarget (longitudinal) 

TFCW 

- TT ≤ 1.5s , fte which n ev sive ction c n be st ted 

It is at the labs discretion to select and use one of the options above to ensure a safe testing environment. 

# 5 ASSESSMENT

Each scenario in this assessment consists of a matrix combining vehicle longitudinal speeds, and ranges of impact locations or target longitudinal speeds. Each combination in a matrix is referred to as grid cell. The grid cells forming a matrix are grouped into 2 groups: 1) Standard Range and 2) Extended Range. 

In addition, a number of points are awarded on each scenario for system Robustness, with Robustness Layers assessed against grid cells of the Standard Range where there is performance, as described in 5.2.1. 

# General requirements

To be eligible for scoring points in this assessment, the following conditions shall be met: 

- AEB and/or FCW system shall be default ON at the start of every journey and deactivation of the system should not be possible with a momentary single push on a button. 

- AEB and/or FCW system shall have a loud and clear audible component of the FCW system (if applicable). 

For AEB Pedestrian, the system shall operate (i.e. warn or brake) from speeds of 10 km/h in the CPNA-75 scenario in both day and night. In addition, the system shall be able to detect pedestrians walking as slow as 3 km/h and reduce speed in the CPNA-75 scenario at $2 0 ~ \mathrm { k m / h }$ , also for both day and night. 

For the AEB CCRs scenario, full avoidance shall be achieved for test speeds up to and including $2 0 ~ \mathrm { k m / h }$ for all impact locations within the Standard Range, which is verified by one randomly selected test point. 

# Criteria

The following criteria and associated KPIs are used across scenarios to evaluate the performance of the AEB and/or FCW system: 

<table><tr><td rowspan="2">Criteria</td><td rowspan="2">KPI</td><td colspan="2">Scenarios</td></tr><tr><td>Car &amp; PTW</td><td>Pedestrian &amp; Cyclist</td></tr><tr><td>Mitigation OR avoidance</td><td>Vrel_impact</td><td>CCRs, CCRm, CCRb CMRs, CMRb</td><td>CPLA (AEB), CBLA (AEB) CPNA, CPFA, CPNCO CBNA, CBFA, CBNAO</td></tr><tr><td>Mitigation</td><td>Vreduction</td><td>CCFhos, CCFhol</td><td>-</td></tr><tr><td>Avoidance</td><td>Vimpact</td><td>CCFtap, CMFtap CCCscp, CMCscp</td><td>CPTA, CBTA</td></tr><tr><td>Warning</td><td>FCW TTC</td><td>-</td><td>CPLA (FCW), CBLA (FCW),</td></tr></table>

For CPNA, CPFA, CPNCO, CBNA, CBFA, CBNAO, the velocity component of the target is always 0 km/h. 

Where Vrel_impact or Vreduction is used, a criteria based on a stepped sliding scale using colour bands is applied: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/cbd9bdae47373bff2ca19c53eaaeb79d4c180fa662dc4c5687bfe43d32254302.jpg)



Figure 5-1 Relative Impact Speed colour band criteria (applicable to Car & PTW Rear, and Pedestrian & Cyclist Longitudinal / Crossing)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/e8ddfcb8a082e3647c461933156915d951f54a4a4aeea13e6e410c4118938751.jpg)



Figure 5-2 Speed Reduction colour band criteria (applicable to Car-to-Car Front scenarios)


If the VUT chieves speed eduction >35km/h (fo VUT speeds ${ \ge } 4 0 \ \mathsf { k m / h } .$ ), the Vehicle Manufacturer shall demonstrate, by means of a dossier, that the system is balanced to ensure a low False Positive rate in real world driving conditions. Euro NCAP may verify this with specific True Negative scenarios. 

Where $\mathsf { V } _ { \mathrm { i m p a c t } }$ is used, the following criteria applies: 

<table><tr><td>Colour band</td><td>Vimpact [km/h]</td></tr><tr><td>Green</td><td>0</td></tr><tr><td>Red</td><td>&gt;0</td></tr></table>


Note: For CPTA the VUT may enter the path of the EPT, as long as the VUT velocity = 0 before impact with the EPT 


Where FCW TTC is used, the following criteria applies: 

<table><tr><td>Colour band</td><td>FCW TTC [s]</td></tr><tr><td>Green</td><td>≥1.7</td></tr><tr><td>Red</td><td>&lt;1.7</td></tr></table>

Euro NCAP 

Version 1.1 — October 2025 

# 5.2.1 Robustness Layers

The Robustness Layers are clustered in two categories: Decision & Control and Perception. 


* Verification test may be conducted under request of Euro NCAP Secretariat. 


# 5.2.1.1 Decision & Control

<table><tr><td colspan="2">Robustness layers (Decision &amp; Control)</td><td rowspan="2">Description</td><td rowspan="2">Verification Test</td><td rowspan="2">Performance prediction source</td></tr><tr><td>Type</td><td>Layer</td></tr><tr><td>VUT</td><td>Driver input pre-crash</td><td>Normal driving without steering robot and/or speed control function</td><td>Yes</td><td>OEM information on system overriding conditions</td></tr><tr><td rowspan="4">Target</td><td>Speed</td><td>Small variance in the nominal target speed</td><td>Yes</td><td rowspan="4">Virtual Testing or Self-claimed</td></tr><tr><td>Acceleration</td><td>Small variance in the nominal target acceleration</td><td>Yes</td></tr><tr><td>Initial position offset</td><td>Small variance in the nominal target initial position</td><td>Yes</td></tr><tr><td>Trajectory/Heading</td><td>Small variance in the nominal target heading</td><td>Yes</td></tr></table>

# 5.2.1.2 Perception

<table><tr><td colspan="2">Robustness layers (Perception)</td><td rowspan="2">Description</td><td rowspan="2">Verification Test</td><td rowspan="2">Performance prediction source</td></tr><tr><td>Type</td><td>Layer</td></tr><tr><td rowspan="2">Target</td><td>Type</td><td>Different collision partner type (e.g., Car: Vehicle Cat.: N1, N2, N3 PTW: Vehicle Cat.: L1, Bicyclist: Powered Standing Scooter)</td><td>No</td><td rowspan="6">Field Data**</td></tr><tr><td>Appearance</td><td>Same collision partner type but with different appearance (e.g., colour, accessories, shape)</td><td>No</td></tr><tr><td rowspan="4">Environment</td><td>Adverse weather conditions</td><td>Functionality available under the presence of Rain, Fog, Dirt/ice/moisture</td><td>No</td></tr><tr><td>Illumination (Night time)</td><td>Performance in darkness (1 lux) for all daytime-only scenarios. Target shall be equipped with realistic lighting.</td><td>No*</td></tr><tr><td>Illumination (Sun glare)</td><td>Functionality available under the presence of glare caused by Low sun (all scenarios during daytime condition)</td><td>No</td></tr><tr><td>Illumination (Headlamp glare)</td><td>Performance under the presence of glare caused by headlamps of a stationary vehicle on adjacent lane (all standard nighttime scenarios)</td><td>No*</td></tr><tr><td rowspan="2"></td><td>Infrastructure / clutter</td><td>Performance in environments cluttered with objects such as urban furniture or secondary road users (without fully obscuring the main target)</td><td>No*</td><td rowspan="2"></td></tr><tr><td>Obscuration / Obstruction</td><td>Variance in the layout of nominal obstructions</td><td>No*</td></tr></table>


** As outlined in 4.1.3 


# 5.2.1.3 Verification Tests Conditions

For the Robustness Layers where verification tests shall or may be done, the following conditions apply: 

<table><tr><td colspan="2">VUT Robustness layers</td><td rowspan="2">Verification condition*</td><td rowspan="2">Assessment Criteria</td></tr><tr><td>Layer</td><td>Scenarios</td></tr><tr><td rowspan="4">Driver input pre-crash</td><td>Longitudinal</td><td>·TDriver_steer @ 4.0s TTC
·TDriver_throttle @ 8.0s TTC
·Resulting Impact location must be within the range where the OEM predicted performance</td><td rowspan="4">Same or better than Standard Range**</td></tr><tr><td>Crossing, C2P, C2B</td><td>·TDriver_steer @ 4.0s TTC
·TDriver_throttle @ [4.0]s TTC
·Resulting Impact location must be within the range where the OEM predicted performance</td></tr><tr><td>Crossing C2C, C2M</td><td>·TDriver_steer @ 4.0s TTC
·TDriver_throttle @ [4.0]s TTC
·Impact location tolerance (against nominal) ±20%</td></tr><tr><td>Turning</td><td>·VUT Lateral deviation 0 ± 0.4 m (manual turn)
·Impact location tolerance (against nominal) ±20%</td></tr></table>


**Assessment of the resulting test case is conducted against the closest grid cell inside the standard range. Performance shall be the same or better than without layer present. 


# Driver Input Pre-Crash Robustness Layer

Testing with the "Driver Input Pre-Crash" robustness layer is intended to replicate naturalistic human driving behaviour before an accident. 

Euro NCAP 

Version 1.1 — October 2025 

For Longitudinal and Crossing scenarios, when control is transferred from the steering or accelerator robot to the test driver (TDriver_steer or TDriver_throttle), the following conditions shall apply: 

Driving style shall be natural and relaxed, replicating a situation where a driver follows the road/traffic i.e. no curves or complex road situations ahead. 

After the control transfer, the driver shall not focus on the target ahead but instead maintain stable steering and speed. This may be realized by looking at the IVI/phone to avoid unintended reactions. 

For turning tests, when the control is transferred from the steering robot to the driver (TDriver_steer), the driver shall steer naturally through the junction towards and attempt to hit the target at approximately the designated impact location. 

<table><tr><td colspan="2">Target Robustness layers</td><td rowspan="2">Verification condition*</td><td rowspan="2">Assessment Criteria</td></tr><tr><td>Layer</td><td>Scenarios</td></tr><tr><td rowspan="8">Speed</td><td>CCFhos/hol</td><td rowspan="2">±5 km/h</td><td>#red</td></tr><tr><td>CCFtap, CMFtap
CCCscp, CMCscp</td><td rowspan="3">Same or better than Standard Range</td></tr><tr><td>CPTA</td><td>+3 km/h</td></tr><tr><td>CBTA</td><td>+5 km/h</td></tr><tr><td rowspan="2">CPNA, CPFA,
CPNCO</td><td>+3 km/h</td><td>#red</td></tr><tr><td>-2 km/h</td><td>Same or better than Standard Range</td></tr><tr><td rowspan="2">CBNA, CBFA,
CBNAO</td><td>+5 km/h</td><td>#red</td></tr><tr><td>-3 km/h</td><td>Same or better than Standard Range</td></tr><tr><td rowspan="2">Acceleration</td><td rowspan="2">CCRb, CMRb</td><td>+2 m/s²</td><td>Same or better than Standard Range</td></tr><tr><td>-2 m/s²</td><td>#red</td></tr><tr><td rowspan="4">Initial position offset</td><td>CPNA, CPFA,
CBNA, CBFA,
CPNCO, CBNAO</td><td rowspan="2">-25% m of distance to impact point</td><td>#red</td></tr><tr><td>CPTA</td><td rowspan="2">Same or better than Standard Range</td></tr><tr><td>CCFtap, CMFtap,
CBTA</td><td>±0.5m Path offset</td></tr><tr><td>CCRb, CMRb</td><td>±0.5s Time headway</td><td>#red</td></tr><tr><td rowspan="2">Trajectory/Heading</td><td>CCRs, CMRs</td><td rowspan="2">±20° (target rotation around the impact point)</td><td rowspan="2">Same or better than Standard Range</td></tr><tr><td>CPNA, CPFA, CBNA, CBFA, CPNCO, CBNAO</td></tr></table>

<table><tr><td colspan="2">Environment robustness layers</td><td rowspan="2">Verification condition*</td><td rowspan="2">Assessment Criteria</td></tr><tr><td>Layer</td><td>Scenarios</td></tr><tr><td>Illumination (Night time)</td><td>ALL except Standard nighttime scenarios</td><td>Performance in darkness (1 lux) for all daytime scenarios</td><td>\(\#red\)</td></tr><tr><td>Illumination (Headlamp glare)</td><td>ALL Standard nighttime scenarios</td><td>Headlight of stationary vehicle on adjacent lane</td><td>\(\#red\)</td></tr><tr><td rowspan="8">Infrastructure / clutter</td><td>CCRs</td><td>Vehicle aside of main target</td><td rowspan="6">Same or better than Standard Range</td></tr><tr><td>CMRs</td><td>Vehicle aside of main target OR GVT in front of main target</td></tr><tr><td>CCRm, CCRb, CMRb</td><td>Vehicle aside of main target (moving)</td></tr><tr><td>CCRb</td><td>GVT in front of main target (moving)</td></tr><tr><td>Turning (C2P, C2B)</td><td>Typical crossing scenery e.g., traffic sign, refuge, trash bin</td></tr><tr><td>CCCscp, CMCscp</td><td>Typical crossing scenery e.g., traffic sign, stationary pedestrians on sidewalk, stationary (secondary) GVT on crossing road</td></tr><tr><td>CPNA, CPFA</td><td>Randomly selected case from Technical Bulletin CA 002</td><td>\(\#red\)</td></tr><tr><td>CBNA, CBFA</td><td>Randomly selected case from Technical Bulletin CA 002 (To be further populated with Bicyclist cases over the course of 2025)</td><td>\(\#red\)</td></tr><tr><td rowspan="2">Obscuration / Obstruction</td><td>CPNCO</td><td>Randomly selected CPNCO case from Technical Bulletin CA 002</td><td>\(\#red\)</td></tr><tr><td>CBNAO</td><td>Randomly selected CBNCO case from Technical Bulletin CA 002</td><td>\(\#red\)</td></tr><tr><td></td><td></td><td>(To be further populated with Bicyclist cases over the course of 2025)</td><td></td></tr></table>


* Versus the condition used in the Standard Range (excluding red cells) 


# Scoring

# 5.3.1 Standard Ranges

For score calculation in the Standard Range of each scenario, first each grid cell is given a subscore according to the Vehicle Manufacturer colour prediction: 

<table><tr><td>Predicted Colour</td><td>Standard Range Sub-score per grid cell</td></tr><tr><td>Green</td><td>1.00</td></tr><tr><td>Yellow</td><td>0.75</td></tr><tr><td>Orange</td><td>0.50</td></tr><tr><td>Brown</td><td>0.25</td></tr><tr><td>Red</td><td>0.00</td></tr></table>

Secondly, the resulting score is calculated by normalizing all the Standard Range sub-scores to the total score of the Standard Range in that scenario(rounded to hundredth): 

$$
S c o r e S t a n d a r d R a n g e = \frac {\sum S u b s c o r e s i n S t a n d a r d R a n g e \times T o t a l S t a n d a r d R a n g e S c o r e}{N u m b e r o f G r i d C e l l s i n S t a n d a r d R a n g e}
$$

# 5.3.2 Extended Ranges

For score calculation in the Extended Range of each scenario, first each grid cell is given a subscore according to the Vehicle Manufacturer prediction: 

<table><tr><td>Predicted Colour</td><td>Extended Range Sub-score per grid cell</td></tr><tr><td>Green</td><td rowspan="4">1.00</td></tr><tr><td>Yellow</td></tr><tr><td>Orange</td></tr><tr><td>Brown</td></tr><tr><td>Red</td><td>0.00</td></tr></table>

Secondly, the resulting score is calculated by normalizing all the Extended Range sub-scores to the total score of the Extended Range in that scenario(rounded to hundredth): 

$$
S c o r e E x t e n d e d R a n g e = \frac {\sum S u b s c o r e s i n E x t e n d e d R a n g e \times T o t a l E x t e n d e d R a n g e S c o r e}{N u m b e r o f G r i d C e l l s i n E x t e n d e d R a n g e}
$$

The final score for each Extended Range in a given scenario is calculated as follows: 

<table><tr><td colspan="2">Extended Range Scoring</td></tr><tr><td>% of total score</td><td>Final score</td></tr><tr><td>50 ≤ Score Extended Range &lt; 75</td><td>50%</td></tr><tr><td>75 ≤ Score Extended Range &lt; 100</td><td>75%</td></tr><tr><td>Score Extended Range = 100</td><td>100%</td></tr></table>

# 5.3.2.1 AES

For the impact locations in the Extended Range, the Vehicle Manufacturer may implement an AES function that provides full avoidance by in-lane steering. The Vehicle Manufacturer shall elaborate to Euro NCAP the AES function strategy and will provide a specific test method to verify performance, which shall be carried out by the test laboratory. 

# 5.3.2.2 ESS

For the following situations, the Vehicle Manufacturer may implement an ESS function that is effective at supporting the driver in fully avoiding a collision by a steering manoeuvre: 

<table><tr><td>Steering manoeuvre</td><td>Direction</td><td>Scenario</td><td>VUT speed</td><td>Impact location</td></tr><tr><td rowspan="3">In-lane</td><td rowspan="3">Farside and/or Nearside</td><td>CCRs</td><td rowspan="2">&gt;=60 km/h</td><td>-25%, 125%</td></tr><tr><td>CMRs</td><td>10%, 90%</td></tr><tr><td>CPLA, CBLA</td><td>&gt;=50 km/h</td><td>10%, 75%</td></tr><tr><td rowspan="3">Partial lane change*</td><td rowspan="3">Farside</td><td>CCRs</td><td rowspan="2">&gt;=60 km/h</td><td>0%, 25%, 50%</td></tr><tr><td>CMRs</td><td>50%, 25%</td></tr><tr><td>CPLA, CBLA</td><td>&gt;=50 km/h</td><td>25%, 50%</td></tr></table>

* Only when ESS is able to evaluate free space in neighbour lane. If neighbour lane is obstructed or occupied with oncoming/overtaking traffic, the performance criteria should be based on nominal conditions (i.e., FCW to be issued ${ \geq } 1 . 7 s$ TTC for CPLA & CBLA / speed reduction by FCW/AEB for CCRs/CMRs). 

The Vehicle Manufacturer shall elaborate to Euro NCAP the ESS function strategy and will provide a specific test method to verify performance, which shall be carried out by the test laboratory. 

# 5.3.3 Robustness Layers

To be eligible for scoring points in Robustness Layers in a specific scenario, the e sh ll be $\mathtt { \ge 5 0 \% }$ of the total available score in the Standard Range of that scenario. 

The score for each Robustness Layer in each scenario where the manufacturer predicted performance according to 5.2.1 is calculated as follows: 

$$
\text {S c o r e R o b u s t n e s s L a y e r s} = \frac {\text {T o t a l R o b u s t n e s s S c o r e}}{\text {N u m b e r o f a p p l i c a b l e R o b u s t n e s s L a y e r s}}
$$

An overview of the applicable Robustness Layers in each scenario can be found in APPENDIX A. 

# 5.3.4 Verification tests

The outcome of the verification tests will dictate the final score of a given scenario, and will depend on how the predicted performance is reported by the Vehicle Manufacturer, as illustrated in the table below: 

<table><tr><td rowspan="4"># of tests→Passed* tests↓</td><td colspan="8">Score % from verification tests outcome</td></tr><tr><td colspan="6">Standard Range</td><td colspan="2">Extended Range</td></tr><tr><td colspan="3">Virtual TestingPredictions</td><td colspan="3">Self-claimPredictions</td><td>Virtual TestingPredictions</td><td>Self ClaimPredictions</td></tr><tr><td>5</td><td>4</td><td>3</td><td>5</td><td>4</td><td>3</td><td>2</td><td>2</td></tr><tr><td>5</td><td>100%</td><td>-</td><td>-</td><td>100%</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4</td><td>80%</td><td>100%</td><td>-</td><td>80%</td><td>100%</td><td>-</td><td>-</td><td>-</td></tr><tr><td>3</td><td>60%</td><td>75%</td><td>100%</td><td>0%</td><td>75%</td><td>100%</td><td>-</td><td>-</td></tr><tr><td>2</td><td>40%</td><td>50%</td><td>67%</td><td>0%</td><td>0%</td><td>67%</td><td>100%</td><td>100%</td></tr><tr><td>1</td><td>20%</td><td>25%</td><td>33%</td><td>0%</td><td>0%</td><td>0%</td><td>50%</td><td>0%</td></tr><tr><td>0</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr></table>


* Passed $=$ in line or beyond the predicted performance 


Where performance was predicted by Virtual Testing, and acceptance criteria set forth in the VTA protocol are not met, all scenarios in that scenario cluster will be treated as Self-claim for scoring. 

# 5.3.5 Scoring example

Below flowchart illustrates an example of how to calculate the final scores in a CCFhol scenario: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d937a988-c5b9-482b-a485-613e0e6a3484/84651caa5e81c9a7e7ef88064adcd1e7ca2ab35be2a20951932f5d106f1b2bb2.jpg)


# Links to Driver State

The Vehicle Manufacturer may implement a sensitivity change strategy for FCW and/or AEB according to the state of the driver detected by the DSM as described in the Euro NCAP Driver Engagement protocol, provided that following conditions are met: 

The DSM shall offer minimum performance across different driver states: 

o Transient states: $50 \%$ of total score in Forward Support Sensitivity intervention 

o Non-transient states: Forward Support Sensitivity intervention on Drowsiness and Sleep 

The sensitivity change shall be set back to the nominal setting < 1 second after the DSM system is in degraded mode, non-functional or turned off. 

The acceptance criteria for FCW and/or AEB Sensitivity Change across scenarios and driver states is summarized in the table below: 

<table><tr><td colspan="5">FCW and/or AEB Sensitivity Change</td></tr><tr><td colspan="2">Impact location ranges</td><td>Standard Range not adjacent to Extended Range</td><td>Standard Range adjacent to Extended Range</td><td>Extended Range</td></tr><tr><td colspan="2">Applicable Scenarios</td><td>CCRs, CMRs CCRm</td><td>CCRs, CMRs CCRm</td><td>CCRs, CMRs CCRmCPLA, CBLA CPNA, CPFA, CBNA, CBFA CPTA, CBTA CCCscp, CMCscp CCFhos, CCFhol</td></tr><tr><td rowspan="3">Acceptance Criteria</td><td>Attentive driver state</td><td>Performance according to prediction (FCW can be later)</td><td>Any colour (#red)</td><td>Any colour OR suppression (no performance requirements)</td></tr><tr><td>Unknown driver state**</td><td>Performance according to prediction</td><td>Performance according to prediction</td><td>Any colour (#red)</td></tr><tr><td>Distracted driver state</td><td>Performance according to prediction or better*</td><td>Performance according to prediction</td><td>Performance according to prediction</td></tr></table>


* May be used to verify DSM requirements for increased sensitivity (1.4.3.1. FCW and/or AEB 200ms earlier distracted driver state relative to unknown driver state). 



** DSM switched off and/or system degraded or not available 



For the scenarios where the Vehicle Manufacturer claimed usage of the Driver State Link, verification tests shall be performed with a test driver that is classified as distracted. 


# APPENDIX A APPLICABILITY OF ROBUSTNESS LAYERS


A.1 Car-to-Car Scenarios


<table><tr><td>Type</td><td>Robustness Layer</td><td>Assessment</td><td>CCR s</td><td>CCR m</td><td>CCR b</td><td>CCF hos</td><td>CCF hol</td><td>CCF tap</td><td>CCC scp</td></tr><tr><td>VUT</td><td>Driver input pre-crash</td><td>Verification Test</td><td>YES</td><td>YES</td><td>YES</td><td>N/A</td><td>N/A</td><td>YES</td><td>YES</td></tr><tr><td rowspan="6">Target</td><td>Speed</td><td>Verification Test</td><td>N/A</td><td>N/A</td><td>N/A</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Acceleration</td><td>Verification Test</td><td>N/A</td><td>N/A</td><td>YES</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Initial position offset</td><td>Verification Test</td><td>N/A</td><td>N/A</td><td>YES</td><td>N/A</td><td>N/A</td><td>YES</td><td>N/A</td></tr><tr><td>Trajectory/Heading</td><td>Verification Test</td><td>YES</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Type</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Appearance</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td rowspan="5">Environment</td><td>AWC</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Illumination (Night)</td><td>Field Data*</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Illumination (Sun glare)</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Infrastructure / Clutter</td><td>Field Data*</td><td>YES</td><td>YES</td><td>YES</td><td>N/A</td><td>N/A</td><td>N/A</td><td>YES</td></tr><tr><td>Obscuration / Obstruction</td><td>Field Data*</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td colspan="3">Total applicable Robustness Layers</td><td>8</td><td>7</td><td>9</td><td>6</td><td>6</td><td>8</td><td>8</td></tr></table>


* NOT to be selected as part of the Verification tests process. This layer may only be conducted under request of Euro NCAP Secretariat. 



A.2



Car-to-PTW Scenarios


<table><tr><td>Type</td><td>Robustness Layer</td><td>Assessment</td><td>CMRs</td><td>CMRb</td><td>CMFtap</td><td>CMCscp</td></tr><tr><td>VUT</td><td>Driver input pre-crash</td><td>Verification Test</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td rowspan="6">Target</td><td>Speed</td><td>Verification Test</td><td>N/A</td><td>N/A</td><td>YES</td><td>YES</td></tr><tr><td>Acceleration</td><td>Verification Test</td><td>N/A</td><td>YES</td><td>N/A</td><td>N/A</td></tr><tr><td>Initial position offset</td><td>Verification Test</td><td>N/A</td><td>YES</td><td>YES</td><td>N/A</td></tr><tr><td>Trajectory/Heading</td><td>Verification Test</td><td>YES</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Type</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Appearance</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td rowspan="5">Environment</td><td>AWC</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Illumination (Night)</td><td>Field Data*</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Illumination (Sun glare)</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Infrastructure / Clutter</td><td>Field Data*</td><td>YES</td><td>YES</td><td>N/A</td><td>YES</td></tr><tr><td>Obscuration / Obstruction</td><td>Field Data*</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td colspan="3">Total applicable Robustness Layers</td><td>8</td><td>9</td><td>8</td><td>8</td></tr></table>


* NOT to be selected as part of the Verification tests process. This layer may only be conducted under request of Euro NCAP Secretariat. 


# A.3 Car-to-Pedestrian Scenarios

<table><tr><td>Type</td><td>Robustness Layer</td><td>Assessment</td><td>CPLA</td><td>CPTA</td><td>CPNA</td><td>CPFA</td><td>CPNCO</td></tr><tr><td>VUT</td><td>Driver input pre-crash</td><td>Verification Test</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td rowspan="6">Target</td><td>Speed</td><td>Verification Test</td><td>N/A</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Acceleration</td><td>Verification Test</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Initial position offset</td><td>Verification Test</td><td>N/A</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Trajectory/Heading</td><td>Verification Test</td><td>N/A</td><td>N/A</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Type</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Appearance</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td rowspan="6">Environment</td><td>AWC</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Illumination (Night)</td><td>Field Data*</td><td>N/A</td><td>YES</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Illumination (Sun glare)</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Illumination (Hea clamp glare)</td><td>Field Data*</td><td>YES</td><td>N/A</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Infrastructure / Clutter</td><td>Field Data*</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>N/A</td></tr><tr><td>Obscuration / Obstruction</td><td>Field Data*</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>YES</td></tr><tr><td colspan="3">Total applicable Robustness Layers</td><td>7</td><td>9</td><td>10</td><td>10</td><td>10</td></tr></table>


* NOT to be selected as part of the Verification tests process. This layer may only be conducted under request of Euro NCAP Secretariat. 


<table><tr><td>Type</td><td>Robustness Layer</td><td>Assessment</td><td>CBLA</td><td>CBTA</td><td>CBNA</td><td>CBFA</td><td>CBNAO</td></tr><tr><td>VUT</td><td>Driver input pre-crash</td><td>Verification Test</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td rowspan="6">Target</td><td>Speed</td><td>Verification Test</td><td>N/A</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Acceleration</td><td>Verification Test</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Initial position offset</td><td>Verification Test</td><td>N/A</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Trajectory/Heading</td><td>Verification Test</td><td>N/A</td><td>N/A</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Type</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Appearance</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td rowspan="5">Environment</td><td>AWC</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Illumination (Night)</td><td>Field Data*</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Illumination (Sun glare)</td><td>Field Data</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Infrastructure / Clutter</td><td>Field Data*</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>N/A</td></tr><tr><td>Obscuration / Obstruction</td><td>Field Data*</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>YES</td></tr><tr><td colspan="3">Total applicable Robustness Layers</td><td>7</td><td>9</td><td>10</td><td>10</td><td>10</td></tr></table>


* NOT to be selected as part of the Verification tests process. This layer may only be conducted under request of Euro NCAP Secretariat. 


# APPENDIX B OBSTRUCTION DIMENSIONS

# B.1 Smaller obstruction vehicle

The smaller obstruction vehicle shall be: 

Of the category Small Family Car 

Of a dark colour 

Within the following geometrical dimensions: 

<table><tr><td></td><td>Vehicle length</td><td>Vehicle width (without mirrors)</td><td>Vehicle height</td><td>Bonnet length (till A pillar)</td><td>Bonnet Leading Edge height</td></tr><tr><td>Minimum</td><td>4100 mm</td><td>1700 mm</td><td>1300 mm</td><td>1000 mm</td><td>650 mm</td></tr><tr><td>Maximum</td><td>4400 mm</td><td>1900 mm</td><td>1500 mm</td><td>1500 mm</td><td>850 mm</td></tr></table>

# B.2 Larger obstruction vehicle

The larger obstruction vehicle shall be: 

Of the category Small SUV 

Of a dark colour 

Within the following geometrical dimensions: 

<table><tr><td></td><td>Vehicle length</td><td>Vehicle width
(without mirrors)</td><td>Vehicle height</td></tr><tr><td>Minimum</td><td>4300 mm</td><td>1750 mm</td><td>1500 mm</td></tr><tr><td>Maximum</td><td>4700 mm</td><td>1900 mm</td><td>1800 mm</td></tr></table>