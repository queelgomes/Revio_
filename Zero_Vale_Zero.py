while True:
    try:
        input_1 = int(input())
        input_2 = int(input())
        result = str(input_1 + input_2)

        final = ""

        for v, k in enumerate(result):
            if k != "0":
                final += k

        print(final)
        break
    except ValueError:
        print("Digite apenas numeros.")
