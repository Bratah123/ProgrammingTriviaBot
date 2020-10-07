def to_string():
    with open('code.txt', 'r') as f:
        file = f.readlines()
        output = ""
        for line in file:
            output += line.strip('\n') + "\n"
        f.close()
        return "```" + output + "```"


def main():
    print(to_string())


if __name__ == '__main__':
    main()
