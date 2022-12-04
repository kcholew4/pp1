import json
import statistics

def f(age, course, average):
  def fileFilter(x):
    if x["age"] < age:
      return False

    courses: list = x["studies"]["courses"];

    desiredCourse = [i for i in courses if i["name"] == course]

    if len(desiredCourse) != 1:
      return False

    if statistics.mean(desiredCourse[0]["grades"]) < average:
      return False

    return True

  with open("test.json", "r") as file:
    jsonFile = json.load(file)
    filtered = filter(fileFilter, jsonFile)
    return len(list(filtered))
