
def pre_process(a):
    def decorator(func):
        def dec_process(s):
            for i in range(len(s)):
                s[i] = round(s[i] - a*s[i-1], 1)
            return func(s)
        return dec_process
    return decorator


@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)


def main():
    s = [1.2, 3.0, 0.79]
    plot_signal(s)


if __name__ == "__main__":
    main()
