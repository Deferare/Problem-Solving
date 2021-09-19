def solution(nums):
    find_number = len(nums)//2
    pokemon_type_set = set()
    for pokemon in nums:
        pokemon_type_set.add(pokemon)
        if len(pokemon_type_set) >= find_number:
            break
    return len(pokemon_type_set)
