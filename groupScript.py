import pandas as pd
from datetime import datetime, timedelta

def create_external_id(prefix, index):
    # Create a unique externalID using the provided prefix and index
    return f"{prefix}_{index}"

def group_rides(data, time_threshold_minutes=30):
    # Convert scheduled_to field to datetime format
    data['scheduled_to'] = pd.to_datetime(data['scheduled_to'])

    # Sort data by scheduled time for better grouping
    data = data.sort_values(by=['scheduled_to'])

    # Initialize a dictionary to store grouped rides
    grouped_rides = {}

    for index, ride in data.iterrows():
        leg_type = ride['custom_fields']['Leg']
        matching_type = ride['matching_type']
        dispatch_type = ride['dispatch_type']
        dropoff_zone = ride['custom_fields'].get('dropOffZone', None)
        scheduled_time = ride['scheduled_to']

        # Define the key for grouping based on specified criteria
        group_key = (
            leg_type,
            matching_type,
            dispatch_type,
            dropoff_zone,
        )

        # Check if the group already exists
        if group_key in grouped_rides:
            # Find rides with similar criteria and within the time threshold
            similar_rides = [r for r in grouped_rides[group_key] if abs((scheduled_time - r['scheduled_to']).total_seconds()) <= (time_threshold_minutes * 60)]

            # Incremental index for ExternalID
            index_in_group = len(similar_rides) + 1
        else:
            index_in_group = 1
            grouped_rides[group_key] = []

        # Create ExternalID and completeAfterExternalSpId
        external_id = create_external_id(f"ride_{leg_type}", index_in_group)
        complete_after_external_sp_id = create_external_id(f"ride_{leg_type}", index_in_group - 1) if index_in_group > 1 else None

        # Update the ride with ExternalID and completeAfterExternalSpId
        ride['externalID'] = external_id
        ride['preferences'] = {'completeAfterExternalSpId': complete_after_external_sp_id}

        # Append the ride to the group
        grouped_rides[group_key].append(ride)

    return grouped_rides

def main():
    # Read the provided CSV data into a Pandas DataFrame
    data = pd.read_csv("your_dataset.csv")

    # Group rides based on specified criteria and time threshold
    grouped_rides = group_rides(data, time_threshold_minutes=30)

    # Print the results (you can modify this part based on your needs)
    for group_key, rides in grouped_rides.items():
        print(f"Group Key: {group_key}")
        for ride in rides:
            print(f"Ride ID: {ride['ride_id']}, Leg: {ride['custom_fields']['Leg']}, Scheduled Time: {ride['scheduled_to']}, ExternalID: {ride['externalID']}, completeAfterExternalSpId: {ride['preferences']['completeAfterExternalSpId']}")
        print("\n")

if __name__ == "__main__":
    main()
