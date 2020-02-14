voewels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")
found = []
for i in word:
    if i in voewels:
        found.append(i)
#print(found)

text = """Configuration for a Spark application. Used to set various Spark parameters as key-value pairs.
Most of the time, you would create a SparkConf object with SparkConf(), which will load values from spark.
* Java system properties as well. In this case, 
any parameters you set directly on the SparkConf object take priority over system properties.
For unit tests, you can also call SparkConf(false) to skip loading external settings and get the same configuration no matter what the system properties are.
All setter methods in this class support chaining. For example, you can write conf.setMaster(“local”).setAppName(“My app”)."""

text = text.lower().split()
result = {}
for i in text:
    if i in result.keys():
        result[i] += 1
    else:
        result[i] = 1

print(result)
