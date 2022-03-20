# Create a function nextVersion, that will take a string in parameter, and will return a string containing the next version number.
# A question from an interview.

def nextVersion(version):
    # converting it into a list of int so that processing becomes easier
    list_version = list(map(int, version.split(".")))
    # using a flag to determine when to add one if sum >= 10
    add_one = True
    # we are iterating it in reversed way so that addition is easy
    for index, value in reversed(list(enumerate(list_version))):
        if add_one:
            if value>=0 and value<=8:
                list_version[index] = value + 1
                # nothing to add in the next step.
                # we are good to make the flag False
                break
            else:
                # if it is the first index, we just add 1
                if index==0:
                    list_version[index] = value + 1
                else:
                    list_version[index] = 0
                    add_one = True
    return ".".join(map(str,list_version))

# print(nextVersion("10.1.8"))
# print(nextVersion("10"))
