# Zevi Lift Assignment

**Python Code**
```
class Lift:
    def __init__(self, max_floor):
        self.current_floor = 0
        self.state = "CLOSE"
        self.max_floor = max_floor

    def move(self, dest_floor):
        time_taken = abs(dest_floor - self.current_floor)
        self.current_floor = dest_floor
        return time_taken + 2  # 1 unit to open, 1 unit to close

def main():
    num_lifts = int(input("No of Lifts: "))
    num_floors = int(input("No of Floors: "))
    lifts = [Lift(num_floors) for _ in range(num_lifts)]
    print("Initial positions of lifts:", [lift.current_floor for lift in lifts])

    requests = []
    while True:
        request = input("Enter request (format: 'starting_floor destination_floor') or type 'done' to finish: ").strip()
        if request.lower() == 'done':
            break
        requests.append(tuple(map(int, request.split())))

    for time, request in enumerate(requests):
        print(f"T={time}")
        for lift_index, lift in enumerate(lifts):
            print(f"LIFT {lift_index + 1} -- > {lift.current_floor} ({lift.state})", end=", ")
        print()

        starting_floor, destination_floor = request
        lift_time_taken = []
        for lift in lifts:
            if lift.state == "CLOSE":
                lift_time_taken.append(lift.move(starting_floor))
            else:
                lift_time_taken.append(float('inf'))

        nearest_lift_index = lift_time_taken.index(min(lift_time_taken))
        nearest_lift = lifts[nearest_lift_index]
        total_time = min(lift_time_taken) + abs(starting_floor - destination_floor) + 2  # 1 unit to open, 1 unit to close
        nearest_lift.current_floor = destination_floor
        nearest_lift.state = "OPEN"
        print(f"T={time + 1}")
        for lift_index, lift in enumerate(lifts):
            if lift_index == nearest_lift_index:
                print(f"LIFT {lift_index + 1} -- > {lift.current_floor} (OPEN)", end=", ")
            else:
                print(f"LIFT {lift_index + 1} -- > {lift.current_floor} ({lift.state})", end=", ")
            if lift.state == "OPEN":
                lift.state = "CLOSE"
        print(f"\nLIFT {nearest_lift_index + 1}: {total_time} SECONDS")

if __name__ == "__main__":
    main()

```
**OUTPUT**

```
No of Lifts: 2
No of Floors: 10
Initial positions of lifts: [0, 0]
Enter request (format: 'starting_floor destination_floor') or type 'done' to finish: 0 7
Enter request (format: 'starting_floor destination_floor') or type 'done' to finish: 3 0
Enter request (format: 'starting_floor destination_floor') or type 'done' to finish: done
T=0
LIFT 1 -- > 0 (CLOSE), LIFT 2 -- > 0 (CLOSE), 
T=1
LIFT 1 -- > 7 (OPEN), LIFT 2 -- > 0 (CLOSE), 
LIFT 1: 11 SECONDS
T=1
LIFT 1 -- > 7 (CLOSE), LIFT 2 -- > 0 (CLOSE),
T=2
LIFT 1 -- > 3 (CLOSE), LIFT 2 -- > 0 (OPEN),
LIFT 2: 10 SECONDS

```

## Setup and Running the Project

1. **Clone the repository**
    ```
    git clone https://github.com/username/projectname.git
    ```

2. **Navigate into the project directory**
    ```
    cd projectname
    ```

3. **Create a virtual environment**
    ```
    python -m venv env
    ```

4. **Activate the virtual environment**
    - On Windows, run:
        ```
        env\Scripts\activate
        ```
    - On Unix or MacOS, run:
        ```
        source env/bin/activate
        ```

5. **Install the required packages**
    ```
    pip install -r requirements.txt
    ```

6. **Apply migrations**
    ```
    python manage.py migrate
    ```

7. **Run the server**
    ```
    python manage.py runserver
    ```

Now, you can navigate to `http://127.0.0.1:8000/` in your web browser to view the application.

## Running Tests

To run tests, use the following command:


