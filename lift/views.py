from django.http import JsonResponse
from django.shortcuts import render

def handle_lift_requests(request):
    if request.method == 'POST':
        data = request.POST
        # print(f"data: {data.get('num_floors')}")
        if 'num_floors' in data and 'num_lifts' in data:
            print("num_floors and num_lifts are Received")
            return render(request, 'home.html', context={'num_floors': data.get('num_floors'), 'num_lifts': data.get('num_lifts'), 'liftrange':range(int(data.get('num_lifts')))} )
        
        
        else:
            data = request.POST  # Assuming POST request with JSON data
            lifts = int(data['lifts'][0])
            floors = int(data['floors'][0])
            lift_requests = {f'lift{i}': data[f'lift{i}'] for i in range(lifts)}
            
            # Process lift requests
            current_floors = [0] * lifts
            lift_states = ['CLOSE'] * lifts
            output = []

            def move_lift(lift_index, destination_floor):
                nonlocal current_floors, lift_states
                time_taken = abs(current_floors[lift_index] - destination_floor) + 1
                current_floors[lift_index] = destination_floor
                lift_states[lift_index] = 'OPEN'
                output.append(f"LIFT {lift_index + 1} -- > {destination_floor} (OPEN)")
                lift_states[lift_index] = 'CLOSE'
                output.append(f"LIFT {lift_index + 1} -- > {destination_floor} (CLOSE)")
                return time_taken

            for t in range(floors):  # Time iterations
                output.append(f"T={t}")
                lift_responses = []
                for lift_index in range(lifts):
                    lift_request = lift_requests[f'lift{lift_index}']
                    if t < len(lift_request):
                        destination_floor = int(lift_request[t])
                        if current_floors[lift_index] < destination_floor:
                            time_taken = move_lift(lift_index, destination_floor)
                            lift_responses.append(f"LIFT {lift_index + 1} will cater the request in {time_taken} units.")
                        elif current_floors[lift_index] > destination_floor:
                            time_taken = move_lift(lift_index, destination_floor)
                            lift_responses.append(f"LIFT {lift_index + 1} will cater the request in {time_taken} units.")
                    else:
                        lift_responses.append(f"LIFT {lift_index + 1} -- > {current_floors[lift_index]} ({lift_states[lift_index]})")
                
                output.extend(lift_responses)

            return render(request, 'home.html', context={'result': output})

    else:   
        return render(request, 'home.html')   

