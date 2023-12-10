# Technical Specification for Grouping Rides in Autofleet

1. Leg Type:

- Utilize the "Leg" field to distinguish between rides going to school ("A") and rides returning from school ("B").

2. Home Location Matching:

- Leverage the latitude (lat) and longitude (lng) fields to identify passengers with similar home locations
- Define a proximity threshold to group passengers whose home locations are within a certain distance of each other.

3. ExternalID and completeAfterExternalSpId Mechanism:

- Leverage the "externalID" field to label each stop point uniquely.
- Use the "completeAfterExternalSpId" field to establish relationships between stop points, ensuring the sequential execution of trips.

4. Group rides based on the "dropOffZone" field to facilitate efficient routing and reduce detours.

5. Time Window Constraints:

- Utilize the "scheduled_to" field to create time constraints for grouping passengers.
- Ensure that rides with similar scheduled pickup or drop-off times are grouped together.


## Success Metrics:
1. Reduction in Overlapping Rides:

Measure the reduction in the number of rides with overlapping pickup or drop-off locations.
Identify and quantify instances where grouping has effectively minimized detours and improved route efficiency.

2. Vehicle Capacity Utilization:

Track and analyze the utilization of vehicle capacity.
Measure the increase in the number of passengers accommodated in each vehicle, optimizing capacity for cost efficiency.

3. Operational Efficiency:

Assess the overall operational efficiency of the ride-sharing system.
Monitor changes in route optimization, pickup and drop-off sequencing, and adherence to scheduled time windows.

4. Cost Savings:

Evaluate cost savings resulting from reduced vehicle mileage, fuel consumption, and improved vehicle capacity utilization.
Compare operational costs before and after implementing the grouping criteria.


# Trip Grouping Script

This script is designed to group trips based on specified criteria, including `pickUpZone`, `dropOffZone`, time window constraints, and the `completeAfterExternalSpId` and `externalID` mechanism.

## Requirements

- Python 3.x
- Pandas library (`pip install pandas`)

## Usage

1. Install the required dependencies:

   ```bash
   pip install pandas
   
## Script Logic

Grouping Logic

The script applies the following grouping criteria:

- Leg Type:
Differentiates between rides going to school ("A") and rides from school ("B").
- Home Location Matching:
- Utilizes the latitude (lat) and longitude (lng) fields to group passengers with similar home locations.
- Matching Type, Dispatch Type, and Drop-Off Zone:
Considers matching type, dispatch type, and drop-off zone for grouping.
ExternalID and completeAfterExternalSpId Mechanism:
Assigns unique ExternalIDs to stop points within a ride.
Uses the completeAfterExternalSpId mechanism to define the execution order of stop points.
- Time Window Constraints:
Groups rides with similar scheduled pickup or drop-off times.
- Time Threshold:
Applies a time threshold of 30 minutes to group rides with the same destination, the same pickUpZone, and within the specified time threshold.


## Ideas for Improvement

1. Capacity Calculation

Utilize the number_of_passengers field to calculate the number of passengers for each ride.
Implement logic to ensure that there is enough capacity in a bus for a specific ride.

2. Accessibility Ordering

Introduce an accessibility field to indicate whether a ride requires an accessible bus.
Prioritize or group rides that require accessibility services for students with special needs.
