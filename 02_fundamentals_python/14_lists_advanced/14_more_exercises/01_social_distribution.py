population = list(map(int, input().split(", ")))
min_wealth = int(input())
no_distribution = False
if len(population) * min_wealth > sum(population):
    print("No equal distribution possible")
    no_distribution = True
else:
    for person in range(len(population)):
        the_wealthiest = max(population)
        index_of_the_wealthiest = population.index(the_wealthiest)
        if population[person] < min_wealth:
            population[index_of_the_wealthiest] -= min_wealth - population[person]
            population[person] = min_wealth

if not no_distribution:
    print(population)
