def greet(name):
    return f"你好，{name}！这是 Git 练习项目。"


def count_words(text):
    return len(text.split())


if __name__ == "__main__":
    print(greet("Carlos"))
    print(f"这句话里有 {count_words('Git 让每一次改动都可追溯')} 个词")
