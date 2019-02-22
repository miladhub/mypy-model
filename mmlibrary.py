import sys, json;

def getArgument(args, name):
	return args[name]

def returnScore(score):
	scoreMap = { "score" : score }
	print(json.dumps(scoreMap))

def getModel():
	return "binary.zip"
