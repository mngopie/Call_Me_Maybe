import argparse


def parse_args():
    parse = argparse.ArgumentParser(
        description="Translate natural language prompts into function calls..."
    )

    parse.add_argument(
        "--input",
        type=str,
        default="data/input/function_calling_tests.json"
    )

    parse.add_argument(
        "--functions_definition",
        type=str,
        default="data/input/functions_definition.json"
    )

    parse.add_argument(
        "--output",
        type=str,
        default="data/output/functions_results.json"
    )

    parse.add_argument(
        "--model",
        type=str,
        default="Qwen/Qwen3-0.6B"
    )

    return parse.parse_args()


def main():
    print("Starting function and prompts...")
    args = parse_args()

    # print(args.input)
    # print(args.output)
    # print(args.model)


main()
