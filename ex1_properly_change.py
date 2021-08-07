
""" The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
 """

def run():
    def tickets(people):
        change = people[0] - people[1]
        if change < 0:
            return "NO"
        else:
            return "YES"

    people = []

    for i in range(2):
        first = int(input('number: '))
        people.append(first)

    print()
    print(tickets(people))



if __name__ == '__main__':
    run()