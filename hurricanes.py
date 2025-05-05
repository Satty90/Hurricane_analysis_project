from data import names, months, years, max_sustained_winds, areas_affected, damages, deaths, conversion, mortality_scale, damage_scale


def update_damage(damage):
    updated_damage = []
    for damage in damages:
        if damage == "Damages not recorded":
            updated_damage.append(damage)
        else:
            if "M" in damage:
                value = float(damage.replace("M", ""))
                damage_update = value * conversion["M"]
                updated_damage.append(damage_update)
            elif "B" in damage:
                value = float(damage.replace("B", ""))
                damage_update = value * conversion["B"]
                updated_damage.append(damage_update)
            else:
                updated_damage.append(damage)
    return updated_damage


updated_damages = update_damage(damages)
# print(updated_damages)


def create_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damages": damages[i],
            "Deaths": deaths[i]
        }

    return hurricanes


hurricane_dict = create_hurricane_dictionary(
    names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

print(hurricane_dict)


def dictionary_by_year(hurricane_dict):
    hurricanes_year = {}
    for hurricane in hurricane_dict.values():
        year = hurricane["Year"]
        if year in hurricanes_year:
            hurricanes_year[year].append(hurricane)
        else:
            hurricanes_year[year] = [hurricane]

    return hurricanes_year


hurricane_year_dict = dictionary_by_year(hurricane_dict)
print(hurricane_year_dict)


def count_affected_areas(hurricane_dict):
    affected_areas_count = {}
    for hurricane in hurricane_dict.values():
        for area in hurricane["Areas Affected"]:
            if area in affected_areas_count:
                affected_areas_count[area] += 1
            else:
                affected_areas_count[area] = 1

    return affected_areas_count


area_count = count_affected_areas(hurricane_dict)
print(area_count)


def most_area_affected(area_count):
    most_affected = max(area_count.items(), key=lambda x: x[1])

    return most_affected


most_hit_area = most_area_affected(area_count)
print(most_hit_area)


def deadliest_hurricane(hurricane_dict):
    max_deaths = 0
    deadliest_hurricane_name = ""
    for name, hurricane in hurricane_dict.items():
        deaths = hurricane["Deaths"]
        if deaths > max_deaths:
            max_deaths = deaths
            deadliest_hurricane_name = name

    return deadliest_hurricane_name, max_deaths


deadliest = deadliest_hurricane(hurricane_dict)
print(deadliest)


def mortality_rate(hurricane_dict):
    hurricane_by_mortality = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    for hurricane in hurricane_dict.values():
        deaths = hurricane["Deaths"]
        if deaths == 0:
            rating = 0
        elif deaths <= mortality_scale[1]:
            rating = 1
        elif deaths <= mortality_scale[2]:
            rating = 2
        elif deaths <= mortality_scale[3]:
            rating = 3
        elif deaths <= mortality_scale[4]:
            rating = 4
        else:
            rating = 5
        hurricane_by_mortality[rating].append(hurricane)

    return hurricane_by_mortality


mortlity_dict = mortality_rate(hurricane_dict)
print(mortlity_dict)


def maximum_damage(hurricane_dict):
    max_damage = 0
    max_hurricane_name = ""
    for name, hurricane in hurricane_dict.items():
        damage = hurricane["Damages"]
        if damage == "Damages not recorded":
            continue
        if damage > max_damage:
            max_damage = damage
            max_hurricane_name = name

    return max_hurricane_name, max_damage


max_damage_hurricane = maximum_damage(hurricane_dict)
print(max_damage_hurricane)


def damage_rate(hurricane_dict):
    hurricane_by_damage = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }

    for hurricane in hurricane_dict.values():
        damage = hurricane["Damages"]
        if damage == "Damages not recorded":
            hurricane_by_damage[0].append(hurricane)
            continue

        if damage == 0:
            rating = 0
        elif damage <= damage_scale[1]:
            rating = 1
        elif damage <= damage_scale[2]:
            rating = 2
        elif damage <= damage_scale[3]:
            rating = 3
        elif damage <= damage_scale[4]:
            rating = 4
        else:
            rating = 5

        hurricane_by_damage[rating].append(hurricane)

    return hurricane_by_damage


damage_dict = damage_rate(hurricane_dict)
print(damage_dict)
