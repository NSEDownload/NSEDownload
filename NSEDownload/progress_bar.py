import sys

def init_bar(total_stages):

	# setup toolbar
	sys.stdout.write("Downloading  [%s]" % (" " * total_stages))
	sys.stdout.flush()
	sys.stdout.write("\r")

def print_bar(stage, total_stages):

	rem = total_stages - stage
	sys.stdout.write("Downloading  [%s] %.2f %s" % ("-" * stage + " "*(rem),stage/total_stages*100,"%"))
	sys.stdout.write("\r")
	sys.stdout.flush()


def end_bar(total_stages):
	sys.stdout.write("Downloading  [%s] %.2f %s \n" % ("-" * total_stages,100,"%"))
