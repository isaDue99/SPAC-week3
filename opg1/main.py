# python intro assignment

NAMES = ["Jenny", "Adam", "Beatrice", "Gort", "Brunhilde", "Jennice", "Johnathan", 
    "Slimshady", "Michael", "Robert", "Warriormale", "Dickinson", "Trevor", 
    "Grant", "William", "Weston", "Kennedy", "Ada", "Wong", "Tiffany", 
    "Ryukazaki", "Bo", "Peter", "Matthewson", "Ericaline", "Yvonne", "Yrsa", 
    "Fredrick", "Holmes", "Sherlock", "Watson", "Alexander", "Benjamin", 
    "Charlotte", "Daniel", "Emily", "Frederik", "DuBois", "Kitsuragi",
    "Gabriel", "Hannah", "Isabella", "Jacob", "Katherine", "Liam", "Mia", 
    "Nathan", "Olivia", "Peter", "Quinn", "Rebecca", "Samuel", "Theresa", 
    "Ulysses", "Victoria", "William", "Xander", "Yasmine", "Zachary",
    "Amelia", "Aaron", "Sophia", "Noah", "Ava", "James", "Lucas", "Ethan", 
    "Ella", "David", "Elijah", "Aria", "Jackson", "Aiden", "Scarlett", 
    "Sofia", "Matthew", "Logan", "Abigail", "Grace", "Henry", "Isla", 
    "Ryan", "Evelyn", "Oliver", "Sebastian", "Harper", "Caleb", "Chloe", 
    "Julian", "Penelope", "Levi", "Victoria", "Dylan", "Aurora", "Luke", 
    "Hazel", "Isaac", "Samantha", "Theodore", "Lily", "Grayson", "Lillian", 
    "Joshua", "Layla", "Zoe", "Madison", "Owen", "Caroline", "Leo", 
    "Alice", "Mason", "Eleanor", "Wyatt", "Ellie", "Jack", "Nora", "Lucas",
    "Sarah", "Evan", "Luna", "Mila", "Eli", "Sadie", "Landon", "Addison",
    "Jaxon", "Piper", "Lincoln", "Stella", "Connor", "Grace", "Hudson", 
    "Ruby", "Carson", "Sophia", "Asher", "Kinsley", "Christian", "Brielle",
    "Maverick", "Vivian", "Nolan", "Emilia", "Hunter", "Camila", "Adrian", 
    "Archer", "Easton", "Emery", "Maddox", "Faith", "Roman", "Riley"]


# remove duplicates by converting to set and back
NAMES = list(set(NAMES))


### task 1: sort list of names by length and then alphabetically

def sortkey(n):
    """
    sorting function to sort a list's elements by length, then alphabetically, by returning a tuple of that info per element
    """
    return (len(n), n)

sortedNAMES = sorted(NAMES, key=sortkey)
print(sortedNAMES)


### task 2: count occurence of each letter in each name in the sorted list, and collect into a dict

from collections import defaultdict

d = defaultdict(int)

for name in sortedNAMES:
    for letter in name:
        # convert to uppercase cus im more interested in absolute counts of each letter
        d[letter.upper()] += 1


sortedd = sorted(d.items())
print(sortedd)