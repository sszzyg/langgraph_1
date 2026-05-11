# Crash Avoidance

# Lane Departure

# Collisions

Protocol 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/4898d053efa58de1cefc06a261bcf225aa3c55bd70918812953b2bfd6f42abe7.jpg)


# PREFACE

During the test preparation, vehicle manufacturers are encouraged to liaise with the laboratory and to check that they are satisfied with the way cars are set up for testing. Where a manufacturer feels that a particular item should be altered, they should ask the laboratory staff to make any necessary changes. Manufacturers are forbidden from making changes to any parameter that will influence the test, such as dummy positioning, vehicle setting, laboratory environment etc. 

It is the responsibility of the test laboratory to ensure that any requested changes satisfy the requirements of Euro NCAP. Where a disagreement exists between the laboratory and manufacturer, the Euro NCAP secretariat should be informed immediately to pass final judgment. Where the laboratory staff suspect that a manufacturer has interfered with any of the set up, the manufacturer's representative should be warned that they are not allowed to do so themselves. They should also be informed that if another incident occurs, they will be asked to leave the test site. 

Whe e the e is ecu ence of the p oblem, the m nuf ctu e ’s ep esent tive will be told to le ve the test site and the Secretary General should be immediately informed. Any such incident may be reported by the Secretary General to the manufacturer and the person concerned may not be allowed to attend further Euro NCAP tests. 

DISCLAIMER: Euro NCAP has taken all reasonable care to ensure that the information published in this protocol is accurate and reflects the technical decisions taken by the organisation. In the unlikely event that this protocol contains a typographical error or any other inaccuracy, Euro NCAP reserves the right to make corrections and determine the assessment and subsequent result of the affected requirement(s). 

# CONTENTS

# DEFINITIONS 2

# 1 MEASURING EQUIPMENT 4

Reference system 4 

Scenario Parameters 5 

VUT 7 

Targets 7 

Measurements and variables 9 

2 TEST CONDITIONS 10 

Test track 1 0 

VUT Preparation 1 1 

3 TEST PROCEDURE 14 

Single vehicle 1 4 

Car & PTW 1 8 

4 TEST EXECUTION 24 

Performance Predictions 2 4 

Verification tests 2 5 

Test Conduct 2 6 

5 ASSESSMENT 29 

General requirements 2 9 

Criteria 2 9 

Scoring 3 4 

# APPENDIX A LANE DEPARTURE PATHS 37

# APPENDIX B APPLICABILITY OF ROBUSTNESS LAYERS 39

# DEFINITIONS

Throughout this protocol the following terms are used: 

Peak Braking Coefficient (PBC) – the measure of tyre to road surface friction based on the maximum deceleration of a rolling tyre, measured using the American Society for Testing and Materials (ASTM) E1136-10 (2010) standard reference test tyre, in accordance with ASTM Method E 1337-90 (reapproved 1996), at a speed of 64.4 km/h, without water delivery. Alternatively, the method as specified in UNECE R13-H. 

Emergency Lane Keeping (ELK) – default ON heading correction that is applied automatically by the vehicle in response to the detection of the vehicle that is about to drift beyond a lane boundary (i.e. solid lane marking, road edge) and/or into oncoming or overtaking traffic in the adjacent lane. 

Lane Keeping Assist (LKA) – heading correction that is applied automatically by the vehicle in response to the detection of the vehicle that is about to drift beyond a delineated edge line of the current travel lane. 

Lane Departure Warning (LDW) – a warning that is provided automatically by the vehicle in response to the vehicle that is about to drift beyond a delineated edge line of the current travel lane. 

Blind Spot Monitoring (BSM) – A sensing system that detects and warns the driver of an object (i.e. other road user) in an adjacent lane, which may be obscured from vision. This system must be default ON to be eligible for assessment. 

Vehicle under test (VUT) – means the vehicle tested according to this protocol with an Emergency Lane Keeping, Lane Keep Assist and/or Lane Departure Warning system. 

Global Vehicle Target (GVT) – means the vehicle target used in this protocol as defined in ISO 19206-3:2021 

Euro NCAP Target (EMT) – means the Motorcyclist target used in this protocol as specified in ISO 19206-5. 

Real Motorcycle – Means a motorcyclist target that can be used in the Blind-Spot Monitoring Tests of this protocol, as an alternative to the EMT. The Real Motorcycle shall be a type approved two-wheeled motorcycle, with a maximum speed of at least 80km/h by design, without front fairing or windshield. It shall closely resemble the EMT (as specified in section 2.1 of deliverable D2.1 of the MUSE project), thus staying within the mean dimensions of the most registered middleweight naked motorcycles in Europe (i.e. wheelbase $> 1 4 0 5 \mathsf { m m }$ . and $< 1 4 4 5 \mathsf { m m }$ .). 

Time To Collision (TTC) – means the remaining time before the VUT strikes the target, assuming the VUT and target would continue to travel with the speed it is travelling. 

Standard range – refers to the most basic and controlled format a test scenario will be tested. Tests within the standard range are deemed the foundational level performance expectations for any given test scenario. 

Euro NCAP 

Version 1.1 — October 2025 

Extended range – refers to test points in which minor levels of complexity are introduced to the standard range tests. Changes for this range are limited to lateral or longitudinal velocity variations for the VUT and / or test target. 

Robustness layer – refers to the introduction of test complexity and variation, designed to ch llenge vehicle systems nd encou ge eli ble “ e l-wo ld” pe fo m nce. 

Lane Edge – the road edge or inner side of the lane marking for the lane that the VUT is travelling. 

Distance To Lane Edge (DTLE) – means the remaining lateral distance (perpendicular to the Lane Edge) between the Lane Edge and most outer edge of the tyre, before the VUT crosses Lane Edge, assuming the VUT would continue to travel with the same lateral velocity towards it. 

Driver Intention Monitoring system – means a system that is effective at distinguishing intentional from unintentional lane crossing and suppressing undesired interventions and/or warnings. 

Driver State Link (DSL) – refers to a vehicle system strategy that uses the detection of driver state (via Driver Status Monitoring system) to alter the Active Safety system response settings with respect to the levels of driver engagement. System sensitivity can be increased, or decreased, based on the detected driver state. 

# 1 MEASURING EQUIPMENT

# Reference system

# 1.1.1 Local Coordinate System

Use the convention specified in ISO 8855:2011, with the origin at the most forward point on the centreline of the VUT for dynamic data measurements as shown in Figure 1-1. This reference system should be used for both left- and right-hand drive vehicles. In Figure 1-1 nearside and farside are shown for a left-hand drive vehicle. For a right-hand drive vehicle, nearside and far-side are swapped. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/48b663d558d42bcb315a74297898fae1573e8943999867f11487e57a717b0890.jpg)



Figure 1-1 Local Coordinate System and notation


# 1.1.2 Global Coordinate System

The origin of the Global Coordinate System $( \mathsf { x } { = } 0 , \mathsf { y } { = } 0 )$ shall be located, by default, at the theoretical intersection of the VUT test path and the inner side of the lane edge in which DTLE is measured from, as illustrated below: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/7a52e135047836cdd50057c30b647665926e0916c0bad7db656dbf7766787ac2.jpg)



Figure 1-2 Global Coordinate System origin


Euro NCAP 

Version 1.1 — October 2025 

All positional measurements relating to the VUT and test targets shall be referenced to the Global Coordinate System. 

In all cases, the x-axis shall be aligned with the nominal direction of travel of the VUT, and the yxis pe pendicul to it, with positive y defined to the left of the VUT’s di ection of t vel. 

# Scenario Parameters

# 1.2.1 Impact location

The impact location is defined as where the reference point of the test target coincides with the required $\%$ -age of the VUT width (subtracting the mirrors). 

# 1.2.1.1 Car-to-car Oncoming

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/e75ce18465565ef171448d3ac58178a382dbb781198926ccf615964f21f4c15e.jpg)



Figure 1-3 Impact Locations for Car-to-Car Oncoming


# 1.2.1.2 Car-to-Motorcyclist Oncoming

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/2991a2e30afa821a9296c1302ba1eeb13ab7828b5319612deaf8d4476519e7d0.jpg)



Figure 1-4 Impact Locations for Car-to-Motorcyclist Oncoming


# 1.2.1.3 Car-to-car Overtaking

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/9375a3a7c622517d165eef5940b847d4509989f07bf3e9932a1f2ff30d154d8b.jpg)



Figure 1-5 Impact Locations for Car-to-Car Overtaking


# 1.2.1.4 Car-to-Motorcyclist Overtaking

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/f9df92780a4036788094b996d3a606e7d6a3f8a48f453a16994af0740d018531.jpg)



Figure 1-6 Impact Locations for Car-to-Motorcyclist Overtaking


# 1.3 VUT

# 1. 3. 1 VU T P ro f il e

A virtual profiled line is defined around both the front end and the rear end of the VUT, as well as around the right and left side of the VUT. The front and rear profiles are defined by straight line segments connecting seven points that are equally distributed over the vehicle width minus 50mm on each side. The side profiles are defined by straight line segments connecting seven points that are equally distributed between the outermost rear and front profiles, on each side. The theoretical x,y coordinates for each of these points are provided by the OEMs and verified by the test laboratory. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/02efe201b8369ca0336323af289c708288145c0e87a38e160f9ca22fddc2651b.jpg)



Figure 1-7 Virtual profiled line around the front end, rear end of the VUT


# Targets

Only equipment listed in the current version of Technical Bulletin G 003 may be used for testing. The current version can be found on the Euro NCAP website. 

# 1.4.1 Virtual Boxes

# 1.4.1.1 Euro NCAP Motorcyclist Target ( EMT)

The dimensions of the EMT virtual box are shown in the figure below with reference points on the most forward point on the front wheel (applicable to longitudinal-front, turning and crossing scenarios) and most rearward point on the rear wheel (applicable to longitudinal-rear scenarios). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/505963ffc9570f7a16165fe8adb5d23026567048be89dc3f2aa7d855a28464a7.jpg)



Figure 1-8 Virtual box dimensions around EMT


# 1.4.1.2 Global Vehicle Target (GVT)

The virtual box of the GVT is shown in the figure below, with reference points on: the most forward point on the front profile (1 in the centre and 1 in the intersection of the front profile and each of the side profiles), the most rearward point on the rear profile (in the centre), and at $7 5 \%$ along the length of each side of the GVT. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/013a5ccb700168d8ac02ab268a982ca0a1381483db3ed9e71e61f3c716f0f682.jpg)



Figure 1-9 Virtual box dimensions around GVT


# Measurements and variables

Record all dynamic data at a frequency of at least 100Hz. Synchronise using the DGPS time stamp of the test target data with that of the VUT. 

# 1.5.1 Variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>T</td><td>Time</td></tr><tr><td>T0</td><td>Time of test start T0 = time where manoeuvre starts with 2s straight path</td></tr><tr><td>TLDW</td><td>Time where LDW activates</td></tr><tr><td>Tsteer</td><td>Time where the VUT enters in curve segment</td></tr><tr><td>Tcrossing</td><td>Time where VUT crosses the line or road edge</td></tr><tr><td>Tend</td><td>Time of test end (see 4.3.2 Test Scenarios)</td></tr><tr><td>XVUT, YVUT</td><td>Position of the VUT during the entire test</td></tr><tr><td>Vlong,VUT, VIat,VUT</td><td>Speed of the VUT during the entire test</td></tr><tr><td>ΨVUT</td><td>Yaw velocity of the VUT during the entire test</td></tr><tr><td>ΩVUT</td><td>Steering wheel velocity of the VUT during the entire test</td></tr><tr><td>Xtarget, Ytarget</td><td>Position of the target during the entire test</td></tr><tr><td>Vtarget</td><td>Speed of the target during the entire test</td></tr><tr><td>Atarget</td><td>Acceleration of the target during the entire test</td></tr><tr><td>Ψtarget</td><td>Yaw velocity of the target during the entire test</td></tr></table>

# 1.5.2 Measurements

Equip the VUT with data measurement and acquisition equipment to record test data with an accuracy of at least: 

VUT and target longitudinal speed to 0.1km/h 

- VUT and target lateral and longitudinal position to 0.03m 

VUT heading angle to $0 . 1 ^ { \circ }$ 

- VUT and target yaw rate to $0 . 1 \%$ 

VUT longitudinal acceleration to $0 . 1 \mathsf { m } / \mathsf { s } ^ { 2 }$ 

VUT steering wheel velocity to $1 . 0 ^ { \circ } / \mathsf { s }$ 

# 1 . 5 . 3 D a t a F i l t e r i n g

Filter the measured data as follows: 

Position and speed are not filtered and are used in their raw state. 

Acceleration, yaw rate, steering wheel torque and steering wheel velocity with a 12-pole phase less Butterworth filter with a cut off frequency of 10Hz. 

# 2 TEST CONDITIONS

# Test track

Conduct tests on a dry (no visible moisture on the surface), uniform, solid-paved surface with a maximum slope of $\pm 1 \%$ in the longitudinal direction and a maximum lateral slope of $\pm 3 \%$ . 

The test track surface shall have a minimal peak braking coefficient (PBC) of 0.9, must be paved and may not contain any irregularities (e.g. large dips or cracks, manhole covers or reflective studs) within a lateral distance of $3 . 0 \mathsf { m }$ to either side of the centre of the test lane and with a longitudinal distance of 30m ahead of the VUT from the point after the test is complete. 

# 2.1.1 Lane Markings and Road Edge

The tests described in this document require use of two different types of lane markings conforming to one of the lane markings as defined in UNECE Regulation 130 to mark a lane with a width of 3.5 to $3 . 7 \mathsf { m }$ when measured from the inside edge of the lane marking and a road edge: 

1. Dashed line with a width between 0.10 and 0.25m (0.10 and 0.15m for centre lines) 

2. Solid line with a width between 0.10 and 0.25m 

3. Road Edge consisting of grass and/or gravel 

The inner edge of the lane marking shall be at 0.20 to 0.30m from the road edge (transition between paved test surface and road edge material), where applicable. 

The lane markings and/or road edge should be sufficiently long to ensure that there is at least 20m of marking remaining ahead of the vehicle after the test is complete. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/39227ca5dc21106556d8d9a8d6bf00ddeae48cfa9e840bfe109168845400b9da.jpg)



Figure 2-1: Layout of the lane markings


# 2.1.2 Weather conditions

Conduct tests in dry conditions with ambient temperature above $5 \textdegree C$ and below $4 0 ^ { \circ } \mathsf { C }$ . 

No precipitation shall be falling and horizontal visibility at ground level shall be greater than 1km. Wind speeds shall be below 10m/s to minimise VUT disturbance. 

Natural ambient illumination must be homogenous in the test area and in excess of 2000 lux for daylight testing with no strong shadows cast across the test area other than those caused by the VUT. Ensure testing is not performed driving towards, or away from the sun when there is direct sunlight. 

Measure and record the following parameters preferably at the commencement of every single test or at least every 30 minutes: 

a) Ambient temperature in $^ \circ \mathsf { C }$ ; 

b) Track Temperature in $^ \circ \mathsf { C }$ 

c) Wind speed in $\mathsf { m } / \mathsf { s }$ ; 

d) Wind direction in azimuth ° and/or compass point direction (monitoring); 

e) Ambient illumination in Lux. 

# VUT Preparation

# 2.2.1 System Settings

Set any driver configurable elements of the system (e.g. the timing of the Lane Departure Warning or the Lane Keep Assist if present) to the middle setting or midpoint and then next poorer performing setting (refer to the examples shown in Figure 2-2). Lane Centering functions should be turned OFF. Furthermore, if a vehicle has a system where ELK or ELK $^ +$ LKA mode can be selected, test the vehicle in ELK $^ +$ LKA mode. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/cd3083b3a0fd91adae6b3295f2b8ca47bfc211006c7d3af6c1bcbfb4ac49e9de.jpg)



Figure 2-2: System setting for testing


# 2.2.2 Wheel Alignment Measurement and Unladen Kerb Mass

The vehicle should be subject to a vehicle (in-line) geometry check to record the wheel alignment set by the OEM. This should be done with the vehicle in kerb weight. 

If pplic ble, fill up the t nk with fuel to t le st $90 \%$ of the t nk’s c p city of fuel. 

Check the oil level and top up to its maximum level if necessary. Similarly, top up the levels of all other fluids to their maximum levels if necessary. 

Ensure that the vehicle has its spare wheel on board, if fitted, along with any tools supplied with the vehicle. Nothing else should be in the car. 

Euro NCAP 

Version 1.1 — October 2025 

Ensu e th t ll ty es e infl ted cco ding to the m nuf ctu e ’s inst uctions fo the le st lo ding condition. 

Measure the front and rear axle masses and determine the total mass of the vehicle. The total m ss is the ‘unl den ke b m ss’ of the vehicle. Reco d this m ss in the test det ils. 

Calculate the required ballast mass, by subtracting the mass of the test driver and test equipment from the required 200 kg interior load. 

# 2.2.3 Tyres

Perform the testing with new original fitment tyres of the make, model, size, speed and load rating as specified by the vehicle manufacturer. It is permitted to change the tyres which are supplied by the manufacturer or acquired at an official dealer representing the manufacturer if those tyres are identical make, model, size, speed and load rating to the original fitment. Use inflation pressures corresponding to least loading normal condition. 

Run-in tyres according to the tyre conditioning procedure. After running-in maintain the run-in tyres in the same position on the vehicle for the duration of the testing. 

# 2.2.4 Vehicle Preparation

Fit the on-board test equipment and instrumentation in the vehicle. Also fit any associated cables, cabling boxes and power sources and place weights with a mass of the ballast mass. Any items added should be securely attached to the car. 

With the driver in the vehicle, weigh the front and rear axle loads of the vehicle and compare these lo ds with the “unl den ke b m ss” 

The total vehicle mass shall be within $\pm 1 \%$ of the sum of the unladen kerb mass, plus 200kg. The front/rear axle load distribution needs to be within $5 \%$ of the front/rear axle load distribution of the original unladen kerb mass plus full fuel load. If the vehicle differs from the requirements given in this paragraph, items may be removed or added to the vehicle which has no influence on its performance. Any items added to increase the vehicle mass should be securely attached to the car. 

Care needs to be taken when adding or removing weight in order to approximate the original vehicle inertial properties as close as possible. Record the final axle loads in the test details. Reco d the xle weights of the VUT in the ‘ s tested’ condition. 

Vehicle dimensional measurements shall be taken. For purposes of this test procedure, vehicle dimensions shall be represented by a two-dimensional polygon defined by the lateral and longitudinal dimensions relative to the centroid of the vehicle using the standard ISO 8855 coordinate system. The corners of the polygon are defined by the lateral and longitudinal locations where the plane of the outside edge of each tyre makes contact with the road. This plane is defined by running a perpendicular line from the outer most edge of the tyre to the ground at the wheelbase, as illustrated in Figure 2-3. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/46bed483a6f88dd737e93dd41c7abb87754f4e8984fdb5188f457173eb5075cc.jpg)



Figure 2-3: Vehicle dimensional measurements


The vehicle’s wheelb se nd the l te l nd longitudin l loc tions sh ll be me su ed nd recorded. 

Requirements for Steering Robot friction levels should be checked prior to testing, as detailed in the Technical Bulletin CA 201. 

# 3 TEST PROCEDURE

Each scenario in this assessment consists of a matrix combining vehicle longitudinal speeds, and ranges of impact locations or target longitudinal speeds. Each combination in a matrix is referred to as grid cell. The grid cells forming a matrix are grouped into two groups: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/62f177aa54ecf0901517f899d7e889a4a69958a0bfad348c7b0cd42f2e557b84.jpg)


Standard Range 

Extended Range 

# Single vehicle

Single Vehicle tests are to be conducted with the DSM system having not determined a driver state (i.e. unknown driver state). The vehicle should have automatically adjusted system performance or sensitivity (for systems when there is a link between LSS and DSM) to default settings. 

If a vehicle is equipped with Driver Intention Monitoring (DIM) functionality, the tests conducted for Driveability – Overriding Torque and Continuous Intervention may be performed with the DIM able to operate as intended by the vehicle manufacturer. 

<table><tr><td>Single Vehicle</td><td>Standard</td><td>Extended</td><td>Robustness</td><td>TOTAL</td></tr><tr><td>Driver Acceptance</td><td>5</td><td>-</td><td>-</td><td>5</td></tr><tr><td>Driveability</td><td>2</td><td>-</td><td>-</td><td>2</td></tr><tr><td>Driver State Link</td><td>3</td><td>-</td><td>-</td><td>3</td></tr><tr><td>Lane Departure</td><td>4</td><td>0.5</td><td>0.5</td><td>5</td></tr><tr><td>ELK Road edge*</td><td>4</td><td>0.5</td><td>0.5</td><td>5</td></tr></table>


* Half points awarded with LDW in Extended Range cases 


# 3.1.1 Driver Acceptance - Driveability

To be eligible for assessment in the Steering Response and Returning $\mathsf { V } _ { \mathsf { l a t } }$ Driveability metrics, a vehicle must, at minimum, be able to recognise and react to lane departures against road edges. 

Where this condition is met and when the verification tests are not fully compatible with vehicle system design, the vehicle manufacturer can propose an alternative test method and request the Euro NCAP Secretariat assess the Steering Response and Returning $\mathsf { V } _ { \mathsf { l a t } }$ Driveability metrics via their proposal. 

<table><tr><td>Driveability Requirement</td><td>Steering Robot Control</td><td>Longitudinal Speed Verification Test / Applicable Speed Range</td><td>Lateral Speed</td><td>Lane Boundary Type</td></tr><tr><td>Overriding Torque</td><td>Locked mode</td><td>70 km/h</td><td>0.2 to 0.6 m/s</td><td>Solid Line</td></tr><tr><td>Continuous Intervention</td><td>Path following mode</td><td>70 km/h</td><td>0.5 m/s</td><td>Road Edge Dashed Line Solid Line</td></tr><tr><td>Steering Response</td><td rowspan="2" colspan="3">Recorded during verification tests of Lane Departure – ELK Road Edge*</td><td>Road Edge</td></tr><tr><td>Returning Vlat</td><td>Road Edge</td></tr></table>


*Applicable for tests with the VUT speed between 70-100km/h longitudinal, and 0.2-0.6m/s lateral 


# 3.1.1.1 Overriding Torque

Perform the Overriding Torque measurements utilising the procedure outlined in 4.3.2.1 Calibration Runs. 

Each Overriding Torque measurement run will be conducted with all vehicle systems turned ON and with the vehicle travelling at 70km/h. 

The test laboratory shall record the VUT steering wheel torque for lane departures with lateral speeds between $0 . 2 \mathsf { m } / \mathsf { s }$ and $0 . 6 \mathsf { m } / \mathsf { s }$ (incremented by $0 . 1 \mathsf { m } / \mathsf { s } )$ , on either side of the vehicle and against solid line lane boundaries to determine whether the overriding torque requirements are met. 

# 3.1.1.2 Continuous Intervention

Continuous intervention testing will be conducted at $0 . 5 \mathsf { m } / \mathsf { s }$ lateral speed (per the table below) The test lab must conduct two test runs, against a randomly selected lane boundary type (i.e., Road Edge, Solid Line, LKA Dashed) and a randomly selected side of the VUT. 

Run 1: Complete the required test path with all lane support systems turned OFF 

Run 2: Complete the required test path with all system turned ON 

The VUT shall be driven at 70km/h and follow the test path (hold path mode), in which the test laboratory will record the steering wheel torque. 

<table><tr><td>Vlat</td><td>R</td><td>d1</td><td>d2</td><td>d3</td><td>d4</td></tr><tr><td>0.5m/s</td><td>1200</td><td>0.397</td><td>0.32</td><td>0.397</td><td>0.05</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/1b46c59509f73ee42bfbfadfba61630fd37aeb3a9f47030598b44f2b949db987.jpg)



Figure 3-1 Continuous Intervention test path


The duration of intervention will be measured from when the VUT yaw angle is parallel $( 0 \pm 0 . 1$ degrees) to the targeted lane boundary, until such time that the LSS response is fully suppressed, or the steering torque requirement is reduced to levels of ≤[1.5]Nm measured relative to inactive system. 

Alternatively, and with Euro NCAP Secretariat approval, the duration of intervention can be measured via an appropriate CAN signal that has been made accessible to the test lab by the vehicle manufacturer. 

# 3.1.1.3 Steering Response

The test laboratory shall record the VUT Steering Wheel Velocity and VUT Steering Angle (or any other alternative metrics if requested by the Vehicle Manufacturer) until test end for all selected verification tests within the standard and extended range of 3.1.3 Lane Departure – ELK Road Edge. 

# 3 . 1 . 1 . 4 R e t u r n i n g V l a t

The test laboratory shall record the VUT lateral velocity until Tend (test end) for all selected verification tests within the standard and extended range of 3.1.3 Lane Departure – ELK Road Edge. 

# 3.1.2 Driver Acceptance – Driver State Link

If a vehicle is equipped with a Driver Status Monitoring system that can adjust the LSS sensitivity with respect to the level of attentiveness of the driver; the manufacturer is encouraged to inform Euro NCAP on the specific details of this driver state link strategy. 

In accordance with the information provided, and at the direction of the Euro NCAP Secretariat, the test laboratory may verify the lane support system performance for both inattentive and attentive states. 

Verification testing will be selected in line with the requirements outlined in Technical Bulletin SD 202 – Driver Monitoring Test Procedure. 

# 3.1.3 Lane Departure – ELK Road Edge

The standard and extended test Ranges for Lane Departure – ELK Road Edge are shown below: 

<table><tr><td>ELK-RE</td><td>0.2 m/s</td><td>0.3 m/s</td><td>0.4 m/s</td><td>0.5 m/s</td><td>0.6 m/s</td><td>0.7 m/s</td></tr><tr><td>50 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

At the test labs discretion, and in agreement with the Vehicle Manufacturer, the tests in this scenario can be conducted either robotically, or manually by controlled inputs from the driver, or intersecting a curved section. 

Where the vehicle and test are to be controlled via driver inputs, the resulting $\mathsf { V } _ { \mathsf { l a t } }$ and $\mathsf { V } _ { \mathsf { I o n g } }$ shall be maintained within the grid points where performance is expected. 

The following test track and lane marking format is applied to the standard and extended test ranges. Tests for Lane Departure – ELK Road Edge will be performed to the passenger side of the VUT only. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/8b05bb9780af7c3435d8b0077f7714b524840ccce7baf04d1ac44745fa09872b.jpg)



Figure 3-2 Lane Departure – ELK Road Edge test format


For verification tests within the extended range of Lane Departure – ELK Road Edge, it is possible that both ELK and LDW could be assessed simultaneously (per the conditions detailed in 5.2.2.2 Lane Departure Warning). Therefore, the test lab shall record the timing of the Lane Departure Warning (e.g. notable heading correction, steering wheel vibration, etc.) during tests conducted for the extended range of Lane Departure – ELK Road Edge. 

# Car & PTW

<table><tr><td>CAR &amp; PTW</td><td>Standard</td><td>Extended</td><td>Robustness</td><td>TOTAL</td></tr><tr><td>ELK Car-to-car</td><td>4</td><td>0.5</td><td>0.5</td><td>5</td></tr><tr><td>Oncoming</td><td>2</td><td>0.25</td><td>0.25</td><td>2.5</td></tr><tr><td>Overtaking Intentional*</td><td>1</td><td>0.125*</td><td>0.125</td><td>1.25</td></tr><tr><td>Overtaking Unintentional*</td><td>1</td><td>0.125*</td><td>0.125</td><td>1.25</td></tr><tr><td>ELK Car-to-motorcyclist</td><td>4</td><td>0.5</td><td>0.5</td><td>5</td></tr><tr><td>Oncoming</td><td>2</td><td>0.25</td><td>0.25</td><td>2.5</td></tr><tr><td>Overtaking Intentional*</td><td>1</td><td>0.125*</td><td>0.125</td><td>1.25</td></tr><tr><td>Overtaking Unintentional*</td><td>1</td><td>0.125*</td><td>0.125</td><td>1.25</td></tr></table>


* Half points awarded with BSM in Extended Range cases 


# 3.2.1 ELK Car-to-Car Oncoming

The standard and extended test ranges for ELK Car-to-Car Oncoming are shown below: 

<table><tr><td>ELK-ON</td><td>Target</td><td>0.3 m/s</td><td>0.4 m/s</td><td>0.5 m/s</td><td>0.6 m/s</td></tr><tr><td>50 km/h</td><td>50 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>60 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>80 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>90 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td>100 km/h</td><td></td><td></td><td></td><td></td></tr></table>

For the oncoming scenario, the GVT will follow a straight-line path in the lane adjacent to the VUT’s initi l position, in the opposite di ection to the VUT. The st ight-line path of the target will be 1.5m from the inner side of the centre dashed lane marking of the VUT lane. 

The following test track and lane marking format is applied to the standard and extended test ranges. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/36df56c4b2ce79679bf64ae4650af1ba069337122b38ce2523bf330c8586d286.jpg)



Figure 3-3 ELK Car-to-Car Oncoming test format


Euro NCAP 

Version 1.1 — October 2025 

The paths of the VUT and target vehicle will be synchronised so that the reference point of the GVT meet with the VUT at a $90 \%$ impact location (assuming no system reaction). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/b18a811de097984029369f2503916a1475bdc3da148f13a4c8fd6b3101ebcdfd.jpg)



Figure 3-4 Standard Range Impact Location for ELK Car-to-Car Oncoming


# 3.2.2 ELK Car-to-Car Overtaking

The Standard Range ELK Car-To-Car Overtaking tests will be performed with $0 . 1 \mathsf { m } / \mathsf { s }$ incremental steps within the lateral velocity range of 0.3 to $0 . 6 \mathsf { m } / \mathsf { s }$ for unintentional lane changes, and 0.5 to $0 . 7 \mathsf { m } / \mathsf { s }$ for intentional lane changes. 

The standard and extended test ranges for ELK Car-to-Car Overtaking are shown below: 

<table><tr><td>ELK-OV
(Unintentional)</td><td>Target</td><td>0.2 m/s</td><td>0.3 m/s</td><td>0.4 m/s</td><td>0.5 m/s</td><td>0.6 m/s</td><td>0.7 m/s</td></tr><tr><td>50 km/h</td><td>60 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>80 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>90 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>100 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td>110 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>110 km/h</td><td>120 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>120 km/h</td><td>130 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>130 km/h</td><td>140 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>ELK-OV (Intentional)</td><td>Target</td><td>0.4 m/s</td><td>0.5 m/s</td><td>0.6 m/s</td><td>0.7 m/s</td><td>0.8 m/s</td></tr><tr><td>50 km/h</td><td>60 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>80 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>90 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>100 km/h</td><td></td><td></td><td></td><td></td><td></td></tr></table>

For the overtaking scenario a GVT will follow a straight-line p th in the l ne dj cent to the VUT’s initial position at the driver side, in the same direction as the VUT. The straight-line path of the target will be 1.5m from the inner side of the centre dashed lane marking of the VUT lane. 

Euro NCAP 

Version 1.1 — October 2025 

The following test track and lane marking format is applied to the standard and extended test ranges. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/9aa820aa8b8091e482d7d85c48a2a5f137c19b101fde1874753c39491188d294.jpg)



Figure 3-5 ELK Car-to-Car Overtaking test format


The paths of the VUT and target vehicle will be synchronised so that the longitudinal position of the leading edge of the target vehicle impacts $2 5 \%$ of the length of the VUT (assuming no system reaction). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/d2255ba0f8591eb7cd8eee08f93574d88a5f57762fa014a9ec1447b6d1c8c59a.jpg)



Figure 3-6 Standard Range Impact Location for ELK Car-to-Car Overtaking


Lane departures will be performed toward the driver side only, and intentional lane change manoeuvres will be conducted with the turn indicator ON, applied $1 . 0 \pm 0 . 5$ sec before Tsteer. 

# 3.2.3 ELK Car-to-Motorcyclist Oncoming

The standard and extended test ranges for ELK Car-to-Motorcyclist Oncoming are shown below: 

<table><tr><td>ELK-ON</td><td>Target</td><td>0.3 m/s</td><td>0.4 m/s</td><td>0.5 m/s</td><td>0.6 m/s</td></tr><tr><td>50 km/h</td><td>50 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>60 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>80 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>90 km/h</td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td>100 km/h</td><td></td><td></td><td></td><td></td></tr></table>

Euro NCAP 

Version 1.1 — October 2025 

For the oncoming scenario the EMT will follow a straight-line path at 70 km/h in the lane adjacent to the VUT’s initi l position, in the opposite di ection to the VUT who lso d ives t $7 0 \mathrm { ~ k m / h ~ }$ . The straight-line path of the target will be 1m from the inner side of the centre dashed lane marking of the VUT lane. 

The following test track and lane marking format is applied to the standard and extended test ranges. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/0d0145d6c0797e52b19cfe81667d6737d4dfaf037e3c9a5178edb48176458173.jpg)



Figure 3-7 ELK Car-to-Motorcyclist Oncoming test format


The paths of the VUT and EMT will be synchronised so that the front wheel of the EMT impacts the VUT at a $1 1 0 \%$ impact location (assuming no system reaction). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/03ede84bd0e5fbce07fc102a9831dbd288da97200b7172957343aedf5543722e.jpg)



Figure 3-8 Standard Range impact location for ELK Car-to-Motorcyclist Oncoming


# 3.2.4 ELK Car-to-Motorcyclist Overtaking

The Standard Range ELK Car-To-Motorcyclist Overtaking tests will be performed with $0 . 1 \mathsf { m } / \mathsf { s }$ incremental steps within the lateral velocity range of 0.3 to $0 . 6 \mathsf { m } / \mathsf { s }$ for unintentional lane changes, and 0.5 to $0 . 7 \mathsf { m } / \mathsf { s }$ for intentional lane changes. 

The standard and extended test ranges for ELK Car-to-Motorcyclist Overtaking are shown below: 

<table><tr><td>ELK-OV
(Unintentional)</td><td>Target</td><td>0.2 m/s</td><td>0.3 m/s</td><td>0.4 m/s</td><td>0.5 m/s</td><td>0.6 m/s</td><td>0.7 m/s</td></tr><tr><td>50 km/h</td><td>60 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>80 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>90 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>100 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100 km/h</td><td>110 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>110 km/h</td><td>120 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>120 km/h</td><td>130 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>130 km/h</td><td>140 km/h</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>ELK-OV
(Intentional)</td><td>Target</td><td>0.4 m/s</td><td>0.5 m/s</td><td>0.6 m/s</td><td>0.7 m/s</td><td>0.8 m/s</td></tr><tr><td>50 km/h</td><td>60 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>60 km/h</td><td>70 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>70 km/h</td><td>80 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>80 km/h</td><td>90 km/h</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>90 km/h</td><td>100 km/h</td><td></td><td></td><td></td><td></td><td></td></tr></table>

For the overtaking scenario, an EMT will follow a straight-line path in the lane adjacent to the VUT’s initi l position t the d ive side in the s me di ection s the VUT. The straight-line path of the target will be 1m from the inner side of the centre dashed lane marking of the VUT line. 

The following test track and lane marking format is applied to the standard and extended test ranges. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/4ee022d8cfc88af6d0385fa8af04125109d0fe1aa95e9afed51af4c4d74b9ab6.jpg)



Figure 3-9 ELK Car-to-Motorcyclist Overtaking test format


The paths of the VUT and EMT will be synchronised so that the front wheel of the EMT impacts the $2 5 \%$ of the length of the VUT (assuming no system reaction). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/76b731074d7dafd29569c94764433a3aa94f555b7259a486f939db6209ad5ff0.jpg)



Figure 3-10 Standard Range impact location for ELK Car-to-Motorcyclist Overtaking


# 3.2.4.1 Blind Spot Monitoring

Where the test vehicle is unable to meet the assessment criteria for the ELK Overtaking (Car and / or Motorcyclist) extended range scenarios, conduct assessment of the blind spot monitoring system, consisting of on-road functionality verification that motorcyclists and cars in both adjacent lanes are detected at the applicable longitudinal speeds of the Extended Range. 

# 4 TEST EXECUTION

# Performance Predictions

The Vehicle Manufacturer shall provide the Euro NCAP with PASS/FAIL data detailing the predicted performance of the LSS for all test scenarios, and in accordance with the assessment criteria outlined in chapter 5.2. The predicted performance will be used as a reference to identify discrepancies between the predicted results and the test results. 

The predicted performance will be used as a reference to verify performance using randomly selected verification tests. Performance predictions may be provided in either of the following formats: 

<table><tr><td colspan="2">Performance predictions</td><td>Virtual Testing</td><td>Self-claimed</td><td>Field Data</td></tr><tr><td colspan="2">Standard Range</td><td>✓</td><td>✓</td><td></td></tr><tr><td colspan="2">Extended Range</td><td>✓</td><td>✓</td><td></td></tr><tr><td rowspan="2">Robustness Layers</td><td>Decision &amp; Control</td><td>✓</td><td>✓</td><td></td></tr><tr><td>Perception</td><td></td><td></td><td>✓</td></tr></table>

The information shall be supplied by the manufacturer before any testing begins, preferably with delivery of the test vehicle(s). 

In case a Vehicle Manufacturer does not supply any prediction data, the test laboratory shall conduct a testing approach defined by the Euro NCAP Secretariat. 

# 4. 1. 1 Vi rt u a l T e st i n g

Virtual Testing refers to as simulation-based performance predictions, following the provisions outlined in Euro NCAP VTA Protocol. 

# 4.1.2 Self- claimed

Self-claimed refers to as PASS/FAIL data provided by the Vehicle Manufacturer where no further evidence is required. For the following cases where Self-claimed performance is declared, the Vehicle Manufacturer shall provide the Euro NCAP Secretariat with supporting evidence in the form of simulation and/or in-house track test data: 

ELK Car-to-Motorcyclist Oncoming & Overtaking tests with EMT speed >80 km/h 

- Lane Departure Road Edge tests with VUT speed >80 km/h 

# 4.1.3 Field Data

Where Field Data is required, the Vehicle Manufacturer shall demonstrate function availability and/or specific performance under the presence of perception-related robustness layers, by means of insights gathered in real-world driving conditions. This is to be reported according to the provisions set forth in the Technical Bulletin CA 003. 

# Verification tests

The verification tests are randomly selected grid cells, distributed in line with the Vehicle Manufacturer prediction (excluding grid cells where there is no performance), and covering Standard Range, Extended Range and Robustness Layers. 

For each scenario, the following random selection of Verification Tests is made by Euro NCAP and executed by the test laboratory: 

# 4.2.1 Standard and Extended Range

For Standard Range, a random selection of 3 verification tests is completed per scenario. For Extended Range, a random selection of 2 verification tests is completed per scenario. 

<table><tr><td rowspan="2">Single Vehicle</td><td rowspan="2">Scenario Type</td><td rowspan="2">Scenario</td><td colspan="2">Verification tests</td></tr><tr><td>Standard Range</td><td>Extended Range</td></tr><tr><td>Lane Departure</td><td>ELK Road Edge</td><td>ELK-RE</td><td>3</td><td>2</td></tr></table>

<table><tr><td rowspan="2">Car &amp; PTW</td><td rowspan="2">Scenario Type</td><td rowspan="2">Scenario</td><td colspan="2">Verification tests</td></tr><tr><td>Standard Range</td><td>Extended Range</td></tr><tr><td rowspan="3">ELK Car-to-Car</td><td>Oncoming</td><td>ELK-ON</td><td>3</td><td>2</td></tr><tr><td rowspan="2">Overtaking</td><td>ELK-OVUnintentional</td><td>3</td><td>2</td></tr><tr><td>ELK-OVIntentional</td><td>3</td><td>2</td></tr><tr><td rowspan="3">ELK Car-to-Motorcyclist</td><td>Oncoming</td><td>ELK-ON</td><td>3</td><td>2</td></tr><tr><td rowspan="2">Overtaking</td><td>ELK-OVUnintentional</td><td>3</td><td>2</td></tr><tr><td>ELK-OVIntentional</td><td>3</td><td>2</td></tr></table>

# 4.2.2 Robustness Layers

For the Robustness Layers (Decision & Control): 1 layer is randomly selected per scenario (see applicability in APPENDIX B. 

For the Standard Range only, the verification tests for ELK Car-to-Car and ELK Car-to-Motorcycle will be performed under the presence of a randomly selected Robustness Layer where performance was predicted. 

Where any verification test with the Robustness Layer applied results in a fail, the selected robustness layer will be failed for that scenario. The test will then be repeated without the layer present. 

Further verification tests in the Standard Range of that scenario will be conducted without the layer present. 

Where a specific Robustness Layer fails in two scenarios of the same collision partner (i.e., car, PTW), that layer will be failed for all scenarios of the same collision partner. 

# Test Conduct

# 4.3.1 VUT Pre-test Conditioning

A new car is used as delivered to the test laboratory; however, a car may have been used for other Euro NCAP active safety tests. 

If requested by the vehicle manufacturer and where not already performed for other tests, drive a maximum of 100km on a mixture of urban and rural roads with other traffic and roadside fu nitu e to ‘c lib te’ the senso system. Avoid h sh ccele tion nd braking. 

# 4.3.1.1 Tyres

ondition the vehicle’s ty es in the following m nne to emove the mould sheen, if this h s not been done before for another test or in case the lab has not performed a 100km of driving: 

Drive around a circle of $_ { 3 0 \mathsf { m } }$ in diameter at a speed sufficient to generate a lateral acceleration of approximately 0.5 to 0.6g for three clockwise laps followed by three anticlockwise laps. 

Immediately following the circular driving, drive four passes at 56km/h, performing ten cycles of a sinusoidal steering input in each pass at a frequency of 1Hz and amplitude sufficient to generate a peak lateral acceleration of approximately 0.5 to 0.6g. 

Make the steering wheel amplitude of the final cycle of the final pass double that of the previous inputs. 

In case of instability in the sinusoidal driving, reduce the amplitude of the steering input to an appropriately safe level and continue the four passes. 

# 4.3.1.2 System Check

Before any testing begins, perform a maximum of ten runs, to ensure proper functioning of the system. 

# 4.3.2 Test Scenarios

Control the VUT with driver inputs or using alternative speed control systems, such as cruise control or speed limiter, that can modulate the vehicle controls as necessary to perform the tests. 

Accelerate the VUT to the targeted speed. 

The test shall start at ${ \sf T } _ { 0 }$ and is valid when all boundary conditions are met between ${ \sf T } _ { 0 }$ and TELK/TLKA/TLDW: 

<table><tr><td>Parameter</td><td>Condition</td><td>VUT</td><td>GVT</td><td>EMT</td></tr><tr><td>Speed</td><td></td><td colspan="3">± 1.0 km/h</td></tr><tr><td>Relative longitudinal speed</td><td>Overtaking</td><td colspan="3">± 1.0 km/h</td></tr><tr><td>Relative longitudinal distance</td><td>Overtaking</td><td colspan="3">± [0.20]m</td></tr><tr><td rowspan="2">Lateral deviation</td><td>Oncoming</td><td>0 ± 0.05 m</td><td>0 ± 0.30m</td><td>0 ± [0.15] m</td></tr><tr><td>Overtaking</td><td>0 ± 0.05 m</td><td>0 ± 0.20m</td><td>-</td></tr><tr><td>Steady state lane departure lateral velocity</td><td></td><td>± 0.05m/s</td><td>-</td><td>-</td></tr><tr><td>Yaw velocity</td><td rowspan="3">Up to TSTEER for VUT</td><td>0 ± 1.0 °/s</td><td>-</td><td>-</td></tr><tr><td>Yaw angle</td><td>-</td><td>-</td><td>0 ± 1.5 °</td></tr><tr><td>Steering wheel velocity</td><td>0 ± 15.0 °/s</td><td>-</td><td>-</td></tr></table>

Steer the vehicle as appropriate to achieve the lateral velocity in a smooth controlled manner and with minimal overshoot. 

The end of a test is considered as: 

LDW tests: when the warning commences. 

BSM tests: when the longitudinal distance between the VUT and test target is 0m (i.e. when the front end of the VUT is aligned with the rear end of the test target). 

LKA/ELK Road Edge tests: 2 seconds after one of the following occurs: 

o The LKA/ELK system fails to maintain the VUT within the permitted lane departure distance. 

o The LKA/ELK system intervenes to maintain the VUT within permitted lane departure distance, such that a maximum lateral position is achieved that subsequently diminishes causing the VUT to turn back towards the lane. 

ELK oncoming or overtaking tests: when one of the following occurs: 

o The ELK system intervenes to prevent a collision between the VUT and target vehicle 

o The ELK system has failed to intervene (sufficiently) to prevent a collision between the VUT and target vehicle. This can be assumed when one of the following occurs: 

The lateral separation between the VUT and target vehicle equal $< 0 . 3 \mathsf { m }$ in the oncoming and overtaking scenario 

▪ No intervention is observed at a TTC $= 0 . 8 { \sf s }$ or a TTC submitted by the OEM 

It is at the labs discretion to select and use one of the options above to ensure a safe testing environment. If the test ends because the vehicle has failed to intervene (sufficiently) or if the EMT h s left it’s design ted p th by mo e th n $0 . 2 \mathsf { m }$ , it is ecommended th t the VUT nd/o EMT are steered away from the impact, either manually or by reactivating the steering control of the driving robot/EMT. 

# 4.3.2.1 Calibration runs

The vehicle manufacturer shall provide information describing the location when the closed loop path and/or speed control shall be ended so as not to interfere with the system intervention for each test. The test laboratory shall then verify the release point for the highest lateral velocity. 

Otherwise, when the vehicle manufacturer does not provide information, two calibration runs shall be performed for each lateral velocity to determine when the system activates. Compare steering wheel torque, vehicle speed or yaw rate of both runs and determine where there is a notable difference that identifies the location of intervention. 

Run 1: Complete the required test path with the system turned OFF and measure the control parameter 

Run 2: Complete the required test path with the system turned ON and measure the control parameter 

Complete the tests while ending the closed loop control before system activation (as defined above). In the case of calibration runs, the release of steering control should occur on the test path and no less than 5m longitudinally before the location of intervention. 

If the intervention point of the function occurs before the target VlatVUT is reached, the test laboratory will conduct a verification check of the $\mathsf { V } _ { \mathsf { I a t V U T } } { = } 0 . 6 \mathsf { m } / \mathsf { s }$ test case (both for dashed and solid line) using a straight-line vehicle path intersecting with a curved lane marking. The intersecting angle of the VUT test path and the curved lane marking shall be equal to the yaw ngle $( \Psi _ { \mathsf { V U T } } )$ achieved by the $0 . 6 \mathsf { m } / \mathsf { s }$ test conducted in the standard test format (ie. straight lane marking tests). 

A maximum of 3 runs shall be conducted (both for solid and dashed line), where the system intervention and resulting DTLE is monitored. 

When the closed loop path ends, the driver's hands, or the control, will remain passive on the steering wheel without applying deliberate force but reflecting the behaviour of an inattentive driver holding the steering wheel. 

# 4.3.2.2 Test parameters

The following figure details the parameters used to create the test paths: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/16ede1be413009bba63c7c6e3ffc19c7d99c697750bd2be29f034eb8b1dd2ff2.jpg)



Figure 4-1: Vehicle paths definition


For the full definition of e ch scen io’s test paths, see APPENDIX A. 

Euro NCAP 

Version 1.1 — October 2025 

# 5 ASSESSMENT

Each scenario in this assessment (except for Driver Acceptance) consists of a matrix combining vehicle & target longitudinal speeds, and ranges of vehicle lateral speeds. Each combination in a matrix is referred to as grid cell. The grid cells forming a test scenario matrix are grouped into two groups: 1) Standard range and 2) Extended range. 

# 5.1 General requirements

# 5.1.1 Driver Acceptance

The requirements specified for Driver Acceptance – Driveability are applicable for the whole operational speeds of the vehicle’s lane support system. Euro NCAP will monitor the performance of these metrics throughout all testing performed within the Standard Range longitudinal speeds; and may also conduct spot checking to verify performance at speeds beyond the standard and extended ranges defined for each scenario. 

The assessment of Driver Acceptance metrics will remain within the test speeds defined; however, it is expected that vehicle responses and the intent to ensure Driver Acceptance will be consistent outside of the protocol test envelope. 

To be eligible for scoring points in Driver State Link, the system shall meet the requirements of Driveability. 

# 5.1.2 Lane Departure

To be eligible for scoring points in Lane Departure, the ELK function of the LSS system needs to be default ON at the start of every journey and deactivation of the system should not be possible with a momentary single push on a button. 

For any system, the driver must be able to override the intervention by the system. 

# 5.2 Criteria

# 5.2.1 Single vehicle

# 5.2.1.1 Driver Acceptance

A maximum of 5 points are available for Driver Acceptance: 2 points for Driveability and 3 points for Driver State Link. 

# 5 . 2 . 1 . 2 D r i v e a b i l i t y

The LSS system shall meet a minimum of 3 conditions, outlined below, to be awarded points for Driveability: 

1. Overriding Torque – the torque applied by the steering robot to maintain the steering wheel angle must not exceed $3 . 0 \mathsf { N m } + [ 0 . 5 \mathsf { N m } ]$ while the lane support system is active. 

2. Continuous Intervention – vehicle’s l ne suppo t system must not ttempt to inte vene over the driver intent for a duration longer than 1.0 second once parallel to a line marking. 

This applies to Lane Departure – Road Edge, Solid Line, LKA Dashed within any speed of Standard Range. 

3. Steering Response – for tests ≥70km/h; if the lane support system requires a steering wheel angle change $\mathtt { \ge 5 }$ degrees to redirect the vehicle path, the vehicle response must not exceed the steering wheel velocity limits defined in the table below. 

<table><tr><td>Lateral Speed</td><td>0.2m/s</td><td>0.3m/s</td><td>0.4m/s</td><td>0.5m/s</td><td>0.6m/s</td></tr><tr><td>Steering wheel velocity</td><td>± 20°/sec</td><td>± 25°/sec</td><td>± 30°/sec</td><td>± 35°/sec</td><td>± 40°/sec</td></tr></table>

Steering wheel angle change will be measured from the steering angle at the beginning of a lane support system response, to the maximum steering angle experienced during the intervention. 

The Steering wheel velocity limit is applied for the duration of the vehicle’s response. 

Vehicle’s th t utilise diffe enti l b king systems do not use controlled steering inputs to edi ect vehicle’s path; and are not compatible with this assessment. Differential braking systems, therefore, become ineligible for the overall assessment of Driveability. 

4. Returning $\forall _ { \mathsf { I a t } }$ : Measurement of the returning $\mathsf { V } _ { \mathsf { l a t } }$ will be taken two seconds after the minimum DTLE, where the following criteria shall apply: 

o For tests with approaching $\mathsf { V } _ { \mathsf { l a t } }$ ${ > } 0 . 3 ~ \mathsf { m } / \mathsf { s }$ , the lane support system shall redirect the VUT such that the correction results in a returning lateral velocity less than or equal to the departing $\mathsf { V } _ { \mathsf { l a t } }$ measured for that test. 

o For tests with approaching $\mathsf { V } _ { \mathsf { l a t } }$ ${ \le } 0 . 3 \mathsf { m } / \mathsf { s }$ , the etu ning $\mathsf { V } _ { \mathsf { l a t } }$ sh ll be ${ \leq } 0 . 3 ~ \mathsf { m } / \mathsf { s }$ . 

If a vehicle does not meet the criteria outlined in 5.2.1.2 Driveability, the vehicle manufacturer can appeal to the secretariat with justification that the lane support system design avoids undesirable characteristics and will be acceptable to drivers. 

Based on this justification, the driveability assessment may be overruled by the Euro NCAP secretariat. 

# 5.2.1.3 Driver State Link

Vehicle manufacturers are encouraged to consider the balance between providing safety and consumer acceptance when implementing a driver state link to the collision avoidance systems available on a vehicle. 

To be able to score points in Driver State Link, the following conditions shall be met: 

Lane Support sensitivity changes shall ensure LKA and LDW availability when the driver state is unknown or classified as inattentive. 

Lane Support sensitivity or steering overriding torque can be reduced, or the vehicle can implement an intervention suppression strategy when the driver is classified as attentive (eyes on road) and not impaired. The strategy shall be described by the Vehicle Manufacturer to Euro NCAP. 

The DSM shall offer minimum Intervention score in Lane Support Sensitivity across different driver states, as described in the Euro NCAP Driver Engagement Protocol: 

o Transient states: $50 \%$ of total intervention score in Lane Support Sensitivity 

Euro NCAP 

o Non-transient states: Intervention score in Lane Support Sensitivity for Drowsiness and Sleep* 

The sensitivity change shall be set back to the nominal setting $< 1$ second after the DSM detects its performance is degraded, or the system is non-functional or turned off. 

* Sleep only applicable for systems with Lane Support Sensitivity as intervention type 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-09/d5b479a5-5745-4b6f-ace6-5cbbf149c3d4/8ec8a36957d4c84d87bd92c47bf5e0a580d38b9daaa748d97ca875d69bb88f25.jpg)


1 For a Degraded DSM System (e.g., when eye gaze determination is not possible and driver attentiveness is estimated only via head pose), Reduced LSS Sensitivity may continue enabled by a standalone (indirect) DIM, provided that the driver is informed of a Degraded DSM System as if the system is “Non-functional”. 

2 For any continuous off-road glance shorter in duration than Transient Driver State, Nominal LSS Sensitivity shall be effective soon enough to ensure Lane Departure performance3. 

3 Lane Departure performance $=$ 2023 LSS performance criteria. For systems separating ELK and ELK+LKA mode, in the ELK mode the LKA dashed line intervention does not need to be re-activated for degraded or unknown DSM 

The Vehicle Manufacturer may implement specific Lane Support sensitivity / performance changes according to the following conditions: 

Intentional steering inputs: e.g., the vehicle recognises continuous steering inputs and control of the vehicle, in which the driver’s level of engagement and driving intent can be inferred. 

Gaze monitoring: specific L ne Suppo t Sensitivity depend nt on the d ive ’s g ze direction, e.g.: 

o Gaze towards central, downward regions: Forward Support Sensitivity change for a vehicle drifting to either left or right side lane boundaries (e.g., in-vehicle infotainment system) 

o Gaze toward right regions: Lane Support Sensitivity change for a vehicle drifting to left-side lane boundaries (e.g., passenger side mirror) 

o Gaze toward left regions: Lane Support Sensitivity change for a vehicle drifting to right-side lane boundaries (e.g., d ive ’s window) 

The use of a turn signal while the vehicle has determined a Transient, Non-Transient or Unknown state can assume driver intent and suppress the lane support system. 

To avoid any unintentional override of the LSS response; if the vehicle determines that the driver is in a higher-risk state (i.e. sleep), the vehicle manufacturer can implement an increase system sensitivity and overriding torque via the Driver State Link. 

# 5.2.2 Lane Departure

# 5.2.2.1 Road edge

The limit value for DTLE in Lane Departure – ELK Road Edge tests is set to -0.1m, meaning that the vehicle is only allowed to have a part of the front wheel outside of the road edge. 

# 5.2.2.2 Lane Departure Warning

Where the test vehicle is unable to meet the assessment and performance criteria for the extended range of Lane Departure – Road Edge tests, the vehicle becomes eligible for the assessment of the Lane Departure Warning. 

Any LDW system that issues a haptic warning clearly relating to the lateral control of the vehicle noticeable by the driver (e.g. notable heading correction, steering wheel vibration, etc.) before a DTLE of -0.1m is awarded when active at lateral velocities up to at least $0 . 7 \mathsf { m } / \mathsf { s }$ . 

# 5.2.3 Car & PTW

# 5.2.3.1 ELK Oncoming & Overtaking

For all ELK Car-to-Car & Car-to-Motorcyclist Oncoming and Overtaking tests with an oncoming or overtaking vehicle, the assessment criteria used is “no impact”, meaning that the VUT is not allowed to contact* the overtaking or oncoming vehicle target at any time during the test. 

* For the motorcyclist test scenarios, the lateral separation between the VUT and the Oncoming or Overtaking EMT must be $> 0 . 3 m$ . 

# 5.2.3.2 Blind Spot Monitoring

Where the test vehicle is unable to meet the assessment and performance criteria for the extended range of ELK Overtaking (Car and Motorcyclist) tests, the test vehicle becomes eligible for the assessment of the blind spot monitoring system. 

For the blind spot monitoring tests, the assessment criteria used is the visual blind spot information that shall be supplied in respect to vehicles in the blind spot of the VUT. 

# 5.2.4 Robustness

To evaluate the overall robustness of the system, the Standard Range of each scenario (where there is performance) is assessed against individual parameter or condition variations referred to as layers, clustered in 3 types: VUT, Target and Environment. 

<table><tr><td colspan="2">Robustness layers</td><td rowspan="2">Description</td><td rowspan="2">Verification Test</td><td rowspan="2">Input source</td></tr><tr><td>Type</td><td>Layer</td></tr><tr><td>VUT</td><td>Impact location</td><td>System performance under different projected impact location</td><td>Yes</td><td rowspan="2">Virtual Testing or Self-Claim</td></tr><tr><td rowspan="3">Target (Collision Partner)</td><td>Initial position offset</td><td>System performance under a small variance in the nominal target initial position</td><td>Yes</td></tr><tr><td>Type</td><td>System ability to detect different collision partner types with similar kinematics</td><td>No</td><td rowspan="6">Field Data**</td></tr><tr><td>Appearance</td><td>System ability to detect same collision partner type but with different appearance (e.g., colour, shape)</td><td>No</td></tr><tr><td>Target (Lane Boundary)</td><td>Appearance</td><td>System performance against diverse lane boundaries, e.g., road edge, lane lines of different colour/width/type/radius</td><td>No*</td></tr><tr><td rowspan="3">Environment</td><td>Adverse weather conditions</td><td>Functionality available under the presence of rain, fog, dirt, dust, ice, moisture</td><td>No</td></tr><tr><td>Illumination (Night time)</td><td>System ability to operate in darkness (1 lux)</td><td>No*</td></tr><tr><td>Illumination (Sun glare)</td><td>Functionality available under the presence of glare caused by low sun (all scenarios)</td><td>No</td></tr></table>


* May be tested under request of Euro NCAP Secretariat. 



** Where FOT data is required, the Vehicle Manufacturer shall demonstrate that the system perception is not significantly degraded, assessed in real driving conditions. This is to be reported according to the provisions set forth in Technical Bulletin CA 003. 


# 5.2.4.1 Verification Tests

Where verification tests are done, the following conditions apply: 

<table><tr><td colspan="2">Robustness</td><td rowspan="2">Scenarios</td><td rowspan="2">Test condition*</td><td rowspan="2">Assessment Criteria</td></tr><tr><td>Type</td><td>Layer</td></tr><tr><td>VUT</td><td>Impact location**</td><td rowspan="2">Car &amp; PTW</td><td>Range change: 
- Oncoming: ±10% 
- Overtaking: +50%</td><td>Same</td></tr><tr><td rowspan="2">Target</td><td>Initial position Offset**</td><td>Range change: 
- Path offset: ±0.25m</td><td>Same</td></tr><tr><td>Appearance</td><td rowspan="2">Single vehicle</td><td>Lane marking type, colour, width (verification during on-road test)</td><td>Same</td></tr><tr><td>Environ-ment</td><td>Illumination (Night time)</td><td>Performance in darkness (1 lux) 
Applicable for Road Edge only – with high beams</td><td>Same</td></tr></table>


* Versus the condition used in the Standard Range. 



** Parameter combinations shall ensure a TTC ≤ 3s (see Chapter 2 in Technical Bulletin CA 002) 


# 5.3 Scoring

# 5.3.1 Standard Ranges

For score calculation in the Standard Range of each scenario, first each grid cell is given a subscore according to the Vehicle Manufacturer prediction: 

Car & PTW 

o PASS (Avoidance) = 1 point 

o FAIL (Impact) $= 0$ points 

Single Vehicle 

o Vlat from 0.2 to $0 . 6 \mathsf { m } / \mathsf { s }$ 

▪ ELK $( \mathsf { P A S S } ) = 1$ point 

▪ ELK (FAIL) = 0 points 

Secondly, the resulting score is calculated by normalizing all the Standard Range sub-scores to the total score of the Standard Range in that scenario (rounded to hundredth): 

$$
S c o r e S t a n d a r d R a n g e = \frac {\sum S u b s c o r e s i n S t a n d a r d R a n g e \times T o t a l S t a n d a r d R a n g e S c o r e}{N u m b e r o f G r i d C e l l s i n S t a n d a r d R a n g e}
$$

# 5.3.2 Extended Ranges

To be eligible for scoring points in the extended ranges across scenarios, $\geq 2 5 \%$ of the total available score is required to have been awarded for the standard test range. 

Euro NCAP 

Version 1.1 — October 2025 

For score calculation in the Extended Range of each scenario, first each grid cell is given a subscore according to the Vehicle Manufacturer prediction: 

# Car & PTW

o PASS (Avoidance) $= 1$ point 

o $\mathsf { B S M } ^ { \star } = 0 . 5$ points 

o FAIL (Impact) $= 0$ points 

# Single Vehicle

o $\mathsf { V } _ { \mathsf { l a t } }$ from 0.2 to $0 . 7 \mathsf { m } / \mathsf { s }$ 

▪ ELK (PASS) = 1 point 

▪ LDW $( \mathsf { P A S S } ) = 0 . 5$ points 

▪ LDW and ELK (FAIL) = 0 points 

# * For overtaking scenarios

Secondly, the resulting score is calculated by normalizing all the Extended Range sub-scores to the total score of the Extended Range in that scenario(rounded to hundredth): 

$$
\text {S c o r e E x t e n d e d R a n g e} = \frac {\sum \text {S u b s c o r e s i n E x t e n d e d R a n g e} \times \text {T o t a l E x t e n d e d R a n g e S c o r e}}{\text {N u m b e r o f G r i d C e l l s i n E x t e n d e d R a n g e}}
$$

The final score for each Extended Range in a given scenario is calculated as follows: 

<table><tr><td colspan="2">Extended Range Scoring</td></tr><tr><td>% of total score</td><td>Final score</td></tr><tr><td>50 ≤ Score Extended Range &lt; 75</td><td>50%</td></tr><tr><td>75 ≤ Score Extended Range &lt; 100</td><td>75%</td></tr><tr><td>Score Extended Range = 100</td><td>100%</td></tr></table>

# 5.3.3 Robustness

To be eligible for scoring points in Robustness Layers in a specific scenario, the e sh ll be $\ge 5 0 \%$ of the total available score in the Standard Range of that scenario. 

The score for each Robustness Layer in each scenario where the manufacturer predicted performance according to 5.2.4 is calculated as follows: 

$$
\text {S c o r e R o b u s t n e s s L a y e r s} = \frac {\text {T o t a l R o b u s t n e s s S c o r e}}{\text {N u m b e r o f a p p l i c a b l e R o b u s t n e s s L a y e r s}}
$$

An overview of the applicable Robustness Layers in each scenario can be found in APPENDIX B 

# 5.3.4 Verification tests

The outcome of the verification tests will dictate the final score of a given scenario, and will depend on how the predicted performance is reported by the Vehicle Manufacturer, as illustrated in the table below: 

# Euro NCAP

Version 1.1 — October 2025 

<table><tr><td rowspan="4"># of tests→Passed* tests↓</td><td colspan="4">Score % from verification tests outcome</td></tr><tr><td colspan="2">Standard Range</td><td colspan="2">Extended Range</td></tr><tr><td>Virtual TestingPredictions</td><td>Self-claimPredictions</td><td>Virtual TestingPredictions</td><td>Self ClaimPredictions</td></tr><tr><td>3</td><td>3</td><td>2</td><td>2</td></tr><tr><td>3</td><td>100%</td><td>100%</td><td>-</td><td>-</td></tr><tr><td>2</td><td>67%</td><td>67%</td><td>100%</td><td>100%</td></tr><tr><td>1</td><td>33%</td><td>0%</td><td>50%</td><td>0%</td></tr><tr><td>0</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr></table>


* Passed $=$ in line or beyond the predicted performance 


If a verification test applied in a scenario where performance was predicted by Virtual Testing does not meet the acceptance criteria set forth in the VTA protocol, all scenarios in that cluster will be treated as Self claim for scoring. 

# APPENDIX A LANE DEPARTURE PATHS

# A.1 Paths for Road Edge, ELK Oncoming and ELK Overtaking

Intended for use in all tests: 

<table><tr><td colspan="2"></td><td colspan="9">D1
(depending on lateral and longitudinal speed)</td></tr><tr><td>Vehicle Speed</td><td>Unintentional
Lateral acceleration
R=600 for V&lt;70 km/h
R=1200 for 70&gt;=V&lt;100
R=2400 for 100&gt;=V&gt;=130
R=4800 for V&gt;130</td><td>0.2m/s</td><td>0.3m/s</td><td>0.4m/s</td><td>0.5m/s</td><td>0.6m/s</td><td>0.7m/s</td><td>0.8m/s</td><td>0.9m/s</td><td>1.0m/s</td></tr><tr><td>50</td><td>0.322</td><td>0.062</td><td>0.140</td><td>0.249</td><td>0.389</td><td>0.560</td><td>0.763</td><td>0.996</td><td>1.261</td><td>1.557</td></tr><tr><td>60</td><td>0.463</td><td>0.043</td><td>0.097</td><td>0.173</td><td>0.270</td><td>0.389</td><td>0.529</td><td>0.692</td><td>0.875</td><td>1.081</td></tr><tr><td>70</td><td>0.315</td><td>0.063</td><td>0.143</td><td>0.254</td><td>0.397</td><td>0.571</td><td>0.778</td><td>1.016</td><td>1.286</td><td>1.588</td></tr><tr><td>72</td><td>0.333</td><td>0.060</td><td>0.135</td><td>0.240</td><td>0.375</td><td>0.540</td><td>0.735</td><td>0.960</td><td>1.216</td><td>1.501</td></tr><tr><td>80</td><td>0.412</td><td>0.049</td><td>0.109</td><td>0.194</td><td>0.304</td><td>0.437</td><td>0.595</td><td>0.778</td><td>0.985</td><td>1.216</td></tr><tr><td>90</td><td>0.521</td><td>0.038</td><td>0.086</td><td>0.154</td><td>0.240</td><td>0.346</td><td>0.470</td><td>0.615</td><td>0.778</td><td>0.960</td></tr><tr><td>100</td><td>0.322</td><td>0.062</td><td>0.140</td><td>0.249</td><td>0.389</td><td>0.560</td><td>0.762</td><td>0.996</td><td>1.260</td><td>1.556</td></tr><tr><td>110</td><td>0.389</td><td>0.051</td><td>0.116</td><td>0.206</td><td>0.321</td><td>0.463</td><td>0.630</td><td>0.823</td><td>1.041</td><td>1.286</td></tr><tr><td>120</td><td>0.463</td><td>0.043</td><td>0.097</td><td>0.173</td><td>0.270</td><td>0.389</td><td>0.529</td><td>0.691</td><td>0.875</td><td>1.080</td></tr><tr><td>130</td><td>0.543</td><td>0.037</td><td>0.083</td><td>0.147</td><td>0.230</td><td>0.331</td><td>0.451</td><td>0.589</td><td>0.746</td><td>0.920</td></tr><tr><td>140</td><td>0.315</td><td>0.063</td><td>0.143</td><td>0.254</td><td>0.397</td><td>0.571</td><td>0.778</td><td>1.016</td><td>1.286</td><td>1.587</td></tr><tr><td>150</td><td>0.362</td><td>0.055</td><td>0.124</td><td>0.221</td><td>0.346</td><td>0.498</td><td>0.677</td><td>0.885</td><td>1.120</td><td>1.383</td></tr><tr><td>Vehicle Speed</td><td></td><td colspan="9">D2 (with or without DIM)</td></tr><tr><td>50 - 150</td><td></td><td>0.7</td><td>0.9</td><td>0.8</td><td>0.75</td><td>0.6</td><td>0.525</td><td>0.4</td><td>0.225</td><td>0</td></tr></table>

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">ELK Road Edge</td><td colspan="3">ELK Oncoming</td><td colspan="3">ELK Overtaking</td></tr><tr><td colspan="9">D1(depending on lateral and longitudinal speed)</td></tr><tr><td>Vehicle Speed</td><td>Intentional Lateral accelerationR=400 for V&lt;70 km/hR=800 for 70&gt;=V&lt; 100R=1600 for 100&gt;=V&lt;=130R=3200 for V&gt;=140for Vlat &gt;0.4m/s</td><td>0.2m/s</td><td>0.3m/s</td><td>0.4m/s</td><td>0.5m/s</td><td>0.6m/s</td><td>0.7m/s</td><td>0.8m/s</td><td>0.9m/s</td><td>1.0m/s</td></tr><tr><td>50</td><td>0.482</td><td>0.062</td><td>0.140</td><td>0.249</td><td>0.259</td><td>0.373</td><td>0.508</td><td>0.664</td><td>0.841</td><td>1.038</td></tr><tr><td>60</td><td>0.694</td><td>0.043</td><td>0.097</td><td>0.173</td><td>0.180</td><td>0.259</td><td>0.353</td><td>0.461</td><td>0.584</td><td>0.721</td></tr><tr><td>70</td><td>0.473</td><td>0.063</td><td>0.143</td><td>0.254</td><td>0.265</td><td>0.381</td><td>0.519</td><td>0.677</td><td>0.857</td><td>1.059</td></tr><tr><td>72</td><td>0.500</td><td>0.060</td><td>0.135</td><td>0.240</td><td>0.250</td><td>0.360</td><td>0.490</td><td>0.640</td><td>0.810</td><td>1.001</td></tr><tr><td>80</td><td>0.617</td><td>0.049</td><td>0.109</td><td>0.194</td><td>0.203</td><td>0.292</td><td>0.397</td><td>0.519</td><td>0.656</td><td>0.810</td></tr><tr><td>90</td><td>0.781</td><td>0.038</td><td>0.086</td><td>0.154</td><td>0.160</td><td>0.230</td><td>0.314</td><td>0.410</td><td>0.519</td><td>0.640</td></tr><tr><td>100</td><td>0.482</td><td>0.062</td><td>0.140</td><td>0.249</td><td>0.259</td><td>0.373</td><td>0.508</td><td>0.664</td><td>0.840</td><td>1.037</td></tr><tr><td>110</td><td>0.584</td><td>0.051</td><td>0.116</td><td>0.206</td><td>0.214</td><td>0.308</td><td>0.420</td><td>0.548</td><td>0.694</td><td>0.857</td></tr><tr><td>120</td><td>0.694</td><td>0.043</td><td>0.097</td><td>0.173</td><td>0.180</td><td>0.259</td><td>0.353</td><td>0.461</td><td>0.583</td><td>0.720</td></tr><tr><td>130</td><td>0.815</td><td>0.037</td><td>0.083</td><td>0.147</td><td>0.153</td><td>0.221</td><td>0.301</td><td>0.393</td><td>0.497</td><td>0.614</td></tr><tr><td>140</td><td>0.473</td><td>0.063</td><td>0.143</td><td>0.254</td><td>0.265</td><td>0.381</td><td>0.518</td><td>0.677</td><td>0.857</td><td>1.058</td></tr><tr><td>150</td><td>0.543</td><td>0.055</td><td>0.124</td><td>0.221</td><td>0.230</td><td>0.332</td><td>0.452</td><td>0.590</td><td>0.747</td><td>0.922</td></tr><tr><td>Vehicle Speed</td><td></td><td colspan="9">D2 (with or without DIM)</td></tr><tr><td>50 - 150</td><td></td><td>0.7</td><td>0.9</td><td>0.8</td><td>0.75</td><td>0.6</td><td>0.525</td><td>0.4</td><td>0.225</td><td>0</td></tr></table>

# A.2 Alternative Paths for Road Edge, ELK Oncoming and ELK Overtaking

Intended for use where the system intervention occurs before robot steady state phase: 

<table><tr><td colspan="3"></td><td colspan="9">D1
(depending on lateral and longitudinal speed)</td></tr><tr><td>Vehicle Speed</td><td>Lateral acceleration
R=600 for V&lt;70 km/h
R=1200 for 70&gt;=V&lt;100
R=2400 for 100&gt;=V&lt;=130
R=4800 for V&gt;=140
for Vlat &lt;=0.4m/s</td><td>Lateral acceleration
R=400 for V&lt;70 km/h
R=800 for 70&gt;=V&lt;100
R=1600 for 100&gt;=V&lt;=130
R=3200 for V&gt;=140
for Vlat &gt;0.4m/s</td><td>0.2m/s</td><td>0.3m/s</td><td>0.4m/s</td><td>0.5m/s</td><td>0.6m/s</td><td>0.7m/s</td><td>0.8m/s</td><td>0.9m/s</td><td>1.0m/s</td></tr><tr><td>50</td><td>0.322</td><td>0.482</td><td>0.062</td><td>0.140</td><td>0.249</td><td>0.259</td><td>0.373</td><td>0.508</td><td>0.664</td><td>0.841</td><td>1.038</td></tr><tr><td>60</td><td>0.463</td><td>0.694</td><td>0.043</td><td>0.097</td><td>0.173</td><td>0.180</td><td>0.259</td><td>0.353</td><td>0.461</td><td>0.584</td><td>0.721</td></tr><tr><td>70</td><td>0.315</td><td>0.473</td><td>0.063</td><td>0.143</td><td>0.254</td><td>0.265</td><td>0.381</td><td>0.519</td><td>0.677</td><td>0.857</td><td>1.059</td></tr><tr><td>72</td><td>0.333</td><td>0.500</td><td>0.060</td><td>0.135</td><td>0.240</td><td>0.250</td><td>0.360</td><td>0.490</td><td>0.640</td><td>0.810</td><td>1.001</td></tr><tr><td>80</td><td>0.412</td><td>0.617</td><td>0.049</td><td>0.109</td><td>0.194</td><td>0.203</td><td>0.292</td><td>0.397</td><td>0.519</td><td>0.656</td><td>0.810</td></tr><tr><td>90</td><td>0.521</td><td>0.781</td><td>0.038</td><td>0.086</td><td>0.154</td><td>0.160</td><td>0.230</td><td>0.314</td><td>0.410</td><td>0.519</td><td>0.640</td></tr><tr><td>100</td><td>0.322</td><td>0.482</td><td>0.062</td><td>0.140</td><td>0.249</td><td>0.259</td><td>0.373</td><td>0.508</td><td>0.664</td><td>0.840</td><td>1.037</td></tr><tr><td>110</td><td>0.389</td><td>0.584</td><td>0.051</td><td>0.116</td><td>0.206</td><td>0.214</td><td>0.308</td><td>0.420</td><td>0.548</td><td>0.694</td><td>0.857</td></tr><tr><td>120</td><td>0.463</td><td>0.694</td><td>0.043</td><td>0.097</td><td>0.173</td><td>0.180</td><td>0.259</td><td>0.353</td><td>0.461</td><td>0.583</td><td>0.720</td></tr><tr><td>130</td><td>0.543</td><td>0.815</td><td>0.037</td><td>0.083</td><td>0.147</td><td>0.153</td><td>0.221</td><td>0.301</td><td>0.393</td><td>0.497</td><td>0.614</td></tr><tr><td>140</td><td>0.315</td><td>0.473</td><td>0.063</td><td>0.143</td><td>0.254</td><td>0.265</td><td>0.381</td><td>0.518</td><td>0.677</td><td>0.857</td><td>1.058</td></tr><tr><td>150</td><td>0.362</td><td>0.543</td><td>0.055</td><td>0.124</td><td>0.221</td><td>0.230</td><td>0.332</td><td>0.452</td><td>0.590</td><td>0.747</td><td>0.922</td></tr><tr><td>Vehicle Speed</td><td></td><td></td><td colspan="9">D2 (with DIM) Alternative on OEM choice</td></tr><tr><td>50 - 150</td><td></td><td></td><td>0.7</td><td>0.9</td><td>0.8</td><td>1</td><td>1.2</td><td>1.4</td><td>1.6</td><td>1.8</td><td>2</td></tr></table>

Testing of higher lateral velocities may also be conducted against the curved section of the S-Bend; where the traditional straight line test approach angle is equal to the intersecting angle of the VUT reference point and the S-Bend line marking. 

# APPENDIX B APPLICABILITY OF ROBUSTNESS LAYERS

The applicability of the different types of Robustness Layers to each scenario are as follows. 

<table><tr><td colspan="2">Robustness layers</td><td rowspan="2">Road Edge (Lane Boundary)</td><td rowspan="2">C2C Overtaking</td><td rowspan="2">C2C Oncoming</td><td rowspan="2">C2M Overtaking</td><td rowspan="2">C2M Oncoming</td></tr><tr><td>Type</td><td>Layer</td></tr><tr><td>VUT</td><td>Impact location</td><td>N/A</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td rowspan="3">Target (Collision Partner)</td><td>Initial position offset</td><td>N/A</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Type</td><td>N/A</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td rowspan="2">Appearance*</td><td rowspan="2">Yes1</td><td rowspan="2">Yes2</td><td rowspan="2">Yes2</td><td rowspan="2">Yes2</td><td rowspan="2">Yes2</td></tr><tr><td>Target (Lane Boundary)</td></tr><tr><td rowspan="3">Environment</td><td>Adverse weather conditions</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Illumination (Night time)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Illumination (Glare)</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>


* Appearance refers: (1) for Road Edge related to the lane boundaries, or (2) for Oncoming and Overtaking to collision partner 
