'''
2018 KAKAO BLIND RECRUITMENT

https://school.programmers.co.kr/learn/courses/30/lessons/17680

'''

def solution(cacheSize, cities):
    
    # hit <- cache에 해당하는 페이지가 있으면 +1
    # miss <- cache에 해당하는 페이지가 없으면 +5
    if cacheSize == 0:
        return len(cities) * 5
    
    time = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)

    return time