
def happy_new_years_greetings():
    friends = ["Joseph", "Chad", "Brian", "Stewie"]
    greetings = []
    for friend in friends:
        greeting = (f"Happy New Years, {friend}!!")
        greetings.append(greeting)
    return sorted(greetings)

message = happy_new_years_greetings()

print(message)

dictionary = {

    "key2": "value2",
    "key3": "value3"
}

print(dictionary.get("key1", "default value"))
