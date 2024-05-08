def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = []
    s = 0
    
    while len(truck_weights) != 0 :
        truck = truck_weights[0]
        
        if len(bridge) == bridge_length :
            s -= bridge[0]
            bridge.remove(bridge[0])
        
        if s + truck <= weight :
            s += truck
            bridge.append(truck)
            truck_weights.remove(truck)

        else :
            bridge.append(0)

        time += 1
        
    return time + bridge_length