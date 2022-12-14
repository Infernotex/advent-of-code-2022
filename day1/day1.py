def main() -> None:
    with open("input", "r") as f:
        index: int = 0
        elves: list[int] = [0]

        calories: str
        for calories in f:
            if calories != "\n":
                elves[index] += int(calories)
            else:
                index += 1
                elves.append(0)

        elves.sort()

        print(f"The elf with the most calories carries: {elves[-1]} calories.")
        print(f"The top 3 elves carries a total of: {elves[-1] + elves[-2] + elves[-3]}")


if __name__ == "__main__":
    main()
