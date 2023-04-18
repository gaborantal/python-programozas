def tell_something(what):
    match what:
        case "joke":
            print("To the guy who invented zero: Thanks for nothing!")
        case "story":
            print("I'm reading a book about anti-gravity. I can't put it down.")
        case "funfact":
            print("Cats are believed to be the only mammals who don't taste sweetness.")


def main():
    while True:
        match input("$ ").split():
            case ["quit" | "exit"]:
                print("Bye!")
                return
            case ["echo", valtozo]:
                print(valtozo)
            case ["add", *args]:
                print(sum([int(arg) for arg in args]))
            case ["tell", "me" | "us", "a", ("joke" | "story" | "funfact") as what]:
                print(f"Here comes a {what}")
                tell_something(what)
            case [*other]:
                print(other)


if __name__ == '__main__':
    main()
