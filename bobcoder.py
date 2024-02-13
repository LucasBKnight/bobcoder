# This is a sample Python script.
import random
import re
import json

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def wrap(s, w):
    sre = re.compile(rf'(.{{{w}}})')
    return [x for x in re.split(sre, s) if x]


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele
    return str1


cypher = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
          [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
          [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
          [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gen = False
    LINE_CLEAR = '\x1b[2K'
    b = True
    print(f'{bcolors.OKCYAN}for a list of commands type "help"{bcolors.ENDC}')
    print("'\r{0}".format("Input command\n> "), end='')
    while b == True:
        a = input()
        if a == "encode" or a == "e":
            if gen == True:
                print(
                    f"Write Message to Encode\n{bcolors.WARNING}please refrain from using any uppercase or special characters{bcolors.ENDC}\n> ",
                    end='')
                ec = input()
                [ec.lower() for i in ec]
                output = []
                for character in ec:
                    number = ord(character) - 97
                    output.append(number)
                print(f"{bcolors.OKGREEN}[CHAR INDEXING SUCCESS]{bcolors.ENDC}")
                # print(output)
                lecyp = []
                for i in range(len(output)):
                    if output[i] == -65:
                        lecyp.append(str(9999))
                    else:
                        number = cypher[output[i]][random.randrange(0, 3)]
                        lecyp.append(str(number))
                print(f"{bcolors.OKGREEN}[MESSAGE SUCCESSFULLY ENCODED]{bcolors.ENDC}")
                print(listToString(lecyp))
                print("'\r{0}".format("Input Command\n> "), end='')
            else:

                print("'\r{0}".format(f"{bcolors.FAIL}[ENCODING FAILED: NO CYPHER]{bcolors.ENDC}"))

                print("'\r{0}".format("Input Command\n> "), end='')
        elif a == "decode" or a == "d":
            print("Write Message to Decode\n> ", end='')
            ec = input()
            if gen == True:
                ecl = wrap(ec, 4)
                # if str in ecl:
                # print(f"{bcolors.FAIL}[DECODING FAILURE: CHECK YOUR INPUT]{bcolors.ENDC}")
                # print("'\r{0}".format("Input command\n> "), end='')'''
                print(f"{bcolors.OKGREEN}[STR WRAPPING SUCCESS]{bcolors.ENDC}")
                fout = [[]]
                foutint = 0
                fouti = 0
                for l in range(len(ecl)):
                    for w in range(len(cypher)):
                        for i in range(4):
                            if str(ecl[l]) == str(cypher[w][i]):
                                foutint += 1
                                print(f"\r{bcolors.OKGREEN}[ENCODED VALUES DETECTED: {foutint}|{fouti}]{bcolors.ENDC}",
                                      end='')
                                fout[fouti].append(chr(w + 97))
                    if str(ecl[l]) == "9999":
                        print(f"\r{bcolors.OKGREEN}[ENCODED VALUES DETECTED: {foutint}|{fouti}]{bcolors.ENDC}", end='')
                        fout.append([])
                        fouti += 1
                print(f"{bcolors.OKGREEN}\n[DECODING SUCCESS]{bcolors.ENDC}")
                ff = []
                for i in range(len(fout)):
                    ff.append("".join(fout[i]))
                print("----------------------")
                print(" ".join(ff))
                print("----------------------")
            else:
                print("'\r{0}".format(f"{bcolors.FAIL}[DECODING FAILED: NO CYPHER]{bcolors.ENDC}"))
            print("'\r{0}".format("Input Command\n> "), end='')
        elif a == "set" or a == "s":
            print("Input Cypher\n> ", end='')
            cypher1 = json.loads(input())
            failure = False
            if len(cypher1) == len(cypher):
                print(f"{bcolors.OKGREEN}[CYPHER FORMAT RECOGNIZED]{bcolors.ENDC}")
                for i in range(len(cypher)):
                    print(f"\r[CYPHER INDEX PASS {i + 1}/{len(cypher)}]{bcolors.ENDC}", end='')
                    if len(cypher1[i]) != len(cypher[i]):
                        failure = True
            else:
                failure = True
            if failure == True:
                print(f"\n{bcolors.FAIL}[CYPHER INPUT NOT RECOGNIZED]{bcolors.ENDC}")
                print("\nInput Command\n> ", end='')
            else:
                gen = True
                cypher = cypher1
                print(f"\n{bcolors.OKGREEN}[CYPHER INPUT SUCCESSFULLY]{bcolors.ENDC}")
                print("Input Command\n> ", end='')
        elif a == "generate" or a == "g":
            gen = True
            rack = 26
            for w in range(rack):
                for i in range(4):
                    cypher[w][i] = int(random.randrange(1000, 9998))
            print("'\r{0}".format(f"{bcolors.OKGREEN}[Generated]{bcolors.ENDC}\n"))
            print(json.dumps(cypher))
            print("\nInput Command\n> ", end='')
        elif a == "terminate" or a == "t":
            print(f"{bcolors.WARNING}Warning: Action will terminate the encoder. Continue (y/n)?{bcolors.ENDC}\n> ",
                  end='')
            if input() == "y":
                b = False
            else:
                print("Input Command\n> ", end='')
        elif a == "help":
            print("'\r{0}".format(
                f"{bcolors.BOLD}{bcolors.OKCYAN}Commands List{bcolors.ENDC}{bcolors.OKCYAN}\n------------------------------------\nhelp: opens a list of commands\nencode: encodes input with current key\ndecode: decodes input with current key\ngenerate:generates a new cypher key\n------------------------------------{bcolors.ENDC}"))
            print("'\r{0}".format("Input Command\n> "), end='')
        else:
            print("'\r{0}".format(f"{bcolors.FAIL}Invalid Command{bcolors.ENDC}"))
            print(f'{bcolors.OKCYAN}Use the "help" command to get a list of commands{bcolors.ENDC}')
            print("'\r{0}".format("Input Command\n> "), end='')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
