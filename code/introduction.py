users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

sorted(users, key=lambda user: user['name'], reverse=True)
print(users)

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user['friends'] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    return len(user['friends'])

total_connections = sum(number_of_friends(user) for user in users)

print(total_connections)

num_users = len(users)
avg_connections = total_connections / num_users

print(avg_connections)

for user in users:
    print(str(user['id']) + " : " + str(number_of_friends(user)))

# create a list (user_id, number_of friends)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

# Ordena, tuve que usar la función sort porque el sorted no funcionaba
#sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends,reverse=True)
print("Lista original")
print(num_friends_by_id)
#sorted(num_friends_by_id, key=lambda x: x[0], reverse=True)
num_friends_by_id.sort(key=lambda user: user[1], reverse=True)
print("Lista ordenada")
print(num_friends_by_id)

def friends_of_friends_ids_bad(user):
    return [foaf['id'] 
            for friend in user['friends']
            for foaf in friend['friends']]

# Muestra los vínculos indirectos de acuerdo al grafo de relaciones     
print("test foaf")
print(friends_of_friends_ids_bad(users[0]))

# Muestra vínculos directos
print("Vínculos directos de los 3 primeros usuarios")
for i in range(0,3):
    print([friend['id'] for friend in users[i]['friends']])
    

from collections import Counter

def not_the_same(user, other_user):
    return user['id'] != other_user['id']

def not_friends(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user['friends'])

def friends_of_friends_ids(user):
    return Counter(foaf['id']
                   for friend in user['friends']
                   for foaf in friend['friends']
                   if not_the_same(user, friend) and not_friends(user, foaf))

print("IDS de amigos de amigos")    
print(friends_of_friends_ids(users[3]))

interests = [
        (0, 'Haddop'), (0, 'BigData'), (0, 'HBase'), (0, 'Java'),
        (0, 'Spark'), (0, 'Storm'), (0, 'Cassandra'),
        (1, 'NoSQL'), (0, 'MongoDB'), (1, 'Cassandra'),(1,'HBase'),
        (1, 'Postgres'), (2,'Python'), (2, 'scikit-learn'), (2,'scipy'),
        (2, 'numpy'), (2,'statsmodels'), (2,'pandas'),(3, 'R'), (3, 'Python'),
        (3, 'statistiis'), (3, 'regression'), (3, 'probability'),
        (4, 'machine learning'), (4, 'regression'), (4, 'decision trees'),
        (4, 'libsum'), (5, 'Python'), (5, 'R'), (5, 'Java'), (5, 'C++'),
        (5, 'Haskell'), (5, 'programming languages'), (6, 'statistics'),
        (6, 'probability'), (6, 'mathematics'), (6, 'theory'),
        (7, 'machine learning'), (7, 'scikit-learn'), (7, 'Mahout'),
        (7, 'neural networks'), (8, 'neural network'), (8, 'deep learning'),
        (8, 'Big Data'), (8, 'artificial intelligence'), (9, 'Haddop'),
        (9, 'Java'), (9, 'MapReduce'), (9, 'Big Data')        
        ]

def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]
    
from collections import defaultdict

# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
print(user_ids_by_interest)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user['id']]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user['id'])
    
print("Test interests")
print(most_common_interests_with(users[0]))
    
# Salaries and experiencie

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                         (48000, 0.7), (76000, 6),
                         (69000, 6.5), (76000, 7.5),
                         (60000, 2.5), (83000, 10),
                         (48000, 1.9), (63000, 4.2)]

# Keys are years, values are lists of the salaries for each tenure

print("***\nSection - Salaries and experiencie\n***")
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

for element in salary_by_tenure:
    print(element)

# Keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
        tenure : sum(salaries) / len(salaries)
        for tenure, salaries in salary_by_tenure.items()
        }

print(average_salary_by_tenure)

####
#for key, value in average_salary_by_tenure:
#    print(key, value)
####
def tenure_bucket(tenure):
    if tenure < 2:
        return 'less than two'
    elif tenure < 5:
        return 'between two and five'
    else:
        return 'more than five'
    
# Keys and tenure buckets, value are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Keys are tenure buckets, values are average salary fir that bucket
average_salary_by_bucket = {
        tenure_bucket : sum(salaries) / len(salaries)
        for tenure_bucket, salaries in salary_by_tenure_bucket.items()
        }        

print(average_salary_by_bucket)

# Section  - Pais accounts

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return 'paid'
    elif years_experience < 8.5:
        return 'unpaid'
    else:
        return 'paid'
    

for salary, tenure in salaries_and_tenures:
    print(tenure, predict_paid_or_unpaid(tenure))
    
# Section topics of interest

print("***\nSection Topics of interest\n***")
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)