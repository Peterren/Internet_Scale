from pyspark import SparkContext
import itertools
import MySQLdb


sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

# Read data in as pairs of (user_id, item_id clicked on by the user)
pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition

# Group data into (user_id, list of item ids they clicked on)
click_of_users = pairs.groupByKey()

# Transform into (user_id, (item1, item2) where item1 and item2 are pairs of items the user clicked on
click_of_users_pair = click_of_users.flatMap(lambda x: [(x[0],y) for y in itertools.combinations_with_replacement(x[1],2)]).distinct()

# Transform into ((item1, item2), list of user1, user2 etc) where users are all the ones who co-clicked (item1, item2)
user_of_item=click_of_users_pair.map(lambda x: (x[1],x[0]))

# Transform into ((item1, item2), count of distinct users who co-clicked (item1, item2)
# Filter out any results where less than 3 users co-clicked the same pair of items
user_of_item_cnt = user_of_item.groupByKey.map(lambda itemuser: (itemuser,len(itemuser))).filter(lambda cnt: cnt[1]>=3)

# Create a recommendation list which has (item1, recommended items for item1)
recommend_items1 = user_of_item_cnt.map(lambda x: (x[0][0]:x[0][1]))
recommend_items2 = user_of_item_cnt.map(lambda x: (x[0][1]:x[0][0]))
recommend_item_final = recommend_items1.union(recommend_items2).groupByKey()

pages = pairs.map(lambda pair: (pair[1], 1))      # re-layout the data to ignore the user id
count = pages.reduceByKey(lambda x,y: int(x)+int(y))        # shuffle the data so that each key is only on one worker
                                              # and then reduce all the values by adding them together

output = count.collect()                          # bring the data back to the master node so we can print it out
for page_id, count in output:
  print("Pairs of products: %s Number of people who viewed both products: %d" % (page_id, count))

output = recommend_item_final.collect()

sc.stop()


db = MySQLdb.connect("db", "root", "$3cureUS", "cs4501")
cursor = db.cursor()

insert_query = "INSERT INTO Recommand (item1, recommended_items) VALUES (%s, %s);"

cursor.execute("TRUNCATE TABLE Recommand;")

for item1, recommended_items in output:
    recommended_items = ",".join(recommended_items)

    # Insert recommendation item into db
    try:
        cursor.execute(insert_query, (item1, recommended_items))
        db.commit()
    except:
        db.rollback()

# Disconnect from server
db.close()


