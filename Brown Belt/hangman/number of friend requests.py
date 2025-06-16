def numFriendRequests(ages):
    def friendRequest(a, b):
        if b<=.5*a+7:return False
        if b>a:return False
        return True
    age_group={}
    for i in ages:
        if i not in age_group:
            age_group[i] = 1
        else:
            age_group[i]+=1
    print(age_group)
    total_requests = 0
    for a, num_a in age_group.items():
        for b, num_b in age_group.items():
            if friendRequest(a, b):
                total_requests += num_a*num_b
                if a==b: total_requests -= num_a
    return total_requests

ages = [16, 17, 18]
print(numFriendRequests(ages))