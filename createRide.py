import requests

def create_ride(access_token):
    url = "https://api.staging.eu.autofleet.io/api/v1/rides"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    payload = {
        "rideType": "passenger",
        "pooling": "active",
        "demandSourceId": "08c9865f-b404-4638-89b0-c3e8e043b62e",
        "businessModelId": "a0ec280e-cae7-4aff-9eea-f49f70b5e1b5",
        "numberOfPassengers": 1,
        "dispatchType": "automatic",
        "stopPoints": [
            {
                "type": "pickup",
                "lat": 123.456,
                "lng": 123.456,
                "contactPersonName": "Name",
                "contactPersonPhone": "phone with prefix",
                "afterTime": "2023-01-31 12:00:00",
                "beforeTime": "2023-01-31 13:00:00",
                "notes": "string",
                "externalId": "string",
                "preferences": {
                    "completeAfterExternalSpId": "string"
                }
            },
            {
                "type": "dropoff",
                "lat": 123.456,
                "lng": 123.456,
                "contactPersonName": "Name",
                "contactPersonPhone": "phone with prefix",
                "afterTime": "2023-01-31 12:00:00",
                "beforeTime": "2023-01-31 13:00:00",
                "notes": "string",
                "externalId": "string",
                "preferences": {
                    "completeAfterExternalSpId": "string"
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Ride created successfully.")
        print(response.json())
    else:
        print(f"Failed to create ride. Status code: {response.status_code}")
        print(response.text)

def main():
    # Replace "your_access_token_here" with the actual access token or use a dynamic mechanism to fetch the token.
    access_token = "your_access_token_here"
    create_ride(access_token)

if __name__ == "__main__":
    main()